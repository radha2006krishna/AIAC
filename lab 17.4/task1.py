from pathlib import Path
import re
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# task1.py
# Python script to clean an employee dataset:
# - handle missing values (salary, department, joining_date)
# - convert joining_date to datetime
# - standardize department names
# - encode categorical variables (department, job_role)
#
# Usage: adjust INPUT_PATH if needed, then run: python task1.py



INPUT_PATH = Path(r"c:\Users\SANGEM RADHA KRISHNA\Downloads\Raw_Employee_Dataset.csv")
OUTPUT_PATH = INPUT_PATH.with_name("Cleaned_Employee_Dataset.csv")
ENCODERS_PATH = INPUT_PATH.with_name("Encoders_mapping.json")


def read_dataset(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_salary(series: pd.Series) -> pd.Series:
    # Remove currency symbols and thousands separators, coerce to float
    cleaned = (
        series.fillna("")
        .astype(str)
        .str.replace(r"[^\d\.\-]", "", regex=True)
        .replace("", np.nan)
    )
    numeric = pd.to_numeric(cleaned, errors="coerce")
    median = numeric.median(skipna=True)
    return numeric.fillna(median)


def standardize_department(value: str) -> str:
    if pd.isna(value):
        return np.nan
    s = str(value).strip().lower()
    if not s:
        return np.nan
    # common mappings by keywords
    if any(k in s for k in ("human", "hr", "h.r", "human resources")):
        return "HR"
    if any(k in s for k in ("finance", "fin", "acct", "accounting")):
        return "Finance"
    if any(k in s for k in ("it", "information", "tech", "technology")):
        return "IT"
    if any(k in s for k in ("sales", "business development", "bd", "sale")):
        return "Sales"
    if any(k in s for k in ("marketing", "market")):
        return "Marketing"
    if any(k in s for k in ("operations", "ops")):
        return "Operations"    
    # fallback: title-case cleaned token
    return s.title()


def clean_joining_date(series: pd.Series) -> pd.Series:
    # Try to parse various date formats, coerce errors to NaT
    dt = pd.to_datetime(series, errors="coerce", dayfirst=False, infer_datetime_format=True)
    # Fill missing joining_date with median date if available, otherwise today's date
    if dt.notna().any():
        median_ts = dt.dropna().median()
        dt = dt.fillna(median_ts)
    else:
        dt = dt.fillna(pd.Timestamp.now())
    return dt


def encode_categories(df: pd.DataFrame, columns: list) -> (pd.DataFrame, dict):
    encoders = {}
    for col in columns:
        le = LabelEncoder()
        # Fill NA with explicit string to ensure consistent encoding
        df[col] = df[col].fillna("Unknown").astype(str)
        df[col + "_enc"] = le.fit_transform(df[col])
        encoders[col] = {int(idx): label for idx, label in enumerate(le.classes_)}
    return df, encoders


def main():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    df = read_dataset(INPUT_PATH)

    # Normalize column names
    df.columns = [c.strip() for c in df.columns]

    # Handle salary
    if "salary" in df.columns:
        df["salary"] = clean_salary(df["salary"])
    else:
        df["salary"] = np.nan

    # Handle department
    if "department" in df.columns:
        df["department"] = df["department"].apply(standardize_department)
        # fill remaining missing departments with mode or 'Unknown'
        if df["department"].notna().any():
            mode = df["department"].mode()
            fill_val = mode.iloc[0] if not mode.empty else "Unknown"
        else:
            fill_val = "Unknown"
        df["department"] = df["department"].fillna(fill_val)
    else:
        df["department"] = "Unknown"

    # Handle joining_date
    if "joining_date" in df.columns:
        df["joining_date"] = clean_joining_date(df["joining_date"])
    else:
        df["joining_date"] = pd.Timestamp.now()

    # Normalize job_role column
    if "job_role" in df.columns:
        df["job_role"] = df["job_role"].fillna("Unknown").astype(str).str.strip().replace("", "Unknown")
    else:
        df["job_role"] = "Unknown"

    # Encode categorical variables
    df, encoders = encode_categories(df, ["department", "job_role"])

    # Optionally drop original textual columns or keep both; here we keep both.
    # Save cleaned dataset
    df.to_csv(OUTPUT_PATH, index=False)

    # Save encoder mappings for reference
    # invert mapping to label -> code for clarity
    mapping = {
        col: {label: int(code) for code, label in enc.items()} for col, enc in encoders.items()
    }
    with open(ENCODERS_PATH, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)

    # Print summary
    print("Cleaned dataset saved to:", OUTPUT_PATH)
    print("Encoders saved to:", ENCODERS_PATH)
    print("\nData preview:")
    print(df.head())


if __name__ == "__main__":
    main()