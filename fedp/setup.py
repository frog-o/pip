# The following comment should be removed at some point in the future.
# mypy: disallow-untyped-defs=False

import os
import sys
from setuptools import find_packages, setup



setup(
    name="fedp",
    version="1.0",
    description="The Freindly Extention to Delvopment Python",
    long_description="Tools to help Delvopment and test version of Pip",

    license='MIT',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    url='https://pip.pypa.io/',
    keywords='distutils easy_install egg setuptools wheel virtualenv pip',
    project_urls={
        "Documentation": "https://pip.pypa.io",
        "Source": "https://github.com/pypa/pip",
        "Changelog": "https://pip.pypa.io/en/stable/news/",
    },

    author='The pip developers and frog-o',
    author_email='pypa-dev@groups.google.com',

    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    #package_data={
    #    "pip._vendor": ["vendor.txt"],
    #    "pip._vendor.certifi": ["*.pem"],
    #    "pip._vendor.requests": ["*.pem"],
    #    "pip._vendor.distlib._backport": ["sysconfig.cfg"],
    #    "pip._vendor.distlib": ["t32.exe", "t64.exe", "w32.exe", "w64.exe"],
    #},
    entry_points={
        "console_scripts": [
            "dpip=fedp.cli.main:main",
            #"pip{}=pip._internal.cli.main:main".format(sys.version_info[0]),
            #"pip{}.{}=pip._internal.cli.main:main".format(
            #    *sys.version_info[:2]
            #),
        ],
    },

    zip_safe=False,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
)
