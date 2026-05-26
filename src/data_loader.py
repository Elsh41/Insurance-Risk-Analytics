import pandas as pd
import os

def load_insurance_data(file_path: str) -> pd.DataFrame:
    """Loads insurance dataset and fixes the pipe-delimited column split issue."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at: {file_path}")
        
    # sep=None lets pandas automatically figure out if it's tab, comma, or pipe separated
    df = pd.read_csv(file_path, sep='|', index_col=False, low_memory=False)
    
    # Clean column names to remove any hidden carriage returns or spaces
    df.columns = [col.strip() for col in df.columns]
    
    # Auto-detect and parse date columns smoothly
    date_cols = [col for col in df.columns if 'date' in col.lower() or 'month' in col.lower()]
    for col in date_cols:
        # format='mixed' handles multiple date variations without throwing warnings
        df[col] = pd.to_datetime(df[col], errors='coerce', format='mixed')
    
    return df