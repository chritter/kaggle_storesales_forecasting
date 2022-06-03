Getting started
===============

Work for the Kaggle Competition [Store Sales - Time Series Forecasting
](https://www.kaggle.com/competitions/store-sales-time-series-forecasting).

I use jupytext to allow effective version control and code sharing of Jupyter notebooks.

Setup
^^^^^

To install the environment you can use pip installation or you use the frozen
environment based on the conda yaml and requirements.txt.

Install package in development mode:

.. code:: bash

    pip install -e .

Add development dependencies:

.. code:: bash

    pip install pytest flake8 black

install pre-commit hooks:

.. code:: bash

    pip install pre-commit
    pre-commit install
