# 🎯 ACE EQUITY COLUMNS - EXACT MAPPING TO YOUR PROJECT

## Overview
This document maps **exactly** which Ace Equity columns you need to select and how each is used in calculating your **14 fundamental indicators**.

---

## 📊 COMPLETE COLUMN SELECTION GUIDE

### ✅ **SECTION 1: COMPANY INFORMATION** (Current/Latest Only)

| Ace Equity Column | Your Variable Name | Used In | Required? |
|-------------------|-------------------|---------|-----------|
| **Company Name** | `company_name` | Reports, identification | ✅ REQUIRED |
| **NSE Symbol** or **BSE Code** | `symbol` | Reports, ticker | ✅ REQUIRED |
| **Sector** | `sector` | Sector analysis, reports | ✅ REQUIRED |
| **Industry** | `industry` | Industry classification | ✅ REQUIRED |
| **Current Market Price (CMP)** | `current_price` | **P/E Ratio**, **P/B Ratio** | ✅ REQUIRED |
| **Market Capitalization** | `market_cap` | Reports, screening | ✅ REQUIRED |
| **Number of Shares Outstanding** | `shares_outstanding` | EPS calculation (if needed) | Optional |

---

### ✅ **SECTION 2: BALANCE SHEET** (Years: FY 2024, 2023, 2022, 2021)

#### **What to select in Ace Equity:**
- Find **"Balance Sheet"** section
- For EACH field below, select **ALL 4 YEARS** (FY24, FY23, FY22, FY21)

| Ace Equity Column | Your Variable Name | Used In Indicators | Years Needed |
|-------------------|-------------------|-------------------|--------------|
| **Total Assets** | `total_assets` | **ROE**, **ROIC**, **Asset Turnover** | FY24, FY23, FY22, FY21 |
| **Current Assets** | `current_assets` | **Current Ratio** | FY24, FY23, FY22, FY21 |
| **Cash & Cash Equivalents** | `cash_and_equivalents` | **ROIC** (subtracted from invested capital) | FY24, FY23, FY22, FY21 |
| **Inventories** / **Stock** | `inventory` | **Inventory Turnover** | FY24, FY23, FY22, FY21 |
| **Current Liabilities** | `current_liabilities` | **Current Ratio** | FY24, FY23, FY22, FY21 |
| **Total Debt** / **Borrowings** | `total_debt` | **Debt-to-Equity**, **ROIC** | FY24, FY23, FY22, FY21 |
| **Shareholders' Equity** / **Net Worth** | `shareholders_equity` | **Debt-to-Equity**, **ROE**, **ROIC** | FY24, FY23, FY22, FY21 |

**Alternative Names in Ace Equity:**
- "Shareholders' Equity" = "Net Worth" = "Equity Capital + Reserves"
- "Total Debt" = "Borrowings" = "Short-term Debt + Long-term Debt"
- "Inventories" = "Stock" = "Stock-in-Trade"

---

### ✅ **SECTION 3: INCOME STATEMENT / P&L** (Years: FY 2024, 2023, 2022, 2021)

#### **What to select in Ace Equity:**
- Find **"Profit & Loss"** or **"Income Statement"** section
- Select **ALL 4 YEARS** for each field

| Ace Equity Column | Your Variable Name | Used In Indicators | Years Needed |
|-------------------|-------------------|-------------------|--------------|
| **Total Revenue** / **Net Sales** | `total_revenue` | **Revenue Growth**, **Net Profit Margin**, **Asset Turnover** | FY24, FY23, FY22, FY21 |
| **Cost of Goods Sold (COGS)** | `cost_of_revenue` | **Inventory Turnover** | FY24, FY23, FY22, FY21 |
| **Operating Profit** / **EBIT** / **PBIT** | `operating_income` | **Interest Coverage**, **ROIC** | FY24, FY23, FY22, FY21 |
| **Interest Expense** / **Finance Costs** | `interest_expense` | **Interest Coverage**, **ROIC** | FY24, FY23, FY22, FY21 |
| **Profit Before Tax (PBT)** | `pretax_income` | **ROIC** (tax rate calculation) | FY24, FY23, FY22, FY21 |
| **Tax Expense** / **Provision for Tax** | `income_tax_expense` | **ROIC** (tax rate calculation) | FY24, FY23, FY22, FY21 |
| **Net Profit** / **PAT** | `net_income` | **ROE**, **Net Profit Margin**, **EPS Growth** | FY24, FY23, FY22, FY21 |

**Alternative Names in Ace Equity:**
- "Total Revenue" = "Net Sales" = "Sales"
- "Operating Profit" = "EBIT" = "PBIT" = "Earnings Before Interest & Tax"
- "Net Profit" = "PAT" = "Profit After Tax" = "Net Income"
- "Interest Expense" = "Finance Costs" = "Financial Charges"

---

### ✅ **SECTION 4: CASH FLOW STATEMENT** (Years: FY 2024, 2023, 2022)

#### **What to select in Ace Equity:**
- Find **"Cash Flow"** section
- Select **3 YEARS** (FY24, FY23, FY22) - FY21 optional

| Ace Equity Column | Your Variable Name | Used In Indicators | Years Needed |
|-------------------|-------------------|-------------------|--------------|
| **Cash from Operating Activities (CFO)** | `operating_cash_flow` | **Free Cash Flow**, **FCF Growth** | FY24, FY23, FY22 |
| **Capital Expenditure (CapEx)** | `capital_expenditure` | **Free Cash Flow** | FY24, FY23, FY22 |
| **Free Cash Flow (FCF)** | `free_cash_flow` | **FCF Growth** | FY24, FY23, FY22 |

**Alternative Names:**
- "Cash from Operating Activities" = "CFO" = "Operating Cash Flow"
- "Capital Expenditure" = "CapEx" = "Purchase of Fixed Assets"

**Note:** If **Free Cash Flow** not available, it's calculated as: `FCF = CFO - CapEx`

---

### ✅ **SECTION 5: PER-SHARE DATA** (Years: FY 2024, 2023, 2022, 2021)

#### **What to select in Ace Equity:**
- Find **"Per Share Data"** or **"Ratios"** section
- Select **ALL 4 YEARS**

| Ace Equity Column | Your Variable Name | Used In Indicators | Years Needed |
|-------------------|-------------------|-------------------|--------------|
| **Earnings Per Share (EPS)** | `eps` | **P/E Ratio**, **PEG Ratio**, **EPS Growth** | FY24, FY23, FY22, FY21 |
| **Book Value Per Share (BVPS)** | `book_value_per_share` | **P/B Ratio** | FY24, FY23, FY22, FY21 |

**Alternative Names:**
- "EPS" = "Earnings Per Share" = "Basic EPS"
- "BVPS" = "Book Value Per Share" = "Net Worth Per Share"

---

## 🎯 **HOW EACH COLUMN IS USED IN YOUR 14 INDICATORS**

### **1. Debt-to-Equity Ratio (7% weight)**
```
Formula: Total Debt ÷ Shareholders' Equity

Ace Equity Columns Needed:
✅ Total Debt (FY 2024)
✅ Shareholders' Equity (FY 2024)
```

---

### **2. Current Ratio (7% weight)**
```
Formula: Current Assets ÷ Current Liabilities

Ace Equity Columns Needed:
✅ Current Assets (FY 2024)
✅ Current Liabilities (FY 2024)
```

---

### **3. Interest Coverage Ratio (6% weight)**
```
Formula: EBIT ÷ Interest Expense

Ace Equity Columns Needed:
✅ Operating Profit/EBIT (FY 2024)
✅ Interest Expense (FY 2024)
```

---

### **4. Return on Equity - ROE (8% weight)**
```
Formula: (Net Profit ÷ Average Equity) × 100

Ace Equity Columns Needed:
✅ Net Profit (FY 2024)
✅ Shareholders' Equity (FY 2024, FY 2023)
   → Average = (FY24 + FY23) ÷ 2
```

---

### **5. Return on Invested Capital - ROIC (9% weight)**
```
Formula: [NOPAT ÷ Invested Capital] × 100

Where:
- NOPAT = EBIT × (1 - Tax Rate)
- Tax Rate = Tax Expense ÷ PBT
- Invested Capital = Equity + Debt - Cash

Ace Equity Columns Needed:
✅ Operating Profit/EBIT (FY 2024)
✅ Tax Expense (FY 2024)
✅ PBT (FY 2024)
✅ Shareholders' Equity (FY 2024)
✅ Total Debt (FY 2024)
✅ Cash & Equivalents (FY 2024)
```

---

### **6. Net Profit Margin (8% weight)**
```
Formula: (Net Profit ÷ Total Revenue) × 100

Ace Equity Columns Needed:
✅ Net Profit (FY 2024)
✅ Total Revenue (FY 2024)
```

---

### **7. Revenue Growth - 3 Year Average (10% weight)**
```
Formula: Average of YoY growth rates for 3 years

Ace Equity Columns Needed:
✅ Total Revenue (FY 2024, FY 2023, FY 2022, FY 2021)

Calculation:
- FY24 vs FY23 growth
- FY23 vs FY22 growth  
- FY22 vs FY21 growth
- Average of 3 growth rates
```

---

### **8. EPS Growth - 3 Year Average (10% weight)**
```
Formula: Average of YoY EPS growth for 3 years

Ace Equity Columns Needed:
✅ EPS (FY 2024, FY 2023, FY 2022, FY 2021)

Calculation:
- FY24 vs FY23 growth
- FY23 vs FY22 growth
- FY22 vs FY21 growth
- Average of 3 growth rates
```

---

### **9. Free Cash Flow Growth (5% weight)**
```
Formula: [(FCF FY24 - FCF FY23) ÷ FCF FY23] × 100

Ace Equity Columns Needed:
✅ Free Cash Flow (FY 2024, FY 2023)

OR if FCF not available:
✅ Operating Cash Flow (FY 2024, FY 2023)
✅ CapEx (FY 2024, FY 2023)
   → FCF = CFO - CapEx
```

---

### **10. P/E Ratio (7% weight)**
```
Formula: Current Price ÷ EPS

Ace Equity Columns Needed:
✅ Current Market Price (Latest)
✅ EPS (FY 2024)
```

---

### **11. P/B Ratio (7% weight)**
```
Formula: Current Price ÷ Book Value Per Share

Ace Equity Columns Needed:
✅ Current Market Price (Latest)
✅ Book Value Per Share (FY 2024)
```

---

### **12. PEG Ratio (6% weight)**
```
Formula: P/E Ratio ÷ EPS Growth Rate

Ace Equity Columns Needed:
✅ Current Market Price (Latest)
✅ EPS (FY 2024, FY 2023, FY 2022, FY 2021)
   → Calculates P/E
   → Calculates EPS Growth
   → PEG = P/E ÷ Growth
```

---

### **13. Asset Turnover Ratio (5% weight)**
```
Formula: Revenue ÷ Average Total Assets

Ace Equity Columns Needed:
✅ Total Revenue (FY 2024)
✅ Total Assets (FY 2024, FY 2023)
   → Average = (FY24 + FY23) ÷ 2
```

---

### **14. Inventory Turnover (5% weight)**
```
Formula: COGS ÷ Average Inventory

Ace Equity Columns Needed:
✅ COGS (FY 2024)
✅ Inventory (FY 2024, FY 2023)
   → Average = (FY24 + FY23) ÷ 2
```

---

## 📋 **QUICK CHECKLIST FOR ACE EQUITY QUERY**

### **Period Selection:**
```
☑ Period Type: Annual
☑ From: FY 2021 (or FY 2015 for 10 years)
☑ To: FY 2024
☑ Data Type: Standalone (or Consolidated)
☑ Units: Rs. Crores
```

### **Columns to Select (Minimum Required):**

**Company Info (Latest only):**
- ☑ Company Name
- ☑ NSE Symbol / BSE Code  
- ☑ Sector
- ☑ Industry
- ☑ Current Market Price
- ☑ Market Cap

**Balance Sheet (4 years: FY24, 23, 22, 21):**
- ☑ Total Assets
- ☑ Current Assets
- ☑ Cash & Cash Equivalents
- ☑ Inventories
- ☑ Current Liabilities
- ☑ Total Debt
- ☑ Shareholders' Equity

**Income Statement (4 years: FY24, 23, 22, 21):**
- ☑ Total Revenue
- ☑ COGS
- ☑ Operating Profit (EBIT)
- ☑ Interest Expense
- ☑ PBT
- ☑ Tax Expense
- ☑ Net Profit

**Cash Flow (3 years: FY24, 23, 22):**
- ☑ Operating Cash Flow
- ☑ Capital Expenditure
- ☑ Free Cash Flow (or calculate)

**Per-Share (4 years: FY24, 23, 22, 21):**
- ☑ EPS
- ☑ Book Value Per Share

---

## 🎯 **TOTAL COLUMNS YOU'LL GET:**

With **4 years** of data:
- **Company Info:** 6 columns
- **Balance Sheet:** 7 fields × 4 years = 28 columns
- **Income Statement:** 7 fields × 4 years = 28 columns
- **Cash Flow:** 3 fields × 3 years = 9 columns
- **Per Share:** 2 fields × 4 years = 8 columns

**Total: ~79 columns** (manageable in Excel/CSV)

---

## ⚠️ **IMPORTANT NOTES:**

1. **Year Format:** Ensure columns are named like:
   - `Total Assets FY24`, `Total Assets FY23`, etc.
   - NOT: `Total Assets 2024`, `Total Assets 2023`

2. **Missing Data:** 
   - If a company doesn't have 4 years of data (newly listed), export what's available
   - Script will skip companies with insufficient data

3. **Units Consistency:**
   - ALL financial figures must be in **same unit** (Rs. Crores recommended)
   - Check export settings in Ace Equity

4. **Service Companies:**
   - If Inventory = 0 (IT, Consulting companies), that's normal
   - Inventory Turnover will be marked as "N/A"

5. **Negative Values:**
   - Loss-making companies will have negative Net Profit - that's okay
   - Enter as negative numbers in CSV

---

## 💡 **VERIFICATION STEPS:**

After export, verify your CSV has:
- ✅ All company names visible
- ✅ Current prices present (not 0)
- ✅ 4 years of Balance Sheet data
- ✅ 4 years of P&L data
- ✅ 3 years of Cash Flow data
- ✅ No #N/A or error values (replace with 0 if needed)
- ✅ Consistent number format (no commas, decimals okay)

---

**This mapping ensures you select EXACTLY the columns needed for your 14 indicators!**
