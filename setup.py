"""Package configuration for AnimalScript."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="animal-script",
    version="1.0.0",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adnanattar/animal-script",
    author="Adnan B. Attar",
    author_email="hello@androtechbuddy.com",
    license="MIT",
    python_requires=">=3.9",
    install_requires=[
        # AnimalScript currently has no runtime dependencies.
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Education",
    ],
    entry_points={
        "console_scripts": [
            "animal-script = animal_script.main:main",
        ],
    },
)
