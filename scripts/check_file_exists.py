from pathlib import Path

leads_file = Path("data/leads.csv")

if leads_file.exists():
    print("File ditemukan:", leads_file)
else:
    print("File tidak ditemukan:", leads_file)
