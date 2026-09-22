import csv

csv_file = "data/leads.csv"

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    print("=== Leads from CSV ===")

    for row in reader:
        print("Name:", row["name"])
        print("Email:", row["email"])
        print("Source:", row["source"])
        print("Status:", row["status"])
        print("---")
