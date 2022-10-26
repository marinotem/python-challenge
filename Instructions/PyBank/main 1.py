
# Module for reading CSV files
import os
import csv
import pandas as pd

csvpath = os.path.join('Resources', 'budget_data.csv')

change = []
avg_change = []
greatest_inc = [0,"April"]
greatest_decr = [0, "May"]
month_tracker = []
months = []
net = []
net_total = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # CSV reader specifies delimiter and variable that holds contents

   # csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #defining some variables
    titles = next(csvreader)
    fr = next(csvreader)
    pre_val = int(fr[1])
    first_month = (fr[0])
     
    #place holder list for changes 
    change = []
    months.append(first_month)
    net.append(pre_val)
    print(months)
    print(net)

    # difference between months change
    for row in csvreader:
        months.append(row[0])
        net.append(int(row[1]))
        avg_change = (int(row[1]) - pre_val)
        pre_val = int(row[1])
        change.append(avg_change)
        if avg_change > greatest_inc[0]:
              greatest_inc[0] = avg_change
              greatest_inc[1] = row[0]
        elif avg_change < greatest_decr[0]:
            greatest_decr[0] = avg_change
            greatest_decr[1] = row[0]

    ttl_months = len(months)
    avg_of_changes = sum(i for i in change)/len(change)
    net_total = sum(net)

    print("Financial Analysis:")
    print(f"Total = {net_total}")
    print(f"Average Change = {avg_of_changes}")
    print(f"Geatest Increase in profits = {greatest_inc[1]} ({greatest_inc[0]})")
    print(f"Greatest Decrease in profits = {greatest_decr[1]} ({greatest_decr[0]})")

    with open("output.txt", "a") as f:
        print("Financial Analysis:", file=f)
        print(f"Total = {net_total}",file=f)
        print(f"Average Change = {avg_of_changes}",file=f)
        print(f"Geatest Increase in profits = {greatest_inc[1]} ({greatest_inc[0]})",file=f)
        print(f"Greatest Decrease in profits = {greatest_decr[1]} ({greatest_decr[0]})",file=f)
        