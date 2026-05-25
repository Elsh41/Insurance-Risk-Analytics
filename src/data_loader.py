import pandas as pd
import os

def load_insurance_data(file_path: str) -> pd.DataFrame:
    """Loads insurance dataset from a text file with auto-detected delimiter."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at: {file_path}")
        
    # sep=None lets pandas automatically figure out if it's tab, comma, or pipe separated
    df = pd.read_csv(file_path, sep=None, engine='python')
    
    # Auto-detect and parse date columns to proper datetime format
    date_cols = [col for col in df.columns if 'date' in col.lower() or 'timestamp' in col.lower()]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        
    return df