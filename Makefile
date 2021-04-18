.PHONY: install
install:
	pip3 install -e .
	pip3 install -e .[devel]

.PHONY: format
format:
	find src/backend -name "*.py" | xargs black
	black setup.py