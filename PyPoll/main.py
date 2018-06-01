from os import path, makedirs 
from csv import reader, writer
from glob import glob # fetching glob function only from the glob lib

filePath = 'C:\\python-challenge\\PyPoll\\raw_data'
# csvpath = path.join('..',fileName,'election_data_1.csv')
csvFilesOnly = glob(filePath + "\\*.csv")
# print(csvpath)

total_number_of_votes = 0
candidate_vote = {} # dictionary to store the months and their revenue


for csvfile in csvFilesOnly:

    skip = True

    with open(csvfile, newline='') as csvfilePoll: # construct to load a csv file
        csvreader = reader(csvfilePoll, delimiter=',') # object to read the file's 1 row at a time

        for row in csvreader: #  Each line is read as a row here
        
            if (row[2] !="" and skip == False): # ensure the revenue is not "" & skip the first row
                total_number_of_votes += 1
                if (row[2] in candidate_vote):
                    candidate_vote[row[2]] += 1 
                else:   
                    candidate_vote[row[2]] =  1 # assign value 1 to row[n]_col 2 or key 2
                    
            skip = False

print("#########################################################################")

print("Election Results")
print("------------------------------------------------------")
print("Total Votes: " +  '{:,}'.format(total_number_of_votes ))
print("------------------------------------------------------")
for candidate in candidate_vote.keys():
        print(candidate + ": " + '{:.2f}'.format((candidate_vote[candidate] * 100 / total_number_of_votes )) + "% (" + '{:,}'.format(candidate_vote[candidate]) + ")")
print("------------------------------------------------------")
max_vote = 0
winner_name = ""
for candidate in candidate_vote:
    if (max_vote < candidate_vote[candidate]):
        winner_name = candidate
        max_vote = candidate_vote[candidate] 
print("The winner : " + winner_name)  
#print("Winner: " + winner_name )
print("------------------------------------------------------")
print("#########################################################################")

# write the file

filePath = C:\\python-challenge\\PyPoll\\output'
#Check if output folder exist, create if not exists!
if not path.exists(filePath):
    makedirs(filePath)

outputFile = filePath +"\\outputPoll.txt"
# Opening in new file and overiting if it exist.
f = open(outputFile,'w')

f.write("#########################################################################")

f.write("\nElection Results")
f.write("\n---------------------------------------------------")
f.write("\nTotal Votes: " +  '{:,}'.format(total_number_of_votes ))
f.write("\n---------------------------------------------------")
for candidate in candidate_vote.keys():
        f.write("\n" + candidate + ": " + '{:.2f}'.format((candidate_vote[candidate] * 100 / total_number_of_votes )) + "% (" + '{:,}'.format(candidate_vote[candidate]) + ")")
f.write("\n---------------------------------------------------")
max_vote = 0
winner_name = ""
for candidate in candidate_vote:
    if (max_vote < candidate_vote[candidate]):
        winner_name = candidate
        max_vote = candidate_vote[candidate] 
f.write("\nThe winner : " + winner_name)  

f.write("\n---------------------------------------------------")

f.write("\n#########################################################################")
          