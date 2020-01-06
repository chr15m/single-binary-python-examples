#!usr/bin/env python
# coding=utf8

from __future__ import print_function

import sh
from sys import version

print("Hello from a Python agnostic binary!")
print("Python version:", version)
print("Uname:", sh.uname("-a"))
