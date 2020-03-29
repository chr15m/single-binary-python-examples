VENV=./venv/bin/activate

demo: $(VENV)
	. $(VENV); pex . -r requirements.txt --no-wheel -c demo.py -o demo --python-shebang='#!/usr/bin/env python'

$(VENV): requirements.txt
	test -d venv || virtualenv venv
	. $(VENV); pip install -Ur requirements.txt
	touch $(VENV)

.PHONY: clean

clean:
	rm -rf demo venv
