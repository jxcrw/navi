#!/usr/bin/python
"""Benchmark and profile Python code."""
# Jak Crow
# Created: 2018/02/04

import cProfile
import os
import pstats
import timeit

def wrapper(function, *args, **kwargs):
    def wrapped():
        return function(*args, **kwargs)
    return wrapped

def my_function(x, y):
    return (y - x)/x*100

# # ─────────────────────────────────────────────────────────────────────────────
# # Put test code here

# # ─────────────────────────────────────────────────────────────────────────────

# N = 298502
# test = pd.to_datetime(datetime.date(2017, 1, 15))

# wrapped = wrapper(get_first_day, test)
# runtime = timeit.timeit(wrapped, number=N)
# print(f'{runtime:,.3f}')

# wrapped = wrapper(get_last_day, test)
# runtime = timeit.timeit(wrapped, number=N)
# print(f'{runtime:,.3f}')

# ─────────────────────────────────────────────────────────────────────────────

# # From command prompt run: python -m cProfile -o profiling_results "full_path_to_script.py"
os.chdir(r'C:\Users\jak\ALL\DV\Translation Workflow Automation\Patent Market Research')
with open('profiling_results.py', 'w+', encoding='utf-8') as file:
    stats = pstats.Stats('profiling_results', stream=file)
    stats.strip_dirs().sort_stats('cumulative').print_stats()
