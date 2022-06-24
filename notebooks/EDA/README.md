# Exploratory Data Analysis of Store Sale Data

* No gap between train and test set, in contrast to documentation
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
0.

* Can description of holidays be used? Maybe group the holidays in specific
types of holidays? eg. Navidad-2, Navidad-3
* National holidays might have a stronger impact on sales. Some local
names might be relevant for specific store locations in certain areas.
Unfortunately there is not explicit relationship given.

Missing data:
* days are missing in train set: ['2013-12-25', '2014-12-25', '2015-12-25', '2016-12-25']
* oil data is also missing, and its not related to holidays. Hence it
remains unclear why. Imputation maybe htrough rolling window average.

* problem of unit of sales and how are different product families combined
to give final error? e.g. more sales of certain product categories would
weight  those higher in simple average!


## Decision Tree System for Applications of Models

Reduce data to most promising stores/families:

### Data Type A

* include only Quito city
* Family constraints:
    * exclude BOOKS, LAWN AND GARDEN, SCHOOL & OFFICE SUPPLIES (3 FAMILIES)
* time constraints
    * all data starting August 1st, 2016
* exclude stores sales for specific families for which the start of selling is later than Augst 1st 2016 (see how many)

### Type B

Deal with outliers, other data to categorize

    * BEVERAGES, FAMILIY CElEBRATION: Jul 2015
    DAIRY: DEC 13
    * HOME & KITCHEN I: OCT 2013
    * exclude HOME CARE before mid 2015
* exclude stores which start selling in 2017
* categorize (store, family) tuples into candidates for modeling and those
which should be excluded for now.
    * if zero sales, exclude
    * ...
