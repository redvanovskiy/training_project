# Declare phony targets
.PHONY: venv pip test clean

# Default target
local: test

# Create virtual environment
venv:
	python3 -m venv venv

# Install dependencies using pip
install-dependencies: venv
	. venv/bin/activate && pip install -r requirements.txt

test:
	# Remove previous test reports
	rm -rf reports/*
  # Activate virtual environment and run tests using pytest
	. venv/bin/activate && python -m pytest -s -v;
 
clean:
	rm -rf venv
	rm -rf reports/*
	rm -rf .pytest_cache
	rm -rf __pycache__
