"""
Fundamental Metrics Analyzer
Analyzes: Market Cap, Trading Activity, Valuation (P/BV), Liquidity
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

class FundamentalMetricsAnalyzer:
    def __init__(self, data_file, company_name, output_base_dir):
        """
        Initialize with enhanced data including fundamental metrics
        Expected columns: Date, Open, High, Low, Close, Volume, MCAP, NO_TRADES, PRICE_BV, VALUE
        """
        self.company_name = company_name
        self.data_file = data_file
        self.output_base_dir = output_base_dir
        
        # Create output directory
        self.output_dir = os.path.join(output_base_dir, "15_Fundamental_Metrics")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load data
        self.df = pd.read_csv(data_file)
        
        # Verify required columns
        required = ['Date', 'Close', 'Volume']
        optional = ['MCAP', 'NO_TRADES', 'PRICE_BV', 'VALUE']
        
        for col in required:
            if col not in self.df.columns:
                raise ValueError(f"Required column '{col}' not found")
        
        # Check which fundamental columns are available
        self.has_mcap = 'MCAP' in self.df.columns
        self.has_trades = 'NO_TRADES' in self.df.columns
        self.has_pbv = 'PRICE_BV' in self.df.columns
        self.has_value = 'VALUE' in self.df.columns
        
        # Convert date and sort
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df = self.df.sort_values('Date').reset_index(drop=True)
        
        # Add time-based features
        self.df['Year'] = self.df['Date'].dt.year
        self.df['Month'] = self.df['Date'].dt.month
        self.df['Quarter'] = self.df['Date'].dt.quarter
        
        print(f"\n Loaded {len(self.df)} rows")
        print(f"  Date Range: {self.df['Date'].min().date()} to {self.df['Date'].max().date()}")
        print(f"\n Available Fundamental Metrics:")
        print(f"  - Market Cap (MCAP): {'' if self.has_mcap else ''}")
        print(f"  - Number of Trades: {'' if self.has_trades else ''}")
        print(f"  - Price to Book Value: {'' if self.has_pbv else ''}")
        print(f"  - Total Value Traded: {'' if self.has_value else ''}")
    
    def analyze_market_cap(self):
        """Analyze market capitalization trends and growth"""
        if not self.has_mcap:
            print("\n  Market Cap data not available, skipping MCAP analysis")
            return
        
        print("\n" + "="*70)
        print("MARKET CAPITALIZATION ANALYSIS")
        print("="*70)
        
        # Remove NaN values
        mcap_data = self.df[self.df['MCAP'].notna()].copy()
        
        if len(mcap_data) == 0:
            print("  No valid MCAP data found")
            return
        
        # Calculate MCAP growth
        mcap_data['MCAP_Change'] = mcap_data['MCAP'].pct_change() * 100
        
        # Overall statistics
        stats = {
            'Metric': [
                'Current Market Cap',
                'Highest Market Cap',
                'Lowest Market Cap',
                'Average Market Cap',
                'MCAP Growth (Total %)',
                'CAGR (%)',
                'Volatility (Std Dev)',
                'Days with MCAP Data'
            ],
            'Value': [
                f"{mcap_data['MCAP'].iloc[-1]:,.2f}",
                f"{mcap_data['MCAP'].max():,.2f}",
                f"{mcap_data['MCAP'].min():,.2f}",
                f"{mcap_data['MCAP'].mean():,.2f}",
                f"{((mcap_data['MCAP'].iloc[-1] / mcap_data['MCAP'].iloc[0] - 1) * 100):.2f}%",
                f"{(((mcap_data['MCAP'].iloc[-1] / mcap_data['MCAP'].iloc[0]) ** (1/(len(mcap_data)/252)) - 1) * 100):.2f}%",
                f"{mcap_data['MCAP'].std():,.2f}",
                f"{len(mcap_data):,}"
            ]
        }
        
        stats_df = pd.DataFrame(stats)
        stats_file = os.path.join(self.output_dir, "market_cap_statistics.csv")
        stats_df.to_csv(stats_file, index=False)
        
        print(f"\n Overall Statistics:")
        for _, row in stats_df.iterrows():
            print(f"  {row['Metric']:.<45} {row['Value']:>20}")
        
        # Yearly MCAP analysis
        yearly = mcap_data.groupby('Year').agg({
            'MCAP': ['first', 'last', 'mean', 'max', 'min']
        }).round(2)
        
        yearly.columns = ['_'.join(col) for col in yearly.columns]
        yearly['Growth_%'] = ((yearly['MCAP_last'] - yearly['MCAP_first']) / yearly['MCAP_first'] * 100).round(2)
        
        yearly_file = os.path.join(self.output_dir, "market_cap_yearly.csv")
        yearly.to_csv(yearly_file)
        
        print(f"\n Yearly Market Cap Growth:")
        for year, row in yearly.tail(10).iterrows():
            print(f"  {year}: {row['MCAP_first']:>12,.0f}  {row['MCAP_last']:>12,.0f} ({row['Growth_%']:>+7.2f}%)")
        
        # Quarterly trends (recent 12 quarters)
        quarterly = mcap_data.groupby(['Year', 'Quarter']).agg({
            'MCAP': ['first', 'last', 'mean']
        }).round(2)
        
        quarterly.columns = ['_'.join(col) for col in quarterly.columns]
        quarterly['Growth_%'] = ((quarterly['MCAP_last'] - quarterly['MCAP_first']) / quarterly['MCAP_first'] * 100).round(2)
        
        quarterly_file = os.path.join(self.output_dir, "market_cap_quarterly.csv")
        quarterly.to_csv(quarterly_file)
        
        print(f"\n Recent Quarterly MCAP Trends:")
        for (year, qtr), row in quarterly.tail(12).iterrows():
            print(f"  {year} Q{qtr}: Avg={row['MCAP_mean']:>12,.0f}, Growth={row['Growth_%']:>+7.2f}%")
        
        print(f"\n Saved market cap analysis to {self.output_dir}/")
    
    def analyze_liquidity(self):
        """Analyze trading liquidity: Volume, Number of Trades, Value Traded"""
        print("\n" + "="*70)
        print("LIQUIDITY & TRADING ACTIVITY ANALYSIS")
        print("="*70)
        
        # Volume analysis (always available)
        vol_data = self.df[self.df['Volume'].notna()].copy()
        
        stats = []
        
        # Volume statistics
        stats.append({
            'Metric': 'Average Daily Volume',
            'Value': f"{vol_data['Volume'].mean():,.0f}"
        })
        stats.append({
            'Metric': 'Median Daily Volume',
            'Value': f"{vol_data['Volume'].median():,.0f}"
        })
        stats.append({
            'Metric': 'Max Daily Volume',
            'Value': f"{vol_data['Volume'].max():,.0f}"
        })
        stats.append({
            'Metric': 'Volume Std Dev',
            'Value': f"{vol_data['Volume'].std():,.0f}"
        })
        
        # Number of trades analysis
        if self.has_trades:
            trades_data = self.df[self.df['NO_TRADES'].notna()].copy()
            if len(trades_data) > 0:
                stats.append({'Metric': '---', 'Value': '---'})
                stats.append({
                    'Metric': 'Average Trades/Day',
                    'Value': f"{trades_data['NO_TRADES'].mean():,.0f}"
                })
                stats.append({
                    'Metric': 'Median Trades/Day',
                    'Value': f"{trades_data['NO_TRADES'].median():,.0f}"
                })
                stats.append({
                    'Metric': 'Max Trades/Day',
                    'Value': f"{trades_data['NO_TRADES'].max():,.0f}"
                })
                
                # Avg volume per trade
                trades_data['Vol_Per_Trade'] = trades_data['Volume'] / trades_data['NO_TRADES']
                stats.append({
                    'Metric': 'Avg Volume per Trade',
                    'Value': f"{trades_data['Vol_Per_Trade'].mean():,.0f}"
                })
        
        # Value traded analysis
        if self.has_value:
            value_data = self.df[self.df['VALUE'].notna()].copy()
            if len(value_data) > 0:
                stats.append({'Metric': '---', 'Value': '---'})
                stats.append({
                    'Metric': 'Avg Daily Value Traded',
                    'Value': f"{value_data['VALUE'].mean():,.0f}"
                })
                stats.append({
                    'Metric': 'Median Daily Value',
                    'Value': f"{value_data['VALUE'].median():,.0f}"
                })
                stats.append({
                    'Metric': 'Max Daily Value',
                    'Value': f"{value_data['VALUE'].max():,.0f}"
                })
                stats.append({
                    'Metric': 'Total Value Traded',
                    'Value': f"{value_data['VALUE'].sum():,.0f}"
                })
        
        stats_df = pd.DataFrame(stats)
        stats_file = os.path.join(self.output_dir, "liquidity_statistics.csv")
        stats_df.to_csv(stats_file, index=False)
        
        print(f"\n Liquidity Statistics:")
        for _, row in stats_df.iterrows():
            print(f"  {row['Metric']:.<45} {row['Value']:>20}")
        
        # Yearly liquidity trends
        yearly_agg = {'Volume': ['mean', 'sum']}
        if self.has_trades:
            yearly_agg['NO_TRADES'] = ['mean', 'sum']
        if self.has_value:
            yearly_agg['VALUE'] = ['mean', 'sum']
        
        yearly = self.df.groupby('Year').agg(yearly_agg).round(0)
        yearly.columns = ['_'.join(col) for col in yearly.columns]
        
        yearly_file = os.path.join(self.output_dir, "liquidity_yearly.csv")
        yearly.to_csv(yearly_file)
        
        print(f"\n Recent Yearly Trends:")
        for year, row in yearly.tail(10).iterrows():
            print(f"  {year}: Avg Vol={row['Volume_mean']:>12,.0f}, Total Vol={row['Volume_sum']:>15,.0f}")
        
        print(f"\n Saved liquidity analysis to {self.output_dir}/")
    
    def analyze_valuation(self):
        """Analyze Price to Book Value trends"""
        if not self.has_pbv:
            print("\n  Price/Book Value data not available, skipping P/BV analysis")
            return
        
        print("\n" + "="*70)
        print("VALUATION ANALYSIS (PRICE TO BOOK VALUE)")
        print("="*70)
        
        pbv_data = self.df[self.df['PRICE_BV'].notna()].copy()
        
        if len(pbv_data) == 0:
            print("  No valid P/BV data found")
            return
        
        # Overall statistics
        stats = {
            'Metric': [
                'Current P/BV',
                'Average P/BV',
                'Median P/BV',
                'Highest P/BV',
                'Lowest P/BV',
                'Std Deviation',
                'Days with P/BV Data'
            ],
            'Value': [
                f"{pbv_data['PRICE_BV'].iloc[-1]:.2f}",
                f"{pbv_data['PRICE_BV'].mean():.2f}",
                f"{pbv_data['PRICE_BV'].median():.2f}",
                f"{pbv_data['PRICE_BV'].max():.2f}",
                f"{pbv_data['PRICE_BV'].min():.2f}",
                f"{pbv_data['PRICE_BV'].std():.2f}",
                f"{len(pbv_data):,}"
            ]
        }
        
        stats_df = pd.DataFrame(stats)
        stats_file = os.path.join(self.output_dir, "valuation_statistics.csv")
        stats_df.to_csv(stats_file, index=False)
        
        print(f"\n Valuation Statistics:")
        for _, row in stats_df.iterrows():
            print(f"  {row['Metric']:.<45} {row['Value']:>20}")
        
        # Yearly P/BV trends
        yearly = pbv_data.groupby('Year').agg({
            'PRICE_BV': ['mean', 'min', 'max', 'first', 'last']
        }).round(2)
        
        yearly.columns = ['_'.join(col) for col in yearly.columns]
        yearly['Change_%'] = ((yearly['PRICE_BV_last'] - yearly['PRICE_BV_first']) / yearly['PRICE_BV_first'] * 100).round(2)
        
        yearly_file = os.path.join(self.output_dir, "valuation_yearly.csv")
        yearly.to_csv(yearly_file)
        
        print(f"\n Yearly P/BV Trends:")
        for year, row in yearly.tail(10).iterrows():
            print(f"  {year}: Avg={row['PRICE_BV_mean']:>6.2f}, Min={row['PRICE_BV_min']:>6.2f}, Max={row['PRICE_BV_max']:>6.2f}")
        
        # Valuation zones (percentile-based)
        p25 = pbv_data['PRICE_BV'].quantile(0.25)
        p50 = pbv_data['PRICE_BV'].quantile(0.50)
        p75 = pbv_data['PRICE_BV'].quantile(0.75)
        current = pbv_data['PRICE_BV'].iloc[-1]
        
        zones = pd.DataFrame({
            'Zone': ['Undervalued (Below 25%)', 'Fair Value (25-75%)', 'Overvalued (Above 75%)'],
            'P/BV Range': [f"< {p25:.2f}", f"{p25:.2f} - {p75:.2f}", f"> {p75:.2f}"],
            'Percentile': ['0-25%', '25-75%', '75-100%']
        })
        
        zones_file = os.path.join(self.output_dir, "valuation_zones.csv")
        zones.to_csv(zones_file, index=False)
        
        print(f"\n Valuation Zones (based on historical percentiles):")
        for _, row in zones.iterrows():
            print(f"  {row['Zone']:.<35} {row['P/BV Range']:>15}")
        
        if current < p25:
            status = "UNDERVALUED"
        elif current > p75:
            status = "OVERVALUED"
        else:
            status = "FAIR VALUE"
        
        print(f"\n  Current Status: {status} (P/BV = {current:.2f})")
        
        print(f"\n Saved valuation analysis to {self.output_dir}/")
    
    def generate_comprehensive_report(self):
        """Generate a comprehensive fundamental analysis report"""
        print("\n" + "="*70)
        print("GENERATING COMPREHENSIVE FUNDAMENTAL REPORT")
        print("="*70)
        
        report_file = os.path.join(self.output_dir, "FUNDAMENTAL_ANALYSIS_SUMMARY.md")
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(f"# Fundamental Analysis Report\n\n")
            f.write(f"**Company:** {self.company_name}\n\n")
            f.write(f"**Analysis Date:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Data Range:** {self.df['Date'].min().date()} to {self.df['Date'].max().date()}\n\n")
            f.write(f"**Total Trading Days:** {len(self.df):,}\n\n")
            f.write(f"---\n\n")
            
            # Market Cap Summary
            if self.has_mcap:
                f.write(f"##  Market Capitalization\n\n")
                mcap_stats = pd.read_csv(os.path.join(self.output_dir, "market_cap_statistics.csv"))
                f.write(f"| Metric | Value |\n")
                f.write(f"|--------|-------|\n")
                for _, row in mcap_stats.iterrows():
                    f.write(f"| {row['Metric']} | {row['Value']} |\n")
                f.write(f"\n")
            
            # Liquidity Summary
            f.write(f"##  Liquidity & Trading Activity\n\n")
            liq_stats = pd.read_csv(os.path.join(self.output_dir, "liquidity_statistics.csv"))
            f.write(f"| Metric | Value |\n")
            f.write(f"|--------|-------|\n")
            for _, row in liq_stats.iterrows():
                if row['Metric'] != '---':
                    f.write(f"| {row['Metric']} | {row['Value']} |\n")
            f.write(f"\n")
            
            # Valuation Summary
            if self.has_pbv:
                f.write(f"##  Valuation (Price to Book Value)\n\n")
                val_stats = pd.read_csv(os.path.join(self.output_dir, "valuation_statistics.csv"))
                f.write(f"| Metric | Value |\n")
                f.write(f"|--------|-------|\n")
                for _, row in val_stats.iterrows():
                    f.write(f"| {row['Metric']} | {row['Value']} |\n")
                f.write(f"\n")
            
            f.write(f"---\n\n")
            f.write(f"*Generated by Universal Stock Analyzer - Fundamental Metrics Module*\n")
        
        print(f"\n Comprehensive report saved: {report_file}")
    
    def run_all_analyses(self):
        """Run all fundamental analyses"""
        print("\n" + "="*70)
        print("FUNDAMENTAL METRICS ANALYZER")
        print("="*70)
        print(f"Company: {self.company_name}")
        print(f"Input File: {self.data_file}")
        print("="*70)
        
        # Run analyses
        self.analyze_market_cap()
        self.analyze_liquidity()
        self.analyze_valuation()
        self.generate_comprehensive_report()
        
        print("\n" + "="*70)
        print(" FUNDAMENTAL ANALYSIS COMPLETE!")
        print("="*70)
        print(f"Output directory: {self.output_dir}/")
        print("\nGenerated files:")
        print("   Market cap statistics & trends")
        print("   Liquidity & trading activity analysis")
        print("   Valuation (P/BV) analysis")
        print("   Comprehensive fundamental report")
        print("="*70 + "\n")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze fundamental metrics from stock data')
    parser.add_argument('--file', required=True, help='CSV file with stock data')
    parser.add_argument('--company', required=True, help='Company name')
    parser.add_argument('--output', default='.', help='Output base directory')
    
    args = parser.parse_args()
    
    analyzer = FundamentalMetricsAnalyzer(args.file, args.company, args.output)
    analyzer.run_all_analyses()

