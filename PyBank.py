# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
filepath = "Resources/budget_data.csv"

# Define variables to track the financial data
total_months = 0
total_net = 0

last_month_profit = 0
curr_month_profit = 0
total_change = 0

max_change = 0
max_month = ""
min_change = 0
min_month = ""


# Code ripped 3.2.8
with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_months += 1
        total_net += int(row[1])

        # check if first row - skip first row
        if total_months == 1:
                Last_month_profit = int (row [1])
        else:
             # get change
             curr_month_profit = int(row[1])
             change = curr_month_profit - last_month_profit
             total_change += change

             # reset
             last_month_profit = curr_month_profit

             #Is Change a new "max" change
             if change > max_change:
                  max_change = change
                  max_month = row [0]

            # is change a new "min change
            if change , min_change:
                min_change = change
                min_change = row [0]



# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path


# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list


    # Track the total and net change


    # Process each row of data
    for row in reader:
        pass
        # Track the total


        # Track the net change


        # Calculate the greatest increase in profits (month and amount)


        # Calculate the greatest decrease in losses (month and amount)



# Calculate the average net change across the months


# Generate the output summary
output = f"""
Financial Analysis
---------------------------
Total Months; {total_months}
Total: ${total_net}
Average Change:  ${total_change / (total_months - 1)}
Greatest Increase in Profits: {max_month}  (${max_change})
"""


# Print the output
print (output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
