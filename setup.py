from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='animal-script',
    version='0.8',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adnanattar/animal-script",
    author="Adnan B. Attar",
    author_email="hello@androtechbuddy.com",
    license="MIT",
    install_requires=[
        # No any dependencies
    ],
    entry_points={
        'console_scripts': [
            'animal-script = animal_script.main:main',
        ],
    },
)
