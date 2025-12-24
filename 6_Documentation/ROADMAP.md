# Fundamental Stock Scoring System - Roadmap

## Overview
A weighted fundamental analysis system to score stocks based on 14 key financial indicators across 5 categories.

---

## Scoring Framework

### Category Breakdown
| Category | Weight | Number of Metrics |
|----------|--------|-------------------|
| Financial Health | 20% | 3 |
| Profitability | 25% | 3 |
| Growth | 25% | 3 |
| Valuation | 20% | 3 |
| Efficiency | 10% | 2 |
| **TOTAL** | **100%** | **14** |

### Detailed Metrics

#### 1. Financial Health (20%)
- **Debt-to-Equity Ratio** (7%) - Lower is better
- **Current Ratio** (7%) - Higher is better
- **Interest Coverage Ratio** (6%) - Higher is better

#### 2. Profitability (25%)
- **Return on Equity (ROE)** (8%) - Higher is better
- **Return on Invested Capital (ROIC)** (9%) - Higher is better
- **Net Profit Margin** (8%) - Higher is better

#### 3. Growth (25%)
- **Revenue Growth (3-Year Avg)** (10%) - Higher is better
- **EPS Growth (3-Year Avg)** (10%) - Higher is better
- **Free Cash Flow Growth** (5%) - Higher is better

#### 4. Valuation (20%)
- **Price-to-Earnings (P/E) Ratio** (7%) - Lower is better
- **Price-to-Book (P/B) Ratio** (7%) - Lower is better
- **PEG Ratio** (6%) - Lower is better

#### 5. Efficiency (10%)
- **Asset Turnover Ratio** (5%) - Higher is better
- **Inventory Turnover** (5%) - Higher is better

---

## Data Requirements

### Required Financial Data

#### Balance Sheet Items
- Total Debt
- Total Equity (Shareholder Equity)
- Total Current Assets
- Total Current Liabilities
- Total Assets
- Book Value
- Inventory

#### Income Statement Items
- Total Revenue (3 years historical)
- Net Income
- Operating Income (EBIT)
- Interest Expense
- Net Profit Margin

#### Cash Flow Statement Items
- Operating Cash Flow
- Capital Expenditures (CapEx)
- Free Cash Flow (3 years historical)

#### Per-Share Metrics
- Earnings Per Share (EPS) - 3 years historical
- Current Stock Price
- Book Value Per Share

#### Calculated Metrics Needed
- Market Capitalization
- Invested Capital (for ROIC)

---

## Recommended Data Sources

### Option 1: FREE APIs (Recommended for MVP)

#### **Yahoo Finance (via yfinance Python library)**
- **Cost**: FREE
- **Data Available**: 
  - Balance sheet, income statement, cash flow
  - Historical prices
  - Key ratios and metrics
  - EPS, P/E, P/B ratios
- **Limits**: 2,000 requests/hour (generous)
- **Best For**: Individual stock analysis, prototyping
- **Installation**: `pip install yfinance`

#### **Alpha Vantage**
- **Cost**: FREE tier - 25 API calls/day, 5 calls/minute
- **Data Available**:
  - Balance sheet, income statement, cash flow
  - Company overview with key ratios
  - Earnings data
- **Limits**: Very limited on free tier
- **Best For**: Supplementary data
- **API Key**: Free registration at https://www.alphavantage.co/

#### **Financial Modeling Prep (FMP)**
- **Cost**: FREE tier - 250 calls/day
- **Data Available**:
  - Comprehensive financial statements
  - Financial ratios
  - Financial growth metrics
  - DCF valuation data
- **Limits**: 250 calls/day
- **Best For**: More reliable than Yahoo, good for daily analysis
- **API Key**: Free registration at https://financialmodelingprep.com/

### Option 2: PAID APIs (For Production)

#### **Polygon.io**
- **Cost**: $99-$299/month
- **Best For**: Real-time data, high-volume applications

#### **Tiingo**
- **Cost**: $10-$500/month
- **Best For**: End-of-day fundamentals

#### **IEX Cloud**
- **Cost**: $9-$999/month
- **Best For**: Reliable fundamentals with good documentation

### Option 3: Web Scraping (Not Recommended)
- Sources: Yahoo Finance, MarketWatch, Seeking Alpha
- **Issues**: Legal concerns, rate limiting, HTML changes

---

## Technical Architecture

### System Components

```
┌─────────────────────────────────────────────────────────┐
│                   USER INTERFACE                         │
│         (Dashboard, Reports, Visualizations)            │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                SCORING ENGINE                            │
│  • Calculate individual metrics                          │
│  • Normalize scores (0-100)                             │
│  • Apply weights                                        │
│  • Generate final score                                 │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│              DATA PROCESSING LAYER                       │
│  • Calculate derived metrics                            │
│  • Handle missing data                                  │
│  • Data validation                                      │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│              DATA EXTRACTION LAYER                       │
│  • API Integration (yfinance, FMP, Alpha Vantage)      │
│  • Rate limiting & caching                              │
│  • Error handling & retries                             │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                 DATA STORAGE                             │
│  • Raw financial data (SQLite/PostgreSQL)               │
│  • Calculated scores & rankings                         │
│  • Historical snapshots                                 │
└─────────────────────────────────────────────────────────┘
```

---

## Implementation Roadmap

### Phase 1: Foundation (Week 1)
**Goal**: Set up project structure and data extraction

1. **Environment Setup**
   - Python virtual environment
   - Install dependencies: pandas, numpy, yfinance, requests
   - Project folder structure

2. **Data Extraction Module**
   - Create API wrapper for Yahoo Finance (yfinance)
   - Implement Financial Modeling Prep API integration
   - Build data fetcher for balance sheet, income statement, cash flow
   - Add caching mechanism to avoid redundant API calls

3. **Data Storage**
   - SQLite database setup
   - Create tables for:
     - Companies
     - Financial statements
     - Calculated metrics
     - Scores history

### Phase 2: Calculation Engine (Week 2)
**Goal**: Implement metric calculations and scoring

1. **Metric Calculators**
   - Financial Health metrics (D/E, Current Ratio, Interest Coverage)
   - Profitability metrics (ROE, ROIC, Net Profit Margin)
   - Growth metrics (Revenue, EPS, FCF growth)
   - Valuation metrics (P/E, P/B, PEG)
   - Efficiency metrics (Asset Turnover, Inventory Turnover)

2. **Normalization Engine**
   - Percentile-based scoring (0-100 scale)
   - Industry-specific benchmarking (optional)
   - Handle outliers and edge cases

3. **Weighted Scoring**
   - Apply category weights
   - Calculate final composite score
   - Generate sub-scores by category

### Phase 3: Analysis & Reporting (Week 3)
**Goal**: Create insights and visualizations

1. **Reporting Module**
   - Individual stock scorecard
   - Multi-stock comparison
   - Historical score tracking
   - Category breakdown analysis

2. **Visualization Dashboard**
   - Radar charts for category scores
   - Score distribution histograms
   - Time-series score evolution
   - Ranking tables

3. **Export Functionality**
   - Excel reports
   - PDF scorecards
   - JSON/CSV data exports

### Phase 4: Enhancement (Week 4+)
**Goal**: Add advanced features

1. **Screening & Filtering**
   - Filter stocks by score thresholds
   - Category-specific filters
   - Custom weight adjustment

2. **Alerts & Monitoring**
   - Score change alerts
   - Threshold breach notifications
   - Automated daily/weekly runs

3. **Portfolio Analysis**
   - Aggregate portfolio score
   - Diversification analysis
   - Risk indicators

---

## Calculation Methodology

### Step 1: Data Collection
- Fetch financial statements for target stock(s)
- Retrieve historical data for growth calculations
- Get current market price data

### Step 2: Calculate Raw Metrics
For each of the 14 metrics, calculate the raw value:

**Example Calculations:**
- **Debt-to-Equity** = Total Debt / Shareholder Equity
- **Current Ratio** = Current Assets / Current Liabilities
- **ROE** = Net Income / Shareholder Equity × 100
- **Revenue Growth (3Y)** = [(Revenue_Year3 - Revenue_Year0) / Revenue_Year0] / 3 × 100
- **Free Cash Flow** = Operating Cash Flow - Capital Expenditures

### Step 3: Normalize to 0-100 Scale
Two approaches:

**A. Percentile Ranking** (Recommended)
- Compare stock against peer group or entire market
- Assign score based on percentile position
- Example: If stock is in 75th percentile for ROE, score = 75

**B. Min-Max Normalization**
- Define ideal ranges for each metric
- Scale linearly: Score = (Value - Min) / (Max - Min) × 100
- Invert for "lower is better" metrics

### Step 4: Apply Weights & Calculate Final Score
```
Final Score = Σ (Normalized_Score_i × Weight_i)

Example:
Financial Health Score = (D/E_Score × 0.07) + (Current_Ratio_Score × 0.07) + (Interest_Coverage_Score × 0.06)
...
Total Score = Financial_Health_Score + Profitability_Score + Growth_Score + Valuation_Score + Efficiency_Score
```

### Step 5: Interpret Results
- **80-100**: Excellent - Strong fundamentals across the board
- **60-79**: Good - Solid company with minor weaknesses
- **40-59**: Average - Mixed signals, requires deeper analysis
- **20-39**: Below Average - Significant concerns
- **0-19**: Poor - Weak fundamentals

---

## Technology Stack Recommendations

### Programming Language
- **Python 3.9+** (Data manipulation, API integration, calculations)

### Core Libraries
```python
# Data Handling
pandas              # Data manipulation
numpy              # Numerical calculations

# Data Sources
yfinance           # Yahoo Finance data (FREE)
requests           # HTTP requests for APIs
finnhub-python     # Alternative data source

# Database
sqlite3            # Lightweight database (built-in)
sqlalchemy         # ORM for database operations

# Visualization
matplotlib         # Basic plotting
seaborn            # Statistical visualizations
plotly             # Interactive charts
dash               # Web dashboard (optional)

# Reporting
openpyxl           # Excel export
fpdf2              # PDF generation
jinja2             # Report templates

# Utilities
python-dotenv      # Environment variables
schedule           # Task scheduling
```

### Optional Enhancements
- **Streamlit**: Quick web UI for dashboards
- **FastAPI**: REST API for scoring service
- **PostgreSQL**: Production database
- **Redis**: Caching layer
- **Docker**: Containerization

---

## Data Source Recommendation

### For Your Use Case: **Hybrid Approach**

**Primary Source: Yahoo Finance (yfinance)**
- FREE and unlimited for reasonable use
- Provides 90% of required data
- Most reliable for price data and basic ratios
- Good historical data

**Supplementary: Financial Modeling Prep (FREE tier)**
- 250 calls/day sufficient for daily analysis
- Better for calculated ratios (ROIC, FCF)
- More comprehensive financial statements
- Good growth metrics

**Implementation Strategy:**
1. Use yfinance as primary data source
2. Fall back to FMP for missing metrics
3. Cache data locally to minimize API calls
4. Update data once daily (after market close)

---

## Example Workflow

### Analyzing a Single Stock (e.g., AAPL)

```python
# 1. Fetch Data
stock = yf.Ticker("AAPL")
balance_sheet = stock.balance_sheet
income_stmt = stock.financials
cash_flow = stock.cashflow
info = stock.info

# 2. Calculate Metrics
debt_to_equity = calculate_de_ratio(balance_sheet)
current_ratio = calculate_current_ratio(balance_sheet)
roe = calculate_roe(income_stmt, balance_sheet)
revenue_growth = calculate_3y_growth(income_stmt, 'Total Revenue')
# ... etc

# 3. Normalize Scores
de_score = normalize_metric(debt_to_equity, 'debt_to_equity', inverse=True)
cr_score = normalize_metric(current_ratio, 'current_ratio')
# ... etc

# 4. Calculate Weighted Score
financial_health = (de_score * 0.07) + (cr_score * 0.07) + (ic_score * 0.06)
profitability = (roe_score * 0.08) + (roic_score * 0.09) + (npm_score * 0.08)
# ... etc

final_score = financial_health + profitability + growth + valuation + efficiency

# 5. Generate Report
print(f"AAPL Fundamental Score: {final_score:.2f}/100")
```

---

## Next Steps

1. **Confirm Data Sources**: Review the recommended sources and confirm which to use
2. **Set Up Environment**: Create Python environment and install dependencies
3. **Start with MVP**: Build basic version with 3-5 stocks to validate approach
4. **Iterate**: Expand to more stocks and refine scoring methodology
5. **Automate**: Schedule daily updates and monitoring

---

## Questions to Consider

1. **Stock Universe**: Which stocks/markets to analyze? (US, India, specific sectors?)
2. **Update Frequency**: Daily, weekly, or on-demand analysis?
3. **Peer Comparison**: Compare against industry peers or entire market?
4. **Historical Tracking**: Store historical scores for trend analysis?
5. **Output Format**: Excel reports, web dashboard, or API service?

---

## Estimated Timeline

- **MVP (Basic scoring for single stock)**: 3-5 days
- **Full System (Multi-stock, database, reports)**: 2-3 weeks
- **Production-Ready (Dashboard, automation)**: 4-6 weeks

---

*This roadmap is designed to be flexible and scalable. Start with the MVP and expand based on your specific needs.*
