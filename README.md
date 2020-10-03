XIRR calculation (in Python)
=============================

Introduction
============

XIRR stands for Extended Internal Rate of Return and is used to calculate return on investments made at different time periods which need not be periodic.

XIRR gives the annualized return of a portfolio that include all cash flows.

XIRR is a financial function available in Excel. The drawback with Excel's XIRR is that it will show the 0% XIRR as a default for negative returns.

For use in Python, I have written this code which calculates XIRR for both positive and negative returns. For the same XIRR calculation using R, please check my other repository: [**XIRR_in_R**](https://github.com/SunilVeeravalli/XIRR_in_R)

I hope you find my xirr function useful.

System requirements
-------------------

1.  Python
2.  Libraries: Pandas, Numpy

Data requirements
-----------------

Prepare your data in two columns:
1. First column - dates
2. Second column - amounts. The invested amount (debit) should be given a negative sign and the redemptions (credit) should be given a positive sign.

Note: Please find the sample data provided in the repository

-   Sample\_Positive\_Returns.csv
-   Sample\_Negative\_Returns.csv



Example: Positive returns
-------------------------

Import the data into R and check the table.

``` r
positive.returns <- read_csv(file = "Sample_Positive_Returns.csv", col_names = TRUE)
```

``` r
head(positive.returns)
```

    ## # A tibble: 6 x 2
    ##   dates      amount
    ##   <chr>       <dbl>
    ## 1 23/03/1990  -1350
    ## 2 23/07/1990   -600
    ## 3 31/10/1990  -1250
    ## 4 13/11/1990  -3550
    ## 5 30/01/1991   -850
    ## 6 03/05/1991  -3600

Since the dates columns is character data type, change it to date data type.

``` r
positive.returns$dates <- as.Date(positive.returns$dates, format = "%d/%m/%Y")
```

Now use the XIRR function

``` r
xirr(positive.returns)
```

    ## [1] "XIRR is 17.425%"

That is, the return of our portfolio is **17.425%** per annum.

Example: Negative returns
-------------------------

Import the data into R and check the table.

``` r
negative.returns <- read_csv(file = "Sample_Negative_Returns.csv", col_names = TRUE)
```

``` r
head(negative.returns)
```

    ## # A tibble: 6 x 2
    ##   dates      amount
    ##   <chr>       <dbl>
    ## 1 09/05/1990   9000
    ## 2 01/07/1990   5100
    ## 3 30/08/1990   9700
    ## 4 28/12/1990  -5300
    ## 5 13/01/1991  -2200
    ## 6 16/01/1991   9800

Since the dates columns is character data type, change it to date data type.

``` r
negative.returns$dates <- as.Date(negative.returns$dates, format = "%d/%m/%Y")
```

Now use the XIRR function

``` r
xirr(negative.returns)
```

    ## [1] "XIRR is -79.845%"

That is, the return of our portfolio is **-79.845%** per annum.









