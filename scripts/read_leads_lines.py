file_path = "data/leads.txt"

print("=== Leads List ===")

with open(file_path, "r") as file:
    for line in file:
        clean_line = line.strip()
        print("- " + clean_line)