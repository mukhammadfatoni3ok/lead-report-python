from datetime import date

leads_file = "data/leads.txt"
log_file = "data/app.log"

today = date.today()
report_file = f"reports/report-{today}.txt"

with open(leads_file, "r") as file:
    leads = file.readlines()

with open(log_file, "r") as file:
    logs = file.readlines()

total_leads = len(leads)

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

    report.write("Summary\n")
    report.write("-------\n")
    report.write(f"Total leads: {total_leads}\n")
    report.write(f"Total error logs: {len(error_logs)}\n")
    report.write(f"Total warning logs: {len(warning_logs)}\n")
    report.write("\n")

    report.write("Latest Leads\n")
    report.write("------------\n")

    for lead in leads[-5:]:
        report.write(lead.strip() + "\n")

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
