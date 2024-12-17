# -*- coding: utf-8 -*-
"""PyPoll Homework Solution for VS Code"""

import os
import csv

# Files to load and output
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")
file_to_output = os.path.join("PyPoll", "analysis", "election_results.txt")

# Initialize variables
total_votes = 0
candidates = {}
winning_candidate = ""
winning_count = 0

# Read the CSV file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Iterate through each row
    for row in reader:
        # Count total votes
        total_votes += 1

        # Track candidate votes
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Determine the winner
for candidate, votes in candidates.items():
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate

# Generate output
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

output += (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------\n"
)

# Print the output
print(output)

# Write the output to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)