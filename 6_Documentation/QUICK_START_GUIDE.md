# Quick Start Guide - Eternal Ltd Analysis Tools

## 🚀 Two Ways to Analyze Stocks

### Method 1: Use Pre-Loaded Real Data (FASTEST)
```bash
python main.py
```
This uses verified Eternal Ltd data from Screener.in and generates:
- `eternal_analysis.png` - Visual dashboard
- `eternal_fundamental_analysis.xlsx` - Detailed Excel report

**Results:** Score of 77.8/100 (GOOD - BUY recommendation)

---

### Method 2: Enter Your Own Company Data (INTERACTIVE)
```bash
python interactive_data_collector.py
```

This interactive tool will guide you through entering:

#### Step 1: Company Information
- Stock symbol, exchange, BSE code
- Current price, market cap
- Shares outstanding

#### Step 2: Financial Statements (Last 4 Years)
For each year (FY 2024, 2023, 2022, 2021):

**Balance Sheet:**
- Total assets, current assets
- Cash & equivalents
- Inventory, receivables
- Total liabilities, debt
- Shareholders equity

**Income Statement:**
- Total revenue
- Cost of revenue, gross profit
- Operating expenses, EBIT
- Interest expense
- Net income

**Cash Flow:**
- Operating cash flow
- Capital expenditure
- Free cash flow

**Per-Share Data:**
- EPS (Earnings Per Share)
- Book Value Per Share
- Dividend Per Share

#### Step 3: Analyst Estimates (Optional)
- Expected EPS growth
- Target price
- Recommendations

### After Data Collection:
The tool automatically saves to `eternal_ltd_real_data.py` and you can run:
```bash
python main.py
```

---

## 📊 Where to Find Financial Data

### Best Sources for Indian Stocks:

1. **Screener.in** (RECOMMENDED)
   - URL: https://www.screener.in/company/[SYMBOL]/
   - Example: https://www.screener.in/company/ETERNAL/
   - Has all quarterly and annual data
   - Easy to read format
   - Free access

2. **MoneyControl**
   - URL: https://www.moneycontrol.com/
   - Comprehensive financial data
   - News and analysis

3. **BSE India**
   - URL: https://www.bseindia.com/
   - Official announcements
   - Annual reports PDFs

4. **Company Annual Reports**
   - Download from BSE/NSE
   - Most detailed information
   - Notes on accounting

### Data Collection Checklist:

Before starting interactive tool, have ready:
- [ ] 4 years of annual financial statements
- [ ] Balance sheet items
- [ ] Income statement items
- [ ] Cash flow statement
- [ ] Current market price
- [ ] Shares outstanding

**Time required:** 15-20 minutes for complete data entry

---

## 🎯 Understanding Your Results

### Score Interpretation:
- **90-100**: Excellent - Strong Buy
- **75-89**: Very Good - Buy
- **60-74**: Good - Buy/Hold
- **40-59**: Average - Hold/Caution
- **Below 40**: Poor - Avoid

### What Gets Analyzed:

#### Financial Health (20% weight):
1. Debt-to-Equity Ratio (7%)
2. Current Ratio (7%)
3. Interest Coverage (6%)

#### Profitability (25% weight):
4. ROE - Return on Equity (8%)
5. ROIC - Return on Invested Capital (9%)
6. Net Profit Margin (8%)

#### Growth (25% weight):
7. 3-Year Revenue Growth (10%)
8. 3-Year EPS Growth (10%)
9. Free Cash Flow Growth (5%)

#### Valuation (20% weight):
10. P/E Ratio (7%)
11. P/B Ratio (7%)
12. PEG Ratio (6%)

#### Efficiency (10% weight):
13. Asset Turnover (5%)
14. Inventory Turnover (5%)

**Total: 100%** across all 14 metrics

---

## 📈 Current Eternal Ltd Results

### Final Score: 77.8/100 (GOOD)

**Top Performers:**
- ✅ Debt-to-Equity: 99.7/100 (Almost debt-free!)
- ✅ Current Ratio: 100.0/100 (Excellent liquidity)
- ✅ EPS Growth: 100.0/100 (353% growth!)
- ✅ Net Margin: 99.9/100 (24.9% margin)

**Concerns:**
- ⚠️ P/E Ratio: 0.0/100 (126x - very expensive)
- ⚠️ ROE: 47.0/100 (6.75% - below average)
- ⚠️ Asset Turnover: 20.6/100 (Capital intensive)

**Recommendation:** BUY for growth investors

---

## 🛠️ Customization Options

### Want Different Weightages?

Edit `scoring_engine.py` and modify:
```python
self.category_weights = {
    'Financial Health': 0.20,  # Change to your preference
    'Profitability': 0.25,     # Change to your preference
    # ... etc
}
```

### Want Different Metrics?

Add new metrics to `metric_calculator.py`:
```python
def calculate_your_metric(self):
    # Your calculation logic
    return result
```

---

## 💾 Saving Your Analysis

All results auto-save to:
- `eternal_analysis.png` - Visual dashboard
- `eternal_fundamental_analysis.xlsx` - Excel with 4 sheets
  - Summary
  - Detailed Metrics
  - Scores & Ratings
  - Category Analysis

Keep these for:
- Quarterly comparison
- Portfolio tracking
- Investment decisions

---

## 🔄 Regular Updates

### Recommended Schedule:

**Quarterly:**
- After each earnings release
- Update key metrics
- Re-run analysis
- Compare trends

**Annually:**
- After annual report release
- Full data refresh
- Comprehensive review

**As Needed:**
- Major news/events
- Price movements >10%
- Sector changes

---

## ❓ Troubleshooting

### "No data found"
- Check internet connection
- Verify stock symbol is correct
- Try manual data entry

### "Calculation errors"
- Ensure all required fields filled
- Check data for negative values where inappropriate
- Verify units (Crores, not Lakhs)

### "Scores seem wrong"
- Review normalization logic in `scoring_engine.py`
- Check if metric is inverse (lower is better)
- Verify weightages sum to 100%

---

## 📞 Support

For questions about:
- **Data entry:** Review `DATA_REQUIREMENTS.md`
- **Scoring logic:** Review `SCORING_LOGIC_EXPLAINED.md`
- **General usage:** Review `USAGE_GUIDE.md`
- **Roadmap:** Review `ROADMAP.md`

---

**Ready to analyze another stock?**
Run `python interactive_data_collector.py` and follow the prompts!

---

*Last Updated: November 12, 2025*  
*Eternal Ltd Analysis: 77.8/100 (GOOD - BUY)*
