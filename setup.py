from setuptools import setup, find_packages

with open("requirements.txt") as install_requires_file:
    requirements = install_requires_file.read().strip().split("\n")

setup(
    name="prefect-gcp",
    description="Data Platform using Prefect for orchestration and observability on GCP",
    author="Eden",
    author_email="eden@hiveventures.io",
    keywords="prefect",
    long_description_content_type="text/markdown",
    version="0.0",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.9",
    install_requires=requirements,
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
    ],
)