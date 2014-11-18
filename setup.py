from setuptools import setup
import os


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='pyepw',
      version='0.0.1-dev',
      description='Python EPW file generator',
      url='https://github.com/rbuffat/pyepw',
      author='Rene Buffat',
      author_email='buffat@gmail.com',
      license='Apache License 2.0',
      long_description=read('README.md'),
      classifiers=['Development Status :: 2 - Pre-Alpha'],
      packages=['pyepw'],
      zip_safe=False)
