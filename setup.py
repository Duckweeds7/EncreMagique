import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()
requires = (HERE / 'requirements.txt').read_text().split('\n')

setup(
    name="encre-magique",
    version="1.0.0",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Duckweeds7/EncreMagique",
    author="Duckweeds7",
    author_email="root@duckweeds7.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=('datasets', 'outputs')),
    include_package_data=True,
    install_requires=requires,
)