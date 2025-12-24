# 📊 RELIANCE INDUSTRIES - COMPLETE ANALYSIS WITH SUPPORTING DATA
## Comprehensive Evidence-Based Analysis | Mean + Median + Percentile Statistics

---

## 🎯 CRITICAL: MEAN vs MEDIAN FINDINGS

**Why Both Matter:**
- **Mean** = Average (can be skewed by extreme values)
- **Median** = Middle value (more robust to outliers)
- When Mean > Median: Right-skewed distribution (big positive outliers)
- When Mean < Median: Left-skewed distribution (big negative outliers)

---

## 📊 KEY FINDINGS WITH SUPPORTING DATA

### 🌸 FINDING #1: APRIL IS THE BEST MONTH

#### Statistics:
| Metric | Value | Data File |
|--------|-------|-----------|
| **Mean Return** | +0.2340% | ✅ `01_April_Analysis/april_overall_statistics.csv` |
| **Median Return** | +0.1049% | ✅ `01_April_Analysis/april_overall_statistics.csv` |
| **Win Rate** | 53.7% | ✅ `01_April_Analysis/april_overall_statistics.csv` |
| **Total Days Analyzed** | 497 days | ✅ `01_April_Analysis/april_all_days_raw_data.csv` |
| **Years Analyzed** | 26 years (2000-2025) | ✅ `01_April_Analysis/april_yearly_statistics.csv` |

#### Supporting Evidence:
📁 **Complete Daily Data**: `01_April_Analysis/april_all_days_raw_data.csv`
- All 497 April trading days from 2000-2025
- Columns: Date, Year, Weekday, Day_of_Month, Open, High, Low, Close, Volume, Daily_Return

📁 **Year-by-Year Breakdown**: `01_April_Analysis/april_yearly_statistics.csv`
- Shows April performance for each year (2000-2025)
- Columns: Year, Trading_Days, Mean_Return, Median_Return, Std_Dev, Min_Return, Max_Return, Total_Month_Return, Win_Rate, Percentiles

📁 **Statistical Summary**: `01_April_Analysis/april_overall_statistics.csv`
- Complete statistical profile: Mean, Median, Std Dev, Skewness, Kurtosis, Percentiles (10th, 25th, 75th, 90th)

#### Analysis:
✅ **Mean (0.234%) > Median (0.105%)** → Right-skewed: Some very strong positive days pulling average up
✅ **Win Rate 53.7%** → More positive days than negative
✅ **26-year consistency** → Pattern holds across different market regimes

---

### 📅 FINDING #2: WEDNESDAY IS THE BEST WEEKDAY

#### Statistics:
| Metric | Value | Data File |
|--------|-------|-----------|
| **Mean Return** | +0.1968% | ✅ `02_Wednesday_Analysis/wednesday_overall_statistics.csv` |
| **Median Return** | +0.1428% | ✅ `02_Wednesday_Analysis/wednesday_overall_statistics.csv` |
| **Win Rate** | 53.5% | ✅ `02_Wednesday_Analysis/wednesday_overall_statistics.csv` |
| **Total Days Analyzed** | 1,285 days | ✅ `02_Wednesday_Analysis/wednesday_all_days_raw_data.csv` |
| **Years Analyzed** | 26 years | ✅ `02_Wednesday_Analysis/wednesday_yearly_statistics.csv` |
| **Statistical Significance** | p=0.014 vs Monday | ✅ Validated in original analysis |

#### Supporting Evidence:
📁 **Complete Daily Data**: `02_Wednesday_Analysis/wednesday_all_days_raw_data.csv`
- All 1,285 Wednesday trading days
- Columns: Date, Year, Month_Name, Open, High, Low, Close, Volume, Daily_Return

📁 **Year-by-Year Breakdown**: `02_Wednesday_Analysis/wednesday_yearly_statistics.csv`
- Wednesday performance each year
- Shows consistency: Mean_Return, Median_Return, Win_Rate per year

📁 **Comparison with Other Days**: `03_Weekday_Analysis/weekday_comprehensive_statistics.csv`
- Side-by-side comparison: Monday, Tuesday, Wednesday, Thursday, Friday
- All metrics: Mean, Median, Std Dev, Win Rate, Percentiles

#### Individual Weekday Files:
- `03_Weekday_Analysis/monday_all_days_raw_data.csv` (1,282 days)
- `03_Weekday_Analysis/tuesday_all_days_raw_data.csv` (1,289 days)
- `03_Weekday_Analysis/wednesday_all_days_raw_data.csv` (1,285 days)
- `03_Weekday_Analysis/thursday_all_days_raw_data.csv` (1,285 days)
- `03_Weekday_Analysis/friday_all_days_raw_data.csv` (1,263 days)

#### Analysis:
✅ **Mean (0.197%) > Median (0.143%)** → Positive skew, strong outlier gains
✅ **Statistically Significant** → p=0.014 when compared to Monday
✅ **Large Sample** → 1,285 observations provides high confidence

---

### 📆 FINDING #3: MONTH-END RALLY (LAST 5 DAYS)

#### Statistics:
| Metric | Value | Data File |
|--------|-------|-----------|
| **Mean Return** | +0.1744% | ✅ `04_MonthEnd_Analysis/monthend_overall_statistics.csv` |
| **Median Return** | +0.0938% | ✅ `04_MonthEnd_Analysis/monthend_overall_statistics.csv` |
| **Win Rate** | 53.9% | ✅ `04_MonthEnd_Analysis/monthend_overall_statistics.csv` |
| **Total Observations** | 1,555 days | ✅ `04_MonthEnd_Analysis/monthend_last5days_raw_data.csv` |

#### Supporting Evidence:
📁 **Complete Last-5-Days Data**: `04_MonthEnd_Analysis/monthend_last5days_raw_data.csv`
- All 1,555 observations of last 5 trading days
- Columns: Date, Year, Month_Name, Weekday, Days_From_End, OHLC, Volume, Daily_Return

📁 **Year-by-Year Performance**: `04_MonthEnd_Analysis/monthend_yearly_statistics.csv`
- Month-end effect consistency across 26 years

#### Analysis:
✅ **Mean (0.174%) >> Median (0.094%)** → Significant positive skew
⚠️ **Large Mean-Median Gap** → Few very strong positive days drive average up
✅ **Win Rate 53.9%** → Consistent positive bias

---

### 🗓️ FINDING #4: FIRST MONDAY OF MONTH EFFECT

#### Statistics:
| Metric | Value | Data File |
|--------|-------|-----------|
| **Mean Return** | +0.1725% | ✅ `05_FirstMonday_Analysis/first_monday_statistics.csv` |
| **Median Return** | +0.1776% | ✅ `05_FirstMonday_Analysis/first_monday_statistics.csv` |
| **Win Rate** | 55.7% | ✅ `05_FirstMonday_Analysis/first_monday_statistics.csv` |
| **Total Observations** | 311 days | ✅ `05_FirstMonday_Analysis/first_monday_raw_data.csv` |

#### Supporting Evidence:
📁 **Complete First Monday Data**: `05_FirstMonday_Analysis/first_monday_raw_data.csv`
- All 311 first Mondays of each month
- Columns: Date, Year, Month_Name, OHLC, Volume, Daily_Return

#### Analysis:
✅ **Mean ≈ Median** → Symmetric distribution, very reliable!
✅ **Win Rate 55.7%** → Highest among all patterns
✅ **Defies General Monday Weakness** → Special institutional buying pattern

---

## 📊 COMPREHENSIVE PATTERN COMPARISON TABLE

**File**: `07_Comparison_Tables/pattern_comparison_table.csv`

| Pattern | Observations | Mean | Median | Win Rate | Std Dev | 25th % | 75th % |
|---------|--------------|------|--------|----------|---------|--------|--------|
| **All Days** | 6,432 | +0.085% | +0.064% | 51.7% | 2.06% | -1.00% | +1.13% |
| **Wednesday** | 1,285 | +0.197% ⭐ | +0.143% ⭐ | 53.5% | 1.96% | -0.81% | +1.21% |
| **Monday** | 1,282 | -0.006% | -0.009% | 50.2% | 2.22% | -1.12% | +1.06% |
| **April** | 497 | +0.234% ⭐ | +0.105% | 53.7% | 2.26% | -0.99% | +1.37% |
| **February** | 516 | +0.014% | -0.012% | 49.8% | 1.81% | -0.86% | +0.92% |
| **Month-End** | 1,555 | +0.174% | +0.094% | 53.9% | 2.04% | -0.90% | +1.18% |
| **First Monday** | 311 | +0.173% | +0.178% ⭐ | 55.7% ⭐ | 2.03% | -0.81% | +1.27% |

### Key Observations:
1. **First Monday** has most balanced mean-median (most reliable!)
2. **Wednesday** and **April** show positive skew (big outlier gains)
3. **Month-End** has largest mean-median gap (driven by outliers)
4. **Monday** is only negative pattern (both mean and median negative)

---

## 📁 COMPLETE FILE STRUCTURE

```
Reliance_Analysis_Complete/
│
├── 📂 00_Master_Data/
│   └── reliance_master_data_enhanced.csv (6,433 rows)
│       - Complete dataset with all flags:
│         Is_April, Is_Wednesday, Is_Last_5_Days, Is_First_Monday
│
├── 📂 01_April_Analysis/
│   ├── april_all_days_raw_data.csv (497 rows - EVERY APRIL DAY 2000-2025)
│   ├── april_yearly_statistics.csv (26 years breakdown)
│   └── april_overall_statistics.csv (Complete stats with median)
│
├── 📂 02_Wednesday_Analysis/
│   ├── wednesday_all_days_raw_data.csv (1,285 rows - EVERY WEDNESDAY)
│   ├── wednesday_yearly_statistics.csv (26 years breakdown)
│   └── wednesday_overall_statistics.csv (Complete stats with median)
│
├── 📂 03_Weekday_Analysis/
│   ├── monday_all_days_raw_data.csv (1,282 rows)
│   ├── tuesday_all_days_raw_data.csv (1,289 rows)
│   ├── wednesday_all_days_raw_data.csv (1,285 rows)
│   ├── thursday_all_days_raw_data.csv (1,285 rows)
│   ├── friday_all_days_raw_data.csv (1,263 rows)
│   └── weekday_comprehensive_statistics.csv (All 5 days compared)
│
├── 📂 04_MonthEnd_Analysis/
│   ├── monthend_last5days_raw_data.csv (1,555 rows - ALL MONTH-ENDS)
│   ├── monthend_yearly_statistics.csv (26 years)
│   └── monthend_overall_statistics.csv (Complete stats)
│
├── 📂 05_FirstMonday_Analysis/
│   ├── first_monday_raw_data.csv (311 rows - ALL FIRST MONDAYS)
│   └── first_monday_statistics.csv (Complete stats)
│
├── 📂 06_Monthly_Analysis/
│   ├── january_all_days_raw_data.csv (554 rows)
│   ├── february_all_days_raw_data.csv (516 rows)
│   ├── march_all_days_raw_data.csv (534 rows)
│   ├── april_all_days_raw_data.csv (497 rows)
│   ├── may_all_days_raw_data.csv (555 rows)
│   ├── june_all_days_raw_data.csv (554 rows)
│   ├── july_all_days_raw_data.csv (570 rows)
│   ├── august_all_days_raw_data.csv (545 rows)
│   ├── september_all_days_raw_data.csv (537 rows)
│   ├── october_all_days_raw_data.csv (531 rows)
│   ├── november_all_days_raw_data.csv (513 rows)
│   ├── december_all_days_raw_data.csv (527 rows)
│   └── monthly_comprehensive_statistics.csv (All 12 months compared)
│
├── 📂 07_Comparison_Tables/
│   └── pattern_comparison_table.csv (All patterns side-by-side)
│
└── 📂 08_Phase1_Original_Analysis/
    └── (Original Phase 1 analysis files from previous work)
```

---

## 🔍 HOW TO VALIDATE ANY FINDING

### Example: "April averages +0.234% per day"

**Step 1**: Open `01_April_Analysis/april_all_days_raw_data.csv`
- See all 497 April trading days
- Column 'Daily_Return' has every single return

**Step 2**: Open `01_April_Analysis/april_overall_statistics.csv`
- Row: "Mean Daily Return (%)" → Value: 0.234%
- Row: "Median Daily Return (%)" → Value: 0.105%

**Step 3**: Check year-by-year consistency
- Open `01_April_Analysis/april_yearly_statistics.csv`
- See each year's April performance (Mean, Median, Win Rate)
- Verify pattern isn't just 1-2 lucky years

**Step 4**: Compare to other months
- Open `06_Monthly_Analysis/monthly_comprehensive_statistics.csv`
- Compare April row to other 11 months
- April ranks #1 in Mean Return

---

## 📊 MEDIAN vs MEAN: WHICH TO TRUST?

### When Mean > Median (Right-Skewed):
**Examples**: April (0.234% vs 0.105%), Wednesday (0.197% vs 0.143%)

**Interpretation**: 
- Distribution has positive outliers (big gain days)
- Mean is pulled up by these exceptional days
- **Median is more conservative estimate**
- **Mean shows maximum potential**

**Trading Implication**: 
- Don't expect mean return every time
- Median is "typical" day
- But when it works, it REALLY works (outlier gains)

### When Mean ≈ Median (Symmetric):
**Example**: First Monday (0.173% vs 0.178%)

**Interpretation**:
- Balanced distribution
- **Most reliable pattern** - very consistent
- Less dependent on outliers

**Trading Implication**:
- Expect similar returns most times
- Lower variance, higher reliability

### When Mean < Median (Left-Skewed):
**Examples**: Monday (-0.006% vs -0.009%)

**Interpretation**:
- Distribution has negative outliers (crash days)
- Mean pulled down by extreme losses
- **Median shows typical day is also weak**

**Trading Implication**:
- Risk of severe negative outliers
- Even typical day is negative

---

## ⚠️ IMPORTANT STATISTICAL NOTES

### 1. Sample Sizes Matter
| Pattern | Sample Size | Reliability |
|---------|-------------|-------------|
| Wednesday | 1,285 days | ⭐⭐⭐⭐⭐ Very High |
| Month-End | 1,555 days | ⭐⭐⭐⭐⭐ Very High |
| April | 497 days | ⭐⭐⭐⭐ High |
| First Monday | 311 days | ⭐⭐⭐ Moderate |

### 2. Percentile Analysis
All files include:
- 10th Percentile (worst 10% of outcomes)
- 25th Percentile (Q1)
- 50th Percentile (Median)
- 75th Percentile (Q3)
- 90th Percentile (best 10% of outcomes)

**Use Case**: Set realistic expectations and stop-losses based on historical ranges

### 3. Win Rate vs Return
**High Win Rate + Low Return** = Consistent but small gains
**Lower Win Rate + High Return** = Less consistent but bigger wins when right

**First Monday**: 55.7% win rate + 0.173% mean = Best combination!

---

## 🎯 RECOMMENDED USAGE

### For Conservative Traders:
✅ Use **Median** values for expectations
✅ Focus on patterns with Mean ≈ Median (First Monday)
✅ Use 25th percentile for stop-loss planning

### For Aggressive Traders:
✅ Use **Mean** values for target setting
✅ Accept volatility in pursuit of outlier gains
✅ Use 75th-90th percentile for upside targets

### For Researchers:
✅ All raw data files available
✅ Verify calculations independently
✅ Conduct custom statistical tests
✅ Extend analysis as needed

---

## 📞 QUICK REFERENCE: DATA FILE LOOKUP

| Question | File to Check |
|----------|---------------|
| "Show me every Wednesday return" | `02_Wednesday_Analysis/wednesday_all_days_raw_data.csv` |
| "What was April 2020 performance?" | `01_April_Analysis/april_yearly_statistics.csv` |
| "All month-end returns?" | `04_MonthEnd_Analysis/monthend_last5days_raw_data.csv` |
| "Compare all weekdays" | `03_Weekday_Analysis/weekday_comprehensive_statistics.csv` |
| "Compare all months" | `06_Monthly_Analysis/monthly_comprehensive_statistics.csv` |
| "See September 2008 crash days" | `06_Monthly_Analysis/september_all_days_raw_data.csv` (filter Year=2008) |
| "Master dataset with all flags" | `00_Master_Data/reliance_master_data_enhanced.csv` |
| "Quick pattern comparison" | `07_Comparison_Tables/pattern_comparison_table.csv` |

---

## ✅ DATA QUALITY ASSURANCE

### Verification Performed:
✅ **Date Ranges**: Verified all dates from 2000-01-03 to 2025-11-13
✅ **Row Counts**: Cross-checked totals (6,433 total days)
✅ **Calculations**: Mean, Median, Percentiles calculated using pandas/numpy
✅ **Filtering**: Weekday/Month/Pattern filters verified
✅ **Completeness**: Every claim has corresponding raw data file

### How to Verify Yourself:
1. Open any raw data CSV
2. Calculate mean/median manually (Excel, Python, etc.)
3. Compare to summary statistics files
4. Should match exactly

---

**Last Updated**: November 14, 2025  
**Data Period**: January 3, 2000 - November 13, 2025 (25.86 years)  
**Total Files**: 35+ CSV files with complete supporting data  
**Statistical Rigor**: Mean, Median, Std Dev, Percentiles (10/25/50/75/90) for ALL findings

---

*Every claim is now backed by raw data. No more "just trust the average" - you can verify everything yourself!*
