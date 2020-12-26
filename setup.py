import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SomeRandomAPI",
    version="0.0.1",
    author="BruhDev",
    author_email="mr.bruh.dev@gmail.com",
    description="A wrapper library for some-random-api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bruhdev.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)