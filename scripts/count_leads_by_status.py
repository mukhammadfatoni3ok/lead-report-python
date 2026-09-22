import csv

csv_file = "data/leads.csv"

new_count = 0
contacted_count = 0
qualified_count = 0

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        status = row["status"]

        if status == "new":
            new_count = new_count + 1

        if status == "contacted":
            contacted_count = contacted_count + 1

        if status == "qualified":
            qualified_count = qualified_count + 1

print("=== Lead Status Summary ===")
print("New:", new_count)
print("Contacted:", contacted_count)
print("Qualified:", qualified_count)
