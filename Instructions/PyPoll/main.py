import os
# from os import path

import pandas as pd

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    pybank = csv.reader(csvfile, delimiter=',')

    ttl_votes = sum(voter_id)
    pct_votes = sum(3/4)
    candidate_total = sum(col(3,4))
    winner = max(candidate_total)