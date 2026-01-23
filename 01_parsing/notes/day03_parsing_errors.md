# DAY 03 — PARSING ERRORS (DELIMITER & QUOTE)

## Dataset Tested
- File: raw_sales_export_broken.csv
- Intended delimiter: ;
- Parser delimiter used: ,

## What Went Wrong (Observed, Not Assumed)
- Setiap baris terbaca sebagai 1 kolom
- Struktur kolom hancur tanpa exception
- Quote rusak tidak menghentikan parsing

## Dangerous Insight
Parser tidak selalu gagal keras.
Ia bisa “berhasil” membaca file dengan struktur SALAH.

## Why This Is Worse Than a Crash
- Tidak ada error
- Tidak ada peringatan
- Data terlihat “ada”

## Evidence of Structural Failure
- Header hanya 1 elemen
- Tidak ada pemisahan kolom
- Data tidak bisa dipercaya untuk tahap lanjut

## Rule Extracted
Parsing harus memverifikasi:
- jumlah kolom
- konsistensi struktur
- delimiter benar

Tanpa ini, anomaly dan validation di atasnya adalah ilusi.
