import os, csv

csvpath = os.path.join('Resources', 'budget_data.csv')
analysis_path = os.path.join('analysis', "analysis.txt")

# function to both read and write at the same time - Referenced from Ashelyn Allred
def write_and_print(output_str, file):
    print(output_str)
    file.write(output_str + "\n")
    return

# reading through CSV data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Skip header
    csv_header = next(csvreader)

    #Create Variables
    months = 0
    total = 0
    change = 0
    change_all = 0
    max = 0
    min = 0

    # Starting loop to gather data
    for row in csvreader:
        
        # Incriment months to gather total months
        months += 1
        
        # Incriment total
        total += int(row[1])

        # Set 'last' variable for the first row in the data
        if months == 1:
            last = int(row[1])

        # Find change from 'last' and current rows value
        else:
            change = int(row[1]) - last
            change_all += change
            last = int(row[1])
        
        # Check if new change is greater or less than current max or min values
        if change > max:
            max = change
            max_month = row[0]
        
        elif change < min:
            min = change
            min_month = row[0]

# Use change all to determine the average change and storing it in the
# Also use the round function to remove excessive decimals 
change_avg = round(change_all / (months - 1), 2)

# Call the writeandprint function to write and print at the same time - Referenced from Ashelyn Allred
with open(analysis_path, "w") as a_file:
    write_and_print('Financial Analysis\n-------------------------------------------------', a_file)
    write_and_print(f'Total Months: {months}\nTotal: ${total}\nAverage Change: ${change_avg}', a_file)
    write_and_print(f'Greatest Increase in Profits: {max_month} (${max})', a_file)
    write_and_print(f'Greatest Decrease in Profits: {min_month} (${min})', a_file)