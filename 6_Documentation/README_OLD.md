# Fundamental Stock Scoring System - Indian Markets

A comprehensive scoring system for Indian stocks based on 14 fundamental indicators across 5 categories.

## Current Analysis
**Stock**: Eternal Ltd (ETERNALIT.NS / ETERNALIT.BO)

## Features
- Automated data extraction from Yahoo Finance (NSE/BSE)
- 14 fundamental metrics calculation
- Weighted scoring system (0-100 scale)
- Detailed scorecard and visualizations
- Indian market specific adjustments

## Categories & Weights
1. **Financial Health** (20%): D/E Ratio, Current Ratio, Interest Coverage
2. **Profitability** (25%): ROE, ROIC, Net Profit Margin
3. **Growth** (25%): Revenue Growth, EPS Growth, FCF Growth
4. **Valuation** (20%): P/E, P/B, PEG Ratio
5. **Efficiency** (10%): Asset Turnover, Inventory Turnover

## Quick Start
```bash
pip install -r requirements.txt
python main.py
```

## Stock Ticker Format for Indian Markets
- NSE: `SYMBOL.NS` (e.g., ETERNALIT.NS)
- BSE: `SYMBOL.BO` (e.g., ETERNALIT.BO)
