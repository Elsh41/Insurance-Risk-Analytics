import pandas as pd

def check_data_quality(df: pd.DataFrame) -> pd.DataFrame:
    """Generates a summary of data types and missing values."""
    return pd.DataFrame({
        'DataType': df.dtypes,
        'MissingValues': df.isnull().sum(),
        'PercentageMissing': (df.isnull().sum() / len(df)) * 100
    })

def calculate_loss_ratio(df, group_by_col = None):
    """Calculates Loss Ratio = Total Claims / Total Premium."""
    if group_by_col:
        grouped = df.groupby(group_by_col).agg(
            Total_Claims=('TotalClaims', 'sum'),
            Total_Premium=('TotalPremium', 'sum')
        ).reset_index()
        grouped['LossRatio'] = grouped['Total_Claims'] / grouped['Total_Premium']
        return grouped.sort_values(by='LossRatio', ascending=False)
    else:
        # Global calculation
        overall_claims = df['TotalClaims'].sum()
        overall_premium = df['TotalPremium'].sum()
        return pd.DataFrame([{
            'TotalClaims': overall_claims,
            'TotalPremium': overall_premium,
            'LossRatio': overall_claims / overall_premium
        }])