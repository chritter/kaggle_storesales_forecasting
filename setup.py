"""setup.py for installing the package."""

from setuptools import (  # pylint: disable=missing-module-docstring
    find_packages,
    setup,
)

setup(
    name="kaggle_storesales_forecasting",
    packages=find_packages(include=["kaggle_storesales_forecasting"]),
    version="0.1.0",
    description="Kaggle Storesales Forecasting",
    author="christian ritter",
    license="MIT",
    entry_points="""
        [console_scripts]
        download_kaggle_data=kaggle_storesales_forecasting.data.download_dataset:download_kaggle_data
    """,
)
