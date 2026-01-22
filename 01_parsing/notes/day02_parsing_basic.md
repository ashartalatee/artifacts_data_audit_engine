# DAY 02 — BASIC CSV PARSING (NO CLEANING)

## Script Identity
- Script name: parse_basic.py
- Library used: csv (standard library)
- Dataset: raw_sales_export.csv

## What Python Actually Reads
- Semua nilai dibaca sebagai string
- Tidak ada konsep angka, tanggal, atau null di tahap ini

## Parsed Preview Observations
- Header terbaca sebagai baris pertama
- Nilai kosong dibaca sebagai string kosong ""
- Angka negatif dan non-numeric tetap string

## Explicit Separation
- Parsing = membaca struktur & isi file
- Cleaning = BELUM dilakukan
- Validation = BELUM dilakukan

## Risks If Assumptions Are Made Here
- Menganggap string numerik sebagai angka
- Menganggap "" sebagai None
- Menganggap format tanggal konsisten

## Key Realization
Jika parsing salah, seluruh pipeline di atasnya adalah ilusi.
Tahap ini harus bisa diulang dan hasilnya sama.
