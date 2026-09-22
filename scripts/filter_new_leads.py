import csv

csv_file = "data/leads.csv"

print("=== New Leads ===")

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["status"] == "new":
            print(row["name"], "-", row["email"], "-", row["source"])
