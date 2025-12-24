# 🎯 Quick Start Examples

## Example 1: Analyze Infosys Stock

### Step 1: Prepare your CSV file

Your `Infosys.csv` should look like this:

```csv
Date,Open,High,Low,Close,Volume
2020-01-01,800.50,810.25,795.00,805.30,1500000
2020-01-02,806.00,815.50,803.00,812.75,1650000
2020-01-03,813.00,820.00,810.50,818.25,1800000
...
```

### Step 2: Run the analyzer

```bash
python analyze_stock.py --file "Infosys.csv" --company "Infosys"
```

### Step 3: View results

```bash
# Open executive summary
notepad "Infosys_Analysis_Complete/09_Reports/EXECUTIVE_SUMMARY.md"

# Or on Mac/Linux
open "Infosys_Analysis_Complete/09_Reports/EXECUTIVE_SUMMARY.md"
```

### Step 4: Explore the data

```bash
# View pattern comparison in Excel/Google Sheets
excel "Infosys_Analysis_Complete/07_Comparison_Tables/pattern_comparison_table.csv"

# View visualizations
start "Infosys_Analysis_Complete/08_Visualizations/pattern_comparison_charts.png"
```

---

## Example 2: Fast Pattern-Only Analysis

If you just want to see patterns without statistical indicators (faster):

```bash
python analyze_stock.py --file "TCS.csv" --company "TCS" --skip-stats --skip-viz --skip-reports
```

**Result**: Gets you pattern data in 10-20 seconds instead of 60 seconds.

**When to use**: 
- Quick exploration
- You only care about weekday/monthly patterns
- Testing on a new dataset

---

## Example 3: Compare Multiple Companies

### Analyze 5 companies

```bash
# Batch script: analyze_all.bat (Windows) or analyze_all.sh (Linux/Mac)

python analyze_stock.py --file "data/Infosys.csv" --company "Infosys"
python analyze_stock.py --file "data/TCS.csv" --company "TCS"
python analyze_stock.py --file "data/Wipro.csv" --company "Wipro"
python analyze_stock.py --file "data/HCL.csv" --company "HCL Tech"
python analyze_stock.py --file "data/TechM.csv" --company "Tech Mahindra"
```

### Compare results

```python
# compare_companies.py
import pandas as pd

# Load all comparison tables
companies = ['Infosys', 'TCS', 'Wipro', 'HCL_Tech', 'Tech_Mahindra']
comparisons = {}

for company in companies:
    file_path = f"{company}_Analysis_Complete/07_Comparison_Tables/pattern_comparison_table.csv"
    comparisons[company] = pd.read_csv(file_path)

# Find best Wednesday performance
for company, df in comparisons.items():
    wed_data = df[df['Pattern'] == 'Wednesday']
    if len(wed_data) > 0:
        median_return = wed_data['Median Daily Return (%)'].iloc[0]
        print(f"{company:20s}: Wednesday median = {median_return:+.3f}%")
```

---

## Example 4: Analyze Only Recent Data (Last 3 Years)

```python
# filter_recent.py
import pandas as pd
from datetime import datetime, timedelta

# Load full history
df = pd.read_csv("Company_Full_History.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Keep only last 3 years
cutoff_date = datetime.now() - timedelta(days=3*365)
df_recent = df[df['Date'] >= cutoff_date]

# Save filtered data
df_recent.to_csv("Company_Recent_3Y.csv", index=False)

print(f"Filtered: {len(df)} rows → {len(df_recent)} rows")
```

```bash
# Now analyze recent data
python analyze_stock.py --file "Company_Recent_3Y.csv" --company "Company (3Y)"
```

---

## Example 5: Incremental Analysis (Run Steps Separately)

Sometimes you want control over each step:

```bash
# Step 1: Pattern analysis only (required first step)
python universal_pattern_analyzer.py --file "Stock.csv" --company "Stock Name"

# Check results before continuing...

# Step 2: Add technical analysis
python universal_statistical_analyzer.py --file "Stock_Name_Analysis_Complete/00_Master_Data/stock_name_master_data_enhanced.csv" --company "Stock Name"

# Step 3: Generate charts
python universal_visualization_generator.py --analysis_dir "Stock_Name_Analysis_Complete" --company "Stock Name"

# Step 4: Create reports
python universal_report_generator.py --analysis_dir "Stock_Name_Analysis_Complete" --company "Stock Name"
```

**When to use**:
- Large datasets (10,000+ rows)
- Want to review intermediate results
- Testing or debugging

---

## Example 6: Backtesting a Pattern

Let's say you found that "First Monday" has a median return of +0.18% with a 55% win rate.

### Extract the data

```python
# backtest_first_monday.py
import pandas as pd

# Load First Monday raw data
df = pd.read_csv("Company_Analysis_Complete/05_FirstMonday_Analysis/first_monday_raw_data.csv")

# Calculate strategy returns
df['Strategy_Return'] = df['Daily_Return']  # Buy every First Monday, sell at close
cumulative_return = (1 + df['Strategy_Return']/100).prod() - 1

# Calculate stats
win_rate = (df['Daily_Return'] > 0).mean()
avg_win = df[df['Daily_Return'] > 0]['Daily_Return'].mean()
avg_loss = df[df['Daily_Return'] < 0]['Daily_Return'].mean()

print(f"First Monday Strategy Backtest:")
print(f"  Total Trades: {len(df)}")
print(f"  Cumulative Return: {cumulative_return*100:.2f}%")
print(f"  Win Rate: {win_rate*100:.1f}%")
print(f"  Avg Win: {avg_win:.2f}%")
print(f"  Avg Loss: {avg_loss:.2f}%")
print(f"  Best Trade: {df['Daily_Return'].max():.2f}%")
print(f"  Worst Trade: {df['Daily_Return'].min():.2f}%")
```

---

## Example 7: Finding the Best Month

```python
# find_best_month.py
import pandas as pd

# Load monthly comparison
df = pd.read_csv("Company_Analysis_Complete/06_Monthly_Analysis/monthly_comprehensive_statistics.csv")

# Sort by median return
df_sorted = df.sort_values('Median Daily Return (%)', ascending=False)

print("Top 3 Months by Median Return:")
print(df_sorted[['Month', 'Median Daily Return (%)', 'Win Rate (%)', 'Total Trading Days']].head(3))

# Best month
best_month = df_sorted.iloc[0]
print(f"\nBest month to invest: {best_month['Month']}")
print(f"  Median daily return: {best_month['Median Daily Return (%)']:.3f}%")
print(f"  Win rate: {best_month['Win Rate (%)']:.1f}%")
print(f"  Sample size: {int(best_month['Total Trading Days'])} days")
```

---

## Example 8: Checking Pattern Consistency

```python
# check_pattern_consistency.py
import pandas as pd

# Load April yearly statistics
df = pd.read_csv("Company_Analysis_Complete/01_April_Analysis/april_yearly_statistics.csv")

# Check consistency
print("April Pattern - Year by Year:")
print(df[['Year', 'Mean Daily Return (%)', 'Median Daily Return (%)', 'Win Rate (%)']].to_string(index=False))

# Calculate consistency metrics
positive_years = (df['Median Daily Return (%)'] > 0).sum()
total_years = len(df)
consistency = positive_years / total_years * 100

print(f"\nConsistency: {consistency:.1f}% ({positive_years}/{total_years} years were positive)")
```

---

## Example 9: Creating Custom Alerts

```python
# pattern_alerts.py
import pandas as pd
from datetime import datetime

# Load comparison table
df = pd.read_csv("Company_Analysis_Complete/07_Comparison_Tables/pattern_comparison_table.csv")

# Define "strong pattern" criteria
strong_patterns = df[
    (df['Median Daily Return (%)'] > 0.15) &  # Median > 0.15%
    (df['Win Rate (%)'] > 52) &                # Win rate > 52%
    (df['Total Trading Days'] > 200)           # Sample size > 200
]

print("🚨 STRONG PATTERNS DETECTED:")
for _, pattern in strong_patterns.iterrows():
    print(f"\n📊 {pattern['Pattern']}")
    print(f"   Median Return: {pattern['Median Daily Return (%)']:+.3f}%")
    print(f"   Win Rate: {pattern['Win Rate (%)']:.1f}%")
    print(f"   Sample: {int(pattern['Total Trading Days'])} days")
    
    # Check if pattern is active today
    today = datetime.now()
    if pattern['Pattern'] == 'Wednesday' and today.weekday() == 2:
        print(f"   ⚠️  PATTERN IS ACTIVE TODAY!")
    elif pattern['Pattern'] == 'First Monday':
        # Check if today is first Monday of month
        if today.weekday() == 0 and today.day <= 7:
            print(f"   ⚠️  PATTERN IS ACTIVE TODAY!")
```

---

## Example 10: Export to Excel with Formatting

```python
# export_to_excel.py
import pandas as pd

# Load comparison table
df = pd.read_csv("Company_Analysis_Complete/07_Comparison_Tables/pattern_comparison_table.csv")

# Create Excel writer
with pd.ExcelWriter("Pattern_Analysis_Formatted.xlsx", engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='All Patterns', index=False)
    
    # Get workbook and worksheet
    workbook = writer.book
    worksheet = writer.sheets['All Patterns']
    
    # Auto-adjust column widths
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        worksheet.column_dimensions[column_letter].width = adjusted_width
    
    # Apply conditional formatting for returns
    from openpyxl.styles import PatternFill
    
    green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    
    for row in range(2, len(df) + 2):  # Skip header
        median_cell = worksheet[f'C{row}']  # Median column
        if median_cell.value and float(median_cell.value) > 0:
            median_cell.fill = green_fill
        elif median_cell.value and float(median_cell.value) < 0:
            median_cell.fill = red_fill

print("✓ Excel file created: Pattern_Analysis_Formatted.xlsx")
```

---

## 💡 Pro Tips

### 1. Always check sample size
```python
# Patterns with < 100 observations are less reliable
df = pd.read_csv("pattern_comparison_table.csv")
reliable = df[df['Total Trading Days'] >= 100]
```

### 2. Look for small Mean-Median gaps
```python
# Small gap = reliable, symmetric pattern
df['Gap'] = abs(df['Mean Daily Return (%)'] - df['Median Daily Return (%)'])
reliable = df[df['Gap'] < 0.05]
```

### 3. Combine patterns
```python
# Wednesday + Month-End = higher confidence
wed_monthend_days = df[
    (df['Is_Wednesday'] == True) & 
    (df['Is_MonthEnd'] == True)
]['Daily_Return'].mean()
```

### 4. Use percentiles for risk management
```python
# Set stop-loss at 25th percentile
stats = pd.read_csv("pattern_overall_statistics.csv")
stop_loss = float(stats[stats['Metric'] == '25th Percentile (%)']['Value'])
print(f"Recommended stop-loss: {stop_loss:.2f}%")
```

---

## 🚀 Next Steps

After running these examples:

1. **Experiment** with your own stock data
2. **Compare** multiple companies to find best patterns
3. **Backtest** strategies before real trading
4. **Monitor** pattern consistency over time
5. **Adapt** the scripts for your specific needs

---

Happy analyzing! 📊
