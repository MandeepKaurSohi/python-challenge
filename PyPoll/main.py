import os
import csv

#CSV path
PyPoll_csv = os.path.join("..","Resources", "election_data.csv")

#with open as csv file:
with open(PyPoll_csv, newline="", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # skip the header
    header = next(csvreader)
    
    # the total number of votes cast
    election_data = list(csvreader)
    total_votes = len(election_data)
    
    # A complete list of candidates who received votes
    candidate_list = list()
    count = list()
    for i in range (0, total_votes):
        candidate = election_data[i][2]
        count.append(candidate)
        if candidate not in candidate_list:
           candidate_list.append(candidate)
           
    candidate_count = len(candidate_list)
    
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes:,}")
    print("----------------------------")
    
    # The percentage/ total number of votes each candidate won
    votes = list()
    percentage = list()
    for j in range(0, candidate_count):
        candidate_name = candidate_list[j]
        votes.append(count.count(candidate_name))
        vote_percentage = votes[j]/total_votes
        percentage.append(vote_percentage)
      
    # The winner of the election
    winner = votes.index(max(votes))
    
    for k in range (0,candidate_count):
        print(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidate_list[winner]}")
    print("----------------------------")
    
    # output in a text file
    
    print("election results", file = open("PyPoll.txt", "a"))
    print("...........", file = open("PyPoll.txt", "a"))
    print("total votes: {total_vote:,}", file = open("PyPoll.txt","a"))
    print(".........", file = open("PyPoll.txt","a"))
    for k in range(0, candidate_count):
        print("{candidate_list[k]}: {percentage[k]:.3% ({votes[k]:, })",file = open("PyPoll.txt","a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {candidate_list[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))

