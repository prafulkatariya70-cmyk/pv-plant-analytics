# PV Plant Performance Analytics

A data analytics project analyzing solar photovoltaic (PV) plant performance using Performance Ratio (PR) and Global Horizontal Irradiance (GHI) metrics.

## Overview

This project processes daily performance data from a PV plant (July 2019 - March 2022) and generates insights through data visualization and statistical analysis.

## Features

- **Data Preprocessing:** Merges 197+ distributed CSV files (PR and GHI data) into a unified dataset
- **Time Series Analysis:** Calculates 30-day moving averages and performance trends
- **Dynamic Budget Calculation:** Implements annual 0.8% degradation model for performance budgeting
- **Interactive Visualization:** Color-coded scatter plots, trend lines, and statistical summaries

## Files

- `preprocess_data.py` - Consolidates raw data from `data/GHI` and `data/PR` folders into a single CSV
- `generate_graph.py` - Generates PR evolution visualization with multi-metric analysis
- `merged_data.csv` - Processed dataset (982 records, 3 columns: Date, GHI, PR)
- `pr_graph.png` - Output visualization

## Usage

### Prerequisites
```bash
pip install pandas matplotlib
```

### Run Preprocessing
```bash
python preprocess_data.py
```
Outputs: `merged_data.csv` (982 rows of merged data)

### Generate Visualization
```bash
python generate_graph.py
```
Outputs: `pr_graph.png`

## Data Format

**merged_data.csv:**
| Date | GHI | PR |
|------|-----|-----|
| 2019-07-01 | 3.26 | 69.58 |
| ... | ... | ... |

- **Date:** Daily measurement (YYYY-MM-DD format)
- **GHI:** Global Horizontal Irradiance [kWh/m²]
- **PR:** Performance Ratio [%]

## Visualization Details

The generated chart includes:
- **Scatter Points:** Color-coded by GHI intensity (Navy < 2 | Light Blue 2-4 | Orange 4-6 | Brown > 6)
- **Red Line:** 30-day moving average of PR
- **Green Line:** Dynamic budget line (73.9% declining 0.8% annually)
- **Statistics Box:** Trailing averages (7, 30, 60, 90, 365 days)

## Technical Approach

- **Language:** Python 3
- **Libraries:** Pandas (data manipulation), Matplotlib (visualization)
- **Data Volume:** 982 daily records across 197 source files
- **Time Period:** July 1, 2019 - March 24, 2022

## Key Insights

- Dynamically computed budget degradation (no hardcoded values)
- Handles data consolidation from nested directory structures
- Efficient rolling window calculations for trend analysis
- Professional visualization with multi-metric analysis

## Author

Praful Kumar

## License

Private submission for assessment purposes
