# import os module to create file paths and csv module for reading CSV files
import os
import csv

# create path for reading the CSV file budget_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')

# open file with path created and create reader with csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and store the header row
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #calculate values

    #print analysis
    #print("Election Results")
    #print("-------------------------")
    #print("Total Votes: " + total_votes)
    #print("-------------------------")
    #print("Charles Casper Stockham: " + stockham_votes)
    #print("Diana DeGette: " + degette_votes)
    #print("Raymon Anthony Doane: " + doane_votes)
    #print("-------------------------")
    #print("Winner: " + winner)
    #print("-------------------------")