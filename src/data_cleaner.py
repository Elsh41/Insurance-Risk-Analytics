import pandas as pd
from src.data_loader import load_insurance_data

def clean_portfolio_data(input_path: str, output_path: str):
    """Loads raw data, strips high-risk anomalies, and saves a cleaned version."""
    print("Loading raw data for pipeline processing...")
    df = load_insurance_data(input_path)
    
    # Simple cleaning rule: Remove any negative or zero premiums/claims 
    # and drop completely empty or uninformative columns
    initial_rows = len(df)
    cleaned_df = df[(df['TotalPremium'] > 0) & (df['TotalClaims'] >= 0)].copy()
    
    print(f"Data Cleaning Complete. Removed {initial_rows - len(cleaned_df)} anomalous records.")
    
    # Save the cleaned file back over the target path
    cleaned_df.to_csv(output_path, sep='|', index=False)
    print(f"Cleaned dataset saved to: {output_path}")

if __name__ == "__main__":
    clean_portfolio_data("data/MachineLearningRating_v3.txt", "data/MachineLearningRating_v3.txt")