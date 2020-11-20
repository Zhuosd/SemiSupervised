import codecs
import os
import sys

try:
	from setuptools import setup
except:
	from distutils.core import setup

import setuptools

def read(fname):
	return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

#long_des = read("README.rst")

with open("README.rst", "r") as fh:
	long_description = fh.read()

platforms = ['linux/Windows']
classifiers = [
	'License :: OSI Approved :: MIT License',
	'Intended Audience :: Developers',
	'Intended Audience :: Education',
	'Intended Audience :: Science/Research',
	'Development Status :: 3 - Alpha',
	'Topic :: Scientific/Engineering',
	'Topic :: Scientific/Engineering :: Artificial Intelligence',
	'Topic :: Software Development',
	'Topic :: Software Development :: Libraries',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	"Operating System :: OS Independent",
]

install_requires = [
	'numpy',
	'pandas'
]

	
setup(
	name='semisupervised',
	version='0.0.1',
	description='Python implementation of semi-supervised learning algorithm',
	long_description=long_description,
	#py_modules=['pyssl'],
	packages=setuptools.find_packages(),
	author = "Rosefun",  
	author_email = "rosefun@foxmail.com" ,
	url = "https://github.com/rosefun/pyssl" ,
	download_url='https://github.com/rosefun/pyssl/tags',
	python_requires=">=3.0",
	#license="Apache License, Version 2.0",
	platforms=platforms,
	classifiers=classifiers,
	install_requires=install_requires,
	keywords=['semi-supervised learning','ssl', 'deep learning', 'machine learning']
	)   