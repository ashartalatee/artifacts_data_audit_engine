# DAY 05 — PARSING MISSING COLUMN

## Dataset Tested
- File: raw_sales_export_missing_col.csv

## Expected vs Actual Structure
- Expected columns: order_id, order_date, customer_id, customer_age, total_amount, notes
- Missing columns detected: customer_age

## Why This Is Dangerous
- Kolom umur mungkin dipakai untuk segmentasi
- Ketidakhadiran kolom mengubah makna dataset
- Asumsi default akan memalsukan analisis

## Parser Behavior
- Parsing tetap berjalan
- Tidak ada data diubah
- Warning dicatat sebagai artefak

## Fatal or Non-Fatal?
- Parsing: NON-FATAL
- Decision making: POTENTIALLY FATAL

## Rule Extracted
Parser tidak boleh diam.
Ketidaksesuaian struktur wajib dicatat walau proses lanjut.
