# PARSING RULES — DATA INGESTION CONTRACT

## 1. Scope of Parsing
Parsing is responsible ONLY for:
- Reading file structure
- Detecting structural inconsistencies
- Reporting factual mismatches
Parsing does NOT:
- Clean data
- Fix values
- Infer meaning

## 2. File-Level Rules
- Encoding must be explicitly defined or detected
- Parser must fail hard on unreadable encoding
- Delimiter must be verified against expected structure

## 3. Header & Column Rules
- Missing expected columns MUST be logged as warnings
- Unexpected extra columns MUST be logged
- Column order MUST NOT be assumed

## 4. Row-Level Rules
- Empty strings are NOT treated as null automatically
- All values are read as raw strings initially
- No row is silently dropped during parsing

## 5. Type Contract Rules
- Expected data types must be declared
- Type mismatches must be logged explicitly
- Type validity does NOT imply semantic validity

## 6. Silent Failure Prevention
- Parser must verify column count consistency
- Parser must never succeed silently with broken structure

## 7. Artefact Requirements
- Every parsing run must produce:
  - Parsing output preview
  - Error or warning log
- Logs are mandatory audit artefacts

## 8. Non-Negotiable Principles
- No assumptions
- No auto-fix
- No silent correction
