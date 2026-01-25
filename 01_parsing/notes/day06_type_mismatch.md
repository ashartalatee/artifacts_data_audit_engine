# DAY 06 — TYPE MISMATCH DETECTION

## Dataset Tested
- File: raw_sales_export.csv

## Expected Type Contract
- customer_age → int
- total_amount → float

## Observed Mismatches
- Empty string in numeric field
- Non-numeric string in numeric field
- Ambiguous numeric values (e.g. 0 for age)

## Why This Is Not Cleaning
- Nilai tidak diubah
- Tidak ada asumsi pemulihan
- Fakta dicatat apa adanya

## Risk If Ignored
- Salah agregasi
- Salah segmentasi
- Keputusan berbasis ilusi numerik

## Rule Extracted
Tipe data adalah kontrak fakta.
Jika kontrak dilanggar, parser wajib bersuara.
