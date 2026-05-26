import pandas as pd
import numpy as np
from scipy import stats

def test_categorical_kpi(df, group_col, category_A, category_B, kpi_col):
    """
    Runs a Chi-Squared test of independence for a categorical KPI (e.g., Claim Occurred: 0 or 1)
    between two distinct groups.
    """
    # Filter for the two target groups
    sub_df = df[df[group_col].isin([category_A, category_B])].copy()
    
    # Create a contingency table (Group vs KPI success/failure)
    contingency_table = pd.crosstab(sub_df[group_col], sub_df[kpi_col])
    
    # Run Chi-Squared Test
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    
    return p_value, chi2


def test_numerical_kpi(df, group_col, category_A, category_B, kpi_col):
    """
    Runs an independent two-sample t-test for continuous numerical KPIs 
    (e.g., Claim Severity or Margin) between two distinct groups.
    """
    # Isolate the metric for Group A and Group B
    group_A_metrics = df[df[group_col] == category_A][kpi_col].dropna()
    group_B_metrics = df[df[group_col] == category_B][kpi_col].dropna()
    
    # Run Independent t-test (Equal_var=False applies Welch's t-test, safer for insurance data)
    t_stat, p_value = stats.ttest_ind(group_A_metrics, group_B_metrics, equal_var=False)
    
    return p_value, t_stat