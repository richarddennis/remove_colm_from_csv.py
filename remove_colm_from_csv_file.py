
import csv

remove_from = 1
remove_to = 2

with open("balances_493587.csv", "rb") as fp_in, open("newfile.csv", "wb") as f$
    reader = csv.reader(fp_in, delimiter=";")
    writer = csv.writer(fp_out, delimiter=";")
    for row in reader:
        del row[remove_from:remove_to]
        writer.writerow(row)
