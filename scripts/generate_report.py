import csv
from datetime import date

leads_file = "data/leads.csv"
log_file = "data/app.log"

today = date.today()
report_file = f"reports/report-{today}.txt"

leads = []

with open(leads_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        leads.append(row)

with open(log_file, "r") as file:
    logs = file.readlines()

total_leads = len(leads)

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
