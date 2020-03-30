#!usr/bin/env python
# coding=utf8

from __future__ import print_function

from sys import version
from platform import uname

print("Hello world! From a Python agnostic binary.")
print("Python version:", version.replace("\n", ""))
print("OS version:", " ".join(uname()))
