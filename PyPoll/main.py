# import os module to create file paths and csv module for reading CSV files
import os
import csv

# create path for reading the CSV file election_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')

# open file with path created and create reader with csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and store the header row
    csv_header = next(csvreader)
    
    #create lists to sort votes into
    stockham = []
    degette = []
    doane = []

    # Define variable to count total number of votes and create for loop to count
    total_votes = 0
    for row in csvreader:
        total_votes += 1
        
        # sort votes into lists based on which candidate they were cast for
        if row[2] == "Charles Casper Stockham":
            stockham.append(row)

        elif row[2] == "Diana DeGette":
            degette.append(row)

        else:
            doane.append(row)

    # count the number of votes in each list
    stockham_votes = 0
    for i in stockham:
        stockham_votes +=1

    degette_votes = 0
    for i in degette:
        degette_votes += 1

    doane_votes = 0
    for i in doane:
        doane_votes += 1

    # Determine the percentage of the total votes each candidate got and 
    # format it as a percentage
    # https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value
    stockham_percent = f"{(stockham_votes/total_votes):.3%}"

    degette_percent = f"{(degette_votes/total_votes):.3%}"

    doane_percent = f"{(doane_votes/total_votes):.3%}"

    most_votes = max(stockham_percent, degette_percent, doane_percent)

    # determine the winner of the election by which candidate had the most votes
    winner = "Candidate"
    if most_votes == stockham_percent:
        winner = "Charles Casper Stockham"

    elif most_votes == degette_percent:
        winner = "Diana DeGette"

    else:
        winner = "Raymon Anthony Doane"

    #print analysis
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    print("Charles Casper Stockham: " + stockham_percent + " (" + str(stockham_votes) + ")")
    print("Diana DeGette: " + degette_percent + " (" + str(degette_votes) + ")")
    print("Raymon Anthony Doane: " + doane_percent + " (" + str(doane_votes) + ")")
    print("-------------------------")
    print("Winner: " + str(winner))
    print("-------------------------")

# write output file
# https://www.pythontutorial.net/python-basics/python-write-text-file/
output_path = os.path.join("analysis", "results.txt")
lines = ["Election Results", "-------------------------","Total Votes: " 
         + str(total_votes), "-------------------------", "Charles Casper Stockham: " 
         + stockham_percent + " (" + str(stockham_votes) + ")", "Diana DeGette: " + 
         degette_percent + " (" + str(degette_votes) + ")", "Raymon Anthony Doane: " + 
         doane_percent + " (" + str(doane_votes) + ")", "-------------------------", 
         "Winner: " + str(winner), "-------------------------"]
with open(output_path, 'w') as f:
    f.writelines('\n'.join(lines))