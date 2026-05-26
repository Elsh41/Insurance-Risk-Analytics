import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def evaluate_regression_model(y_true, y_pred, model_name: str) -> dict:
    """Calculates performance tracking metrics for severity models."""
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    print(f"[{model_name}] RMSE: {rmse:.2f} | R²: {r2:.4%}")
    return {"Model": model_name, "RMSE": round(rmse, 2), "R2_Score": round(r2, 4)}

def train_and_evaluate_all_models(X_train, X_test, y_train, y_test) -> pd.DataFrame:
    """Trains Linear Regression, Random Forest, and XGBoost models side-by-side."""
    results = []
    
    # 1. Linear Regression Baseline
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_preds = lr.predict(X_test)
    results.append(evaluate_regression_model(y_test, lr_preds, "Linear Regression"))
    
    # 2. Random Forest Regressor
    rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)
    results.append(evaluate_regression_model(y_test, rf_preds, "Random Forest"))
    
    # 3. XGBoost Regressor
    xgb = XGBRegressor(n_estimators=150, learning_rate=0.05, max_depth=6, random_state=42, n_jobs=-1)
    xgb.fit(X_train, y_train)
    xgb_preds = xgb.predict(X_test)
    results.append(evaluate_regression_model(y_test, xgb_preds, "XGBoost"))
    
    return pd.DataFrame(results), xgb, rf, lr

def calculate_optimized_premium(p_claim, pred_severity, expense_loading=200.0, profit_margin=0.15) -> float:
    """
    Applies the mathematical insurance pricing equation:
    Premium = (P(Claim) * Predicted Severity) + Expense Loading + Profit Margin
    """
    pure_premium = p_claim * pred_severity
    base_premium = pure_premium + expense_loading
    final_premium = base_premium / (1 - profit_margin)
    return final_premium