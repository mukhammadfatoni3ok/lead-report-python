leads_file = "data/leads.txt"
log_file = "data/app.log"

with open(leads_file, "r") as file:
    leads = file.readlines()

with open(log_file, "r") as file:
    logs = file.readlines()

total_leads = len(leads)
total_logs = len(logs)

print("=== File Summary ===")
print("Leads file:", leads_file)
print("Total leads:", total_leads)
print("Log file:", log_file)
print("Total log lines:", total_logs)

print("")
print("Latest lead:")
print(leads[-1].strip())

print("")
print("Error logs:")

for log in logs:
    clean_log = log.strip()

    if "ERROR" in clean_log:
        print(clean_log)