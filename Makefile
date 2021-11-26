##########################

# === GLOBAL VARIABLES ======================================================
TEST_COVERAGE_PERCENTAGE=80

# === COMMANDS ==============================================================
# Installs the Python dependencies
install:
	pip3 install -r requirements.txt

# Downloads the Python dependencies
download:
	pip3 download -r requirements.txt


#====================================================
# Runs all tests
tests:
	python -m pytest unit -v

tests-coverage:
	coverage run -m pytest unit -v
	coverage report -m --fail-under=$(TEST_COVERAGE_PERCENTAGE)

#====================================================
# Locks the dependency file (from setup.py)
freeze:
	pipreqs . --savepath requirements.txt
