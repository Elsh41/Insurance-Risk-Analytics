import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    

def plot_financial_distributions(df, columns):
    """Generates side-by-side Box plots and Histograms for outlier assessment."""
    for col in columns:
        fig, axes = plt.subplots(1, 2, figsize=(14, 4))
        
        # Histogram for distribution shape
        sns.histplot(data=df, x=col, bins=50, kde=True, ax=axes[0], color='skyblue')
        axes[0].set_title(f'{col} Distribution (Skew: {df[col].skew():.2f})')
        
        # Boxplot to clearly isolate the dots (outliers)
        sns.boxplot(data=df, x=col, ax=axes[1], color='salmon')
        axes[1].set_title(f'{col} Outlier Boxplot')
        
        plt.tight_layout()
        plt.show()


def calculate_temporal_trends(df, date_col='TransactionMonth'):
    """Calculates claim frequency and severity trends over time."""
    # Ensure date is sorted
    df_sorted = df.sort_values(by=date_col)
    
    # Convert period to string format for clean timeline grouping
    df_sorted['TimePeriod'] = df_sorted[date_col].dt.strftime('%Y-%m')
    
    trend = df_sorted.groupby('TimePeriod').agg(
        Total_Policies=('PolicyID', 'count'),
        Total_Claims_Count=('TotalClaims', lambda x: (x > 0).sum()),
        Avg_Claim_Severity=('TotalClaims', lambda x: x[x > 0].mean()), # Average of non-zero claims
        Total_Premium_Income=('TotalPremium', 'sum')
    ).reset_index()
    
    trend['Claim_Frequency_(%)'] = (trend['Total_Claims_Count'] / trend['Total_Policies']) * 100
    return trend