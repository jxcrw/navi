#!/usr/bin/python
"""Demo pandas for the first time."""
# From: http://pandas.pydata.org/pandas-docs/stable/10min.html
# 2014/02/08

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_series = pd.Series([1, 3, 5, np.nan, 6, 8])
print(my_series)

my_list = [1, 2, 3, 4, 5]
my_series = pd.Series(my_list)
print(my_series)

my_tuple = (1, 2, 3, 4, 5)
my_series = pd.Series(my_tuple)
print(my_series)

dates = pd.date_range('20130101', periods=6)
frame = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(frame)

print(frame.dtypes)
print(frame.head(2))
print(frame.tail(2))
