install-pkg:
	@echo Installing dependencies
	pip3 install -e .
	pip3 install -e .[devel]

.PHONY: install
install: install-pkg
	@echo Compiling and installing npm dependencies
	(cd src/frontend && npm install && npm run build && cd -)

.PHONY: format
format:
	find src/backend -name "*.py" | xargs black
	black setup.py