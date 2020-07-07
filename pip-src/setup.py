# The following comment should be removed at some point in the future.
# mypy: disallow-untyped-defs=False

import os
import sys
from setuptools import find_packages, setup



setup(
    name="pip-src",
    version="1.0",
    description="The sourecode manger tool for pip using cvs(just git at the moment)",
    long_description="The sourecode manger tool for pip using cvs(just git at the moment)",

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
    url='https://github.frogo.pip/',
    keywords='distutils easy_install egg setuptools wheel virtualenv pip',
    project_urls={
        "Documentation": "https://pip.pypa.io",
        "Source": "https://github.com/frog-o/pip",
    },

    author='frog-o',

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
            "spip =spip.cli.main:main",
            #"pip{}=pip._internal.cli.main:main".format(sys.version_info[0]),
            #"pip{}.{}=pip._internal.cli.main:main".format(
            #    *sys.version_info[:2]
            #),
        ],
    },

    zip_safe=False,
    install_requires=['venvctrl==0.4.2'],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
)
