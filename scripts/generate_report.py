import csv
from datetime import date
from pathlib import Path

leads_file = Path("data/leads.csv")
log_file = Path("data/app.log")
reports_folder = Path("reports")

today = date.today()
report_file = reports_folder / f"report-{today}.txt"

if not leads_file.exists():
    print("ERROR: Leads file not found.")
    print("Expected file:", leads_file)
    print("Please create data/leads.csv first.")
    exit()

if not log_file.exists():
    print("ERROR: Log file not found.")
    print("Expected file:", log_file)
    print("Please create data/app.log first.")
    exit()

if not reports_folder.exists():
    print("Reports folder not found. Creating reports folder...")
    reports_folder.mkdir()

leads = []

with open(leads_file, "r") as file:
    reader = csv.DictReader(file)

    if reader.fieldnames is None:
        print("ERROR: CSV file is empty.")
        print("Please add header and lead data to data/leads.csv.")
        exit()

    required_columns = ["name", "email", "source", "status"]

    for column in required_columns:
        if column not in reader.fieldnames:
            print("ERROR: Missing CSV column:", column)
            print("Expected columns:", required_columns)
            print("Found columns:", reader.fieldnames)
            exit()

    for row in reader:
        leads.append(row)

with open(log_file, "r") as file:
    logs = file.readlines()

total_leads = len(leads)

if total_leads == 0:
    print("ERROR: No leads found in CSV file.")
    print("Please add at least one lead to data/leads.csv.")
    exit()

new_count = 0
contacted_count = 0
qualified_count = 0

for lead in leads:
    status = lead["status"]

    if status == "new":
        new_count = new_count + 1

    if status == "contacted":
        contacted_count = contacted_count + 1

    if status == "qualified":
        qualified_count = qualified_count + 1

error_logs = []
warning_logs = []

for log in logs:
    clean_log = log.strip()

    if "ERROR" in clean_log:
        error_logs.append(clean_log)

    if "WARNING" in clean_log:
        warning_logs.append(clean_log)

with open(report_file, "w") as report:
    report.write("Lead Report Generator\n")
    report.write("=====================\n")
    report.write(f"Date: {today}\n")
    report.write("\n")

    report.write("Lead Summary\n")
    report.write("------------\n")
    report.write(f"Total leads: {total_leads}\n")
    report.write(f"New leads: {new_count}\n")
    report.write(f"Contacted leads: {contacted_count}\n")
    report.write(f"Qualified leads: {qualified_count}\n")
    report.write("\n")

    report.write("Latest Leads\n")
    report.write("------------\n")

    for lead in leads[-5:]:
        line = f"{lead['name']} | {lead['email']} | {lead['source']} | {lead['status']}"
        report.write(line + "\n")

    report.write("\n")

    report.write("Application Log Summary\n")
    report.write("-----------------------\n")
    report.write(f"Total error logs: {len(error_logs)}\n")
    report.write(f"Total warning logs: {len(warning_logs)}\n")
    report.write("\n")

    report.write("Error Logs\n")
    report.write("----------\n")

    if len(error_logs) == 0:
        report.write("No error logs found.\n")
    else:
        for error in error_logs:
            report.write(error + "\n")

    report.write("\n")

    report.write("Warning Logs\n")
    report.write("------------\n")

    if len(warning_logs) == 0:
        report.write("No warning logs found.\n")
    else:
        for warning in warning_logs:
            report.write(warning + "\n")

print("Report created:", report_file)
print("Total leads:", total_leads)
print("Error logs:", len(error_logs))
print("Warning logs:", len(warning_logs))
