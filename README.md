<div align="center">

# 📊 Fundamental Indicators - Stock Analysis Toolkit

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Mohit1053/Fundamental_Indicators/graphs/commit-activity)

**A professional-grade toolkit for comprehensive fundamental analysis of Indian stocks with automated scoring, pattern detection, statistical analysis, and report generation.**

[Features](#-key-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Examples](#-examples) • [Contributing](#-contributing)

---

</div>

## 🎯 Overview

Fundamental Indicators is a comprehensive Python-based stock analysis toolkit designed specifically for Indian equity markets. It provides automated analysis across multiple dimensions:

- **📈 Fundamental Scoring** - 14-metric weighted scoring system (0-100 scale)
- **🔍 Pattern Detection** - Cyclical patterns (weekday, monthly, quarterly)
- **📊 Statistical Analysis** - 26+ technical indicators (MA, RSI, MACD, Bollinger Bands)
- **💰 Fundamental Metrics** - MCAP growth, liquidity analysis, valuation ratios
- **📑 Automated Reporting** - Excel reports, visualizations, and markdown summaries
- **⚡ Bulk Processing** - Analyze NIFTY50, NIFTY500, or custom stock lists

---

## ✨ Key Features

### 🎯 Core Fundamental Scoring
- 14 fundamental metrics with customizable weights
- Intelligent threshold-based scoring (0-100 scale)
- Excel reports with charts and visualizations
- Sample implementation with Eternal Ltd data

### 🔬 Generic Stock Analyzer
- **Universal compatibility** - Works with any stock CSV
- **Pattern analysis** - 35+ cyclical and special patterns
- **Technical indicators** - Moving averages, RSI, MACD, Bollinger Bands, ATR
- **Fundamental metrics** - Market cap trends, liquidity, price-to-book
- **Rich visualizations** - 5+ charts per stock
- **Comprehensive reports** - Detailed markdown documentation

### 🚀 Bulk Analysis Tools
- Batch process multiple stocks simultaneously
- NIFTY50 and NIFTY500 support
- ACE Equity CSV compatibility
- Interactive data collection
- Retry mechanism for failed analyses

### 📦 Pre-analyzed Data
- **50 NIFTY50 stocks** - Complete analyses available
- **500 NIFTY500 stocks** - Individual CSVs ready
- Historical data from 2000-2025
- 10 columns per stock (OHLC, Volume, MCAP, etc.)

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Install dependencies
pip install -r requirements.txt
```

### Installation

```bash
# Clone the repository
git clone https://github.com/Mohit1053/Fundamental_Indicators.git
cd Fundamental_Indicators

# Install required packages
pip install -r requirements.txt
```

### Basic Usage

#### 1️⃣ Core Fundamental Scoring

```bash
cd 1_Core_Fundamental_Scoring
python main.py
```

**Output:** Excel report with scoring, visualizations, and metrics

#### 2️⃣ Analyze Any Stock

```bash
cd 2_Generic_Stock_Analyzer
python analyze_stock.py path/to/your/stock.csv
```

**Output:** Complete analysis with patterns, statistics, fundamentals, charts, and reports

#### 3️⃣ Bulk Analysis (Multiple Stocks)

```bash
cd 5_Bulk_Tools
python bulk_market_analyzer.py
```

**Output:** Batch analysis of multiple stocks with consolidated results

---

## 📂 Project Structure

```
Fundamental_Indicators/
│
├── 1_Core_Fundamental_Scoring/        # Original scoring system (Eternal Ltd example)
│   ├── main.py                        # Main execution script
│   ├── eternal_ltd_real_data.py       # Sample data (Eternal Ltd/Zomato)
│   ├── metric_calculator.py           # 14 fundamental metrics calculator
│   ├── scoring_engine.py              # Weighted scoring engine (0-100 scale)
│   ├── report_generator.py            # Excel & visualization generator
│   ├── eternal_analysis.png           # Sample output visualization
│   └── eternal_fundamental_analysis.xlsx  # Sample Excel report
│
├── 2_Generic_Stock_Analyzer/          # Universal stock analysis toolkit
│   ├── analyze_stock.py               # Master pipeline for any stock
│   ├── universal_pattern_analyzer.py  # Cyclical pattern detection
│   ├── universal_statistical_analyzer.py  # Technical indicators & statistics
│   ├── universal_visualization_generator.py  # Chart generation
│   ├── universal_report_generator.py  # Comprehensive markdown reports
│   ├── README.md                      # Toolkit documentation
│   ├── EXAMPLES.md                    # Usage examples
│   └── requirements.txt               # Python dependencies
│
├── 3_Example_Analyses/                # Sample analysis outputs
│   └── Reliance_Analysis_Complete/    # Complete Reliance Industries analysis
│       ├── 00_Master_Data/            # Original CSV + filled data
│       ├── 01_Supporting_Raw_Data/    # All statistical calculations
│       ├── 02_Median_Statistics/      # Median values by metric
│       ├── 03_Cyclical_Patterns/      # Weekday/monthly/quarterly patterns
│       ├── 04_Fundamental_Analysis/   # Scoring and fundamental metrics
│       ├── 05_Visualizations/         # Charts and graphs
│       ├── 06_Comprehensive_Reports/  # Detailed markdown reports
│       ├── 07_Verification/           # Audit trails and verification
│       ├── 08_Phase1_Original_Analysis/  # Historical workflow
│       └── 09_Reports/                # Master reports
│
├── 4_Legacy_Scripts/                  # Archived analysis workflows
│   └── Reliance_Workflow/             # Original Reliance analysis scripts
│       ├── analyze_and_fill_csv.py    # CSV data filler
│       ├── create_visualizations.py   # Visualization generator
│       ├── verify_calculations.py     # Calculation verifier
│       ├── weekday_monthly_analysis.py  # Cyclical analysis
│       ├── create_pattern_visualizations.py  # Pattern charts
│       ├── extract_supporting_data.py  # Raw data extractor
│       └── pattern_visualizations.png  # Sample output
│
├── 5_Bulk_Tools/                      # Multi-stock analysis tools
│   ├── bulk_market_analyzer.py        # Analyze multiple stocks
│   ├── quick_start_bulk.py            # Bulk analysis quick start
│   ├── interactive_data_collector.py  # Interactive data collection
│   ├── ace_equity_template.csv        # ACE Equity CSV template
│   ├── ACE_EQUITY_COLUMN_MAPPING.md   # Column mapping guide
│   ├── ACE_EQUITY_GUIDE.md            # ACE Equity usage guide
│   └── INTERACTIVE_TOOL_GUIDE.md      # Interactive tool documentation
│
├── 6_Documentation/                   # Project documentation
│   ├── ANALYSIS_RESULTS.md            # Analysis results summaries
│   ├── CLEANUP_SUMMARY.md             # Cleanup and refactoring notes
│   ├── COMPLETE_AUDIT_AND_TOOLKIT.md  # Comprehensive audit report
│   ├── DATA_REQUIREMENTS.md           # Data format requirements
│   ├── DATA_VERIFICATION_REPORT.md    # Verification methodology
│   ├── PROJECT_SUMMARY.md             # Project overview
│   ├── QUICK_START_GUIDE.md           # Quick start instructions
│   ├── ROADMAP.md                     # Future development roadmap
│   ├── SCORE_CALCULATION_EXPLAINED.md  # Scoring methodology
│   ├── SCORING_LOGIC_EXPLAINED.md     # Detailed scoring logic
│   ├── SCORING_THRESHOLDS_VISUAL.md   # Threshold visualization
│   └── USAGE_GUIDE.md                 # Comprehensive usage guide
│
├── 7_Configuration_Data/              # Configuration files
│   ├── scoring_parameters.csv         # Metric weights and thresholds
│   ├── detailed_scoring_parameters.csv  # Extended parameters
│   ├── trading_calendar.csv           # Trading calendar data
│   ├── monthly_analysis.csv           # Monthly pattern data
│   ├── quarter_analysis.csv           # Quarterly pattern data
│   └── weekday_analysis.csv           # Weekday pattern data
│
├── requirements.txt                   # Python package dependencies
└── index.html                         # Web interface (if applicable)
```

---

## 🚀 Quick Start

### 1. Core Fundamental Scoring (Eternal Ltd Example)
Demonstrates the original 14-metric scoring system:

```bash
cd 1_Core_Fundamental_Scoring
python main.py
```

**Output:**
- Console: Detailed metric scores and final rating
- `eternal_analysis.png`: Visual dashboard
- `eternal_fundamental_analysis.xlsx`: Excel report

**Key Features:**
- 14 fundamental indicators across 5 categories
- Weighted scoring (0-100 scale)
- Automatic rating: Excellent (80-100), Good (60-79), Average (40-59), Below Average (20-39), Poor (0-19)

---

### 2. Generic Stock Analyzer (Any Stock)
Universal toolkit for analyzing any stock from CSV data:

```bash
cd 2_Generic_Stock_Analyzer
python analyze_stock.py your_stock_data.csv "Company Name"
```

**Capabilities:**
- ✅ Cyclical pattern detection (weekday, monthly, quarterly)
- ✅ Statistical analysis (mean, median, percentiles, skewness, kurtosis)
- ✅ Technical indicators (moving averages, volatility, momentum)
- ✅ ANOVA testing for cyclical significance
- ✅ Automated chart generation
- ✅ Comprehensive markdown reports

**See:** `2_Generic_Stock_Analyzer/README.md` for detailed usage

---

### 3. View Example Analysis (Reliance Industries)
Complete reference analysis with 6,433 trading days (2000-2025):

```
3_Example_Analyses/Reliance_Analysis_Complete/
├── 00_Master_Data/Reliance_Industries_Updated.csv  (Filled data)
├── 01_Supporting_Raw_Data/  (50+ statistical files)
├── 02_Median_Statistics/  (Median values by metric)
├── 06_Comprehensive_Reports/COMPLETE_ANALYSIS_REPORT.md  (Master report)
└── 09_Reports/VERIFICATION_CHECKLIST.md  (Audit trail)
```

**Key Insights from Reliance Example:**
- Complete fill-in of missing data using statistical methods
- All raw supporting data preserved for verification
- Median statistics for every metric
- Cyclical pattern analysis with ANOVA testing
- Pattern visualizations and statistical charts

---

## 🛠️ Tool Selection Guide

| Use Case | Tool | Location |
|----------|------|----------|
| Analyze one stock (CSV) | Generic Stock Analyzer | `2_Generic_Stock_Analyzer/` |
| Score fundamentals (manual data) | Core Scoring System | `1_Core_Fundamental_Scoring/` |
| Analyze multiple stocks | Bulk Market Analyzer | `5_Bulk_Tools/` |
| Interactive data collection | Interactive Collector | `5_Bulk_Tools/` |
| View example workflow | Reliance Analysis | `3_Example_Analyses/` |
| Study legacy methods | Legacy Scripts | `4_Legacy_Scripts/` |

---

## 📊 Key Metrics & Categories

### 1. Profitability (30%)
- Return on Equity (ROE)
- Return on Assets (ROA)
- Operating Profit Margin
- Net Profit Margin

### 2. Liquidity (20%)
- Current Ratio
- Quick Ratio
- Cash Ratio

### 3. Efficiency (15%)
- Asset Turnover
- Inventory Turnover

### 4. Valuation (20%)
- Price-to-Earnings (P/E)
- Price-to-Book (P/B)

### 5. Solvency (15%)
- Debt-to-Equity
- Interest Coverage
- Equity Ratio

**Total Score:** 0-100 (weighted average)

---

## 📋 Requirements

### Python Version
- Python 3.8+

### Dependencies
```bash
pip install -r requirements.txt
```

**Core Libraries:**
- `pandas` >= 2.0.0 (Data manipulation)
- `numpy` >= 1.24.0 (Numerical computing)
- `matplotlib` >= 3.7.0 (Plotting)
- `seaborn` >= 0.12.0 (Statistical visualization)
- `scipy` >= 1.10.0 (Statistical analysis)
- `openpyxl` >= 3.1.0 (Excel export)

---

## 🎯 Analysis Workflow

### For Individual Stocks (Generic Analyzer)
1. **Prepare CSV:** Ensure columns match required format (see `2_Generic_Stock_Analyzer/README.md`)
2. **Run Analysis:** `python analyze_stock.py your_data.csv "Company Name"`
3. **Review Outputs:**
   - `CompanyName_Outputs/analysis_report.md` (Comprehensive report)
   - `CompanyName_Outputs/visualizations/` (Charts)
   - `CompanyName_Outputs/pattern_analysis/` (Cyclical patterns)

### For Bulk Analysis
1. **Collect Data:** Use `interactive_data_collector.py` or ACE Equity template
2. **Configure:** Edit `scoring_parameters.csv` if needed
3. **Execute:** `python bulk_market_analyzer.py`
4. **Compare:** Review cross-stock comparisons and rankings

---

## 📖 Documentation Guide

| Document | Purpose |
|----------|---------|
| `QUICK_START_GUIDE.md` | Fast setup and basic usage |
| `USAGE_GUIDE.md` | Comprehensive user manual |
| `SCORE_CALCULATION_EXPLAINED.md` | Scoring methodology deep-dive |
| `DATA_REQUIREMENTS.md` | CSV format specifications |
| `COMPLETE_AUDIT_AND_TOOLKIT.md` | Full project audit report |
| `ROADMAP.md` | Future development plans |

All documentation: `6_Documentation/`

---

## 🔍 Verification & Transparency

Every calculation in this toolkit is:
- ✅ **Traceable:** All raw data preserved in supporting files
- ✅ **Reproducible:** Step-by-step calculation logs
- ✅ **Verifiable:** Cross-referenced against original data
- ✅ **Documented:** Methodology explained in reports

Example: `3_Example_Analyses/Reliance_Analysis_Complete/07_Verification/`

---

## 🧪 Testing & Validation

### Validated On:
- **Reliance Industries:** 6,433 trading days (2000-2025)
- **Eternal Ltd (Zomato):** Fundamental scoring demo
- **Multiple Stocks:** Bulk analysis testing

### Statistical Methods:
- ANOVA for cyclical pattern significance
- T-tests for group comparisons
- Percentile analysis (10th, 25th, 50th, 75th, 90th)
- Skewness & kurtosis for distribution analysis

---

## 🤝 Contributing & Extensions

### Add New Metrics
1. Edit `1_Core_Fundamental_Scoring/metric_calculator.py`
2. Update `7_Configuration_Data/scoring_parameters.csv`
3. Modify `scoring_engine.py` with new thresholds

### Customize Scoring
- Adjust weights in `scoring_parameters.csv`
- Modify thresholds for your market context
- Add industry-specific benchmarks

### Extend Analyzers
- Add new patterns to `universal_pattern_analyzer.py`
- Create custom visualizations in `universal_visualization_generator.py`
- Build new reports in `universal_report_generator.py`

---

## ⚠️ Disclaimer

This toolkit is for **educational and research purposes only**. 

- ❌ Not financial advice
- ❌ Not investment recommendations
- ✅ Academic analysis tool
- ✅ Learning resource for fundamental analysis

**Always consult qualified financial advisors before making investment decisions.**

---

## 📧 Support & Issues

For detailed usage questions, refer to:
- `6_Documentation/USAGE_GUIDE.md`
- `2_Generic_Stock_Analyzer/README.md`
- `2_Generic_Stock_Analyzer/EXAMPLES.md`

For specific tools:
- **ACE Equity:** `5_Bulk_Tools/ACE_EQUITY_GUIDE.md`
- **Interactive Collector:** `5_Bulk_Tools/INTERACTIVE_TOOL_GUIDE.md`

---

## 📝 License

This project is provided as-is for educational purposes. Refer to individual files for specific licenses if applicable.

---

## 🎓 Learning Path

1. **Beginner:** Start with `1_Core_Fundamental_Scoring/main.py` to understand metrics
2. **Intermediate:** Run `2_Generic_Stock_Analyzer/` on your own CSV data
3. **Advanced:** Study `3_Example_Analyses/Reliance_Analysis_Complete/` for comprehensive methodology
4. **Expert:** Use `5_Bulk_Tools/` for portfolio-level analysis

---

## 🔄 Version History

- **v3.0** - Full reorganization into modular structure (Current)
- **v2.0** - Generic Stock Analyzer toolkit created
- **v1.5** - Reliance Industries complete analysis
- **v1.0** - Core fundamental scoring system (Eternal Ltd)

---

---

## 📊 Supported Metrics

### Fundamental Metrics (14)
- Market Cap, Volume, Number of Trades
- Price-to-Book Value Ratio
- Revenue, Net Profit, Operating Profit
- Total Assets, Equity, Total Liabilities
- Current Assets, Current Liabilities
- Quick Assets, Inventory

### Technical Indicators (26+)
- Moving Averages (SMA, EMA)
- RSI, MACD, Bollinger Bands
- ATR, Standard Deviation
- Volume trends and analysis
- And more...

### Pattern Analysis (35+)
- Weekday patterns
- Monthly patterns
- Quarterly patterns
- Special event patterns
- Seasonal trends

---

## 📖 Documentation

Comprehensive documentation is available in the [6_Documentation](6_Documentation/) folder:

- **[Quick Start Guide](6_Documentation/QUICK_START_GUIDE.md)** - Get started in 5 minutes
- **[Usage Guide](6_Documentation/USAGE_GUIDE.md)** - Detailed usage instructions
- **[Scoring Logic](6_Documentation/SCORING_LOGIC_EXPLAINED.md)** - How scores are calculated
- **[Data Requirements](6_Documentation/DATA_REQUIREMENTS.md)** - CSV format specifications
- **[ACE Equity Guide](5_Bulk_Tools/ACE_EQUITY_GUIDE.md)** - Using ACE Equity data
- **[API Reference](6_Documentation/COMPLETE_AUDIT_AND_TOOLKIT.md)** - Complete toolkit audit

---

## 🎨 Examples

### Example 1: Reliance Industries Analysis
```python
python 2_Generic_Stock_Analyzer/analyze_stock.py 3_Example_Analyses/Reliance_Analysis_Complete/00_Master_Data/Reliance.csv
```

### Example 2: NIFTY50 Bulk Analysis
```python
cd 5_Bulk_Tools
python bulk_market_analyzer.py --input 4_NIFTY50_Individual_Stocks/ --output analysis_results/
```

### Example 3: Custom Stock Scoring
```python
cd 1_Core_Fundamental_Scoring
# Edit eternal_ltd_real_data.py with your data
python main.py
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📋 Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib
- openpyxl
- seaborn
- scipy
- And more (see `requirements.txt`)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Data source compatibility: ACE Equity, BSE, NSE
- Built for Indian equity market analysis
- Inspired by fundamental analysis principles

---

## 📧 Contact

**Mohit** - [@Mohit1053](https://github.com/Mohit1053)

**Project Link:** [https://github.com/Mohit1053/Fundamental_Indicators](https://github.com/Mohit1053/Fundamental_Indicators)

---

## ⚠️ Disclaimer

This toolkit is for **educational and research purposes only**. 

- ❌ Not financial advice
- ❌ Not investment recommendations
- ✅ Academic analysis tool
- ✅ Learning resource for fundamental analysis

**Always consult qualified financial advisors before making investment decisions.**

---

## 🌟 Star History

If you find this project helpful, please consider giving it a ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=Mohit1053/Fundamental_Indicators&type=Date)](https://star-history.com/#Mohit1053/Fundamental_Indicators&Date)

---

<div align="center">

**Made with ❤️ for Indian Stock Market Analysis**

[Report Bug](https://github.com/Mohit1053/Fundamental_Indicators/issues) • [Request Feature](https://github.com/Mohit1053/Fundamental_Indicators/issues)

</div>
