# -*- coding: utf-8 -*-
# Copyright (c) 2018 Christiaan Frans Rademan.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holders nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
import os
import sys
import imp
try:
    from setuptools import setup
except ImportError:
    def setuptools():
        print('Requires `setuptools` to be installed')
        print('`pip install setuptools`')
        exit()

from setuptools import find_packages

if not sys.version_info >= (3, 5):
    print('Requires python version 3.5 or higher')
    exit()

# Add the current directory to the module search path.
sys.path.insert(0, os.path.abspath('.'))

# Constants
CODE_DIRECTORY = 'tachyonic_sphinx'
DOCS_DIRECTORY = 'docs'
TESTS_DIRECTORY = 'tests'
PYTEST_FLAGS = ['--doctest-modules']


# Miscellaneous helper functions
def read(filename):
    """Return the contents of a file.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


metadata = imp.load_source(
    'metadata', os.path.join(CODE_DIRECTORY, 'metadata.py'))


# install-requires.txt as install_requires
# minimal dependencies to run.
install_requires = []
if os.path.exists(os.path.join(os.path.dirname(__file__),
                               'install-requires.txt')):
    with open(os.path.join(os.path.dirname(__file__),
                           'install-requires.txt')) as req:
        install_requires = req.read().splitlines()

# dependency-links.txt as dependency_links
# locations of where to find dependencies within
# install-requires.txt ie github.
# setuptools does work with url format for pip.
dependency_links = []
if os.path.exists(os.path.join(os.path.dirname(__file__),
                               'dependency-links.txt')):
    with open(os.path.join(os.path.dirname(__file__),
                           'dependency-links.txt')) as req:
        dependency_links = req.read().splitlines()

# See here for more options:
# <http://pythonhosted.org/setuptools/setuptools.html>
setup_dict = dict(
    name=metadata.package,
    version=metadata.version,
    author=metadata.authors[0],
    author_email=metadata.emails[0],
    maintainer=metadata.authors[0],
    maintainer_email=metadata.emails[0],
    license=metadata.license,
    url=metadata.url,
    description=metadata.description,
    long_description=read('README.rst'),
    include_package_data=True,
    classifiers=metadata.classifiers,
    packages=find_packages(exclude=(TESTS_DIRECTORY,)),
    install_requires=[] + install_requires,
    dependency_links=dependency_links,
    zip_safe=False,  # don't use eggs
    entry_points={
        'sphinx.html_themes': [
            'tachyonic = tachyonic_sphinx',
        ],
    },
)


def main():
    setup(**setup_dict)


if __name__ == '__main__':
    main()
