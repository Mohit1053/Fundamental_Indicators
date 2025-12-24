# 📊 Complete Guide: Analyzing Full Market with Ace Equity

## Overview
This guide helps you analyze **entire market**, **NIFTY 50**, **NIFTY 500**, or any **custom universe** using Ace Equity data.

---

## 🎯 Step 1: Choose Your Market Universe

### Option A: Pre-defined Indices
- **NIFTY 50** - Top 50 companies (Recommended to start)
- **NIFTY 100** - Top 100 companies
- **NIFTY 500** - Broad market (500 companies)
- **BSE 500** - Alternative broad market
- **Sectoral Indices** - NIFTY Bank, NIFTY IT, NIFTY Pharma, etc.

### Option B: Custom Screening
- **Market Cap based** - Large Cap, Mid Cap, Small Cap
- **Sector based** - All companies in specific sectors
- **Custom criteria** - Your own screening filters

---

## 🔧 Step 2: Export Data from Ace Equity

### Method 1: Screener + Bulk Export (RECOMMENDED)

#### A. Create a Screener
1. **Login to Ace Equity**
2. Go to **"Screener"** or **"Search"** module
3. Click **"Create New Screen"**
4. Add filters:
   ```
   Market Cap: > 1000 Cr (or your preference)
   Listing Status: Listed
   Exchange: NSE/BSE
   Financials: Latest data available
   ```

#### B. Select Companies
1. Apply screener
2. **Select "All"** or specific companies
3. Should see list of 50/100/500 companies

#### C. Export Financials
1. Click **"Export"** or **"Download"** button
2. Choose **"Financial Data Export"**
3. Select fields (see template below)
4. Choose **"Annual"** frequency
5. Select **last 4 years** (FY 2024, 2023, 2022, 2021)
6. Export format: **CSV** or **Excel**

---

### Method 2: Index Constituents Export

#### For NIFTY 50/100/500:
1. Go to **"Indices"** section
2. Select **"NIFTY 50"** (or desired index)
3. Click **"View Constituents"**
4. Select **"All Companies"**
5. Click **"Export Financials"**
6. Configure export (see fields below)
7. Download CSV/Excel

---

### Method 3: Manual Sector-wise Export

1. Go to **"Sector Analysis"**
2. Select sector (IT, Banking, Pharma, etc.)
3. View all companies in sector
4. Export financials for entire sector
5. Repeat for each sector
6. Combine all sector files

---

## 📋 Step 3: Configure Export Fields

### Required Fields for Export

Copy this field list when configuring Ace Equity export:

#### **Company Information**
- Company Name
- NSE Symbol / BSE Code
- Sector
- Industry
- Current Market Price (CMP)
- Market Capitalization

#### **Balance Sheet (4 years: FY 2024, 2023, 2022, 2021)**
- Total Assets
- Current Assets
- Cash & Cash Equivalents
- Inventories
- Current Liabilities
- Total Debt / Borrowings
- Shareholders' Equity / Net Worth

#### **Income Statement (4 years: FY 2024, 2023, 2022, 2021)**
- Total Revenue / Net Sales
- Cost of Goods Sold (COGS) / Cost of Revenue
- Operating Profit / EBIT
- Interest Expense / Finance Costs
- Profit Before Tax (PBT)
- Tax Expense
- Net Profit / PAT

#### **Cash Flow (3 years: FY 2024, 2023, 2022)**
- Cash from Operating Activities
- Capital Expenditure (CapEx)
- Free Cash Flow

#### **Per-Share Data (4 years)**
- EPS (Earnings Per Share)
- Book Value Per Share (BVPS)

---

## 📊 Step 4: Format Your Export File

### Excel/CSV Column Headers

Use these **exact column names** (or update the script accordingly):

```
Symbol
Company Name
Sector
Industry
Current Price
Market Cap

Total Assets FY24
Current Assets FY24
Cash FY24
Inventory FY24
Current Liabilities FY24
Total Debt FY24
Equity FY24

Total Assets FY23
Equity FY23
Total Debt FY23

Total Assets FY22
Equity FY22

Total Assets FY21
Equity FY21

Revenue FY24
COGS FY24
EBIT FY24
Interest FY24
PBT FY24
Tax FY24
Net Profit FY24

Revenue FY23
EBIT FY23
Net Profit FY23

Revenue FY22
Net Profit FY22

Revenue FY21
Net Profit FY21

OCF FY24
CapEx FY24
FCF FY24
FCF FY23

EPS FY24
BVPS FY24
EPS FY23
EPS FY22
EPS FY21
```

### Tips:
- **Remove commas** from numbers (5,000 → 5000)
- **Consistent units** - Use Crores (Cr) for all values
- **Handle missing data** - Enter 0 or leave blank
- **No special characters** in company names

---

## 🚀 Step 5: Run Bulk Analysis

### Option A: Using CSV File

```python
# In Python terminal or script
from bulk_market_analyzer import BulkMarketAnalyzer, load_companies_from_csv

# Load companies from your Ace Equity export
companies = load_companies_from_csv('your_ace_equity_export.csv')

# Create analyzer
analyzer = BulkMarketAnalyzer(output_dir='market_analysis')

# Analyze all companies
results_df = analyzer.analyze_market(companies)

# Save results
analyzer.save_results(results_df, prefix='nifty50')

# View top 10
print(results_df.head(10))
```

### Option B: Using Python Script

```powershell
cd C:\Users\mohit1\Desktop\Fundamental_Indicators
python bulk_market_analyzer.py
```

---

## 📈 Step 6: Analyze Results

### Output Files Created:

1. **market_summary_YYYYMMDD_HHMMSS.csv**
   - Ranked list of all companies
   - Scores, ratings, sector info
   - Easy to sort and filter

2. **market_detailed_YYYYMMDD_HHMMSS.json**
   - Complete analysis details
   - All metrics and normalized scores
   - For advanced analysis

3. **market_analysis_YYYYMMDD_HHMMSS.xlsx**
   - Multi-sheet Excel report
   - Sheets: Market Summary, Top 20, Sector Analysis, Rating Distribution

---

## 🎯 Common Use Cases

### Use Case 1: Analyze NIFTY 50
```python
# Export NIFTY 50 from Ace Equity → nifty50_data.csv
companies = load_companies_from_csv('nifty50_data.csv')
analyzer = BulkMarketAnalyzer()
results = analyzer.analyze_market(companies)
analyzer.save_results(results, prefix='nifty50')

# Get top 10 stocks
top10 = results.head(10)
print(top10[['Rank', 'Company', 'Final Score', 'Rating']])
```

### Use Case 2: Sector-wise Analysis
```python
# Export IT sector → it_sector.csv
companies = load_companies_from_csv('it_sector.csv')
analyzer = BulkMarketAnalyzer()
results = analyzer.analyze_market(companies)
analyzer.save_results(results, prefix='it_sector')

# Find sector leaders
leaders = analyzer.get_sector_leaders()
print(leaders)
```

### Use Case 3: Large Cap Screening
```python
# Export Large Cap (>20,000 Cr) → largecap.csv
companies = load_companies_from_csv('largecap.csv')
analyzer = BulkMarketAnalyzer()
results = analyzer.analyze_market(companies)

# Filter by rating
excellent = results[results['Rating'] == 'Excellent']
print(f"Found {len(excellent)} excellent large cap stocks")
```

### Use Case 4: Complete Market (NIFTY 500)
```python
# Export NIFTY 500 → nifty500_data.csv
companies = load_companies_from_csv('nifty500_data.csv')
analyzer = BulkMarketAnalyzer()

# This will take 10-15 minutes for 500 companies
results = analyzer.analyze_market(companies)
analyzer.save_results(results, prefix='nifty500')

# Analyze by sector
sector_summary = results.groupby('Sector')['Final Score'].mean().sort_values(ascending=False)
print(sector_summary)
```

---

## ⚡ Performance Tips

### For Large Datasets (500+ companies):

1. **Split into batches**
   ```python
   # Process in chunks of 100
   for i in range(0, len(companies), 100):
       batch = companies[i:i+100]
       analyzer = BulkMarketAnalyzer(output_dir=f'batch_{i}')
       analyzer.analyze_market(batch)
   ```

2. **Use Excel filtering** instead of CSV for >100 companies

3. **Focus on specific metrics** to speed up analysis

4. **Filter before analysis**
   ```python
   # Only analyze companies with Market Cap > 10,000 Cr
   filtered = [c for c in companies if c['company_info']['market_cap'] > 10000]
   ```

---

## 🛠️ Troubleshooting

### Issue 1: Missing columns in CSV
**Solution:** Update column mapping in `load_companies_from_csv()` function

### Issue 2: Division by zero errors
**Solution:** Check for negative equity, zero assets - exclude these companies

### Issue 3: Ace Equity export format different
**Solution:** Use the provided `ace_equity_template.csv` as reference

### Issue 4: Too many companies to process
**Solution:** Export in batches (50-100 companies each)

---

## 📝 Ace Equity Export Checklist

Before exporting, verify:

- [ ] Selected correct index/universe
- [ ] All companies selected
- [ ] Annual frequency chosen (not quarterly)
- [ ] Last 4 years selected (FY 2024, 2023, 2022, 2021)
- [ ] All required fields included (see field list above)
- [ ] Export format: CSV or Excel
- [ ] Standalone financials (not consolidated, unless preferred)
- [ ] Currency: INR (Crores)
- [ ] Current market prices included

---

## 🎓 Advanced: Custom Data Pipeline

For regular updates, create automated pipeline:

```python
# 1. Export from Ace Equity monthly
# 2. Place in 'data' folder with date: nifty50_20250114.csv
# 3. Run analysis:

import glob
from datetime import datetime

latest_file = max(glob.glob('data/nifty50_*.csv'))
companies = load_companies_from_csv(latest_file)
analyzer = BulkMarketAnalyzer()
results = analyzer.analyze_market(companies)
analyzer.save_results(results, prefix=f'nifty50_{datetime.now().strftime("%Y%m")}')
```

---

## 📞 Next Steps

1. **Export NIFTY 50** from Ace Equity using this guide
2. **Run first analysis** on 50 companies
3. **Review results** - top 10, sector leaders
4. **Expand to NIFTY 100/500** based on needs
5. **Schedule monthly updates** for portfolio tracking

---

## 💡 Pro Tips

- Start with **NIFTY 50** to test the system
- **Verify 5-10 companies manually** before trusting bulk results
- **Update data monthly** for accurate rankings
- **Compare across quarters** to track changes
- **Use sector filters** for focused analysis
- **Combine with technical indicators** for better decisions

---

**Need Help?** Check `bulk_market_analyzer.py` for code examples and `ace_equity_template.csv` for exact format.
