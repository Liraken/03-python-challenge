### Import modules
import os, csv



### Reading through the CSV data
csvpath = os.path.join('Resources', 'election_data.csv')
analysis_path = os.path.join('analysis', "analysis.txt")
def write_and_print(output_str, file):
    print(output_str)
    file.write(output_str + "\n")
    return

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip through header
    csv_header = next(csvreader)

    # Create variables
    count = 0
    cand = {}
    winner = ("", 0)

    # Loop through the file and calculate the information needed  
    for row in csvreader:
        
        if not row[2] in cand.keys():
            cand[row[2]] = 0
        
        cand[row[2]] += 1

        count += 1
    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {count}')
    print("----------------------------")


    # Finding the winner by looping through the dictionary
with open(analysis_path, "w") as a_file:
    for can in cand:
       cand[can] = [cand[can], round(cand[can] / count * 100, 3)]
       write_and_print(f"{can}: {cand[can][1]}% ({cand[can][0]})", a_file)
