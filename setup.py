from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    long_description = f.readline()

setup(
    name='dnry_config',
    version='0.1.0',
    author='Ian Laird',
    author_email='irlaird@gmail.com',
    url='https://github.com/en0/dnry-config',
    keywords=['config', 'configuration', 'dnry'],
    description='Multi-source config library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['dnry.config'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=requirements,
)