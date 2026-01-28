import pandas as pd
import os

def create_test_files():
    """Generates sample CSVs for demonstration."""
    source_data = {
        'ID': [101, 102, 103],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Salary': [70000, 80000, 90000]
    }
    target_data = {
        'ID': [101, 102, 103],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Salary': [70000, 85000, 90000]  
    }
    pd.DataFrame(source_data).to_csv('source.csv', index=False)
    pd.DataFrame(target_data).to_csv('target.csv', index=False)

def run_comparator(source_file, target_file):
    """Loads and compares two CSV files row-by-row."""
    if not os.path.exists(source_file) or not os.path.exists(target_file):
        print("Error: Files not found.")
        return

    df_src = pd.read_csv(source_file)
    df_tgt = pd.read_csv(target_file)

    if df_src.shape != df_tgt.shape:
        print(f"FAILED: Dimension mismatch. Source: {df_src.shape}, Target: {df_tgt.shape}")
        return

    mismatches = (df_src != df_tgt).any(axis=1)
    
    if not mismatches.any():
        print("PASS: Data integrity verified. All rows match.")
    else:
        for idx in df_src.index[mismatches]:
            src_val = df_src.iloc[idx].to_list()
            tgt_val = df_tgt.iloc[idx].to_list()
            print(f"Mismatch at Row {idx}: Source says {src_val}, Target says {tgt_val}")

if __name__ == "__main__":
    create_test_files()
    run_comparator('source.csv', 'target.csv')
