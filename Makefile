##########################

# === GLOBAL VARIABLES ======================================================
PROJECT_SRC=eyecue_tracker
DOCKER_IMAGE=eyecue-tracker
DOCKER_COMPOSE_APP=eyecue_tracker
TEST_COVERAGE_PERCENTAGE=80
TAG=latest
SSH_KEY=$(HOME)/.ssh/id_rsa
BASE_IMAGE=
EXTRA_ARGS=

# === COMMANDS ==============================================================
# Installs the Python dependencies
install:
	pip3 install -r requirements.txt

# Installs the dev Python dependencies
install-dev:
	echo "Installing DEV dependencies"
	pip3 install -e ".[dev]"

# Installs the necessary test tools
install-test:
	pip3 install pytest coverage

# Downloads the Python dependencies
download:
	pip3 download -r requirements.txt

# Installs the dev Python dependencies
download-dev:
	echo "Installing DEV dependencies"
	pip3 download -r requirements-dev.txt

#====================================================
define check_service =
	while true ; do \
		if nc -z -v -w5 $(1) $(2) 2>&1 | grep "Connection refused"; then echo "Connection refused to $(1) $(2). Is $(3) running? Trying again"; sleep 2s; else break; fi ; \
	done

endef

check-connection-local:
	$(call check_service,localhost,15672,rabbitmq)
	$(call check_service,localhost,1883,mqtt)

check-connection-docker:
	$(call check_service,rabbitmq,15672,rabbitmq)
	$(call check_service,rabbitmq,1883,mqtt)

install-net-cat:
	apt update
	apt install -y netcat

#====================================================
# Runs the Unit tests
unit:
	python3 -m pytest eyecue_tracker/__tests__/unit -v

# Runs the functional tests
functional:
	python -m pytest eyecue_tracker/__tests__/functional -v

# Runs all tests
tests:
	python -m pytest eyecue_tracker/__tests__ -v

# Runs all tests locally
tests-local: check-connection-local tests

# Runs all tests through docker (i.e., must be called from inside docker)
docker-tests: install-net-cat check-connection-docker qa

# Tests coverage check and reports
# Note: Only unit for now
coverage:
	coverage run -m pytest eyecue_tracker/__tests__ -v
	coverage report --fail-under=$(TEST_COVERAGE_PERCENTAGE)

#====================================================
# Runs all the QA tooling
qa: tests coverage

# Builds an image for the compose tag.
docker-qa-build: TAG=latest-staging
docker-qa-build: EXTRA_ARGS=--build-arg INSTALL_SUFFIX="-dev"
docker-qa-build: docker-build

# Runs all the QA tooling in the dev docker container
docker-qa: docker-sidecars docker-qa-build
	docker-compose -f docker-compose-tests.yml up $(DOCKER_COMPOSE_APP)
	docker-compose -f docker-compose-tests.yml down --remove-orphans

docker-sidecars:
	docker-compose -f docker-compose-tests.yml up -d redis rabbitmq

# Alias for docker-shell
shell:
	make docker-shell

# Gets a shell inside the development container (note: You can sudo this)
docker-shell: docker-qa-build
	docker-compose run --rm $(DOCKER_COMPOSE_APP) bash

#====================================================
# Locks the dependency file (from setup.py)
freeze:
	pipreqs . --savepath requirements.txt

# Upgrades the dependencies lock file
freeze-upgrade:
	echo "do nothing"

#====================================================
# Builds a production docker container
docker-build-production:
	docker build . -t $(DOCKER_IMAGE):latest-production

# Builds a production docker container
docker-build:
	docker build --force-rm $(EXTRA_ARGS) --build-arg SSH_PRIVATE_KEY="$$(cat $(SSH_KEY))" . -t $(BASE_IMAGE)$(DOCKER_IMAGE):$(TAG)

# Pushes the production docker container
docker-push: docker-build
	docker push $(BASE_IMAGE)$(DOCKER_IMAGE):$(TAG)

#====================================================
# Starts a local integration/live test
local-env: local-sidecars build-frame-grabber build-detector
	docker-compose -f docker-compose-local.yml up -d frame-grabber detector

local-sidecars:
	docker-compose -f docker-compose-local.yml up -d redis rabbitmq

local-sidecars-down:
	docker-compose -f docker-compose-local.yml down --remove-orphans

build-frame-grabber:
	git clone git@bitbucket.org:fingermarkltd/frame-grabber.git
	cd frame-grabber && git checkout master  && make build-compose-tests
	rm -rf frame-grabber

build-detector:
	git clone git@bitbucket.org:fingermarkltd/eyecue-detector-mq.git
	cd eyecue-detector-mq && git checkout development && make build-compose-tests
	rm -rf eyecue-detector-mq
