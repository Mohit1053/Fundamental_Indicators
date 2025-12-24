"""
Universal Stock Pattern Analyzer
=================================
Analyzes cyclical patterns for ANY stock CSV file.

Input CSV Requirements:
- Columns: Date, Open, High, Low, Close, Volume (minimum)
- Date format: YYYY-MM-DD or similar parseable format

Usage:
    python universal_pattern_analyzer.py --file "Company_Name.csv" --company "Company Name"
    
Output:
    Creates a complete analysis directory with all pattern data
"""

import pandas as pd
import numpy as np
from datetime import datetime
import argparse
import os
import sys
from scipy import stats

class UniversalPatternAnalyzer:
    """Analyzes cyclical patterns for any stock data"""
    
    def __init__(self, csv_file, company_name=None):
        """
        Initialize analyzer with stock data
        
        Parameters:
        -----------
        csv_file : str
            Path to CSV file with stock data
        company_name : str, optional
            Company name for reports (extracted from filename if not provided)
        """
        self.csv_file = csv_file
        self.company_name = company_name or self._extract_company_name(csv_file)
        self.df = None
        self.output_dir = f"{self.company_name.replace(' ', '_')}_Analysis_Complete"
        
    def _extract_company_name(self, filename):
        """Extract company name from filename"""
        basename = os.path.basename(filename)
        name = os.path.splitext(basename)[0]
        # Remove common suffixes
        name = name.replace('_', ' ').replace('-', ' ')
        return name.title()
    
    def load_and_prepare_data(self):
        """Load CSV and prepare data with required columns"""
        print(f"\n{'='*70}")
        print(f"UNIVERSAL STOCK PATTERN ANALYZER")
        print(f"{'='*70}")
        print(f"Company: {self.company_name}")
        print(f"Input File: {self.csv_file}")
        print(f"{'='*70}\n")
        
        # Load data
        self.df = pd.read_csv(self.csv_file)
        print(f" Loaded {len(self.df):,} rows")
        
        # Ensure Date column exists
        if 'Date' not in self.df.columns:
            raise ValueError("CSV must have a 'Date' column")
        
        # Parse dates
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df = self.df.sort_values('Date').reset_index(drop=True)
        
        # Map ACE Equity column names to standard names
        column_mapping = {
            'Open (Unit Curr)': 'Open',
            'High (Unit Curr)': 'High',
            'Low (Unit Curr)': 'Low',
            'Close (Unit Curr)': 'Close',
            "Volume (000's)": 'Volume'
        }
        
        # Rename columns if ACE Equity format detected
        for old_name, new_name in column_mapping.items():
            if old_name in self.df.columns and new_name not in self.df.columns:
                self.df[new_name] = self.df[old_name]
                print(f" Mapped '{old_name}'  '{new_name}'")
        
        # Calculate Daily Return if not present
        if 'Daily_Return' not in self.df.columns:
            if 'Close' in self.df.columns:
                self.df['Daily_Return'] = self.df['Close'].pct_change() * 100
                print(f" Calculated Daily_Return from Close prices")
            else:
                raise ValueError("CSV must have 'Close' column to calculate returns")
        
        # Add date components
        self.df['Year'] = self.df['Date'].dt.year
        self.df['Month'] = self.df['Date'].dt.month
        self.df['Month_Name'] = self.df['Date'].dt.month_name()
        self.df['Weekday'] = self.df['Date'].dt.day_name()
        self.df['Day_of_Month'] = self.df['Date'].dt.day
        self.df['Week_of_Year'] = self.df['Date'].dt.isocalendar().week
        self.df['Quarter'] = self.df['Date'].dt.quarter
        
        print(f" Added date components (Year, Month, Weekday, etc.)")
        
        # Calculate additional metrics if columns exist
        if all(col in self.df.columns for col in ['Open', 'High', 'Low', 'Close']):
            if 'Overnight' not in self.df.columns:
                self.df['Overnight'] = ((self.df['Open'] - self.df['Close'].shift(1)) / 
                                        self.df['Close'].shift(1) * 100)
            if 'Intraday' not in self.df.columns:
                self.df['Intraday'] = ((self.df['Close'] - self.df['Open']) / 
                                       self.df['Open'] * 100)
            print(f" Calculated Overnight and Intraday returns")
        
        print(f"\n Data preparation complete!")
        print(f"  Date Range: {self.df['Date'].min().date()} to {self.df['Date'].max().date()}")
        print(f"  Total Trading Days: {len(self.df):,}")
        print(f"  Years Covered: {self.df['Year'].nunique()}")
        
        return self.df
    
    def calculate_statistics(self, data_series, percentiles=[10, 25, 50, 75, 90]):
        """Calculate comprehensive statistics for a data series"""
        clean_data = data_series.dropna()
        
        if len(clean_data) == 0:
            return None
        
        stats_dict = {
            'Total Trading Days': len(clean_data),
            'Mean Daily Return (%)': clean_data.mean(),
            'Median Daily Return (%)': clean_data.median(),
            'Std Deviation (%)': clean_data.std(),
            'Min Daily Return (%)': clean_data.min(),
            'Max Daily Return (%)': clean_data.max(),
            'Win Rate (%)': (clean_data > 0).sum() / len(clean_data) * 100,
            'Average Win (%)': clean_data[clean_data > 0].mean() if (clean_data > 0).any() else 0,
            'Average Loss (%)': clean_data[clean_data < 0].mean() if (clean_data < 0).any() else 0,
        }
        
        # Add percentiles
        for p in percentiles:
            stats_dict[f'{p}th Percentile (%)'] = np.percentile(clean_data, p)
        
        # Add distribution metrics
        stats_dict['Skewness'] = clean_data.skew()
        stats_dict['Kurtosis'] = clean_data.kurtosis()
        
        return stats_dict
    
    def create_output_directories(self):
        """Create organized directory structure for outputs"""
        directories = [
            f"{self.output_dir}/00_Master_Data",
            f"{self.output_dir}/01_April_Analysis",
            f"{self.output_dir}/02_Wednesday_Analysis",
            f"{self.output_dir}/03_Weekday_Analysis",
            f"{self.output_dir}/04_MonthEnd_Analysis",
            f"{self.output_dir}/05_FirstMonday_Analysis",
            f"{self.output_dir}/06_Monthly_Analysis",
            f"{self.output_dir}/07_Comparison_Tables",
            f"{self.output_dir}/08_Visualizations",
            f"{self.output_dir}/09_Reports",
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
        
        print(f"\n Created output directory structure: {self.output_dir}/")
    
    def analyze_weekday_patterns(self):
        """Analyze patterns by day of week"""
        print(f"\n{'='*70}")
        print("ANALYZING WEEKDAY PATTERNS")
        print(f"{'='*70}\n")
        
        weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        weekday_stats = []
        
        for weekday in weekday_order:
            weekday_data = self.df[self.df['Weekday'] == weekday]['Daily_Return']
            stats = self.calculate_statistics(weekday_data)
            
            if stats:
                stats['Weekday'] = weekday
                weekday_stats.append(stats)
                
                # Save individual weekday raw data
                weekday_df = self.df[self.df['Weekday'] == weekday].copy()
                output_file = f"{self.output_dir}/03_Weekday_Analysis/{weekday.lower()}_all_days_raw_data.csv"
                weekday_df.to_csv(output_file, index=False)
                
                print(f" {weekday:10s}: Mean={stats['Mean Daily Return (%)']:+7.3f}%, "
                      f"Median={stats['Median Daily Return (%)']:+7.3f}%, "
                      f"Win Rate={stats['Win Rate (%)']:.1f}% ({int(stats['Total Trading Days'])} days)")
        
        # Save comprehensive statistics
        weekday_stats_df = pd.DataFrame(weekday_stats)
        weekday_stats_df.to_csv(f"{self.output_dir}/03_Weekday_Analysis/weekday_comprehensive_statistics.csv", 
                               index=False)
        
        return weekday_stats_df
    
    def analyze_monthly_patterns(self):
        """Analyze patterns by month"""
        print(f"\n{'='*70}")
        print("ANALYZING MONTHLY PATTERNS")
        print(f"{'='*70}\n")
        
        month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        monthly_stats = []
        
        for month_name in month_names:
            month_data = self.df[self.df['Month_Name'] == month_name]['Daily_Return']
            stats = self.calculate_statistics(month_data)
            
            if stats:
                stats['Month'] = month_name
                monthly_stats.append(stats)
                
                # Save individual month raw data
                month_df = self.df[self.df['Month_Name'] == month_name].copy()
                output_file = f"{self.output_dir}/06_Monthly_Analysis/{month_name.lower()}_all_days_raw_data.csv"
                month_df.to_csv(output_file, index=False)
                
                print(f" {month_name:10s}: Mean={stats['Mean Daily Return (%)']:+7.3f}%, "
                      f"Median={stats['Median Daily Return (%)']:+7.3f}%, "
                      f"Win Rate={stats['Win Rate (%)']:.1f}% ({int(stats['Total Trading Days'])} days)")
        
        # Save comprehensive statistics
        monthly_stats_df = pd.DataFrame(monthly_stats)
        monthly_stats_df.to_csv(f"{self.output_dir}/06_Monthly_Analysis/monthly_comprehensive_statistics.csv", 
                               index=False)
        
        return monthly_stats_df
    
    def analyze_april_pattern(self):
        """Detailed analysis of April"""
        print(f"\n{'='*70}")
        print("DETAILED APRIL ANALYSIS")
        print(f"{'='*70}\n")
        
        april_data = self.df[self.df['Month_Name'] == 'April'].copy()
        
        if len(april_data) == 0:
            print(" No April data found")
            return None
        
        # Overall statistics
        stats = self.calculate_statistics(april_data['Daily_Return'])
        stats_df = pd.DataFrame([stats]).T
        stats_df.columns = ['Value']
        stats_df.to_csv(f"{self.output_dir}/01_April_Analysis/april_overall_statistics.csv")
        
        # Raw data
        april_data.to_csv(f"{self.output_dir}/01_April_Analysis/april_all_days_raw_data.csv", index=False)
        
        # Yearly breakdown
        yearly_stats = []
        for year in sorted(april_data['Year'].unique()):
            year_data = april_data[april_data['Year'] == year]['Daily_Return']
            year_stats = self.calculate_statistics(year_data)
            if year_stats:
                year_stats['Year'] = year
                yearly_stats.append(year_stats)
        
        yearly_df = pd.DataFrame(yearly_stats)
        yearly_df.to_csv(f"{self.output_dir}/01_April_Analysis/april_yearly_statistics.csv", index=False)
        
        print(f" April Analysis: Mean={stats['Mean Daily Return (%)']:+.3f}%, "
              f"Median={stats['Median Daily Return (%)']:+.3f}%, "
              f"Win Rate={stats['Win Rate (%)']:.1f}% ({int(stats['Total Trading Days'])} days)")
        
        return stats
    
    def analyze_wednesday_pattern(self):
        """Detailed analysis of Wednesday"""
        print(f"\n{'='*70}")
        print("DETAILED WEDNESDAY ANALYSIS")
        print(f"{'='*70}\n")
        
        wednesday_data = self.df[self.df['Weekday'] == 'Wednesday'].copy()
        
        if len(wednesday_data) == 0:
            print(" No Wednesday data found")
            return None
        
        # Overall statistics
        stats = self.calculate_statistics(wednesday_data['Daily_Return'])
        stats_df = pd.DataFrame([stats]).T
        stats_df.columns = ['Value']
        stats_df.to_csv(f"{self.output_dir}/02_Wednesday_Analysis/wednesday_overall_statistics.csv")
        
        # Raw data
        wednesday_data.to_csv(f"{self.output_dir}/02_Wednesday_Analysis/wednesday_all_days_raw_data.csv", index=False)
        
        # Yearly breakdown
        yearly_stats = []
        for year in sorted(wednesday_data['Year'].unique()):
            year_data = wednesday_data[wednesday_data['Year'] == year]['Daily_Return']
            year_stats = self.calculate_statistics(year_data)
            if year_stats:
                year_stats['Year'] = year
                yearly_stats.append(year_stats)
        
        yearly_df = pd.DataFrame(yearly_stats)
        yearly_df.to_csv(f"{self.output_dir}/02_Wednesday_Analysis/wednesday_yearly_statistics.csv", index=False)
        
        print(f" Wednesday Analysis: Mean={stats['Mean Daily Return (%)']:+.3f}%, "
              f"Median={stats['Median Daily Return (%)']:+.3f}%, "
              f"Win Rate={stats['Win Rate (%)']:.1f}% ({int(stats['Total Trading Days'])} days)")
        
        return stats
    
    def analyze_monthend_pattern(self):
        """Analyze last 5 days of each month"""
        print(f"\n{'='*70}")
        print("MONTH-END PATTERN ANALYSIS (Last 5 Days)")
        print(f"{'='*70}\n")
        
        # Group by year-month and get last 5 days
        self.df['YearMonth'] = self.df['Date'].dt.to_period('M')
        monthend_data = self.df.groupby('YearMonth').tail(5).copy()
        
        if len(monthend_data) == 0:
            print(" No month-end data found")
            return None
        
        # Overall statistics
        stats = self.calculate_statistics(monthend_data['Daily_Return'])
        stats_df = pd.DataFrame([stats]).T
        stats_df.columns = ['Value']
        stats_df.to_csv(f"{self.output_dir}/04_MonthEnd_Analysis/monthend_overall_statistics.csv")
        
        # Raw data
        monthend_data.to_csv(f"{self.output_dir}/04_MonthEnd_Analysis/monthend_last5days_raw_data.csv", index=False)
        
        # Yearly breakdown
        yearly_stats = []
        for year in sorted(monthend_data['Year'].unique()):
            year_data = monthend_data[monthend_data['Year'] == year]['Daily_Return']
            year_stats = self.calculate_statistics(year_data)
            if year_stats:
                year_stats['Year'] = year
                yearly_stats.append(year_stats)
        
        yearly_df = pd.DataFrame(yearly_stats)
        yearly_df.to_csv(f"{self.output_dir}/04_MonthEnd_Analysis/monthend_yearly_statistics.csv", index=False)
        
        print(f" Month-End Analysis: Mean={stats['Mean Daily Return (%)']:+.3f}%, "
              f"Median={stats['Median Daily Return (%)']:+.3f}%, "
              f"Win Rate={stats['Win Rate (%)']:.1f}% ({int(stats['Total Trading Days'])} days)")
        
        return stats
    
    def analyze_first_monday_pattern(self):
        """Analyze first Monday of each month"""
        print(f"\n{'='*70}")
        print("FIRST MONDAY OF MONTH ANALYSIS")
        print(f"{'='*70}\n")
        
        # Identify first Monday of each month
        self.df['YearMonth'] = self.df['Date'].dt.to_period('M')
        first_mondays = self.df[self.df['Weekday'] == 'Monday'].groupby('YearMonth').first().reset_index()
        
        if len(first_mondays) == 0:
            print(" No first Monday data found")
            return None
        
        # Get the data
        first_monday_data = self.df[self.df['Date'].isin(first_mondays['Date'])].copy()
        
        # Statistics
        stats = self.calculate_statistics(first_monday_data['Daily_Return'])
        stats_df = pd.DataFrame([stats]).T
        stats_df.columns = ['Value']
        stats_df.to_csv(f"{self.output_dir}/05_FirstMonday_Analysis/first_monday_statistics.csv")
        
        # Raw data
        first_monday_data.to_csv(f"{self.output_dir}/05_FirstMonday_Analysis/first_monday_raw_data.csv", index=False)
        
        print(f" First Monday Analysis: Mean={stats['Mean Daily Return (%)']:+.3f}%, "
              f"Median={stats['Median Daily Return (%)']:+.3f}%, "
              f"Win Rate={stats['Win Rate (%)']:.1f}% ({int(stats['Total Trading Days'])} days)")
        
        return stats
    
    def create_comparison_table(self):
        """Create comparison table of all patterns"""
        print(f"\n{'='*70}")
        print("CREATING PATTERN COMPARISON TABLE")
        print(f"{'='*70}\n")
        
        patterns = []
        
        # Overall market
        overall_stats = self.calculate_statistics(self.df['Daily_Return'])
        overall_stats['Pattern'] = 'All Days'
        patterns.append(overall_stats)
        
        # Wednesday
        wed_data = self.df[self.df['Weekday'] == 'Wednesday']['Daily_Return']
        wed_stats = self.calculate_statistics(wed_data)
        wed_stats['Pattern'] = 'Wednesday'
        patterns.append(wed_stats)
        
        # Monday
        mon_data = self.df[self.df['Weekday'] == 'Monday']['Daily_Return']
        mon_stats = self.calculate_statistics(mon_data)
        if mon_stats:
            mon_stats['Pattern'] = 'Monday'
            patterns.append(mon_stats)
        
        # April
        apr_data = self.df[self.df['Month_Name'] == 'April']['Daily_Return']
        apr_stats = self.calculate_statistics(apr_data)
        if apr_stats:
            apr_stats['Pattern'] = 'April'
            patterns.append(apr_stats)
        
        # February
        feb_data = self.df[self.df['Month_Name'] == 'February']['Daily_Return']
        feb_stats = self.calculate_statistics(feb_data)
        if feb_stats:
            feb_stats['Pattern'] = 'February'
            patterns.append(feb_stats)
        
        # Month-End
        self.df['YearMonth'] = self.df['Date'].dt.to_period('M')
        monthend_data = self.df.groupby('YearMonth').tail(5)['Daily_Return']
        me_stats = self.calculate_statistics(monthend_data)
        if me_stats:
            me_stats['Pattern'] = 'Month-End (Last 5)'
            patterns.append(me_stats)
        
        # First Monday
        first_mondays = self.df[self.df['Weekday'] == 'Monday'].groupby('YearMonth').first()
        fm_data = self.df[self.df['Date'].isin(first_mondays['Date'])]['Daily_Return']
        fm_stats = self.calculate_statistics(fm_data)
        if fm_stats:
            fm_stats['Pattern'] = 'First Monday'
            patterns.append(fm_stats)
        
        # Create DataFrame
        comparison_df = pd.DataFrame(patterns)
        
        # Reorder columns
        cols = ['Pattern', 'Total Trading Days', 'Mean Daily Return (%)', 'Median Daily Return (%)', 
                'Std Deviation (%)', 'Win Rate (%)', 'Min Daily Return (%)', 'Max Daily Return (%)',
                '25th Percentile (%)', '75th Percentile (%)', 'Skewness', 'Kurtosis']
        comparison_df = comparison_df[[col for col in cols if col in comparison_df.columns]]
        
        # Save
        comparison_df.to_csv(f"{self.output_dir}/07_Comparison_Tables/pattern_comparison_table.csv", index=False)
        
        print(f" Pattern comparison table created with {len(patterns)} patterns")
        
        return comparison_df
    
    def save_master_data(self):
        """Save enhanced master dataset"""
        print(f"\n{'='*70}")
        print("SAVING MASTER DATA")
        print(f"{'='*70}\n")
        
        # Add pattern flags
        self.df['Is_April'] = self.df['Month_Name'] == 'April'
        self.df['Is_Wednesday'] = self.df['Weekday'] == 'Wednesday'
        self.df['Is_Monday'] = self.df['Weekday'] == 'Monday'
        
        # Month-end flag
        self.df['YearMonth'] = self.df['Date'].dt.to_period('M')
        monthend_dates = self.df.groupby('YearMonth').tail(5)['Date']
        self.df['Is_MonthEnd'] = self.df['Date'].isin(monthend_dates)
        
        # First Monday flag
        first_monday_dates = self.df[self.df['Weekday'] == 'Monday'].groupby('YearMonth').first()['Date']
        self.df['Is_FirstMonday'] = self.df['Date'].isin(first_monday_dates)
        
        # Save
        output_file = f"{self.output_dir}/00_Master_Data/{self.company_name.replace(' ', '_').lower()}_master_data_enhanced.csv"
        self.df.to_csv(output_file, index=False)
        
        print(f" Master data saved: {output_file}")
        print(f"  Total rows: {len(self.df):,}")
        print(f"  Columns: {len(self.df.columns)}")
    
    def run_complete_analysis(self):
        """Run the complete analysis pipeline"""
        try:
            # Load and prepare data
            self.load_and_prepare_data()
            
            # Create output directories
            self.create_output_directories()
            
            # Run all analyses
            self.analyze_weekday_patterns()
            self.analyze_monthly_patterns()
            self.analyze_april_pattern()
            self.analyze_wednesday_pattern()
            self.analyze_monthend_pattern()
            self.analyze_first_monday_pattern()
            self.create_comparison_table()
            self.save_master_data()
            
            print(f"\n{'='*70}")
            print(f" ANALYSIS COMPLETE!")
            print(f"{'='*70}")
            print(f"\nOutput directory: {self.output_dir}/")
            print(f"\nGenerated files:")
            print(f"   Master data with pattern flags")
            print(f"   Weekday analysis (5 files)")
            print(f"   Monthly analysis (12 files)")
            print(f"   April detailed analysis (3 files)")
            print(f"   Wednesday detailed analysis (3 files)")
            print(f"   Month-end analysis (3 files)")
            print(f"   First Monday analysis (2 files)")
            print(f"   Pattern comparison table")
            print(f"\nTotal: 35+ CSV files with complete statistics")
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
        description='Universal Stock Pattern Analyzer - Works with any stock CSV file',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python universal_pattern_analyzer.py --file "INFY.csv" --company "Infosys"
  python universal_pattern_analyzer.py --file "TCS_Stock_Data.csv"
  python universal_pattern_analyzer.py --file "data/HDFC.csv" --company "HDFC Bank"
        """
    )
    
    parser.add_argument('--file', '-f', required=True, 
                       help='Path to CSV file with stock data')
    parser.add_argument('--company', '-c', 
                       help='Company name (optional, extracted from filename if not provided)')
    
    args = parser.parse_args()
    
    # Validate file exists
    if not os.path.exists(args.file):
        print(f" ERROR: File not found: {args.file}")
        sys.exit(1)
    
    # Run analysis
    analyzer = UniversalPatternAnalyzer(args.file, args.company)
    success = analyzer.run_complete_analysis()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

