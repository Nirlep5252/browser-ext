from setuptools import setup
import re
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with open("browser_ext/__init__.py", "r") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
if not version:
    raise RuntimeError("Version is not set.")

setup(
    name='browser-ext',
    version=version,
    description='An easy way to create browser extensions using Python.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/Nirlep5252/browser-ext',
    author='Nirlep5252',
    packages=["browser_ext"],
    classifiers=['Development Status :: 1 - Planning'],
    license="MIT",
    python_requires='>=3.5.3',
    include_package_data=True,
    keywords=['extension', 'browser', 'chrome', 'firefox']
)
