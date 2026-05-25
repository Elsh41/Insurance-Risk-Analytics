
---

# Insurance Risk Analytics: Task 1 - EDA & Environment Setup

This repository contains the foundational phase of an end-to-end insurance risk analysis project. The primary objective of Task 1 is to establish a reproducible development environment and perform a deep-dive Exploratory Data Analysis (EDA) on a portfolio of over 1 million insurance records.

## 📌 Project Overview

The analysis focuses on uncovering patterns in risk and profitability by examining the relationship between **Total Premiums** and **Total Claims**. A key performance indicator used throughout this phase is the **Loss Ratio** ($\frac{Claims}{Premium}$).

---

## 🛠️ Reproducibility & Environment

### 1. Repository Structure

The project follows a modular architecture to separate logic from presentation:

* `data/`: Data directory (Tracked via **DVC**; `.txt` files are git-ignored).
* `notebooks/`: Sequential Jupyter notebooks for analysis (e.g., `01_eda.ipynb`).
* `src/`: Reusable Python modules for data loading and analytical utilities.
* `.github/workflows/`: CI pipeline configuration for automated linting and testing.

### 2. Setup Instructions

To reproduce this environment locally:

```bash
# Clone the repository
git clone <your-repo-url>
cd insurance-risk-analytics

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements| `data/` | Raw and processed data (managed via **DVC**). |
| `notebooks/` | Numbered research notebooks (starting.txt

# Pull the data via DVC (if remote is configured)
dvc pull

```

---

## 🔍 Task 1: Exploratory Data Analysis (EDA)

### Key Analytical Findings

* **Portfolio Health:** The overall portfolio loss ratio was calculated at **104.77%**, indicating that the current underwriting strategy is yielding a net loss on claims alone.
* **Geographic Risk:** Significant volatility was observed across provinces. **Gauteng (122%)** and **Western Cape (106%)** represent high-risk clusters, while **Northern Cape (28%)** remains highly profitable.
* **Data Quality:** Handled a pipe-delimited (`|`) dataset of **1,000,098 rows**. Analysis included a full check extreme outliers representing "shock losses" that significantly impact the mean.

### Visualizations Included

1. **Provincial Loss Ratio Distribution:** A categorical breakdown highlighting profitable vs. unprofitable regions.
2. **Financial Histograms & Boxplots:** Visualizing the skewness and outliers in claim amounts and vehicle values.
3. **18-Month Temporal Trends:** (In progress) Mapping claim frequency and severity over the 1.5-year observation window.

---

## 🤖 CI/CD Integration

This repository uses **GitHub Actions** to maintain code quality.

* **Linting:** `flake8` checks all `src/` and `notebook/` files for PEP 8 compliance on every push.
* **Testing:** Automated tests ensure the `data_loader` and `eda_utils` modules remain stable during refactoring.

---

## 📝 Deliverables

* [x] GitHub Repository with modular `src/` structure.
* [x] DVC integration for large-scale `.txt` data tracking.
* [x] GitHub Actions CI Workflow.
* [x] Comprehensive EDA Notebook (`01_eda.ipynb`) with calculated Loss Ratios and insight-driven plots.

---

