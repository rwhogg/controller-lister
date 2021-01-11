from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="controller-lister",
    version="1.0.0",
    description="Controller lister",
    license="LGPL-2.1",
    long_description=long_description,
    author="Bob Wombat Hogg",
    author_email="wombat@rwhogg.site",
    url="https://github.com/rwhogg/controller-lister",
    packages=["controller-lister"],
    install_requires=["guizero", "pygame"],
)
