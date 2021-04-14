# (C) Copyright Artificial Brain 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
import setuptools
import inspect

if not hasattr(setuptools, 'find_namespace_packages') or not inspect.ismethod(setuptools.find_namespace_packages):
    print("Your setuptools version:'{}' does not support PEP 420 (find_namespace_packages). "
          "Upgrade it to version >='40.1.0' and repeat install.".format(setuptools.__version__))
    sys.exit(1)

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()

setuptools.setup(
    name='quantumcat',
    version='0.1',
    description='A cross platform high-level quantum computing library',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Artificial Brain Development Team',
    author_email='setup@artificialbrain.in',
    license='Apache-2.0',
    # packages=setuptools.find_namespace_packages(include=['quantumcat.*']),
    packages=setuptools.find_namespace_packages(),
    install_requires=REQUIREMENTS,
    include_package_data=True,
)
