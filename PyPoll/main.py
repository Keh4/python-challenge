import os
import csv

#import counter to tally votes
import collections as ct

#Store Variables
totalcount = 0

#Set path to read csv and write txt
election_data = os.path.join("Resources", "election_data.csv")
file_to_output= os.path.join("Analysis", "Election_Analysis.txt")

with open(election_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

#set counter variable
    votecount = ct.Counter()
        
#store header
    header=next(csvreader)

#loop data rows in csv file to get count by candidate and total
    for row in csvreader:
        candidate = row[2]
        #establish counter to tally votes for each candidate
        votecount[candidate] += 1
        #count total vote/rows
        totalcount += 1

#print to above results to terminal
print("Election Results")
print("----------------------------------------")
print ("Total Votes : ",totalcount)
print("----------------------------------------")

#create loop to rank top down all candidates and values and calculate percent
for value, count in votecount.most_common():
    percentvotes = (count/totalcount)
    percentage = "{:.3%}".format(percentvotes)
    #print candidate rank, percentage of votes and vote count
    print(value, percentage, count)

print("----------------------------------------")

#print top rank as winner
for value, count in votecount.most_common(1):
    print("Winner : ", value)


#print to Election_Analysis.txt
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("------------------------------------\n")
    txt_file.write(f"Total Votes: {totalcount}\n")
    txt_file.write("------------------------------------\n")
    for value, count in votecount.most_common():
        percentvotes = (count/totalcount)
        percentage = "{:.3%}".format(percentvotes)   
        txt_file.write(f"{value, percentage, count}\n") 
    txt_file.write("------------------------------------\n")
    for value, count in votecount.most_common(1):
        txt_file.write(f"Winner : {value}\n")

