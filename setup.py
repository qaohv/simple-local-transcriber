import pkg_resources
from setuptools import setup, find_packages

setup(
    name="simple-local-transcriber",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open("requirements.txt", "r", encoding="utf-8").read()
        )
    ],
    entry_points={
        "console_scripts": [
            "slt=src.cli:cli",
        ],
    },
    author="Denis Ryabokon",
    author_email="d.v.ryabokon@gmail.com",
    description="A simple local transcriber tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/qaohv/slt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.11.*",
)