import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="jsdict",
    version="1.0.0",
    author="zevaryx",
    author_email="zevaryx@gmail.com",
    description="Javascript-syle Dictionaries in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zevaryx/jsdict",
    packages=["jsdict"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
)
