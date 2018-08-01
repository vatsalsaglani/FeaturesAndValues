import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FeaturesAndValues_pkg",
    version="0.0.1",
    author="Vatsal Saglani",
    author_email="youknowiamtrying@gmail.com",
    description="A ML python package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vatsalsaglani/FeaturesAndValues",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)