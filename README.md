# Data Descriptive Analysis

This project performs descriptive statistical analysis on datasets related to 2024 presidential election posts and ads. The analysis is implemented using three approaches:

1. `pure_python_stats_cli.py` – Pure Python (standard library only)
2. `pandas_stats_cli.py` – Using **Pandas**
3. `polars_stats_cli.py` – Using **Polars** for high-performance data processing

---

## Files

| File                    | Description                                                              |
|-------------------------|--------------------------------------------------------------------------|
| `pure_python_stats_cli.py` | Loads and analyzes the dataset using only the Python standard library (no external dependencies). |
| `pandas_stats_cli.py`      | Performs the same analysis using the Pandas library.                  |
| `polars_stats_cli.py`      | Uses Polars for fast dataframe computation and analysis.              |

---

## How to Run the Scripts

### Requirements

Install dependencies for the Pandas and Polars scripts:

```bash
pip install pandas polars
```

## Running from the Command Line
All scripts accept the path to the CSV file as the first argument.

### 1. Run the Pure Python Script
```bash
python pure_python_stats_cli.py your_dataset.csv
```
### 2. Run the Pandas Script
```bash
python pandas_stats_cli.py your_dataset.csv
```
## 3. Run the Polars Script
```
python polars_stats_cli.py your_dataset.csv
```
## What Each Script Does
  - Loads the provided dataset (CSV format)

### Computes descriptive statistics:

- Count, mean, min, max, standard deviation for numeric fields

- Unique value count and most frequent value for categorical fields

- Groups data by combinations such as: page_id and ad_id (if applicable)

- Outputs results directly to the console


