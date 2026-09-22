file_path = "data/leads.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

total_leads = len(lines)

print("=== Lead Count ===")
print("Total leads:", total_leads)