import os
import csv

poll_path = os.path.join('..', '..', '..',
                         'UNCRAL20190514DATA',
                         '02-Homework',
                         '03-Python',
                         'Instructions',
                         'PyPoll',
                         'Resources',
                         'election_data.csv')

vote_summary = {}

# Read CSV
with open(poll_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header    = next(csvreader, None)

    for row in csvreader:
        id_        = row[0]
        county_    = row[1]
        candidate_ = row[2]

        if candidate_ not in vote_summary.keys():
            vote_summary[candidate_] = 1
        else:
            vote_summary[candidate_] += 1

vote_total = sum([votes for votes in vote_summary.values()])
max_votes  = max([votes for votes in vote_summary.values()])
winner     = [candidate for candidate in vote_summary.keys() if\
              vote_summary[candidate] == max_votes][0]

# Create output file
output = open("tally.txt", "w", newline="")
output.write("Election Results\n")
output.write("----------------------------\n")
output.write(f"Total Votes: {vote_total}\n")
output.write("----------------------------\n")
for candidate, votes in vote_summary.items():
    pct = str(round((100 * votes / vote_total), 3))
    output.write(f"{candidate}: {pct}% ({votes})\n")
output.write("----------------------------\n")
output.write(f"Winner: {winner}\n") #(chicken dinner)
output.close()

# Send file to STDOUT
readfile = open("tally.txt", "r")
for line in readfile:
    print(line)
