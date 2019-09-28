import os
import csv

candidates = []
num_votes = 0
vote_counts = []

file = 'election_data.csv'
filepath = os.path.join('file')

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    line = next(csvreader,None)

    for line in csvreader:

        num_votes = num_votes + 1

        candidate = line[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1

        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0

for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        max_index = count
winner = candidates[max_index]


print('Election Results')
print('--------------------------')
print(f'Total Votes: {num_votes:,}')
for count in range(len(candidates)):
    print(f'{candidates[count]}: {percentages[count]:.2f}% ({vote_counts[count]:,})')
print('---------------------------')
print(f'Winner: {winner}')
print('---------------------------')


filewrite = open('final_election.txt', mode = 'w')

filewrite.write('Election Results\n')
filewrite.write('--------------------------\n')
filewrite.write(f'Total Votes: {num_votes:,}\n')
for count in range(len(candidates)):
    filewrite.write(f'{candidates[count]}: {percentages[count]:.2f}% ({vote_counts[count]:,})\n')
filewrite.write('---------------------------\n')
filewrite.write(f'Winner: {winner}\n')
filewrite.write('---------------------------\n')

filewrite.close()