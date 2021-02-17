from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="webservermap",
    version=VERSION,
    description="Api to provide a common stack to any host environment",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="webserver web server host environment",
    url="https://github.com/danilocgsilva/webservermap",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["webservermap"],
    include_package_data=True
)

