import csv

csv_file = "data/leads.csv"

total_leads = 0

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_leads = total_leads + 1

print("Total leads:", total_leads)
