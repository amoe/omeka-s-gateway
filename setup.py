import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="omeka-s-gateway",
    version="0.0.4",
    author="David Banks",
    author_email="amoebae@gmail.com",
    description="Omeka-S REST API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amoe/omeka-s-gateway",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
