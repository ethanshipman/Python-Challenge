import os
import csv
from collections import defaultdict

# Utilizing relative paths for accessing the CSV file and saving the output
data_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')
output_path = os.path.join('PyPoll', 'analysis', 'election_analysis.txt')

# Initialize variables
total_votes = 0
candidate_votes = defaultdict(int)

# Open the CSV file from the relative path
with open(data_path, mode='r') as file:
    csvreader = csv.reader(file)
    
    # Skipping the header row
    header = next(csvreader)
    
    # Loop through each row of the CSV
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        
        
        total_votes += 1
        
       
        candidate_votes[candidate] += 1

# analysis results
candidates = list(candidate_votes.keys())
vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
winner = max(candidate_votes, key=candidate_votes.get)
winner_votes = candidate_votes[winner]

# analysis summary
analysis = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# Adding candidate results to the analysis
for candidate in candidates:
    analysis += f"{candidate}: {vote_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n"

analysis += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winner_votes}\n"
    f"-------------------------\n"
)

# Print the analysis to the terminal
print(analysis)

# Exported the analysis to a text file in the "analysis" folder using the relative path
with open(output_path, 'w') as file:
    file.write(analysis)