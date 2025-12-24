# 📊 Universal Stock Pattern Analyzer

A comprehensive, reusable toolkit for analyzing cyclical patterns and statistical characteristics of **ANY** stock CSV data.

## 🎯 Purpose

This toolkit was originally developed for analyzing Reliance Industries stock data but is now **completely generalized** to work with any company's stock data. Simply provide a CSV file and get:

- **35+ data files** with pattern analysis
- **Technical indicators** (MA, RSI, MACD, Bollinger Bands, ATR)
- **Statistical metrics** (Sharpe, Sortino, VaR, CVaR, Max Drawdown)
- **Comprehensive visualizations** (5+ chart types)
- **Markdown reports** (Executive Summary, Trading Strategies, Master Index)

---

## 🚀 Quick Start

### One-Command Complete Analysis

```bash
python analyze_stock.py --file "Your_Company_Data.csv" --company "Company Name"
```

That's it! The script will:
1. ✅ Analyze all patterns (weekday, monthly, special patterns)
2. ✅ Calculate technical indicators
3. ✅ Generate visualizations
4. ✅ Create comprehensive reports

### Example

```bash
python analyze_stock.py --file "Infosys_Stock_Data.csv" --company "Infosys"
```

**Output**: Creates `Infosys_Analysis_Complete/` directory with 40+ files organized in 10 subdirectories.

---

## 📋 Requirements

### Input CSV Format

Your CSV file must have these columns:
- `Date` (YYYY-MM-DD format or parseable date)
- `Open` (opening price)
- `High` (high price)
- `Low` (low price)
- `Close` (closing price)
- `Volume` (trading volume)

**Optional columns** (will be calculated if missing):
- `Daily_Return` (calculated from Close prices)
- `Overnight` (calculated from Open and previous Close)
- `Intraday` (calculated from Open and Close)

### Python Dependencies

```bash
pip install pandas numpy matplotlib seaborn scipy
```

Or install from requirements file:
```bash
pip install -r requirements.txt
```

---

## 🗂️ Toolkit Components

### 1. `analyze_stock.py` - **Master Pipeline**
One script to run everything. Orchestrates all analysis modules.

**Usage**:
```bash
# Full analysis
python analyze_stock.py --file "data.csv" --company "ABC Corp"

# Pattern analysis only (fastest)
python analyze_stock.py --file "data.csv" --company "ABC Corp" --skip-stats --skip-viz --skip-reports

# Skip statistical analysis (still get patterns and visualizations)
python analyze_stock.py --file "data.csv" --company "ABC Corp" --skip-stats
```

### 2. `universal_pattern_analyzer.py` - **Pattern Detection**
Identifies cyclical patterns in stock data.

**Analyzes**:
- Weekday patterns (Monday, Tuesday, Wednesday, Thursday, Friday)
- Monthly patterns (January through December)
- Special patterns (April, Wednesday, Month-End, First Monday)

**Output**: 35+ CSV files with raw data and statistics

**Standalone usage**:
```bash
python universal_pattern_analyzer.py --file "data.csv" --company "Company Name"
```

### 3. `universal_statistical_analyzer.py` - **Technical Analysis**
Calculates technical indicators and performance metrics.

**Calculates**:
- **Technical Indicators**: MA (20/50/100/200), RSI, MACD, Bollinger Bands, ATR
- **Performance Metrics**: CAGR, Sharpe Ratio, Sortino Ratio, Max Drawdown
- **Risk Metrics**: VaR, CVaR
- **Attribution**: Yearly returns, win/loss streaks

**Standalone usage**:
```bash
python universal_statistical_analyzer.py --file "Company_Analysis_Complete/00_Master_Data/company_master_data_enhanced.csv" --company "Company Name"
```

### 4. `universal_visualization_generator.py` - **Chart Generator**
Creates comprehensive visualizations.

**Generates**:
- Pattern comparison charts (Mean vs Median, Win Rates, Volatility)
- Cyclical patterns charts (Weekday, Monthly)
- Technical indicator charts (MA, RSI, MACD, Bollinger)
- Performance charts (Cumulative returns, Drawdown, Volume)
- Yearly returns bar chart

**Standalone usage**:
```bash
python universal_visualization_generator.py --analysis_dir "Company_Analysis_Complete" --company "Company Name"
```

### 5. `universal_report_generator.py` - **Report Writer**
Generates markdown reports with findings and strategies.

**Creates**:
- **EXECUTIVE_SUMMARY.md**: Key findings, best patterns, reliability analysis
- **TRADING_STRATEGIES.md**: Pattern-based trading strategies with entry/exit rules
- **MASTER_INDEX.md**: Complete data file navigation guide

**Standalone usage**:
```bash
python universal_report_generator.py --analysis_dir "Company_Analysis_Complete" --company "Company Name"
```

---

## 📂 Output Structure

Running the analysis creates this directory structure:

```
Company_Analysis_Complete/
│
├── 00_Master_Data/
│   └── company_master_data_enhanced.csv (Enhanced dataset with all flags)
│
├── 01_April_Analysis/
│   ├── april_all_days_raw_data.csv (All April trading days)
│   ├── april_yearly_statistics.csv (Year-by-year breakdown)
│   └── april_overall_statistics.csv (Overall statistics)
│
├── 02_Wednesday_Analysis/
│   ├── wednesday_all_days_raw_data.csv
│   ├── wednesday_yearly_statistics.csv
│   └── wednesday_overall_statistics.csv
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
│   ├── monthend_last5days_raw_data.csv
│   ├── monthend_yearly_statistics.csv
│   └── monthend_overall_statistics.csv
│
├── 05_FirstMonday_Analysis/
│   ├── first_monday_raw_data.csv
│   └── first_monday_statistics.csv
│
├── 06_Monthly_Analysis/
│   ├── january_all_days_raw_data.csv
│   ├── february_all_days_raw_data.csv
│   ├── ... (all 12 months)
│   └── monthly_comprehensive_statistics.csv
│
├── 07_Comparison_Tables/
│   └── pattern_comparison_table.csv (All patterns side-by-side)
│
├── 08_Visualizations/
│   ├── pattern_comparison_charts.png
│   ├── cyclical_patterns_charts.png
│   ├── technical_indicators_charts.png
│   ├── performance_charts.png
│   └── yearly_returns_chart.png
│
├── 09_Reports/
│   ├── EXECUTIVE_SUMMARY.md
│   ├── TRADING_STRATEGIES.md
│   └── MASTER_INDEX.md
│
└── 10_Statistical_Analysis/
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

**Total**: 40+ files with complete analysis

---

## 📊 Statistics Provided

Every pattern includes comprehensive statistics:

| Metric | Description |
|--------|-------------|
| **Mean Daily Return** | Average return (can be skewed by outliers) |
| **Median Daily Return** | Typical return (50th percentile) |
| **10th Percentile** | Worst 10% threshold |
| **25th Percentile** | First quartile (stop-loss guide) |
| **75th Percentile** | Third quartile (profit target) |
| **90th Percentile** | Best 10% threshold |
| **Standard Deviation** | Volatility measure |
| **Skewness** | Distribution asymmetry |
| **Kurtosis** | Tail thickness |
| **Win Rate** | Percentage of positive days |
| **Average Win** | Typical winning day |
| **Average Loss** | Typical losing day |
| **Min/Max** | Extreme values |

---

## 💡 Use Cases

### 1. Compare Multiple Companies

```bash
# Analyze Infosys
python analyze_stock.py --file "INFY.csv" --company "Infosys"

# Analyze TCS
python analyze_stock.py --file "TCS.csv" --company "TCS"

# Analyze HDFC Bank
python analyze_stock.py --file "HDFC.csv" --company "HDFC Bank"

# Compare pattern_comparison_table.csv across all three
```

### 2. Identify Best Patterns for a Stock

1. Run analysis
2. Open `07_Comparison_Tables/pattern_comparison_table.csv`
3. Sort by `Median Daily Return (%)`
4. Look for patterns with:
   - High median return
   - High win rate (>50%)
   - Large sample size (>100 days)
   - Small Mean-Median gap (reliable)

### 3. Backtest Pattern Strategies

1. Check pattern's raw data (e.g., `01_April_Analysis/april_all_days_raw_data.csv`)
2. Review yearly statistics for consistency
3. Calculate returns if you had traded the pattern every time
4. Compare with buy-and-hold strategy

### 4. Monitor Pattern Degradation

Run analysis quarterly:
```bash
# Q1 2025
python analyze_stock.py --file "Company_Q1_2025.csv" --company "Company"

# Q2 2025
python analyze_stock.py --file "Company_Q2_2025.csv" --company "Company"

# Compare pattern_comparison_table.csv between quarters
# If median returns declining → pattern may be weakening
```

---

## 🎓 Understanding the Output

### Mean vs Median

**Why both matter**:
- **Mean**: Average of all returns (can be skewed by outliers)
- **Median**: Middle value (50% of days better, 50% worse)

**Interpretation**:
- **Mean ≈ Median** (gap < 0.03%): Symmetric, reliable pattern
- **Mean > Median** (gap > 0.05%): Right-skewed, outliers boost average
- **Mean < Median** (gap > 0.05%): Left-skewed, outliers drag down average

**Example**:
```
April: Mean = +0.234%, Median = +0.105%
Gap = +0.129% → Right-skewed

Interpretation:
- Typical April day: ~+0.10%
- But occasional +3% to +5% days boost average to +0.23%
- Use median for realistic expectations
- Mean shows upside potential
```

### Percentiles for Risk Management

| Percentile | Use Case |
|------------|----------|
| **10th** | Worst 10% - rare bad outcomes |
| **25th** | Stop-loss guide (if below this, you're in worst 25%) |
| **50th (Median)** | Typical outcome |
| **75th** | Profit target (aggressive) |
| **90th** | Best 10% - rare good outcomes |

---

## ⚙️ Advanced Usage

### Custom Analysis

Each module can be run independently for custom workflows:

```bash
# Step 1: Just pattern analysis (fast, 10-30 seconds)
python universal_pattern_analyzer.py --file "data.csv" --company "ABC"

# Step 2: Add statistical analysis later (if needed)
python universal_statistical_analyzer.py --file "ABC_Analysis_Complete/00_Master_Data/abc_master_data_enhanced.csv" --company "ABC"

# Step 3: Generate visualizations
python universal_visualization_generator.py --analysis_dir "ABC_Analysis_Complete" --company "ABC"

# Step 4: Create reports
python universal_report_generator.py --analysis_dir "ABC_Analysis_Complete" --company "ABC"
```

### Batch Processing

Analyze multiple stocks:

```bash
# analyze_multiple_stocks.sh (or .bat on Windows)

python analyze_stock.py --file "stocks/INFY.csv" --company "Infosys"
python analyze_stock.py --file "stocks/TCS.csv" --company "TCS"
python analyze_stock.py --file "stocks/WIPRO.csv" --company "Wipro"
python analyze_stock.py --file "stocks/HCLTECH.csv" --company "HCL Tech"
```

### Subset Analysis

Analyze only recent data:

```python
import pandas as pd

# Load full data
df = pd.read_csv("Company_Full_History.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Keep only last 5 years
df_recent = df[df['Date'] >= '2020-01-01']
df_recent.to_csv("Company_Recent.csv", index=False)

# Analyze recent data
# python analyze_stock.py --file "Company_Recent.csv" --company "Company"
```

---

## 🔍 Troubleshooting

### Common Issues

**1. "File not found" error**
```
Solution: Use absolute path or ensure CSV is in current directory
python analyze_stock.py --file "C:/full/path/to/data.csv" --company "Company"
```

**2. "Date column not found" error**
```
Solution: Ensure CSV has a column named "Date"
Or rename your date column to "Date" before running
```

**3. "Close column not found" error**
```
Solution: Ensure CSV has "Close" column for price data
```

**4. Missing visualizations**
```
Solution: Install matplotlib and seaborn
pip install matplotlib seaborn
```

**5. Script runs but no output**
```
Solution: Check if output directory was created
If not, check file permissions in current directory
```

---

## 📈 Performance

**Typical execution times** (on standard laptop, ~6,000 rows of data):

- Pattern Analysis: 10-30 seconds
- Statistical Analysis: 5-10 seconds
- Visualization: 10-20 seconds
- Report Generation: 2-5 seconds

**Total (complete pipeline)**: 30-70 seconds

**For faster results**:
```bash
# Pattern analysis only (fastest, ~10-30 sec)
python analyze_stock.py --file "data.csv" --company "Company" --skip-stats --skip-viz --skip-reports
```

---

## 🤝 Contributing

This toolkit is designed to be extensible. To add new patterns:

1. Edit `universal_pattern_analyzer.py`
2. Add new pattern analysis method (e.g., `analyze_earnings_month_pattern()`)
3. Call it in `run_complete_analysis()`
4. Follow existing pattern structure for consistency

---

## 📜 License

This toolkit is provided as-is for educational and research purposes.

---

## 🎯 Example: Complete Workflow

```bash
# 1. Get your stock data CSV
# (Download from Yahoo Finance, NSE, BSE, or your broker)

# 2. Ensure it has required columns
# Date, Open, High, Low, Close, Volume

# 3. Run analysis
python analyze_stock.py --file "MyStock.csv" --company "My Company"

# 4. Wait 30-60 seconds...

# 5. Open results:
#    - Read: MyCompany_Analysis_Complete/09_Reports/EXECUTIVE_SUMMARY.md
#    - View charts: MyCompany_Analysis_Complete/08_Visualizations/
#    - Check patterns: MyCompany_Analysis_Complete/07_Comparison_Tables/pattern_comparison_table.csv

# 6. Identify best patterns (high median, high win rate, large sample)

# 7. Review raw data for those patterns

# 8. Develop trading strategy based on findings
```

---

## 📞 Support

For issues or questions:
1. Check this README thoroughly
2. Review example output in `Reliance_Analysis_Complete/` (included as reference)
3. Ensure CSV format matches requirements
4. Check Python version (3.7+ required)

---

**Happy Analyzing! 📊**

Made for analyzing **Reliance Industries**, generalized for **ANY stock**. ✨
