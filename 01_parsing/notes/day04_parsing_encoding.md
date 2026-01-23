# DAY 04 — PARSING ENCODING

## Dataset Tested
- File: raw_sales_export_latin1.csv
- Suspected encoding: tidak diketahui di awal

## Encoding Tests Performed
- utf-8 → FAIL (UnicodeDecodeError)
- latin-1 → SUCCESS

## Key Evidence
- Error byte: 0xe9
- Karakter bermasalah: é, café, résumé

## Dangerous Wrong Fixes (NOT USED)
- errors="ignore"
- replace karakter
- manual edit data

## Why Encoding Is Parsing, Not Cleaning
- Data tidak rusak
- Interpretasi pembaca yang salah
- Kesalahan di sini mengubah makna data

## Rule Extracted
Parsing harus:
- eksplisit soal encoding
- gagal keras jika salah
- meninggalkan jejak bukti

Tanpa ini, audit bahasa & nama pelanggan menjadi tidak sah.
