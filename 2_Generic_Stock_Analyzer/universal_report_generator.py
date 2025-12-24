"""
Universal Stock Report Generator
=================================
Generates comprehensive markdown reports for ANY stock analysis.

Creates:
- Executive Summary Report
- Pattern Analysis Report
- Trading Strategies Report
- Master Index

Usage:
    python universal_report_generator.py --analysis_dir "Company_Analysis_Complete" --company "Company Name"
"""

import pandas as pd
import numpy as np
import argparse
import os
import sys
from datetime import datetime

class UniversalReportGenerator:
    """Generate comprehensive reports for stock analysis"""
    
    def __init__(self, analysis_dir, company_name):
        self.analysis_dir = analysis_dir
        self.company_name = company_name
        self.reports_dir = f"{analysis_dir}/09_Reports"
        
        # Create output directory
        os.makedirs(self.reports_dir, exist_ok=True)
        
    def load_comparison_data(self):
        """Load pattern comparison table"""
        file_path = f"{self.analysis_dir}/07_Comparison_Tables/pattern_comparison_table.csv"
        return pd.read_csv(file_path)
    
    def load_performance_metrics(self):
        """Load performance metrics if available"""
        stats_dir = f"{self.analysis_dir}/10_Statistical_Analysis"
        perf_file = f"{stats_dir}/performance_metrics.csv"
        
        if os.path.exists(perf_file):
            return pd.read_csv(perf_file)
        return None
    
    def generate_executive_summary(self):
        """Generate executive summary report"""
        print(f"\n{'='*70}")
        print("GENERATING EXECUTIVE SUMMARY")
        print(f"{'='*70}\n")
        
        comparison_df = self.load_comparison_data()
        perf_metrics = self.load_performance_metrics()
        
        report = f"""#  {self.company_name.upper()} - EXECUTIVE SUMMARY

## Analysis Overview

**Generated**: {datetime.now().strftime('%B %d, %Y')}

This comprehensive analysis examines {self.company_name} stock data to identify cyclical patterns, technical indicators, and statistical characteristics that can inform trading decisions.

---

##  KEY FINDINGS

### Overall Market Performance

"""
        
        # Add performance metrics if available
        if perf_metrics is not None:
            report += f"""
| Metric | Value |
|--------|-------|
"""
            for _, row in perf_metrics.iterrows():
                report += f"| {row['Metric']} | {row['Value']} |\n"
        
        # Get overall stats
        overall = comparison_df[comparison_df['Pattern'] == 'All Days'].iloc[0]
        
        report += f"""

### Market Statistics
- **Total Trading Days**: {int(overall['Total Trading Days']):,}
- **Mean Daily Return**: {overall['Mean Daily Return (%)']:.3f}%
- **Median Daily Return**: {overall['Median Daily Return (%)']:.3f}%
- **Win Rate**: {overall['Win Rate (%)']:.1f}%
- **Volatility (Std Dev)**: {overall['Std Deviation (%)']:.2f}%

---

##  BEST PERFORMING PATTERNS

### Top 3 Patterns by Median Return

"""
        
        # Sort by median return
        top_patterns = comparison_df.sort_values('Median Daily Return (%)', ascending=False).head(3)
        
        for idx, (_, pattern) in enumerate(top_patterns.iterrows(), 1):
            mean_median_gap = pattern['Mean Daily Return (%)'] - pattern['Median Daily Return (%)']
            reliability = " Excellent" if abs(mean_median_gap) < 0.02 else \
                         " Good" if abs(mean_median_gap) < 0.05 else \
                         " Moderate"
            
            report += f"""
### {idx}. {pattern['Pattern']}

- **Median Return**: {pattern['Median Daily Return (%)']:+.3f}%
- **Mean Return**: {pattern['Mean Daily Return (%)']:+.3f}%
- **Win Rate**: {pattern['Win Rate (%)']:.1f}%
- **Sample Size**: {int(pattern['Total Trading Days']):,} days
- **Reliability**: {reliability}

**Mean-Median Gap**: {mean_median_gap:+.3f}% 
{" Small gap = Symmetric, reliable" if abs(mean_median_gap) < 0.05 else " Large gap = Outlier-driven"}

"""
        
        report += f"""
---

##  PATTERN COMPARISON

| Pattern | Median % | Mean % | Win Rate % | Sample Size | Reliability |
|---------|----------|--------|------------|-------------|-------------|
"""
        
        for _, row in comparison_df.iterrows():
            gap = abs(row['Mean Daily Return (%)'] - row['Median Daily Return (%)'])
            reliability = "" if gap < 0.02 else "" if gap < 0.05 else ""
            
            report += f"| {row['Pattern']} | {row['Median Daily Return (%)']:+.3f} | "
            report += f"{row['Mean Daily Return (%)']:+.3f} | {row['Win Rate (%)']:.1f} | "
            report += f"{int(row['Total Trading Days']):,} | {reliability} |\n"
        
        report += f"""

---

##  KEY INSIGHTS

### Reliability Assessment (Mean vs Median)

**Why Median Matters**:
- **Mean** can be skewed by outliers (a few extreme days)
- **Median** represents the "typical" outcome (50th percentile)
- **Small gap** between Mean and Median = Consistent, reliable pattern
- **Large gap** = Pattern depends on occasional big moves

### Pattern Interpretation:
"""
        
        # Analyze each major pattern
        for pattern_name in ['Wednesday', 'Monday', 'April', 'First Monday']:
            pattern_data = comparison_df[comparison_df['Pattern'] == pattern_name]
            if len(pattern_data) > 0:
                pattern = pattern_data.iloc[0]
                gap = pattern['Mean Daily Return (%)'] - pattern['Median Daily Return (%)']
                
                if gap > 0.05:
                    interpretation = "Positive outliers boost average (use median for realistic expectations)"
                elif gap < -0.05:
                    interpretation = "Negative outliers drag down average (be cautious)"
                else:
                    interpretation = "Symmetric distribution (mean and median both reliable)"
                
                report += f"\n**{pattern_name}**: {interpretation}"
        
        report += f"""

---

##  DATA FILES

All findings are backed by raw data files in:
```
{self.analysis_dir}/
 00_Master_Data/ (Enhanced dataset with all flags)
 01_April_Analysis/ (Complete April data)
 02_Wednesday_Analysis/ (Complete Wednesday data)
 03_Weekday_Analysis/ (All weekdays)
 04_MonthEnd_Analysis/ (Month-end periods)
 05_FirstMonday_Analysis/ (First Mondays)
 06_Monthly_Analysis/ (All 12 months)
 07_Comparison_Tables/ (Pattern comparisons)
 08_Visualizations/ (Charts and graphs)
 09_Reports/ (This report)
 10_Statistical_Analysis/ (Technical indicators)
```

---

##  RECOMMENDED ACTIONS

1. **Focus on high-reliability patterns** (small Mean-Median gap)
2. **Use Median for position sizing** (more realistic expectations)
3. **Monitor statistical significance** (larger sample = more confidence)
4. **Combine patterns for confirmation** (e.g., Wednesday + Month-End)
5. **Review raw data** for pattern consistency over time

---

**Generated by**: Universal Stock Analyzer  
**Date**: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}  
**Company**: {self.company_name}
"""
        
        # Save report
        output_file = f"{self.reports_dir}/EXECUTIVE_SUMMARY.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f" Executive summary saved: {output_file}")
        
        return report
    
    def generate_trading_strategies_report(self):
        """Generate trading strategies report"""
        print(f"\n{'='*70}")
        print("GENERATING TRADING STRATEGIES REPORT")
        print(f"{'='*70}\n")
        
        comparison_df = self.load_comparison_data()
        
        # Get top patterns
        top_patterns = comparison_df.sort_values('Median Daily Return (%)', ascending=False).head(5)
        
        report = f"""#  {self.company_name.upper()} - TRADING STRATEGIES

## Pattern-Based Trading Strategies

**Generated**: {datetime.now().strftime('%B %d, %Y')}

This report outlines specific trading strategies based on identified cyclical patterns and statistical analysis.

---

##  STRATEGY OVERVIEW

"""
        
        strategy_num = 1
        for _, pattern in top_patterns.iterrows():
            if pattern['Median Daily Return (%)'] > 0 and pattern['Win Rate (%)'] > 50:
                
                mean_median_gap = pattern['Mean Daily Return (%)'] - pattern['Median Daily Return (%)']
                
                report += f"""
### Strategy {strategy_num}: {pattern['Pattern']} Pattern

**Pattern Characteristics**:
- **Median Return**: {pattern['Median Daily Return (%)']:+.3f}%
- **Mean Return**: {pattern['Mean Daily Return (%)']:+.3f}%
- **Win Rate**: {pattern['Win Rate (%)']:.1f}%
- **Sample Size**: {int(pattern['Total Trading Days']):,} days
- **25th Percentile**: {pattern['25th Percentile (%)']:.2f}% (downside risk)
- **75th Percentile**: {pattern['75th Percentile (%)']:.2f}% (upside target)

**Trading Rules**:

1. **Entry**:
   - Enter position on {pattern['Pattern']}
   - Position size: {"1.5x normal" if mean_median_gap < 0.03 else "1.0-1.3x normal"} (based on reliability)

2. **Profit Target**:
   - Conservative: {pattern['Median Daily Return (%)'] * 1.1:+.3f}% (slightly above median)
   - Aggressive: {pattern['75th Percentile (%)']:.3f}% (75th percentile)

3. **Stop Loss**:
   - Set at {pattern['25th Percentile (%)'] * 1.1:.2f}% (below 25th percentile)

4. **Risk-Reward**:
   - Typical gain: {pattern['Median Daily Return (%)']:.3f}%
   - Typical loss: {pattern['25th Percentile (%)']:.3f}%
   - Win probability: {pattern['Win Rate (%)']:.1f}%

**Pattern Reliability**:
{" **Excellent** - Mean  Median (symmetric distribution)" if abs(mean_median_gap) < 0.03 else
 " **Good** - Moderate Mean-Median gap" if abs(mean_median_gap) < 0.07 else
 " **Moderate** - Large Mean-Median gap (outlier-driven)"}

**When to Avoid**:
- Major news events (earnings, regulatory changes)
- Market-wide panic or euphoria
- When stock is at 52-week high/low (pattern may not hold)

---
"""
                strategy_num += 1
        
        report += f"""
##  STRATEGY PRINCIPLES

### 1. Position Sizing Based on Median
- Use **median** (not mean) for calculating expected returns
- Median represents "typical" outcome, mean can be skewed by outliers

### 2. Risk Management with Percentiles
- **25th Percentile**: If you're in worst 25% of outcomes, exit
- **75th Percentile**: Target for aggressive profit-taking
- **Median (50th)**: Conservative profit target

### 3. Pattern Combination
Combine multiple patterns for higher confidence:
- **Example**: Wednesday + Month-End + Positive trend
- Each additional confirming pattern increases probability

### 4. Mean-Median Gap Analysis
- **Small gap (< 0.03%)**: Reliable, symmetric pattern
- **Large gap (> 0.07%)**: Outlier-driven, use median for planning

---

##  RISK WARNINGS

1. **Past performance  Future results**
   - Patterns can change over time
   - Market regimes shift

2. **Pattern degradation**
   - As more traders discover patterns, they may weaken
   - Monitor pattern consistency quarterly

3. **Sample size matters**
   - Patterns with < 100 observations are less reliable
   - Large samples (> 500) are more trustworthy

4. **External factors**
   - Global events can override patterns
   - Company-specific news takes precedence

---

##  SUPPORTING DATA

All strategies backed by raw data:
- **Pattern raw data**: See `{self.analysis_dir}/` subdirectories
- **Statistical validation**: See `07_Comparison_Tables/pattern_comparison_table.csv`
- **Year-by-year breakdown**: Available in each pattern's `*_yearly_statistics.csv`

---

##  RECOMMENDED USAGE

1. **Backtest before trading**: Verify patterns hold in recent data
2. **Paper trade first**: Test strategies without risking capital
3. **Start small**: Use 0.5x normal position size initially
4. **Track performance**: Log all pattern-based trades
5. **Review quarterly**: Patterns may weaken or strengthen

---

**Disclaimer**: These strategies are based on historical data analysis. No guarantee of future performance. Always use proper risk management and never risk more than you can afford to lose.

---

**Generated by**: Universal Stock Analyzer  
**Date**: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}  
**Company**: {self.company_name}
"""
        
        # Save report
        output_file = f"{self.reports_dir}/TRADING_STRATEGIES.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f" Trading strategies report saved: {output_file}")
        
        return report
    
    def generate_master_index(self):
        """Generate master index for all data files"""
        print(f"\n{'='*70}")
        print("GENERATING MASTER INDEX")
        print(f"{'='*70}\n")
        
        comparison_df = self.load_comparison_data()
        
        report = f"""#  {self.company_name.upper()} - MASTER DATA INDEX

## Complete Analysis Navigation Guide

**Generated**: {datetime.now().strftime('%B %d, %Y')}

This document provides a comprehensive index of all data files and findings with supporting evidence.

---

##  DIRECTORY STRUCTURE

```
{self.analysis_dir}/

 00_Master_Data/
    {self.company_name.replace(' ', '_').lower()}_master_data_enhanced.csv
       (Complete dataset with all pattern flags)

 01_April_Analysis/
    april_all_days_raw_data.csv (All April trading days)
    april_yearly_statistics.csv (Year-by-year April performance)
    april_overall_statistics.csv (Overall April statistics)

 02_Wednesday_Analysis/
    wednesday_all_days_raw_data.csv (All Wednesdays)
    wednesday_yearly_statistics.csv (Year-by-year Wednesday performance)
    wednesday_overall_statistics.csv (Overall Wednesday statistics)

 03_Weekday_Analysis/
    monday_all_days_raw_data.csv
    tuesday_all_days_raw_data.csv
    wednesday_all_days_raw_data.csv
    thursday_all_days_raw_data.csv
    friday_all_days_raw_data.csv
    weekday_comprehensive_statistics.csv

 04_MonthEnd_Analysis/
    monthend_last5days_raw_data.csv (All month-end periods)
    monthend_yearly_statistics.csv
    monthend_overall_statistics.csv

 05_FirstMonday_Analysis/
    first_monday_raw_data.csv (All first Mondays)
    first_monday_statistics.csv

 06_Monthly_Analysis/
    january_all_days_raw_data.csv
    february_all_days_raw_data.csv
    march_all_days_raw_data.csv
    april_all_days_raw_data.csv
    may_all_days_raw_data.csv
    june_all_days_raw_data.csv
    july_all_days_raw_data.csv
    august_all_days_raw_data.csv
    september_all_days_raw_data.csv
    october_all_days_raw_data.csv
    november_all_days_raw_data.csv
    december_all_days_raw_data.csv
    monthly_comprehensive_statistics.csv

 07_Comparison_Tables/
    pattern_comparison_table.csv (All patterns compared)

 08_Visualizations/
    pattern_comparison_charts.png
    cyclical_patterns_charts.png
    technical_indicators_charts.png
    performance_charts.png
    yearly_returns_chart.png

 09_Reports/
    EXECUTIVE_SUMMARY.md (This file)
    TRADING_STRATEGIES.md
    MASTER_INDEX.md

 10_Statistical_Analysis/ (if run)
     moving_averages.csv
     rsi_data.csv
     macd_data.csv
     bollinger_bands.csv
     atr_data.csv
     performance_metrics.csv
     yearly_returns.csv
     risk_metrics.csv
     enhanced_data_with_indicators.csv
```

---

##  FINDING  DATA FILE LOOKUP

### Pattern Analysis Findings

| Finding | Supporting Raw Data | Sample Size |
|---------|-------------------|-------------|
"""
        
        for _, pattern in comparison_df.iterrows():
            pattern_name = pattern['Pattern']
            
            if 'Wednesday' in pattern_name:
                file_path = "02_Wednesday_Analysis/wednesday_all_days_raw_data.csv"
            elif 'Monday' in pattern_name and 'First' not in pattern_name:
                file_path = "03_Weekday_Analysis/monday_all_days_raw_data.csv"
            elif 'First Monday' in pattern_name:
                file_path = "05_FirstMonday_Analysis/first_monday_raw_data.csv"
            elif 'April' in pattern_name:
                file_path = "01_April_Analysis/april_all_days_raw_data.csv"
            elif 'Month-End' in pattern_name:
                file_path = "04_MonthEnd_Analysis/monthend_last5days_raw_data.csv"
            else:
                file_path = "07_Comparison_Tables/pattern_comparison_table.csv"
            
            report += f"| {pattern_name}: Mean={pattern['Mean Daily Return (%)']:+.3f}%, "
            report += f"Median={pattern['Median Daily Return (%)']:+.3f}% | "
            report += f"`{file_path}` | {int(pattern['Total Trading Days']):,} days |\n"
        
        report += f"""

---

##  HOW TO VERIFY ANY FINDING

### Example: Verifying "Wednesday averages +X%"

1. **Open the raw data**:
   ```
   {self.analysis_dir}/02_Wednesday_Analysis/wednesday_all_days_raw_data.csv
   ```

2. **Check the statistics file**:
   ```
   {self.analysis_dir}/02_Wednesday_Analysis/wednesday_overall_statistics.csv
   ```

3. **Review year-by-year consistency**:
   ```
   {self.analysis_dir}/02_Wednesday_Analysis/wednesday_yearly_statistics.csv
   ```

4. **Compare with other patterns**:
   ```
   {self.analysis_dir}/07_Comparison_Tables/pattern_comparison_table.csv
   ```

### Understanding the Statistics Files

Each `*_overall_statistics.csv` contains:
- **Mean Daily Return**: Average return (can be skewed by outliers)
- **Median Daily Return**: Typical return (50th percentile)
- **10th/25th/75th/90th Percentile**: Distribution insights
- **Std Deviation**: Volatility measure
- **Win Rate**: Percentage of positive days
- **Skewness**: Distribution asymmetry
- **Kurtosis**: Tail thickness

---

##  USING THIS INDEX

### For Quick Analysis:
1. Start with `07_Comparison_Tables/pattern_comparison_table.csv`
2. Identify interesting patterns
3. Drill down to pattern-specific folders

### For Deep Dive:
1. Open pattern's raw data file (all daily records)
2. Review yearly statistics (year-by-year consistency)
3. Check overall statistics (comprehensive metrics)
4. Compare with other patterns

### For Validation:
1. Open raw data in Excel/spreadsheet
2. Calculate your own statistics
3. Compare with provided statistics files
4. Verify sample sizes and date ranges

---

##  VISUALIZATION FILES

All charts saved in `08_Visualizations/`:

1. **pattern_comparison_charts.png**
   - Mean vs Median returns
   - Win rates by pattern
   - Volatility comparison
   - Sample size overview

2. **cyclical_patterns_charts.png**
   - Weekday performance
   - Monthly performance
   - Seasonal trends

3. **technical_indicators_charts.png** (if statistical analysis run)
   - Moving averages
   - RSI
   - MACD
   - Bollinger Bands

4. **performance_charts.png**
   - Cumulative returns
   - Drawdown analysis
   - Price chart
   - Volume trends

5. **yearly_returns_chart.png**
   - Year-by-year returns
   - Performance consistency

---

##  KEY INSIGHTS

### Mean vs Median Analysis
"""
        
        for _, pattern in comparison_df.head(5).iterrows():
            gap = pattern['Mean Daily Return (%)'] - pattern['Median Daily Return (%)']
            
            report += f"\n**{pattern['Pattern']}**:\n"
            report += f"- Mean: {pattern['Mean Daily Return (%)']:+.3f}%\n"
            report += f"- Median: {pattern['Median Daily Return (%)']:+.3f}%\n"
            report += f"- Gap: {gap:+.3f}%\n"
            
            if abs(gap) < 0.03:
                report += f"- **Interpretation**: Symmetric, reliable (mean  median)\n"
            elif gap > 0:
                report += f"- **Interpretation**: Right-skewed (positive outliers boost mean)\n"
            else:
                report += f"- **Interpretation**: Left-skewed (negative outliers drag mean down)\n"
        
        report += f"""

---

**Generated by**: Universal Stock Analyzer  
**Date**: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}  
**Company**: {self.company_name}
"""
        
        # Save report
        output_file = f"{self.reports_dir}/MASTER_INDEX.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f" Master index saved: {output_file}")
        
        return report
    
    def run_all_reports(self):
        """Generate all reports"""
        print(f"\n{'='*70}")
        print(f"UNIVERSAL REPORT GENERATOR")
        print(f"{'='*70}")
        print(f"Company: {self.company_name}")
        print(f"Analysis Directory: {self.analysis_dir}")
        print(f"{'='*70}\n")
        
        try:
            self.generate_executive_summary()
            self.generate_trading_strategies_report()
            self.generate_master_index()
            
            print(f"\n{'='*70}")
            print(f" ALL REPORTS GENERATED!")
            print(f"{'='*70}")
            print(f"\nOutput directory: {self.reports_dir}/")
            print(f"\nGenerated reports:")
            print(f"   EXECUTIVE_SUMMARY.md (Key findings and performance)")
            print(f"   TRADING_STRATEGIES.md (Pattern-based strategies)")
            print(f"   MASTER_INDEX.md (Complete data file navigation)")
            print(f"{'='*70}\n")
            
            return True
            
        except Exception as e:
            print(f"\n ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Universal Report Generator - Creates comprehensive markdown reports',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python universal_report_generator.py --analysis_dir "Infosys_Analysis_Complete" --company "Infosys"
  python universal_report_generator.py --analysis_dir "TCS_Analysis_Complete" --company "TCS"
        """
    )
    
    parser.add_argument('--analysis_dir', '-d', required=True,
                       help='Path to analysis directory')
    parser.add_argument('--company', '-c', required=True,
                       help='Company name for reports')
    
    args = parser.parse_args()
    
    # Validate directory exists
    if not os.path.exists(args.analysis_dir):
        print(f" ERROR: Directory not found: {args.analysis_dir}")
        sys.exit(1)
    
    # Run report generation
    generator = UniversalReportGenerator(args.analysis_dir, args.company)
    success = generator.run_all_reports()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

