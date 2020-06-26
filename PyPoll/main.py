# import modules needed
import csv
import os

# set path for importing the election data and exporting finished data
inputfile = os.path.join('C:/Users/mdcra/Desktop/python-challenge/PyPoll/Resources/election_data.csv') 
outputfile = os.path.join('C:/Users/mdcra/Desktop/python-challenge/PyPoll/Analysis/election_analysis.txt')

# set initial start number of votes
totalvotes = 0

# make list for candidate options
candidate_list = []

# make dictionary for candidate votes
candidate_votes = {}

# set initial winning number of votes
winning_votes = 0

# reading the csv data
with open(inputfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # reading the header
    csvheader = next(csvreader)

    # add a count to total votes and set candidate name from col.2
    for row in csvreader:
        totalvotes = totalvotes + 1
        candidate = row[2]

        # add the candidate name to the candidate option list and set amount of votes to 0
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 0
        
        # if candidate is in list, then add a vote to their count
        candidate_votes[candidate] = candidate_votes[candidate] + 1

# write total votes into output text file
with open(outputfile, 'w') as textfile:

    totalresults = ( f"Election Results\n"
        f"----------------------------------\n"
        f"Total Votes : {totalvotes}\n"
        f"----------------------------------\n")
    #print to terminal
    print(totalresults)

    # write total results to text file
    textfile.write(totalresults)

    # isolating the each candidates amount of votes and finding the percentage of each in total votes
    for candidate in candidate_votes:
        numberofvotes = candidate_votes.get(candidate)
        percentvotes = (numberofvotes) / (totalvotes) * 100

        # if the amount of the candidate votes are greater than the current winning votes, that amount will
        # replace the current winning votes. Then set the winner to that specific candidate.
        if (numberofvotes > winning_votes):
            winning_votes = numberofvotes
            winner = candidate
        
        # print each candidate's name and their vote precentage and total number of votes to terminal
        voter_results = f"{candidate}: {percentvotes:.2f}%' ({numberofvotes})\n"
        print (voter_results)

        # write the above data into the text file
        textfile.write(voter_results)

    # print winning candidate info into terminal
    winningcandidate = (f"------------------------------\n"
        f"Winner : {winner}\n"
        f"---------------------------------\n")
    print(winningcandidate)

    # write the winning candidate data into text file
    textfile.write(winningcandidate)