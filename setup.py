from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    long_description = f.readline()

setup(
    name='dnry_configuration',
    version='0.1.0',
    author='Ian Laird',
    author_email='irlaird@gmail.com',
    url='https://github.com/irlaird/dnry-configuration',
    description='Multi-source configuration library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['dnry.configuration'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=requirements,
)