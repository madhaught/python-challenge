# First need to import the os module to create file paths 
# and the csv module for reading CSV files
import os
import csv

# Next create path for reading the CSV file budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# open file with path created and create reader with csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and store the header row
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Store value of row 2 in csv, to use when determining monthly profit
    previous = next(csvreader)

    # after the header and row 2, read each row of data and perform functions
    for row in csvreader:
        print(row[0])

    #calculate values

    #print analysis
    #print("Financial Analysis")
    #print("----------------------------")
    #print("Total Months: " + total_months)
    #print("Total: " + net_total)
    #print("Average Change: " + average_change)
    #print("Greatest Increase in Profits: " + greatest_profit_increase)
    #print("Greatest Decrease in Profts: " + greatest_profit_decrease)
  