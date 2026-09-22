file_path = "data/app.log"

print("=== Error Logs ===")

with open(file_path, "r") as file:
    for line in file:
        clean_line = line.strip()

        if "ERROR" in clean_line:
            print(clean_line)