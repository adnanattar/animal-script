from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='animal-script',
    version='0.4',
    packages=find_packages(),
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'animal-script = animal_script.interpreter:main',
        ],
    },
)
