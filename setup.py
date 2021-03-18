from pathlib import Path

from setuptools import setup

# load long description
p = Path("README.md")
long_description = p.read_text() if p.exists() else None

setup(
    name='pz',
    version='1.0.0-rc.1',
    author='Edvard Rejthar',
    author_email='edvard.rejthar@nic.cz',
    url='https://github.com/CZ-NIC/pz',
    license='GNU GPLv3',
    description='Ever wished to use the Python syntax to work in Bash?'
                ' Then pythonize it, piping the contents through your tiny Python script with `pz` utility!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=['pz'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6',
)
