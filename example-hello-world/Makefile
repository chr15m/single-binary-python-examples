VENV=./venv/bin/activate
MAIN=helloworld

$(MAIN): $(VENV)
	. $(VENV); pex . -r requirements.txt --no-wheel -c $@.py -o $@ --python-shebang='#!/usr/bin/env python'

$(VENV): requirements.txt
	test -d venv || virtualenv venv
	. $(VENV); pip install -Ur requirements.txt
	touch $(VENV)

.PHONY: clean

clean:
	rm -rf $(MAIN) venv
