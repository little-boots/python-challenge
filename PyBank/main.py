import os
import csv

budget_path = os.path.join('..', '..', '..',
                           'UNCRAL20190514DATA',
                           '02-Homework',
                           '03-Python',
                           'Instructions',
                           'PyBank',
                           'Resources',
                           'budget_data.csv')

month_ct  = 0
tru_total = 0
greatest_inc = [None, 0]
greatest_dec = [None, 0]
first = None
last = None

# Read CSV
with open(budget_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader, None)

    for row in csvreader:
        mo = row[0]
        val = int(row[1])

        if first is None:
            first = val
        if last is not None:
            diff = val - last
            if diff > greatest_inc[1]:
                greatest_inc = [mo, diff]
            if diff < greatest_dec[1]:
                greatest_dec = [mo, diff]
        last = val
        month_ct += 1
        tru_total += val

    avg_chg = tru_total / month_ct

# Output results to text file
output = open("analysis.txt", "w")

output.write("Financial Analysis\n")
output.write("----------------------------\n")
output.write(f"Total Months: {month_ct}\n")
output.write(f"Total: ${tru_total}\n")
output.write(f"Average Change: {avg_chg}\n")
output.write(f"Average Change: {round((last - first) / (month_ct - 1), 2)}\n")
output.write(f"Greatest Increase in Profits: {greatest_inc[0]}, (${greatest_inc[1]})\n")
output.write(f"Greatest Decrease in Profits: {greatest_dec[0]}, (${greatest_dec[1]})\n")

output.close()

# Send file to STDOUT
readfile = open("analysis.txt", "r")
for line in readfile:
    print(line)
