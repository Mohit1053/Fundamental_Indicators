# Data Requirements & Mapping

## Complete Data Mapping for All 14 Metrics

### 1. Financial Health Category (20%)

#### Metric 1.1: Debt-to-Equity Ratio (7%)
**Formula**: Total Debt / Total Shareholder Equity

**Data Required:**
- **Total Debt** (Balance Sheet)
  - Short-term Debt
  - Long-term Debt
  - OR: Total Liabilities (alternative)
- **Total Shareholder Equity** (Balance Sheet)
  - Common Stock
  - Retained Earnings
  - Additional Paid-in Capital

**Yahoo Finance Mapping:**
```python
balance_sheet = stock.balance_sheet
total_debt = balance_sheet.loc['Total Debt']  # or calculate from short + long term
shareholder_equity = balance_sheet.loc['Stockholders Equity']
debt_to_equity = total_debt / shareholder_equity
```

---

#### Metric 1.2: Current Ratio (7%)
**Formula**: Current Assets / Current Liabilities

**Data Required:**
- **Current Assets** (Balance Sheet)
  - Cash and Cash Equivalents
  - Short-term Investments
  - Accounts Receivable
  - Inventory
  - Other Current Assets
- **Current Liabilities** (Balance Sheet)
  - Accounts Payable
  - Short-term Debt
  - Other Current Liabilities

**Yahoo Finance Mapping:**
```python
balance_sheet = stock.balance_sheet
current_assets = balance_sheet.loc['Total Current Assets']
current_liabilities = balance_sheet.loc['Total Current Liabilities']
current_ratio = current_assets / current_liabilities
```

---

#### Metric 1.3: Interest Coverage Ratio (6%)
**Formula**: EBIT / Interest Expense

**Data Required:**
- **EBIT (Earnings Before Interest and Taxes)** (Income Statement)
  - Operating Income
  - OR: Net Income + Interest Expense + Tax Expense
- **Interest Expense** (Income Statement)

**Yahoo Finance Mapping:**
```python
income_stmt = stock.financials
ebit = income_stmt.loc['Operating Income']  # or 'EBIT'
interest_expense = income_stmt.loc['Interest Expense']
interest_coverage = ebit / interest_expense
```

---

### 2. Profitability Category (25%)

#### Metric 2.1: Return on Equity (ROE) (8%)
**Formula**: (Net Income / Shareholder Equity) × 100

**Data Required:**
- **Net Income** (Income Statement) - Most recent annual
- **Average Shareholder Equity** (Balance Sheet) - Current and previous year

**Yahoo Finance Mapping:**
```python
income_stmt = stock.financials
balance_sheet = stock.balance_sheet
net_income = income_stmt.loc['Net Income'].iloc[0]  # Most recent
equity_current = balance_sheet.iloc[:, 0].loc['Stockholders Equity']
equity_previous = balance_sheet.iloc[:, 1].loc['Stockholders Equity']
avg_equity = (equity_current + equity_previous) / 2
roe = (net_income / avg_equity) * 100
```

---

#### Metric 2.2: Return on Invested Capital (ROIC) (9%)
**Formula**: (NOPAT / Invested Capital) × 100

Where:
- NOPAT = Net Operating Profit After Tax = EBIT × (1 - Tax Rate)
- Invested Capital = Total Equity + Total Debt - Cash

**Data Required:**
- **EBIT** (Income Statement)
- **Tax Rate** (Income Statement: Income Tax Expense / Pre-tax Income)
- **Total Equity** (Balance Sheet)
- **Total Debt** (Balance Sheet)
- **Cash and Equivalents** (Balance Sheet)

**Yahoo Finance Mapping:**
```python
income_stmt = stock.financials
balance_sheet = stock.balance_sheet

# Calculate NOPAT
ebit = income_stmt.loc['Operating Income'].iloc[0]
tax_expense = income_stmt.loc['Income Tax Expense'].iloc[0]
pretax_income = income_stmt.loc['Pretax Income'].iloc[0]
tax_rate = tax_expense / pretax_income
nopat = ebit * (1 - tax_rate)

# Calculate Invested Capital
total_equity = balance_sheet.loc['Stockholders Equity'].iloc[0]
total_debt = balance_sheet.loc['Total Debt'].iloc[0]
cash = balance_sheet.loc['Cash And Cash Equivalents'].iloc[0]
invested_capital = total_equity + total_debt - cash

roic = (nopat / invested_capital) * 100
```

---

#### Metric 2.3: Net Profit Margin (8%)
**Formula**: (Net Income / Total Revenue) × 100

**Data Required:**
- **Net Income** (Income Statement)
- **Total Revenue** (Income Statement)

**Yahoo Finance Mapping:**
```python
income_stmt = stock.financials
net_income = income_stmt.loc['Net Income'].iloc[0]
total_revenue = income_stmt.loc['Total Revenue'].iloc[0]
net_profit_margin = (net_income / total_revenue) * 100
```

---

### 3. Growth Category (25%)

#### Metric 3.1: Revenue Growth - 3-Year Average (10%)
**Formula**: Average Annual Growth Rate over 3 years

**Calculation**: 
```
Year 1 Growth = (Revenue_Year1 - Revenue_Year0) / Revenue_Year0
Year 2 Growth = (Revenue_Year2 - Revenue_Year1) / Revenue_Year1
Year 3 Growth = (Revenue_Year3 - Revenue_Year2) / Revenue_Year2
Average = (Year 1 + Year 2 + Year 3) / 3 × 100
```

**Data Required:**
- **Total Revenue** (Income Statement) - Last 4 years

**Yahoo Finance Mapping:**
```python
income_stmt = stock.financials
revenues = income_stmt.loc['Total Revenue'].iloc[0:4]  # Last 4 years

# Calculate year-over-year growth
growth_rates = []
for i in range(len(revenues) - 1):
    growth = (revenues.iloc[i] - revenues.iloc[i+1]) / revenues.iloc[i+1]
    growth_rates.append(growth * 100)

avg_revenue_growth = sum(growth_rates) / len(growth_rates)
```

---

#### Metric 3.2: EPS Growth - 3-Year Average (10%)
**Formula**: Average Annual EPS Growth Rate over 3 years

**Data Required:**
- **Earnings Per Share (Diluted)** (Income Statement or Key Stats) - Last 4 years

**Yahoo Finance Mapping:**
```python
# Method 1: From financials
income_stmt = stock.financials
net_income = income_stmt.loc['Net Income'].iloc[0:4]
shares_outstanding = stock.info['sharesOutstanding']  # May need historical
eps = net_income / shares_outstanding

# Method 2: Direct from earnings history
earnings = stock.earnings_history
eps_values = earnings['epsActual'].tail(4)

# Calculate growth (same logic as revenue)
growth_rates = []
for i in range(len(eps_values) - 1):
    growth = (eps_values.iloc[i] - eps_values.iloc[i+1]) / eps_values.iloc[i+1]
    growth_rates.append(growth * 100)

avg_eps_growth = sum(growth_rates) / len(growth_rates)
```

---

#### Metric 3.3: Free Cash Flow Growth (5%)
**Formula**: (Current FCF - Previous FCF) / Previous FCF × 100

Where: FCF = Operating Cash Flow - Capital Expenditures

**Data Required:**
- **Operating Cash Flow** (Cash Flow Statement) - Last 2 years
- **Capital Expenditures (CapEx)** (Cash Flow Statement) - Last 2 years

**Yahoo Finance Mapping:**
```python
cash_flow = stock.cashflow
operating_cf = cash_flow.loc['Operating Cash Flow'].iloc[0:2]
capex = cash_flow.loc['Capital Expenditure'].iloc[0:2]

fcf_current = operating_cf.iloc[0] + capex.iloc[0]  # CapEx is negative
fcf_previous = operating_cf.iloc[1] + capex.iloc[1]

fcf_growth = ((fcf_current - fcf_previous) / abs(fcf_previous)) * 100
```

---

### 4. Valuation Category (20%)

#### Metric 4.1: Price-to-Earnings (P/E) Ratio (7%)
**Formula**: Current Stock Price / Earnings Per Share (TTM)

**Data Required:**
- **Current Stock Price** (Market Data)
- **Trailing Twelve Months (TTM) EPS** (Income Statement or Key Stats)

**Yahoo Finance Mapping:**
```python
# Direct from info
pe_ratio = stock.info['trailingPE']

# OR calculate manually
current_price = stock.info['currentPrice']
ttm_eps = stock.info['trailingEps']
pe_ratio = current_price / ttm_eps
```

---

#### Metric 4.2: Price-to-Book (P/B) Ratio (7%)
**Formula**: Market Cap / Book Value

Or: Stock Price / Book Value Per Share

**Data Required:**
- **Market Capitalization** (Market Data)
- **Book Value** (Balance Sheet: Total Shareholder Equity)
- **Shares Outstanding** (Key Stats)

**Yahoo Finance Mapping:**
```python
# Direct from info
pb_ratio = stock.info['priceToBook']

# OR calculate manually
market_cap = stock.info['marketCap']
book_value = balance_sheet.loc['Stockholders Equity'].iloc[0]
pb_ratio = market_cap / book_value
```

---

#### Metric 4.3: PEG Ratio (6%)
**Formula**: P/E Ratio / Earnings Growth Rate

**Data Required:**
- **P/E Ratio** (from above)
- **Expected Earnings Growth Rate** (Analyst estimates or historical EPS growth)

**Yahoo Finance Mapping:**
```python
# Direct from info
peg_ratio = stock.info['pegRatio']

# OR calculate manually
pe_ratio = stock.info['trailingPE']
earnings_growth = stock.info['earningsGrowth'] * 100  # Convert to percentage
peg_ratio = pe_ratio / earnings_growth
```

---

### 5. Efficiency Category (10%)

#### Metric 5.1: Asset Turnover Ratio (5%)
**Formula**: Total Revenue / Average Total Assets

**Data Required:**
- **Total Revenue** (Income Statement) - Most recent year
- **Total Assets** (Balance Sheet) - Current and previous year

**Yahoo Finance Mapping:**
```python
income_stmt = stock.financials
balance_sheet = stock.balance_sheet

revenue = income_stmt.loc['Total Revenue'].iloc[0]
assets_current = balance_sheet.loc['Total Assets'].iloc[0]
assets_previous = balance_sheet.loc['Total Assets'].iloc[1]
avg_assets = (assets_current + assets_previous) / 2

asset_turnover = revenue / avg_assets
```

---

#### Metric 5.2: Inventory Turnover (5%)
**Formula**: Cost of Goods Sold / Average Inventory

**Data Required:**
- **Cost of Goods Sold (COGS)** (Income Statement)
- **Inventory** (Balance Sheet) - Current and previous year

**Yahoo Finance Mapping:**
```python
income_stmt = stock.financials
balance_sheet = stock.balance_sheet

cogs = income_stmt.loc['Cost Of Revenue'].iloc[0]
inventory_current = balance_sheet.loc['Inventory'].iloc[0]
inventory_previous = balance_sheet.loc['Inventory'].iloc[1]
avg_inventory = (inventory_current + inventory_previous) / 2

inventory_turnover = cogs / avg_inventory
```

**Note**: Service companies may not have inventory. Handle this edge case.

---

## Data Extraction Summary

### From Yahoo Finance (yfinance)

#### Balance Sheet Data
```python
stock = yf.Ticker("AAPL")
balance_sheet = stock.balance_sheet

# Key items needed:
- Total Assets
- Total Current Assets
- Current Liabilities
- Total Debt
- Stockholders Equity
- Cash And Cash Equivalents
- Inventory
```

#### Income Statement Data
```python
income_stmt = stock.financials

# Key items needed:
- Total Revenue
- Cost Of Revenue (COGS)
- Operating Income (EBIT)
- Pretax Income
- Income Tax Expense
- Net Income
- Interest Expense
```

#### Cash Flow Statement Data
```python
cash_flow = stock.cashflow

# Key items needed:
- Operating Cash Flow
- Capital Expenditure
- Free Cash Flow (calculated)
```

#### Market Data & Key Stats
```python
info = stock.info

# Key items available:
- currentPrice
- marketCap
- sharesOutstanding
- trailingPE
- priceToBook
- pegRatio
- trailingEps
- earningsGrowth
```

---

## Alternative Data Sources

### Financial Modeling Prep (FMP) API

**Better for calculated metrics:**

```python
import requests

API_KEY = "your_api_key"
symbol = "AAPL"

# Financial Ratios (All at once!)
url = f"https://financialmodelingprep.com/api/v3/ratios/{symbol}?apikey={API_KEY}"
ratios = requests.get(url).json()

# Available ratios:
- currentRatio
- debtToEquityRatio
- returnOnEquity (ROE)
- returnOnAssets (ROA)
- assetTurnover
- inventoryTurnover
- netProfitMargin
- priceToBookRatio
```

**Financial Growth Metrics:**
```python
url = f"https://financialmodelingprep.com/api/v3/financial-growth/{symbol}?apikey={API_KEY}"
growth = requests.get(url).json()

# Available growth metrics:
- revenueGrowth
- epsGrowth
- freeCashFlowGrowth
```

**Advantage**: Pre-calculated metrics save computation time and reduce errors.

---

## Data Validation Checklist

### Essential Checks Before Scoring

1. **Data Completeness**
   - ✓ All 14 metrics have values
   - ✓ No None or NaN values in critical fields
   - ✓ Historical data available (3-4 years for growth metrics)

2. **Data Reasonableness**
   - ✓ Ratios are within expected ranges (e.g., Current Ratio > 0)
   - ✓ Growth rates are not extreme outliers (e.g., > 1000%)
   - ✓ Market data matches financial statement period

3. **Edge Cases**
   - ✓ Negative equity (handle division by zero)
   - ✓ No inventory for service companies
   - ✓ Missing interest expense (non-levered companies)
   - ✓ Recent IPOs (insufficient historical data)

4. **Currency & Units**
   - ✓ All values in same currency
   - ✓ Consistent units (millions vs billions)
   - ✓ Per-share vs total values

---

## Sample Data Structure

### Raw Data JSON Format
```json
{
  "symbol": "AAPL",
  "company_name": "Apple Inc.",
  "date_extracted": "2025-11-12",
  "data_source": "yahoo_finance",
  "financial_data": {
    "balance_sheet": {
      "total_assets": 352755000000,
      "current_assets": 143566000000,
      "current_liabilities": 145308000000,
      "total_debt": 111088000000,
      "stockholders_equity": 50672000000,
      "cash": 29965000000,
      "inventory": 6511000000
    },
    "income_statement": {
      "total_revenue": 394328000000,
      "cost_of_revenue": 214137000000,
      "operating_income": 119437000000,
      "net_income": 99803000000,
      "interest_expense": 3933000000,
      "income_tax_expense": 16741000000
    },
    "cash_flow": {
      "operating_cash_flow": 110543000000,
      "capital_expenditure": -10959000000,
      "free_cash_flow": 99584000000
    },
    "market_data": {
      "current_price": 226.40,
      "market_cap": 3443000000000,
      "shares_outstanding": 15204100000,
      "pe_ratio": 34.51,
      "pb_ratio": 67.94,
      "peg_ratio": 2.73
    }
  }
}
```

---

## Implementation Priority

### Phase 1: Core Metrics (Easiest to Calculate)
1. Current Ratio ✓
2. Debt-to-Equity Ratio ✓
3. Net Profit Margin ✓
4. P/E Ratio ✓
5. P/B Ratio ✓

### Phase 2: Moderate Complexity
6. Asset Turnover ✓
7. Revenue Growth ✓
8. Interest Coverage Ratio ✓
9. ROE ✓

### Phase 3: Advanced Metrics
10. ROIC (requires calculated NOPAT)
11. EPS Growth (requires historical EPS)
12. FCF Growth (requires CF statement)
13. PEG Ratio (requires growth estimates)
14. Inventory Turnover (N/A for some companies)

---

**Next Step**: Would you like me to start building the actual Python implementation?
