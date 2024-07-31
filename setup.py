# coding: utf-8

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyqweather',
    version='1.0.3',
    description='和风天气 api for python3', 
    author='xuwh',  
    author_email='xuwhdev@gmail.com',
    url='https://github.com/imaxu/py-qweather',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)