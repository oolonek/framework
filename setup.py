import os
import io
from setuptools import setup, find_packages


# Helpers


def read(*paths):
    """Read a text file."""
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, *paths)
    contents = io.open(fullpath, encoding="utf-8").read().strip()
    return contents


# Prepare


PACKAGE = "frictionless"
NAME = PACKAGE.replace("_", "-")
TESTS_REQUIRE = [
    "moto",
    "httpx",
    "black",
    "yattag",
    "pylama",
    "pytest",
    "pyright==1.1.308",
    "ipython",
    "livemark",
    "pytest-cov",
    "pytest-vcr",
    "pytest-mock",
    "pytest-only",
    "oauth2client",
    "requests-mock",
    "pytest-dotenv",
    "pytest-timeout",
    "pytest-lazy-fixture",
]
EXTRAS_REQUIRE = {
    "aws": ["boto3>=1.9"],
    "bigquery": ["google-api-python-client>=1.12.1"],
    "ckan": ["frictionless-ckan-mapper>=1.0"],
    "csv": [],
    "dev": TESTS_REQUIRE,
    "excel": ["xlrd>=1.2", "xlwt>=1.2", "openpyxl>=3.0", "tableschema-to-template>=0.0"],
    "json": ["ijson>=3.0", "jsonlines>=1.2"],
    "github": ["pygithub>=1.50"],
    "gsheets": ["pygsheets>=2.0"],
    "html": ["pyquery>=1.4"],
    "markdown": ["livemark>=0.110"],
    "mysql": ["sqlalchemy>=1.4", "pymysql>=1.0"],
    "ods": ["ezodf>=0.3", "lxml>=4.0"],
    "pandas": ["pandas>=1.0"],
    "parquet": ["fastparquet>=0.8"],
    "postgresql": ["sqlalchemy>=1.4", "psycopg>=3.0", "psycopg2>=2.9"],
    "server": ["fastapi>=0.78", "uvicorn>=0.17", "python-multipart>=0.0"],
    "spss": ["savReaderWriter>=3.0"],
    "sql": ["sqlalchemy>=1.4"],
    "visidata": ["visidata>=2.10"],
    "wkt": ["grako>=3.99"],
    "zenodo": ["pyzenodo3>=1.0"],
    "datasette": ["datasette>=0.64.2"],
}
EXTRAS_REQUIRE["framework"] = (
    EXTRAS_REQUIRE["ckan"]
    + EXTRAS_REQUIRE["csv"]
    + EXTRAS_REQUIRE["excel"]
    + EXTRAS_REQUIRE["json"]
    + EXTRAS_REQUIRE["sql"]
)
EXTRAS_REQUIRE["application"] = (
    EXTRAS_REQUIRE["framework"] + EXTRAS_REQUIRE["markdown"] + EXTRAS_REQUIRE["server"]
)
INSTALL_REQUIRES = [
    "petl>=1.6",
    "marko>=1.0",
    "attrs>=22.2.0",
    "jinja2>=3.0",
    "pyyaml>=5.3",
    "isodate>=0.6",
    "rfc3986>=1.4",
    "chardet>=3.0",
    "pydantic>=1.9",
    "requests>=2.10",
    "humanize>=4.2",
    "tabulate>=0.8.10",
    "jsonschema>=2.5",
    "simpleeval>=0.9.11",
    "stringcase>=1.2",
    "typer[all]>=0.5",
    "validators>=0.18",
    "python-slugify>=1.2",
    "python-dateutil>=2.8",
    "typing-extensions>=4.3",
]
README = read("README.md")
VERSION = read(PACKAGE, "__version__")
PACKAGES = find_packages(exclude=["tests"])
ENTRY_POINTS = {"console_scripts": ["frictionless = frictionless.__main__:console"]}


# Run


setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require=EXTRAS_REQUIRE,
    entry_points=ENTRY_POINTS,
    zip_safe=False,
    long_description=README,
    long_description_content_type="text/markdown",
    description="Data management framework for Python that provides functionality to describe, extract, validate, and transform tabular data",
    author="Open Knowledge Foundation",
    author_email="info@okfn.org",
    url="https://github.com/frictionlessdata/frictionless-py",
    license="MIT",
    keywords=[
        "data validation",
        "frictionless data",
        "open data",
        "json schema",
        "json table schema",
        "data package",
        "tabular data package",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
