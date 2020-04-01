from distutils.core import setup
from glob import glob
setup(name='webserver', version='0.0.1', scripts=['webserver.py'], data_files=[('bin/pages', glob("pages/*"))])
