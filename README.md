# Task 1 - Data Cleaning (Medical Appointment No Shows)

## Overview
This project is part of a Data Analyst Internship Task where the goal was to clean a real-world dataset of medical appointments . The objective was to identify and fix common issues such as missing values, duplicates, inconsistent formats, and incorrect data types.

## Tools Used
- Python (Pandas)
- Excel / WPS Office (for validation)

## Task Goals
- Handle missing values
- Remove duplicates
- Standardize column names and text fields
- Clean and format date columns
- Fix data types (e.g., Age as int)
- Prevent Excel from corrupting large ID values
- Export a cleaned dataset ready for analysis

## Cleaning Steps Performed

1. **Missing Values** — Checked with `isnull().sum()` (no nulls found)
2. **Duplicates** — Removed using `drop_duplicates()`
3. **Date Formatting** — Converted ISO strings to `dd-mm-yyyy`
4. **Text Cleaning** — Standardized `Gender` and `No-show` with `str.upper().strip()`
5. **Column Renaming** — All lowercase, snake_case format
6. **Data Types** — Converted `age` to `int`; fixed large IDs for Excel display
7. **Final Save** — Output to `cleaned_medical_no_shows.csv`

## Files
- `cleaned_medical_no_shows.csv` — Cleaned dataset
- `Data cleaning task.py` — Python script
- `README.md` — This file

## Result
The dataset is now clean and can be used for analysis


