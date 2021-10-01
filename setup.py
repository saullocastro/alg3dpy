import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

VERSION = "0.18.1"

CLASSIFIERS = """\

Development Status :: 4 - Beta
Intended Audience :: Science/Research
Intended Audience :: Education
Topic :: Scientific/Engineering
Topic :: Education
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: POSIX :: BSD
Operating System :: Microsoft :: Windows
Operating System :: Unix
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
License :: OSI Approved :: BSD License

"""

setup(
    name = "alg3dpy",
    version = VERSION,
    author = "Saullo G. P. Castro",
    author_email = "S.G.P.Castro@tudelft.nl",
    description = ("3D Algebra in Python"),
    license = "BSD",
    keywords = "algebra 3D mathematics geometry",
    url = "https://github.com/saullocastro/alg3dpy",
    packages=find_packages(),
    long_description=read('README.rst'),
    classifiers = [_f for _f in CLASSIFIERS.split('\n') if _f],
    install_requires=["numpy"],
)

with open("./alg3dpy/version.py", "wb") as f:
    f.write(b'__version__ = "%s"\n' % VERSION.encode())

