# DAY 08 — CHUNKED PARSING REALITY

## Why Chunking Is Non-Negotiable
Parsing sekali jalan hanya cocok untuk data kecil.
Chunking memisahkan logika dari keterbatasan hardware.

## Failure Observed
- Program mati di tengah
- Output parsial tapi valid
- Tidak ada silent corruption

## Key Insight
Parsing profesional harus bisa gagal tanpa merusak hasil sebelumnya.

## Next Risk
Chunking membuka risiko duplikasi dan header chaos.
Ini harus dikontrol eksplisit.
