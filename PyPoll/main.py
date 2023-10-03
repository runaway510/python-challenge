
#Import Dependencies
import os
import csv

csv_path = os.path.abspath(os.path.join("Resources", "election_data.csv"))
csv_output = os.path.abspath(os.path.join("Analysis", "Analysis.txt"))

# Initialize variables to store data
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Open and read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row if it exists
    header = next(csvreader, None)

    # Iterate through each row in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        
        # Check if candidate_name is already in candidates dictionary
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Find the winner
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#output to text file
file = open(csv_output, "w")
file.write("Election Results" + "\n")
file.write("-------------------------" + "\n")
file.write(f"Total Votes: {total_votes}"+ "\n")
file.write("-------------------------"+ "\n")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    file.write(f"{candidate}: {percentage:.3f}% ({votes})"+ "\n")

file.write("-------------------------"+ "\n")
file.write(f"Winner: {winner}"+ "\n")
file.write("-------------------------"+ "\n")

file.close()


