import os
# from os import path

import pandas as pd

# Module for reading CSV files
import csv

#csvpath = os.path.join('Resources', 'election_data.csv')
csvpath = './Resources/election_data.csv'
votes = []
candidates = []
pct_votes = []
pct = 0
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    first_row = next(csvreader)

    df =  pd.DataFrame(csvreader)
    candidates = list(df[2].unique())
    votes = sum(list(df[0].value_counts()))
    candidate_votes = (list(df[2].value_counts()))

    x = 0

    for v in candidate_votes:
        pct = round(candidate_votes[x]/votes,3)
        pct="{:.3%}".format(pct)
        pct_votes.append(pct)
        x+=1

    final = list(zip(candidates,candidate_votes,pct_votes))
    winner_calc = max(final, key=lambda x: x[1])
    
    print("Election Results:", file = f)
    print(f"Total Votes: {votes}", file =f)
    print(f"{final}", file=f)
    print(winner_calc[0],file=f)

    with open("output.txt", "a") as f:
        print("Election Results:", file = f)
        print(f"Total Votes: {votes}", file =f)
        print(f"{final}", file=f)
        print(winner_calc[0],file=f)


