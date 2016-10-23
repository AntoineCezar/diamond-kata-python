VIRTUAL_ENV?=.venv
PYTHON?=$(VIRTUAL_ENV)/bin/python
PIP?=$(VIRTUAL_ENV)/bin/pip
WATCHMEDO?=$(VIRTUAL_ENV)/bin/watchmedo

virtualenv: $(PYTHON)
$(PYTHON):
	virtualenv $(VIRTUAL_ENV)

watch-test: $(WATCHMEDO)
	$(WATCHMEDO) shell-command \
		--patterns="*.py" \
		--command='$(MAKE) test' \
		--drop \
		.

test:
	$(PYTHON) -m unittest

$(WATCHMEDO): virtualenv
	$(PIP) install watchdog
