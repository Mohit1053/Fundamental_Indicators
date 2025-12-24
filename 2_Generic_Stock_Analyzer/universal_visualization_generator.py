"""
Universal Stock Visualization Generator
========================================
Creates comprehensive visualizations for ANY stock analysis.

Generates:
- Cyclical pattern charts (weekday, monthly)
- Technical indicator charts (MA, RSI, MACD, Bollinger)
- Performance charts (returns, drawdown, yearly performance)

Usage:
    python universal_visualization_generator.py --analysis_dir "Company_Analysis_Complete" --company "Company Name"
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os
import sys
from datetime import datetime

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class UniversalVisualizationGenerator:
    """Create visualizations for stock analysis"""
    
    def __init__(self, analysis_dir, company_name):
        self.analysis_dir = analysis_dir
        self.company_name = company_name
        self.viz_dir = f"{analysis_dir}/08_Visualizations"
        
        # Create output directory
        os.makedirs(self.viz_dir, exist_ok=True)
        
    def load_comparison_data(self):
        """Load pattern comparison table"""
        comparison_file = f"{self.analysis_dir}/07_Comparison_Tables/pattern_comparison_table.csv"
        return pd.read_csv(comparison_file)
    
    def create_pattern_comparison_chart(self):
        """Create pattern comparison visualization"""
        print(f"\n{'='*70}")
        print("CREATING PATTERN COMPARISON CHARTS")
        print(f"{'='*70}\n")
        
        df = self.load_comparison_data()
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle(f'{self.company_name} - Pattern Analysis Overview', 
                    fontsize=16, fontweight='bold')
        
        # 1. Mean vs Median Returns
        ax1 = axes[0, 0]
        x = np.arange(len(df))
        width = 0.35
        
        ax1.bar(x - width/2, df['Mean Daily Return (%)'], width, label='Mean', alpha=0.8)
        ax1.bar(x + width/2, df['Median Daily Return (%)'], width, label='Median', alpha=0.8)
        ax1.set_xlabel('Pattern')
        ax1.set_ylabel('Daily Return (%)')
        ax1.set_title('Mean vs Median Returns by Pattern')
        ax1.set_xticks(x)
        ax1.set_xticklabels(df['Pattern'], rotation=45, ha='right')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        
        # 2. Win Rate Comparison
        ax2 = axes[0, 1]
        colors = ['green' if x > 50 else 'red' for x in df['Win Rate (%)']]
        ax2.barh(df['Pattern'], df['Win Rate (%)'], color=colors, alpha=0.7)
        ax2.set_xlabel('Win Rate (%)')
        ax2.set_title('Win Rate by Pattern')
        ax2.axvline(x=50, color='black', linestyle='--', linewidth=1, label='50% baseline')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # 3. Volatility (Std Deviation)
        ax3 = axes[1, 0]
        ax3.bar(df['Pattern'], df['Std Deviation (%)'], color='orange', alpha=0.7)
        ax3.set_xlabel('Pattern')
        ax3.set_ylabel('Standard Deviation (%)')
        ax3.set_title('Volatility by Pattern')
        ax3.set_xticklabels(df['Pattern'], rotation=45, ha='right')
        ax3.grid(True, alpha=0.3)
        
        # 4. Sample Size
        ax4 = axes[1, 1]
        ax4.bar(df['Pattern'], df['Total Trading Days'], color='purple', alpha=0.7)
        ax4.set_xlabel('Pattern')
        ax4.set_ylabel('Number of Observations')
        ax4.set_title('Sample Size by Pattern')
        ax4.set_xticklabels(df['Pattern'], rotation=45, ha='right')
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        output_file = f"{self.viz_dir}/pattern_comparison_charts.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f" Pattern comparison charts saved: {output_file}")
        
    def create_weekday_monthly_charts(self):
        """Create weekday and monthly pattern charts"""
        print(f"\n{'='*70}")
        print("CREATING WEEKDAY AND MONTHLY CHARTS")
        print(f"{'='*70}\n")
        
        # Load data
        weekday_file = f"{self.analysis_dir}/03_Weekday_Analysis/weekday_comprehensive_statistics.csv"
        monthly_file = f"{self.analysis_dir}/06_Monthly_Analysis/monthly_comprehensive_statistics.csv"
        
        weekday_df = pd.read_csv(weekday_file)
        monthly_df = pd.read_csv(monthly_file)
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle(f'{self.company_name} - Cyclical Patterns Analysis', 
                    fontsize=16, fontweight='bold')
        
        # 1. Weekday Returns
        ax1 = axes[0, 0]
        x = np.arange(len(weekday_df))
        width = 0.35
        
        ax1.bar(x - width/2, weekday_df['Mean Daily Return (%)'], width, 
               label='Mean', alpha=0.8, color='steelblue')
        ax1.bar(x + width/2, weekday_df['Median Daily Return (%)'], width,
               label='Median', alpha=0.8, color='coral')
        ax1.set_xlabel('Weekday')
        ax1.set_ylabel('Daily Return (%)')
        ax1.set_title('Average Returns by Weekday')
        ax1.set_xticks(x)
        ax1.set_xticklabels(weekday_df['Weekday'], rotation=45, ha='right')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        
        # 2. Weekday Win Rates
        ax2 = axes[0, 1]
        colors = ['green' if x > 50 else 'red' for x in weekday_df['Win Rate (%)']]
        ax2.bar(weekday_df['Weekday'], weekday_df['Win Rate (%)'], 
               color=colors, alpha=0.7)
        ax2.set_xlabel('Weekday')
        ax2.set_ylabel('Win Rate (%)')
        ax2.set_title('Win Rate by Weekday')
        ax2.set_xticklabels(weekday_df['Weekday'], rotation=45, ha='right')
        ax2.axhline(y=50, color='black', linestyle='--', linewidth=1)
        ax2.grid(True, alpha=0.3)
        
        # 3. Monthly Returns
        ax3 = axes[1, 0]
        x = np.arange(len(monthly_df))
        width = 0.35
        
        ax3.bar(x - width/2, monthly_df['Mean Daily Return (%)'], width,
               label='Mean', alpha=0.8, color='steelblue')
        ax3.bar(x + width/2, monthly_df['Median Daily Return (%)'], width,
               label='Median', alpha=0.8, color='coral')
        ax3.set_xlabel('Month')
        ax3.set_ylabel('Daily Return (%)')
        ax3.set_title('Average Returns by Month')
        ax3.set_xticks(x)
        ax3.set_xticklabels([m[:3] for m in monthly_df['Month']], rotation=45, ha='right')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        
        # 4. Monthly Win Rates
        ax4 = axes[1, 1]
        colors = ['green' if x > 50 else 'red' for x in monthly_df['Win Rate (%)']]
        ax4.bar([m[:3] for m in monthly_df['Month']], monthly_df['Win Rate (%)'],
               color=colors, alpha=0.7)
        ax4.set_xlabel('Month')
        ax4.set_ylabel('Win Rate (%)')
        ax4.set_title('Win Rate by Month')
        ax4.set_xticklabels([m[:3] for m in monthly_df['Month']], rotation=45, ha='right')
        ax4.axhline(y=50, color='black', linestyle='--', linewidth=1)
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        output_file = f"{self.viz_dir}/cyclical_patterns_charts.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f" Cyclical patterns charts saved: {output_file}")
    
    def create_technical_indicator_charts(self):
        """Create technical indicator visualizations"""
        print(f"\n{'='*70}")
        print("CREATING TECHNICAL INDICATOR CHARTS")
        print(f"{'='*70}\n")
        
        # Check if statistical analysis exists
        stats_dir = f"{self.analysis_dir}/10_Statistical_Analysis"
        if not os.path.exists(stats_dir):
            print(" Statistical analysis not found. Run universal_statistical_analyzer.py first.")
            return
        
        # Load enhanced data
        enhanced_file = f"{stats_dir}/enhanced_data_with_indicators.csv"
        if not os.path.exists(enhanced_file):
            print(" Enhanced data file not found.")
            return
        
        df = pd.read_csv(enhanced_file)
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Use last 500 days for visibility
        df_recent = df.tail(500)
        
        fig, axes = plt.subplots(4, 1, figsize=(16, 16))
        fig.suptitle(f'{self.company_name} - Technical Indicators (Last 500 Days)', 
                    fontsize=16, fontweight='bold')
        
        # 1. Price with Moving Averages
        ax1 = axes[0]
        ax1.plot(df_recent['Date'], df_recent['Close'], label='Close Price', linewidth=2)
        if 'MA_20' in df_recent.columns:
            ax1.plot(df_recent['Date'], df_recent['MA_20'], label='MA 20', alpha=0.7)
        if 'MA_50' in df_recent.columns:
            ax1.plot(df_recent['Date'], df_recent['MA_50'], label='MA 50', alpha=0.7)
        if 'MA_200' in df_recent.columns:
            ax1.plot(df_recent['Date'], df_recent['MA_200'], label='MA 200', alpha=0.7)
        ax1.set_ylabel('Price')
        ax1.set_title('Price with Moving Averages')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. RSI
        ax2 = axes[1]
        if 'RSI' in df_recent.columns:
            ax2.plot(df_recent['Date'], df_recent['RSI'], label='RSI', color='purple', linewidth=2)
            ax2.axhline(y=70, color='red', linestyle='--', label='Overbought (70)', alpha=0.7)
            ax2.axhline(y=30, color='green', linestyle='--', label='Oversold (30)', alpha=0.7)
            ax2.axhline(y=50, color='gray', linestyle='-', alpha=0.3)
            ax2.set_ylabel('RSI')
            ax2.set_title('Relative Strength Index (RSI)')
            ax2.legend()
            ax2.grid(True, alpha=0.3)
            ax2.set_ylim([0, 100])
        
        # 3. MACD
        ax3 = axes[2]
        if 'MACD' in df_recent.columns:
            ax3.plot(df_recent['Date'], df_recent['MACD'], label='MACD', linewidth=2)
            ax3.plot(df_recent['Date'], df_recent['MACD_Signal'], label='Signal', linewidth=2)
            ax3.bar(df_recent['Date'], df_recent['MACD_Histogram'], label='Histogram', alpha=0.3)
            ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
            ax3.set_ylabel('MACD')
            ax3.set_title('MACD Indicator')
            ax3.legend()
            ax3.grid(True, alpha=0.3)
        
        # 4. Bollinger Bands
        ax4 = axes[3]
        if all(col in df_recent.columns for col in ['BB_Upper', 'BB_Middle', 'BB_Lower']):
            ax4.plot(df_recent['Date'], df_recent['Close'], label='Close Price', linewidth=2, color='blue')
            ax4.plot(df_recent['Date'], df_recent['BB_Upper'], label='Upper Band', 
                    linestyle='--', color='red', alpha=0.7)
            ax4.plot(df_recent['Date'], df_recent['BB_Middle'], label='Middle Band',
                    linestyle='--', color='gray', alpha=0.7)
            ax4.plot(df_recent['Date'], df_recent['BB_Lower'], label='Lower Band',
                    linestyle='--', color='green', alpha=0.7)
            ax4.fill_between(df_recent['Date'], df_recent['BB_Upper'], df_recent['BB_Lower'],
                           alpha=0.1, color='gray')
            ax4.set_ylabel('Price')
            ax4.set_title('Bollinger Bands')
            ax4.legend()
            ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        output_file = f"{self.viz_dir}/technical_indicators_charts.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f" Technical indicator charts saved: {output_file}")
    
    def create_performance_charts(self):
        """Create performance visualization charts"""
        print(f"\n{'='*70}")
        print("CREATING PERFORMANCE CHARTS")
        print(f"{'='*70}\n")
        
        # Load master data
        master_files = [f for f in os.listdir(f"{self.analysis_dir}/00_Master_Data") 
                       if f.endswith('_master_data_enhanced.csv')]
        
        if not master_files:
            print(" Master data file not found.")
            return
        
        df = pd.read_csv(f"{self.analysis_dir}/00_Master_Data/{master_files[0]}")
        df['Date'] = pd.to_datetime(df['Date'])
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle(f'{self.company_name} - Performance Analysis', 
                    fontsize=16, fontweight='bold')
        
        # 1. Cumulative Returns
        ax1 = axes[0, 0]
        df['Cumulative_Return'] = (1 + df['Daily_Return']/100).cumprod() - 1
        ax1.plot(df['Date'], df['Cumulative_Return'] * 100, linewidth=2, color='steelblue')
        ax1.set_ylabel('Cumulative Return (%)')
        ax1.set_title('Cumulative Returns Over Time')
        ax1.grid(True, alpha=0.3)
        ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        
        # 2. Drawdown
        ax2 = axes[0, 1]
        cumulative = (1 + df['Daily_Return']/100).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max * 100
        ax2.fill_between(df['Date'], drawdown, 0, alpha=0.7, color='red')
        ax2.set_ylabel('Drawdown (%)')
        ax2.set_title('Drawdown Over Time')
        ax2.grid(True, alpha=0.3)
        
        # 3. Price Chart
        ax3 = axes[1, 0]
        ax3.plot(df['Date'], df['Close'], linewidth=1.5, color='darkgreen')
        ax3.set_ylabel('Price')
        ax3.set_title('Stock Price Over Time')
        ax3.grid(True, alpha=0.3)
        
        # 4. Volume
        ax4 = axes[1, 1]
        if 'Volume' in df.columns:
            ax4.bar(df['Date'], df['Volume'], alpha=0.5, color='purple')
            ax4.set_ylabel('Volume')
            ax4.set_title('Trading Volume Over Time')
            ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        output_file = f"{self.viz_dir}/performance_charts.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f" Performance charts saved: {output_file}")
    
    def create_yearly_performance_chart(self):
        """Create yearly performance bar chart"""
        print(f"\n{'='*70}")
        print("CREATING YEARLY PERFORMANCE CHART")
        print(f"{'='*70}\n")
        
        # Check if yearly returns exist
        stats_dir = f"{self.analysis_dir}/10_Statistical_Analysis"
        yearly_file = f"{stats_dir}/yearly_returns.csv"
        
        if not os.path.exists(yearly_file):
            print(" Yearly returns file not found.")
            return
        
        df = pd.read_csv(yearly_file)
        
        fig, ax = plt.subplots(figsize=(14, 6))
        
        colors = ['green' if x > 0 else 'red' for x in df['Return (%)']]
        ax.bar(df['Year'], df['Return (%)'], color=colors, alpha=0.7)
        ax.set_xlabel('Year')
        ax.set_ylabel('Annual Return (%)')
        ax.set_title(f'{self.company_name} - Yearly Returns')
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax.grid(True, alpha=0.3)
        
        # Rotate x-axis labels
        plt.xticks(rotation=45, ha='right')
        
        plt.tight_layout()
        
        output_file = f"{self.viz_dir}/yearly_returns_chart.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f" Yearly returns chart saved: {output_file}")
    
    def run_all_visualizations(self):
        """Generate all visualizations"""
        print(f"\n{'='*70}")
        print(f"UNIVERSAL VISUALIZATION GENERATOR")
        print(f"{'='*70}")
        print(f"Company: {self.company_name}")
        print(f"Analysis Directory: {self.analysis_dir}")
        print(f"{'='*70}\n")
        
        try:
            self.create_pattern_comparison_chart()
            self.create_weekday_monthly_charts()
            self.create_technical_indicator_charts()
            self.create_performance_charts()
            self.create_yearly_performance_chart()
            
            print(f"\n{'='*70}")
            print(f" ALL VISUALIZATIONS COMPLETE!")
            print(f"{'='*70}")
            print(f"\nOutput directory: {self.viz_dir}/")
            print(f"\nGenerated charts:")
            print(f"   Pattern comparison charts")
            print(f"   Cyclical patterns (weekday/monthly)")
            print(f"   Technical indicators (MA, RSI, MACD, Bollinger)")
            print(f"   Performance charts (returns, drawdown, volume)")
            print(f"   Yearly returns chart")
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
        description='Universal Visualization Generator - Creates charts for any stock analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python universal_visualization_generator.py --analysis_dir "Infosys_Analysis_Complete" --company "Infosys"
  python universal_visualization_generator.py --analysis_dir "TCS_Analysis_Complete" --company "TCS"
        """
    )
    
    parser.add_argument('--analysis_dir', '-d', required=True,
                       help='Path to analysis directory (e.g., Company_Analysis_Complete)')
    parser.add_argument('--company', '-c', required=True,
                       help='Company name for chart titles')
    
    args = parser.parse_args()
    
    # Validate directory exists
    if not os.path.exists(args.analysis_dir):
        print(f" ERROR: Directory not found: {args.analysis_dir}")
        sys.exit(1)
    
    # Run visualization
    generator = UniversalVisualizationGenerator(args.analysis_dir, args.company)
    success = generator.run_all_visualizations()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

