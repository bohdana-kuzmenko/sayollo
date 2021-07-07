from setuptools import setup, find_packages

with open('requirements.txt') as requirements_txt:
    install_requires = requirements_txt.read().splitlines()

setup(
    name='sayollo',
    version='0.0.1',
    description='Test',
    author='Bohdana Kuzmenko',
    author_email='bogdana.kuzmenko.16@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
)