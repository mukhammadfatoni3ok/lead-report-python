file_path = "data/app.log"

print("=== Application Log ===")

with open(file_path, "r") as file:
    for line in file:
        clean_line = line.strip()
        print(clean_line)