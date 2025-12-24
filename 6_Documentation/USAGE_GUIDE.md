# Quick Start Guide - Fundamental Stock Analysis System

## Overview
This system performs comprehensive fundamental analysis of Indian stocks using 14 key financial indicators across 5 categories, producing a weighted score from 0-100.

## For Indian Markets (NSE/BSE)
Stock tickers should use NSE format: `SYMBOLNAME.NS` or BSE format: `SYMBOLNAME.BO`

---

## Installation

### Step 1: Ensure Python 3.9+ is installed
```bash
python --version
```

### Step 2: Install required packages
```bash
pip install -r requirements.txt
```

This installs:
- yfinance (Yahoo Finance data)
- pandas (data manipulation)
- numpy (numerical operations)
- matplotlib & seaborn (visualizations)
- openpyxl (Excel export)

---

## Usage

### Quick Analysis (Using Sample Data)
```bash
python main.py
```

This will:
1. Calculate all 14 fundamental metrics
2. Normalize scores to 0-100 scale
3. Apply weighted scoring
4. Generate visualization (PNG)
5. Export Excel report

**Output Files:**
- `eternal_analysis.png` - Visual dashboard
- `eternal_fundamental_analysis.xlsx` - Detailed Excel report

---

## System Components

### 1. `sample_data.py`
- Contains representative financial data for Eternal IT
- Can be replaced with real API data fetcher
- Structured format matching balance sheet, income statement, cash flow

### 2. `metric_calculator.py`
- Calculates all 14 fundamental indicators
- Functions for each metric (D/E, ROE, ROIC, etc.)
- Handles edge cases (missing data, service companies with no inventory)

### 3. `scoring_engine.py`
- Normalizes raw metrics to 0-100 scale
- Applies category weights
- Calculates final composite score
- Defines ideal ranges for each metric

### 4. `report_generator.py`
- Creates comprehensive analysis report
- Generates visualizations (charts, radar plots, heatmaps)
- Exports to Excel with multiple sheets
- Identifies strengths and weaknesses

### 5. `main.py`
- Main entry point
- Orchestrates the entire analysis workflow

---

## Understanding the Score

### Score Ranges
- **80-100:** Excellent - Strong fundamentals across the board
- **60-79:** Good - Solid company with minor weaknesses
- **40-59:** Average - Mixed signals, requires deeper analysis
- **20-39:** Below Average - Significant concerns
- **0-19:** Poor - Weak fundamentals

### Category Weights
1. **Financial Health (20%)** - Debt levels, liquidity, solvency
2. **Profitability (25%)** - Returns to shareholders and efficiency
3. **Growth (25%)** - Revenue, earnings, and cash flow expansion
4. **Valuation (20%)** - Price relative to fundamentals
5. **Efficiency (10%)** - Asset and inventory utilization

---

## Using with Real Stock Data

### For Live Data Analysis (requires yfinance to work)
Replace `sample_data.py` usage with:

```python
from data_extractor import IndianStockDataExtractor

# Fetch real data
extractor = IndianStockDataExtractor('INFY', exchange='NS')  # Infosys
extractor.fetch_all_data()

# Continue with metric calculation...
```

**Note:** Due to SSL certificate issues on some Windows systems, the current implementation uses sample data. In production environments, this would be replaced with real-time API calls.

---

## Customization

### Adjusting Weights
Edit `scoring_engine.py` - `METRIC_CONFIG` dictionary:

```python
'roe': {
    'category': 'Profitability',
    'weight': 0.08,  # Change this to adjust weight
    'direction': 'higher',
    ...
}
```

### Changing Ideal Ranges
Modify the same `METRIC_CONFIG` section:

```python
'roe': {
    ...
    'ideal_min': 15.0,   # Adjust based on industry
    'ideal_max': 30.0,
    'acceptable_min': 5.0,
}
```

### Adding New Metrics
1. Add calculation function in `metric_calculator.py`
2. Add scoring configuration in `scoring_engine.py`
3. Update category weights to sum to 100%

---

## Output Interpretation

### Excel Report Structure
**Sheet 1: Executive Summary**
- Company information
- Final score and rating
- Recommendation

**Sheet 2: Category Scores**
- Breakdown by 5 categories
- Weighted contributions

**Sheet 3: Individual Metrics**
- All 14 metrics with raw values
- Normalized scores
- Individual ratings

**Sheet 4: Financial Data**
- Raw financial statement items
- Source data verification

### Visualization Dashboard
- **Category Bar Chart:** Compare performance across categories
- **Radar Chart:** Visual representation of balance
- **Heatmap:** Individual metric scores at a glance
- **Score Distribution:** Statistical view of metric performance
- **Pie Chart:** Weighted contribution breakdown

---

## Troubleshooting

### SSL Certificate Errors (yfinance)
**Issue:** `CertificateVerifyError` when fetching data

**Solution:**
- Use sample data approach (current implementation)
- Or install certificates: `pip install certifi`
- Or use alternative APIs (Financial Modeling Prep, Alpha Vantage)

### Missing Data Points
The system handles common edge cases:
- Service companies with no inventory (Inventory Turnover = N/A)
- Companies with no debt (D/E ratio = 0)
- Negative growth (assigned low scores)

### Excel File Already Open
Close the Excel file before running the script again.

---

## Extending the System

### Multi-Stock Comparison
Create a wrapper to analyze multiple stocks:

```python
stocks = ['INFY.NS', 'TCS.NS', 'WIPRO.NS']
results = []

for symbol in stocks:
    # Run analysis for each
    # Store results
    results.append(final_score)

# Compare results
```

### Historical Score Tracking
Store scores in database:

```python
import sqlite3

conn = sqlite3.connect('stock_scores.db')
# Store: date, symbol, score, category_scores
```

### Automated Alerts
Add monitoring logic:

```python
if final_score >= 80:
    send_email("Strong Buy Alert: {symbol}")
elif final_score < 40:
    send_email("Sell Alert: {symbol}")
```

---

## Best Practices

1. **Update Frequency:** Run analysis after quarterly earnings
2. **Cross-Verification:** Compare with manual fundamental analysis
3. **Sector Context:** Interpret scores relative to industry averages
4. **Trend Analysis:** Track score changes over time
5. **Risk Assessment:** Don't rely solely on score - consider qualitative factors

---

## Example Workflow

```python
# 1. Import modules
from sample_data import ETERNAL_DATA
from metric_calculator import FundamentalMetricsCalculator
from scoring_engine import ScoringEngine
from report_generator import ReportGenerator

# 2. Calculate metrics
calculator = FundamentalMetricsCalculator(ETERNAL_DATA)
metrics = calculator.calculate_all_metrics()

# 3. Score metrics
scorer = ScoringEngine(metrics)
scorer.calculate_scores()
scorer.calculate_category_scores()
final_score = scorer.calculate_final_score()

# 4. Generate report
report = ReportGenerator(
    company_info=ETERNAL_DATA['company_info'],
    metrics=metrics,
    scores=scorer.scores,
    category_scores=scorer.category_scores,
    final_score=final_score
)
report.generate_complete_report()
```

---

## Support & Documentation

- **ROADMAP.md** - Complete project roadmap and methodology
- **DATA_REQUIREMENTS.md** - Detailed data mapping for all metrics
- **ANALYSIS_RESULTS.md** - Sample analysis results for Eternal IT
- **README.md** - Project overview

---

## Future Enhancements

- [ ] Real-time data integration with NSE/BSE APIs
- [ ] Support for multiple sectors with sector-specific weights
- [ ] Machine learning-based optimal weight discovery
- [ ] Portfolio-level aggregate scoring
- [ ] Web dashboard using Streamlit or Dash
- [ ] Automated daily email reports
- [ ] Peer comparison within industry
- [ ] Technical analysis integration

---

**Version:** 1.0  
**Last Updated:** November 12, 2025  
**Maintained by:** Automated Fundamental Analysis System
