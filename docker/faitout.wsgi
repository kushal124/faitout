#-*- coding: utf-8 -*-

# The three lines below are required to run on EL6 as EL6 has
# two possible versions of python-sqlalchemy and python-jinja2
# These lines make sure the application uses the correct version.
#import __main__
#__main__.__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
#import pkg_resources

## Set the environment variable pointing to the configuration file
import os
os.environ['FAITOUT_CONFIG'] = '/etc/faitout/faitout.cfg'

## The following is only needed if you did not install faitout
## as a python module (for example if you run it from a git clone).
import sys
sys.path.insert(0, '/srv/faitout/')


## The most import line to make the wsgi working
from faitout import APP as application
application.debug = True
