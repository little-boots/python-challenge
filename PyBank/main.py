#!/usr/bin/python
import os
import csv


# NOTE: I didn't want two copies of this dataset and my (exfat) hard drive
#       doesn't support symlinks?
budget_path = os.path.join('..', '..', '..',
                           'UNCRAL20190514DATA',
                           '02-Homework',
                           '03-Python',
                           'Instructions',
                           'PyBank',
                           'Resources',
                           'budget_data.csv')

# I'm assuming we're not supposed to use pandas on this one.  Instead...
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

# Output results to STDOUT
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_ct}")
print(f"Total: ${tru_total}")
print(f"Average Change: {avg_chg}")
print(f"Average Change: {round((last - first) / (month_ct - 1), 2)}")
print(f"Greatest Increase in Profits: {greatest_inc[0]}, (${greatest_inc[1]})")
print(f"Greatest Decrease in Profits: {greatest_dec[0]}, (${greatest_dec[1]})")

# Output results to text file

output = open("analysis.txt", "w")

output.write("Financial Analysis")
output.write("----------------------------")
output.write(f"Total Months: {month_ct}")
output.write(f"Total: ${tru_total}")
output.write(f"Average Change: {avg_chg}")
output.write(f"Average Change: {round((last - first) / (month_ct - 1), 2)}")
output.write(f"Greatest Increase in Profits: {greatest_inc[0]}, (${greatest_inc[1]})")
output.write(f"Greatest Decrease in Profits: {greatest_dec[0]}, (${greatest_dec[1]})")

output.close()
