from setuptools import setup, find_packages

version = "0.0.1"

setup(
    name='pyperseus_treebank',
    version=version,
    packages=find_packages(exclude=["tests"]),
    url='https://github.com/ponteineptique/pyperseus-treebank',
    license='GNU GPL v2',
    author='Thibault Clerice',
    author_email='leponteineptique@gmail.com',
    description='Perseus XML Treebank Parser',
    test_suite="tests",
    install_requires=[
        "lxml"
    ],
    test_requires=[
        "coverage==4.4.1"
    ]
)