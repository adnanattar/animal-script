from setuptools import setup, find_packages

setup(
    name='animal-script',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'animal-script = animal_script.interpreter:main',
        ],
    },
)
