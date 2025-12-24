# 📚 INFOSYS LIMITED - MASTER DATA INDEX

## Complete Analysis Navigation Guide

**Generated**: November 15, 2025

This document provides a comprehensive index of all data files and findings with supporting evidence.

---

## 📂 DIRECTORY STRUCTURE

```
..\3_Example_Analyses\Infosys_Analysis_Complete/
│
├── 00_Master_Data/
│   └── infosys_limited_master_data_enhanced.csv
│       (Complete dataset with all pattern flags)
│
├── 01_April_Analysis/
│   ├── april_all_days_raw_data.csv (All April trading days)
│   ├── april_yearly_statistics.csv (Year-by-year April performance)
│   └── april_overall_statistics.csv (Overall April statistics)
│
├── 02_Wednesday_Analysis/
│   ├── wednesday_all_days_raw_data.csv (All Wednesdays)
│   ├── wednesday_yearly_statistics.csv (Year-by-year Wednesday performance)
│   └── wednesday_overall_statistics.csv (Overall Wednesday statistics)
│
├── 03_Weekday_Analysis/
│   ├── monday_all_days_raw_data.csv
│   ├── tuesday_all_days_raw_data.csv
│   ├── wednesday_all_days_raw_data.csv
│   ├── thursday_all_days_raw_data.csv
│   ├── friday_all_days_raw_data.csv
│   └── weekday_comprehensive_statistics.csv
│
├── 04_MonthEnd_Analysis/
│   ├── monthend_last5days_raw_data.csv (All month-end periods)
│   ├── monthend_yearly_statistics.csv
│   └── monthend_overall_statistics.csv
│
├── 05_FirstMonday_Analysis/
│   ├── first_monday_raw_data.csv (All first Mondays)
│   └── first_monday_statistics.csv
│
├── 06_Monthly_Analysis/
│   ├── january_all_days_raw_data.csv
│   ├── february_all_days_raw_data.csv
│   ├── march_all_days_raw_data.csv
│   ├── april_all_days_raw_data.csv
│   ├── may_all_days_raw_data.csv
│   ├── june_all_days_raw_data.csv
│   ├── july_all_days_raw_data.csv
│   ├── august_all_days_raw_data.csv
│   ├── september_all_days_raw_data.csv
│   ├── october_all_days_raw_data.csv
│   ├── november_all_days_raw_data.csv
│   ├── december_all_days_raw_data.csv
│   └── monthly_comprehensive_statistics.csv
│
├── 07_Comparison_Tables/
│   └── pattern_comparison_table.csv (All patterns compared)
│
├── 08_Visualizations/
│   ├── pattern_comparison_charts.png
│   ├── cyclical_patterns_charts.png
│   ├── technical_indicators_charts.png
│   ├── performance_charts.png
│   └── yearly_returns_chart.png
│
├── 09_Reports/
│   ├── EXECUTIVE_SUMMARY.md (This file)
│   ├── TRADING_STRATEGIES.md
│   └── MASTER_INDEX.md
│
└── 10_Statistical_Analysis/ (if run)
    ├── moving_averages.csv
    ├── rsi_data.csv
    ├── macd_data.csv
    ├── bollinger_bands.csv
    ├── atr_data.csv
    ├── performance_metrics.csv
    ├── yearly_returns.csv
    ├── risk_metrics.csv
    └── enhanced_data_with_indicators.csv
```

---

## 🔍 FINDING → DATA FILE LOOKUP

### Pattern Analysis Findings

| Finding | Supporting Raw Data | Sample Size |
|---------|-------------------|-------------|
| All Days: Mean=+0.065%, Median=+0.038% | `07_Comparison_Tables/pattern_comparison_table.csv` | 6,433 days |
| Wednesday: Mean=+0.103%, Median=+0.040% | `02_Wednesday_Analysis/wednesday_all_days_raw_data.csv` | 1,285 days |
| Monday: Mean=+0.033%, Median=+0.036% | `03_Weekday_Analysis/monday_all_days_raw_data.csv` | 1,281 days |
| April: Mean=-0.200%, Median=-0.086% | `01_April_Analysis/april_all_days_raw_data.csv` | 497 days |
| February: Mean=+0.012%, Median=+0.004% | `07_Comparison_Tables/pattern_comparison_table.csv` | 516 days |
| Month-End (Last 5): Mean=+0.149%, Median=+0.057% | `04_MonthEnd_Analysis/monthend_last5days_raw_data.csv` | 1,555 days |
| First Monday: Mean=+0.236%, Median=+0.155% | `05_FirstMonday_Analysis/first_monday_raw_data.csv` | 310 days |


---

## 📊 HOW TO VERIFY ANY FINDING

### Example: Verifying "Wednesday averages +X%"

1. **Open the raw data**:
   ```
   ..\3_Example_Analyses\Infosys_Analysis_Complete/02_Wednesday_Analysis/wednesday_all_days_raw_data.csv
   ```

2. **Check the statistics file**:
   ```
   ..\3_Example_Analyses\Infosys_Analysis_Complete/02_Wednesday_Analysis/wednesday_overall_statistics.csv
   ```

3. **Review year-by-year consistency**:
   ```
   ..\3_Example_Analyses\Infosys_Analysis_Complete/02_Wednesday_Analysis/wednesday_yearly_statistics.csv
   ```

4. **Compare with other patterns**:
   ```
   ..\3_Example_Analyses\Infosys_Analysis_Complete/07_Comparison_Tables/pattern_comparison_table.csv
   ```

### Understanding the Statistics Files

Each `*_overall_statistics.csv` contains:
- **Mean Daily Return**: Average return (can be skewed by outliers)
- **Median Daily Return**: Typical return (50th percentile)
- **10th/25th/75th/90th Percentile**: Distribution insights
- **Std Deviation**: Volatility measure
- **Win Rate**: Percentage of positive days
- **Skewness**: Distribution asymmetry
- **Kurtosis**: Tail thickness

---

## 🎓 USING THIS INDEX

### For Quick Analysis:
1. Start with `07_Comparison_Tables/pattern_comparison_table.csv`
2. Identify interesting patterns
3. Drill down to pattern-specific folders

### For Deep Dive:
1. Open pattern's raw data file (all daily records)
2. Review yearly statistics (year-by-year consistency)
3. Check overall statistics (comprehensive metrics)
4. Compare with other patterns

### For Validation:
1. Open raw data in Excel/spreadsheet
2. Calculate your own statistics
3. Compare with provided statistics files
4. Verify sample sizes and date ranges

---

## 📈 VISUALIZATION FILES

All charts saved in `08_Visualizations/`:

1. **pattern_comparison_charts.png**
   - Mean vs Median returns
   - Win rates by pattern
   - Volatility comparison
   - Sample size overview

2. **cyclical_patterns_charts.png**
   - Weekday performance
   - Monthly performance
   - Seasonal trends

3. **technical_indicators_charts.png** (if statistical analysis run)
   - Moving averages
   - RSI
   - MACD
   - Bollinger Bands

4. **performance_charts.png**
   - Cumulative returns
   - Drawdown analysis
   - Price chart
   - Volume trends

5. **yearly_returns_chart.png**
   - Year-by-year returns
   - Performance consistency

---

## 💡 KEY INSIGHTS

### Mean vs Median Analysis

**All Days**:
- Mean: +0.065%
- Median: +0.038%
- Gap: +0.027%
- **Interpretation**: Symmetric, reliable (mean ≈ median)

**Wednesday**:
- Mean: +0.103%
- Median: +0.040%
- Gap: +0.063%
- **Interpretation**: Right-skewed (positive outliers boost mean)

**Monday**:
- Mean: +0.033%
- Median: +0.036%
- Gap: -0.003%
- **Interpretation**: Symmetric, reliable (mean ≈ median)

**April**:
- Mean: -0.200%
- Median: -0.086%
- Gap: -0.114%
- **Interpretation**: Left-skewed (negative outliers drag mean down)

**February**:
- Mean: +0.012%
- Median: +0.004%
- Gap: +0.008%
- **Interpretation**: Symmetric, reliable (mean ≈ median)


---

**Generated by**: Universal Stock Analyzer  
**Date**: November 15, 2025 at 03:37 PM  
**Company**: Infosys Limited
