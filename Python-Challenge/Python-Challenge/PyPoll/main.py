import os
import csv
from collections import defaultdict

# Define the base directory (where your script is located)
base_dir = '/Users/EthanShipman/Desktop/school/Python-Challenge/Python-Challenge/PyPoll'
data_path = os.path.join(base_dir, 'Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = defaultdict(int)

# Open the CSV file from the specified path
with open(data_path, mode='r') as file:
    csvreader = csv.reader(file)
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through each row of the CSV
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        
        # Count the total number of votes
        total_votes += 1
        
        # Count the votes for each candidate
        candidate_votes[candidate] += 1

# Prepare analysis results
candidates = list(candidate_votes.keys())
vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
winner = max(candidate_votes, key=candidate_votes.get)
winner_votes = candidate_votes[winner]

# Prepare the analysis summary
analysis = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# Add candidate results to the analysis
for candidate in candidates:
    analysis += (f"{candidate}: {vote_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")

analysis += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winner_votes}\n"
    f"-------------------------\n"
)

# Print the analysis to the terminal
print(analysis)

# Define the path to save the analysis in the "analysis" folder
output_path = os.path.join(base_dir, 'analysis', 'election_analysis.txt')

# Export the analysis to a text file in the "analysis" folder
with open(output_path, 'w') as file:
    file.write(analysis)