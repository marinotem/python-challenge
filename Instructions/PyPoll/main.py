import os
# from os import path

import pandas as pd

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

votes = []
candidates = []
pct_votes = 0.0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    first_vote = next(csvreader)
    pre_val = int(fr[0])
    print(pre_val)


