import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SomeRandomAPI",
    version="0.0.6",
    author="BruhDev",
    author_email="mr.bruh.dev@gmail.com",
    description="A wrapper library for some-random-api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bruhdev.com",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires=">=3.7",
)
