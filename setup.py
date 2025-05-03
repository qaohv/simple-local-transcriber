from setuptools import setup, find_packages

setup(
    name="simple-local-transcriber",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "yt_dlp==2025.4.30",
        "ffmpeg-python==0.2.0",
        "gigaam[longform]==0.1.0",
        "numpy==1.26.4",
        "validators==0.35.0",
    ],  # Dependencies
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