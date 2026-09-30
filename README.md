# Lead Report Generator

Project automation menggunakan Python untuk membaca data lead dari file CSV, menganalisis log aplikasi, memvalidasi file input, dan membuat laporan otomatis.

## Fitur

- Membaca data lead dari file CSV
- Menghitung jumlah lead berdasarkan status
- Memfilter lead dengan status `new`
- Membaca application log
- Mendeteksi log `ERROR` dan `WARNING`
- Memeriksa keberadaan file input
- Memeriksa keberadaan folder laporan
- Memvalidasi kolom wajib pada file CSV
- Menangani kondisi file CSV kosong
- Membuat laporan otomatis berdasarkan tanggal

## Struktur Project

```text
lead-report-python/
├── data/
│   ├── leads.csv
│   └── app.log
├── reports/
├── scripts/
│   ├── read_leads.py
│   ├── read_leads_lines.py
│   ├── count_leads.py
│   ├── read_log.py
│   ├── filter_error_log.py
│   ├── day16_file_summary.py
│   ├── read_csv.py
│   ├── count_csv_leads.py
│   ├── count_leads_by_status.py
│   ├── filter_new_leads.py
│   ├── check_file_exists.py
│   └── generate_report.py
├── day15_summary.py
├── hello.py
├── variables.py
└── README.md
```

## Cara Menjalankan

Pastikan berada di folder project:

```bash
cd ~/latihan/portfolio/lead-report-python
```

Jalankan generator laporan:

```bash
python3 scripts/generate_report.py
```

Laporan akan dibuat di folder:

```text
reports/report-YYYY-MM-DD.txt
```

## Contoh Hasil

```text
Lead Report Generator
=====================
Date: 2026-09-30

Lead Summary
------------
Total leads: 5
New leads: 3
Contacted leads: 1
Qualified leads: 1

Application Log Summary
-----------------------
Total error logs: 1
Total warning logs: 1
```

## Tujuan Pembelajaran

Project ini merupakan bagian dari proses belajar Python automation.

Tujuan project adalah mempraktikkan penggunaan Python untuk membaca data, memproses data, melakukan validasi, menganalisis log, dan menghasilkan laporan secara otomatis.

Project ini juga digunakan sebagai bagian dari portfolio untuk mengembangkan kemampuan automation yang dapat diterapkan pada pekerjaan remote.

## Teknologi yang Digunakan

- Python
- CSV
- pathlib
- Git
- GitHub
