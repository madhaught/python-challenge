# import the os module to create file paths and csv module for reading CSV files
import os
import csv

# create path for reading the CSV file budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')
    
# open file with path created and create reader with csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and store the header row
    csv_header = next(csvreader)

    # define variables and create lists before creating a for loop
    total_months = 0
    profits = []
    profit_change = []
    dates = []
   
   # Use a for loop to: get month count by counting each row of data 
   # after header row, add each row of data to separate lists
    for row in csvreader:
        total_months += 1 
        profits.append(row[1])
        dates.append(row[0])
    
    # define variable and get sum of all data in profits list
    net_profit = 0
    for i in profits:
        i = int(i)
        net_profit += i

        # determine the changes in profit per month by subtracting the profit of
        # the previous month from the current month (successive difference in values)
        # https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/
        profit_change = [int(profits[i + 1]) - int(profits [i]) for i in range (len(profits)-1)]
    
    # determine the total change in profits by adding up the individual values
    # of the change in monthly profits
    net_change = 0
    for i in profit_change:
        i = int(i)
        net_change += i
    
    # create a list of dates with the corresponding length and index numbers
    # to the profit_change list
    # https://www.geeksforgeeks.org/python-removing-first-element-of-list/
    reduced_dates = dates[1:]

    # determine the average change in profits by dividing net_change by the number
    # of values in net_change
    # https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings
    average_change = f"{(net_change/(total_months-1)):.2f}"
   
    # find the greatest increase in profits and the greatest decrease
    greatest_increase = max(profit_change)
    greatest_decrease = min(profit_change)

    # find the index number of the greatest increase and decrease in the list
    index_increase = profit_change.index(greatest_increase)
    index_decrease = profit_change.index(greatest_decrease)

    # use the stored index number to find the month of the greatest increase and
    # decrease in profits in the date list
    val1 = reduced_dates[index_increase]
    val2 = reduced_dates[index_decrease]

    # print analysis
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(net_profit))
    print("Average Change: " + "$" + average_change)
    print("Greatest Increase in Profits: " + val1 + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profts: " + val2 + " ($" + str(greatest_decrease) + ")")

# write output file
# https://www.pythontutorial.net/python-basics/python-write-text-file/
output_path = os.path.join("analysis", "results.txt")
lines = ["Financial Analysis", "----------------------------", 
         "Total Months: " + str(total_months), "Total: " + "$" + str(net_profit), 
         "Average Change: " + "$" + average_change, "Greatest Increase in Profits: " 
         + val1 + " ($" + str(greatest_increase) + ")", "Greatest Decrease in Profts: " 
         + val2 + " ($" + str(greatest_decrease) + ")"]
with open(output_path, 'w') as f:
    f.writelines('\n'.join(lines))