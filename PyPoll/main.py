import os, csv

csv_path = os.path.join('Resources', 'election_data.csv')
analysis_path = os.path.join('analysis', "analysis.txt")

 
total_votes = 0
# Used to hold canditates their vote totals and their vote % 
cand = {}
winner_count = 0

# both prints to console and writes to file - Referenced from Ashelyn Allred
def write_and_print(output_str, file):
    print(output_str)
    file.write(output_str + "\n")
    return

with open(csv_path) as csv_file:

    csvreader = csv.reader(csv_file)
    # Skip header on csv before going into data
    next(csvreader)

    # iterate through rows
    for row in csvreader:
        
        if not row[2] in cand.keys():
            cand[row[2]] = 0
        
        cand[row[2]] += 1

        total_votes += 1


with open(analysis_path, "w") as a_file:
    # Assign variable to use as a divider
    divider = '----------------------------------------'
    # Use write_and_print command to output total votes and header for analysis file
    write_and_print(f"Election Results\n{divider}\nTotal Votes: {total_votes}\n{divider}", a_file)
    # Loop to write and print each candidates Name, % total votes and total vote count from the cand dictionary
    for can in cand:
        write_and_print(f"{can}: {format(round(cand[can] / total_votes * 100, 3))}% ({cand[can]})", a_file)
        if cand[can] > winner_count:
            winner_count = cand[can]
            winner = can
    write_and_print(f"{divider}\nWinner:{winner}\n{divider}", a_file)