from setuptools import setup, find_packages
import os

# List of required dependencies
install_requires = [
    "mailchimp3~=3.0.2",
    "oauth2client~=4.1.2",
    "gspread~=3.0.0",
    "beautifulsoup4~=4.6.3",
    "requests~=2.24.0",
    "geopy~=1.18.1",
    "pandas>=0.25.0",
    "algoliasearch>=2.0,<3.0",
    "spacy~=2.2.4",
]

# Current directory
here = os.path.abspath(os.path.dirname(__file__))

# Read the long description from README.md
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Setup configuration
setup(
    name="rasa-demo",
    version="2.0.0",
    description="Rasa Demo Bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rasa Technologies GmbH",
    author_email="kartikshastrakar04@gmail.com",
    maintainer="Kartik-Shastrakar",
    maintainer_email="kartikshastrakar@rasa.com",
    license="GNU General Public License v3.0",
    url="https://github.com/rasahq/rasa-demo",
    download_url="https://github.com/RasaHQ/rasa-demo/archive/main.zip",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(where="demo"),
    install_requires=install_requires,
    project_urls={
        "Bug Reports": "https://github.com/rasahq/rasa-demo/issues",
        "Source": "https://github.com/RasaHQ/rasa-demo",
    },
    python_requires='>=3.6',
)
