# Interactive Data Collector - Step-by-Step Demo

## 🎯 Purpose
This guide shows you EXACTLY how to use the interactive data collection tool to analyze ANY Indian stock.

---

## 📋 Before You Start

### What You Need:
1. **Financial data** for your target company (last 4 years)
2. **15-20 minutes** of uninterrupted time
3. **Data sources** open in browser:
   - Screener.in (recommended)
   - MoneyControl
   - Company's annual report PDF

### Example: We'll walk through Eternal Ltd

---

## 🚀 Starting the Tool

### Command:
```bash
python interactive_data_collector.py
```

### What You'll See:
```
🚀 Starting Interactive Data Collection...

NOTE: Have your financial data ready from:
  - Annual Report PDF
  - Screener.in page
  - MoneyControl page

Press Ctrl+C anytime to cancel.

======================================================================
INTERACTIVE FINANCIAL DATA COLLECTION FOR ETERNAL LTD
======================================================================

This tool will guide you through entering all required financial data.
Press Enter to skip optional fields (will default to 0).

Data should be from:
  - Annual Reports
  - Screener.in
  - MoneyControl
  - BSE/NSE Filings
======================================================================
```

---

## 📝 Step-by-Step Data Entry

### STEP 1: Company Information

#### What You'll Be Asked:
```
======================================================================
STEP 1: COMPANY INFORMATION
======================================================================

Stock Symbol (e.g., ETERNAL): 
```

#### Your Inputs:
```
Stock Symbol (e.g., ETERNAL): ETERNAL
Exchange (NSE/BSE): NSE
BSE Code (e.g., 543320): 543320
Company Name: Eternal Ltd
Sector: Consumer Services
Industry: E-Commerce

📊 Current Market Data:
Current Stock Price (Rs.): 310
Market Cap (Rs. Crores): 29936
Shares Outstanding (Crores): 96.57
```

#### Where to Find:
- **Screener.in:** Top of page shows symbol, price, market cap
- **Share count:** Market Cap ÷ Current Price

---

### STEP 2: Financial Statements

#### FY 2024 (Most Recent Year)

#### 2.1 Balance Sheet Data for FY 2024:

```
====================================================================
COLLECTING DATA FOR FY 2024 (Most Recent)
====================================================================

📋 Balance Sheet Data for FY 2024:

  Assets:
    Total Assets (Cr): 37853
    Current Assets (Cr): 36293
    Cash & Cash Equivalents (Cr): 27259
    Accounts Receivable (Cr): 380
    Inventory (Cr): 0

  Liabilities:
    Current Liabilities (Cr): 1785
    Accounts Payable (Cr): 600
    Short-term Debt (Cr): 50
    Long-term Debt (Cr): 198
    Total Debt (Auto-calculated): 248.00 Cr
    Total Liabilities (Cr): 2033

  Equity:
    Shareholders Equity (Cr): 35820
    Common Stock (Cr): 910
    Retained Earnings (Cr): 34910
```

#### Where to Find on Screener.in:
1. Scroll to "Balance Sheet" section
2. Look at rightmost column (latest year)
3. Copy values:
   - Total Assets
   - Current Assets (if available)
   - Cash = Investments row
   - Receivables = estimated from debtor days
   - Inventory (usually 0 for e-commerce)
   - Total Liabilities
   - Borrowings = Debt
   - Equity Capital + Reserves = Shareholders Equity

---

#### 2.2 Income Statement for FY 2024:

```
💰 Income Statement Data for FY 2024:
  Total Revenue (Cr): 9481
  Cost of Revenue/COGS (Cr): 8184
  Gross Profit (Cr): 1297
  Operating Expenses (Cr): 8184
  Operating Income/EBIT (Cr): 1297
  Interest Expense (Cr): 20
  Other Income (Cr): 1545
  Pre-tax Income (Cr): 2675
  Income Tax Expense (Cr): 313
  Net Income (Cr): 2362
```

#### Where to Find on Screener.in:
1. Scroll to "Profit & Loss" section
2. Rightmost column (latest year):
   - Sales = Total Revenue
   - Expenses = Cost of Revenue
   - Operating Profit = EBIT
   - Interest row = Interest Expense
   - Other Income row
   - Profit before tax
   - Net Profit

---

#### 2.3 Cash Flow for FY 2024:

```
💵 Cash Flow Data for FY 2024:
  Operating Cash Flow (Cr): 1614
  Capital Expenditure (Cr, enter positive): 250
  Free Cash Flow (Auto-calculated): 1364.00 Cr
  Financing Activities (Cr): 8388
  Investing Activities (Cr): -9752
```

#### Where to Find on Screener.in:
1. Scroll to "Cash Flows" section
2. Latest year column:
   - Cash from Operating Activity
   - CapEx (from notes or estimate from depreciation)
   - Financing Activities
   - Investing Activities

**Note:** Tool auto-calculates FCF = Operating CF - CapEx

---

#### 2.4 Per-Share Data for FY 2024:

```
📈 Per-Share Data for FY 2024:
  EPS (Rs.): 2.45
  Book Value Per Share (Rs.): 37.1
  Dividend Per Share (Rs.): 0
```

#### Where to Find on Screener.in:
1. "Profit & Loss" section has EPS row
2. Top section shows "Book Value"
3. Dividend Payout % tells you if dividend paid

---

### STEP 3: Historical Data (FY 2023, 2022, 2021)

#### The tool will repeat for:
- **FY 2023** - Full data (same questions as FY 2024)
- **FY 2022** - Minimal data (key items only)
- **FY 2021** - Minimal data (key items only)

#### For FY 2022 and FY 2021 (Minimal):
```
📋 Minimal data needed for FY 2021:
  Total Assets (Cr): 21927
  Shareholders Equity (Cr): 20806
  Total Debt (Cr): 157
  Total Revenue (Cr): 4707
  Cost of Revenue (Cr): 5234
  Operating Income (Cr): -527
  Interest Expense (Cr): 16
  Net Income (Cr): 117
  EPS (Rs.): 0.14
  Book Value Per Share (Rs.): 24.9
```

---

### STEP 4: Analyst Estimates (Optional)

```
======================================================================
STEP 3: ANALYST ESTIMATES (Optional)
======================================================================

Expected EPS Growth (5Y %) [Optional]: 23.2
Analyst Target Price (Rs.) [Optional]: 368
Number of Analysts Covering [Optional]: 15
Recommendation (Buy/Hold/Sell) [Optional]: Buy
```

#### Where to Find:
- MoneyControl "Research" section
- Screener.in growth rates
- Company presentations

**You can skip this by pressing Enter**

---

## ✅ Completion

### What Happens Next:

```
======================================================================
✓ DATA COLLECTION COMPLETE!
======================================================================

Data saved to: eternal_ltd_real_data.py

You can now run the analysis using this data:
  python main.py

✓ Success! Data collection completed.
```

### Generated File:

The tool creates `eternal_ltd_real_data.py` with structure:
```python
ETERNAL_DATA = {
    'company_info': {
        'symbol': 'ETERNAL',
        'ticker': 'ETERNAL.NS',
        # ... all company info
    },
    'balance_sheet': {
        'fy_2024': { ... },
        'fy_2023': { ... },
        'fy_2022': { ... },
        'fy_2021': { ... },
    },
    'income_statement': { ... },
    'cash_flow': { ... },
    'per_share_data': { ... },
    'estimates': { ... },
}
```

---

## 🎯 Tips for Efficient Data Entry

### 1. Prepare Data Beforehand
- Open Screener.in in one tab
- Have Excel/notepad open
- Copy all numbers first, then enter

### 2. Use Shortcuts
- Press **Enter** to skip optional fields
- Press **Ctrl+C** to cancel anytime
- Copy-paste numbers (don't retype)

### 3. Data Validation
- Tool validates as you go
- Won't accept negative values where inappropriate
- Auto-calculates derived fields (Total Debt, FCF)

### 4. Common Mistakes to Avoid
- ❌ Mixing Lakhs and Crores (use Crores only)
- ❌ Using consolidated instead of standalone
- ❌ Copying wrong year column
- ❌ Forgetting to convert percentages (enter as decimal)

---

## 📊 Example: Full FY 2024 Entry

### Balance Sheet - Complete Example:

**From Screener.in Balance Sheet section:**

| Item | Screener Value | Your Entry |
|------|---------------|------------|
| Total Assets | 37,853 | 37853 |
| Investments | 27,259 | 27259 (cash) |
| Other Assets | 9,034 | 9034 |
| Borrowings | 248 | 50 (short) + 198 (long) |
| Other Liabilities | 1,785 | 1785 |
| Equity Capital | 910 | 910 |
| Reserves | 34,910 | 34910 |

### Income Statement - Complete Example:

| Item | Screener Value | Your Entry |
|------|---------------|------------|
| Sales | 9,481 | 9481 |
| Expenses | 8,184 | 8184 |
| Operating Profit | 1,297 | 1297 |
| Other Income | 1,545 | 1545 |
| Interest | 20 | 20 |
| Net Profit | 2,362 | 2362 |

---

## 🔄 What to Do After Data Entry

### 1. Verify the Saved File
```bash
python eternal_ltd_real_data.py
```

Should print summary of entered data.

### 2. Run Complete Analysis
```bash
python main.py
```

Generates:
- `eternal_analysis.png` - Visual dashboard
- `eternal_fundamental_analysis.xlsx` - Excel report
- Terminal output with scores

### 3. Review Results
- Check if scores make sense
- Verify metrics look correct
- Compare with known ratios (P/E, ROE, etc.)

---

## 🐛 Troubleshooting

### "Invalid input. Please enter a number."
→ You entered text instead of number  
→ Use numbers only (no commas, no currency symbols)

### "Value cannot be negative."
→ Field doesn't accept negative (like total assets)  
→ Check if you entered the right field

### "Value cannot be zero."
→ Critical field needs a value  
→ Cannot skip (e.g., total assets, revenue)

### Calculation seems wrong?
→ Review input data  
→ Check units (Crores, not Lakhs)  
→ Verify you used standalone, not consolidated

---

## 📚 Data Fields Reference

### Required vs. Optional

#### Always Required:
- Company name, ticker, price
- Total assets (all years)
- Shareholders equity (all years)
- Revenue (all years)
- Net income (all years)
- EPS (all years)

#### Optional (can skip):
- Inventory (for service companies)
- Accounts receivable/payable
- Analyst estimates
- Dividend per share (if no dividend)

### Field Definitions:

**Total Assets:** Everything company owns  
**Current Assets:** Cash, receivables, inventory (< 1 year)  
**Total Liabilities:** Everything company owes  
**Current Liabilities:** Due within 1 year  
**EBIT:** Earnings Before Interest & Tax  
**CapEx:** Capital Expenditure (investments in fixed assets)  
**FCF:** Free Cash Flow = Operating CF - CapEx  

---

## ⏱️ Time Estimates

### By Experience Level:

**First Time:**
- Data gathering: 10 minutes
- Data entry: 15 minutes
- Review & verify: 5 minutes
- **Total: 30 minutes**

**Second Time:**
- Data gathering: 5 minutes
- Data entry: 10 minutes
- Review & verify: 3 minutes
- **Total: 18 minutes**

**Expert:**
- With data ready: 10 minutes
- **Total: 10-12 minutes**

---

## 🎓 Learning Resources

### Understanding Financial Statements:

**Balance Sheet:**
- Assets = Liabilities + Equity
- Shows financial position at a point in time

**Income Statement:**
- Revenue - Expenses = Profit
- Shows performance over a period

**Cash Flow:**
- Actual cash in/out
- Operating, Investing, Financing activities

### Key Ratios to Know:

1. **Debt/Equity:** Total Debt ÷ Shareholders Equity
2. **Current Ratio:** Current Assets ÷ Current Liabilities
3. **ROE:** Net Income ÷ Shareholders Equity
4. **P/E:** Stock Price ÷ EPS
5. **P/B:** Stock Price ÷ Book Value Per Share

---

## 🎉 Success Checklist

After completing data entry, verify:

- [ ] All 4 years of data entered
- [ ] Numbers match source (Screener.in)
- [ ] Units are consistent (all in Crores)
- [ ] File saved successfully
- [ ] Test run executed (`python main.py`)
- [ ] Reports generated (PNG + XLSX)
- [ ] Scores look reasonable
- [ ] Metrics match known values (check P/E, ROE)

---

## 💡 Pro Tips

### 1. Keyboard Shortcuts
```
Enter: Accept default (0 or skip)
Ctrl+C: Cancel immediately
Ctrl+V: Paste copied number
```

### 2. Data Entry Strategy
```
Phase 1: Gather all data (10 min)
Phase 2: Enter in one go (10 min)
Phase 3: Verify & analyze (5 min)
```

### 3. Quality Control
```
After entry:
1. Verify P/E matches Screener.in
2. Check ROE is reasonable
3. Ensure debt numbers make sense
4. Cross-check revenue growth %
```

---

## 📞 Quick Reference Card

### Essential Screener.in Sections:

| Section | What to Copy |
|---------|-------------|
| Top Banner | Price, Market Cap, P/E, ROE |
| Balance Sheet | Assets, Liabilities, Equity, Debt |
| Profit & Loss | Sales, Expenses, Profit, EPS |
| Cash Flows | Operating CF, Investing, Financing |
| Ratios | Debtor Days, ROCE (for validation) |

### Data Entry Flow:

```
1. Company Info (9 fields) → 2 min
2. FY 2024 Full (40 fields) → 8 min
3. FY 2023 Full (40 fields) → 8 min
4. FY 2022 Minimal (10 fields) → 2 min
5. FY 2021 Minimal (10 fields) → 2 min
6. Estimates (4 fields) → 1 min
────────────────────────────────────
Total: ~23 minutes first time
```

---

## 🚀 You're Ready!

Now you know:
- ✅ How to start the tool
- ✅ What data you need
- ✅ Where to find it
- ✅ How to enter it
- ✅ What happens next
- ✅ How to verify
- ✅ How to troubleshoot

**Go ahead and analyze your first stock!**

---

**Need help?** Refer to:
- `QUICK_START_GUIDE.md` - Quick reference
- `DATA_REQUIREMENTS.md` - Detailed data specs
- `PROJECT_SUMMARY.md` - Complete overview

---

*Happy Analyzing! 📊*
