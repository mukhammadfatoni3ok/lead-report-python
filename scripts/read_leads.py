file_path = "data/leads.txt"

with open(file_path, "r") as file:
    content = file.read()

print("=== Leads Data ===")
print(content)