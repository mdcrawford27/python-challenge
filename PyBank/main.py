# import the modules needed
import csv
import os

# identifying the file path where the budget data is located and the output file
inputcsv = os.path.join('C:/Users/mdcra/Desktop/python-challenge/PyBank/Resources/budget_data.csv')
outputfile = os.path.join('C:/Users/mdcra/Desktop/python-challenge/PyBank/Analysis/budget_analysis.txt')

# create values that we are trying to calculate
totalmonths = 0
totalPL = 0
PLchange_list = []

# reading the csv file
with open(inputcsv) as csvfile:
    csvreader =csv.reader(csvfile, delimiter = ",")

    # reading the header row
    csv_header = next(csvreader)

    # reading row 1 so we can calculate change from there
    row1 = next(csvreader)
    # setting the total months to 1 since we are skipping over row 1
    totalmonths = 1
    # starting total net with first amount since we are skipping over row 1
    totalPL = int(row1[1])
    # setting starting amount with first row's P/L
    start_amount = int(row1[1])

    # calculating total months and net total P/L
    for row in csvreader:
        totalmonths = totalmonths + 1
        totalPL = totalPL + int(row[1])

        # calculating the change from row to row, adding it to our P/L change list and then
        # setting the start amount to the current row
        change = int(row[1]) - start_amount
        PLchange_list.append(change)
        start_amount = int(row[1])

        # calculating average change between months
        avgchange = sum(PLchange_list) / (totalmonths-1)

# creating output data to be written in text file
output = (f"Financial Analysis\n"
    f"---------------------------------------------------------\n"
    f"Total Months : {totalmonths}\n"
    f"Total Net Change : ${totalPL}\n"
    f"Average Change : ${round(avgchange,2)}\n"
    f"Greatest Increase : ${max(PLchange_list)}\n"
    f"Greatest Decrease : ${min(PLchange_list)}")

print(output)

with open(outputfile, 'w') as textfile:
    textfile.write(output)
