# Exploratory Data Analysis of Store Sale Data

* No gap between train and test set
* Problem of the forecasting scenario
* the transactions data goes only until the end of train.csv, and hence
cannot be used as daily features for the test data, only as aggregates.
* Using transactions with missing values is tricky, as we don't know
why exactly the transactions are missing. Hence do not include this
feature in modelling.

* > Did not all start a the same time. Data is not avialalbe for all stores equally.
A few stores start selling products later in 2013, or even 2014, 2015 and 2017.
For these stores less data will be available for predictions

* Some stores have not sold certain categories, e.g. BOOKS and we don't
have data to predict on store level. IMpossible to predict for these or
do we just predict 0?

> Given the complexity, maybe its the best to handle with different cases/
scenario, decision tree on which method to use, based on which family and which store?
e.g. with too little data, use baseline method? if 0 sales, predict constantly
0...
