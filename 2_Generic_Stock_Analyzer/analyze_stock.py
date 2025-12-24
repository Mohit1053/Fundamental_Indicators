"""
Universal Stock Analyzer - Master Pipeline
===========================================
Complete end-to-end analysis pipeline for ANY stock CSV file.

This script orchestrates all analysis modules:
1. Pattern Analysis (weekday, monthly, special patterns)
2. Statistical Analysis (technical indicators, performance metrics)
3. Visualization Generation (charts and graphs)
4. Report Generation (comprehensive markdown reports)

Usage:
    python analyze_stock.py --file "Company_Stock_Data.csv" --company "Company Name"
    
    # Optional: Skip certain steps
    python analyze_stock.py --file "data.csv" --company "ABC Corp" --skip-stats --skip-viz

    # Full analysis with all options
    python analyze_stock.py --file "INFY.csv" --company "Infosys" --all
"""

import subprocess
import argparse
import os
import sys
from datetime import datetime

class StockAnalysisPipeline:
    """Master pipeline for complete stock analysis"""
    
    def __init__(self, csv_file, company_name, skip_stats=False, skip_viz=False, skip_reports=False):
        self.csv_file = csv_file
        self.company_name = company_name
        self.skip_stats = skip_stats
        self.skip_viz = skip_viz
        self.skip_reports = skip_reports
        
        # Determine output directory
        self.output_dir = f"{company_name.replace(' ', '_')}_Analysis_Complete"
        self.master_data_file = None
        
        # Get script directory
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        
    def print_banner(self):
        """Print analysis banner"""
        print(f"\n{'='*80}")
        print(f"{'UNIVERSAL STOCK ANALYZER - COMPLETE PIPELINE':^80}")
        print(f"{'='*80}")
        print(f"\nCompany: {self.company_name}")
        print(f"Input File: {self.csv_file}")
        print(f"Output Directory: {self.output_dir}/")
        print(f"\nAnalysis Pipeline:")
        print(f"   1. [PATTERN] Weekday, monthly, special patterns")
        print(f"   2. [STATS] Technical indicators, metrics {'[ENABLED]' if not self.skip_stats else '[SKIPPED]'}")
        print(f"   3. [FUNDAMENTAL] MCAP, liquidity, valuation")
        print(f"   4. [VIZ] Visualization generation {'[ENABLED]' if not self.skip_viz else '[SKIPPED]'}")
        print(f"   5. [REPORTS] Markdown reports {'[ENABLED]' if not self.skip_reports else '[SKIPPED]'}")
        print(f"\n{'='*80}\n")
        
        # input("Press ENTER to begin analysis...")  # Auto-proceed for automated runs
        print()
    
    def run_pattern_analysis(self):
        """Step 1: Run pattern analysis"""
        print(f"\n{'='*80}")
        print(f"STEP 1: PATTERN ANALYSIS")
        print(f"{'='*80}\n")
        
        script = os.path.join(self.script_dir, "universal_pattern_analyzer.py")
        
        cmd = [
            sys.executable,
            script,
            "--file", self.csv_file,
            "--company", self.company_name
        ]
        
        result = subprocess.run(cmd, capture_output=False)
        
        if result.returncode != 0:
            print(f"\n Pattern analysis failed!")
            return False
        
        # Determine master data file
        company_slug = self.company_name.replace(' ', '_').lower()
        self.master_data_file = f"{self.output_dir}/00_Master_Data/{company_slug}_master_data_enhanced.csv"
        
        if not os.path.exists(self.master_data_file):
            print(f"\n Master data file not found: {self.master_data_file}")
            return False
        
        print(f"\n Pattern analysis complete!")
        return True
    
    def run_statistical_analysis(self):
        """Step 2: Run statistical analysis"""
        if self.skip_stats:
            print(f"\n  Skipping statistical analysis")
            return True
        
        print(f"\n{'='*80}")
        print(f"STEP 2: STATISTICAL ANALYSIS")
        print(f"{'='*80}\n")
        
        script = os.path.join(self.script_dir, "universal_statistical_analyzer.py")
        
        cmd = [
            sys.executable,
            script,
            "--file", self.master_data_file,
            "--company", self.company_name
        ]
        
        result = subprocess.run(cmd, capture_output=False)
        
        if result.returncode != 0:
            print(f"\n  Statistical analysis failed (continuing anyway)")
            return True  # Don't fail entire pipeline
        
        print(f"\n Statistical analysis complete!")
        return True
    
    def run_fundamental_analysis(self):
        """Step 3: Run fundamental metrics analysis"""
        print(f"\n{'='*80}")
        print(f"STEP 3: FUNDAMENTAL METRICS ANALYSIS")
        print(f"{'='*80}\n")
        
        script = os.path.join(self.script_dir, "fundamental_metrics_analyzer.py")
        
        # Use original CSV file (has all fundamental columns)
        cmd = [
            sys.executable,
            script,
            "--file", self.csv_file,
            "--company", self.company_name,
            "--output", self.output_dir
        ]
        
        result = subprocess.run(cmd, capture_output=False)
        
        if result.returncode != 0:
            print(f"\n  Fundamental analysis failed (continuing anyway)")
            return True  # Don't fail entire pipeline
        
        print(f"\n Fundamental analysis complete!")
        return True
    
    def run_visualization(self):
        """Step 4: Generate visualizations"""
        if self.skip_viz:
            print(f"\n  Skipping visualization generation")
            return True
        
        print(f"\n{'='*80}")
        print(f"STEP 4: VISUALIZATION GENERATION")
        print(f"{'='*80}\n")
        
        script = os.path.join(self.script_dir, "universal_visualization_generator.py")
        
        cmd = [
            sys.executable,
            script,
            "--analysis_dir", self.output_dir,
            "--company", self.company_name
        ]
        
        result = subprocess.run(cmd, capture_output=False)
        
        if result.returncode != 0:
            print(f"\n  Visualization generation failed (continuing anyway)")
            return True  # Don't fail entire pipeline
        
        print(f"\n Visualization generation complete!")
        return True
    
    def run_report_generation(self):
        """Step 5: Generate reports"""
        if self.skip_reports:
            print(f"\n  Skipping report generation")
            return True
        
        print(f"\n{'='*80}")
        print(f"STEP 5: REPORT GENERATION")
        print(f"{'='*80}\n")
        
        script = os.path.join(self.script_dir, "universal_report_generator.py")
        
        cmd = [
            sys.executable,
            script,
            "--analysis_dir", self.output_dir,
            "--company", self.company_name
        ]
        
        result = subprocess.run(cmd, capture_output=False)
        
        if result.returncode != 0:
            print(f"\n  Report generation failed (continuing anyway)")
            return True  # Don't fail entire pipeline
        
        print(f"\n Report generation complete!")
        return True
    
    def print_summary(self):
        """Print final summary"""
        print(f"\n{'='*80}")
        print(f"{'ANALYSIS COMPLETE!':^80}")
        print(f"{'='*80}\n")
        
        print(f"Company: {self.company_name}")
        print(f"Output Directory: {self.output_dir}/\n")
        
        print(f"Generated Files:\n")
        
        # Count files
        total_files = 0
        for root, dirs, files in os.walk(self.output_dir):
            total_files += len(files)
        
        print(f"   Total Files: {total_files}")
        
        # List subdirectories
        subdirs = [d for d in os.listdir(self.output_dir) 
                  if os.path.isdir(os.path.join(self.output_dir, d))]
        
        print(f"\nDirectories Created:")
        for subdir in sorted(subdirs):
            file_count = len(os.listdir(os.path.join(self.output_dir, subdir)))
            print(f"   - {subdir}/ ({file_count} files)")
        
        # Key reports
        print(f"\nKey Reports:")
        reports_dir = f"{self.output_dir}/09_Reports"
        if os.path.exists(reports_dir):
            reports = [f for f in os.listdir(reports_dir) if f.endswith('.md')]
            for report in sorted(reports):
                print(f"   - 09_Reports/{report}")
        
        # Visualizations
        viz_dir = f"{self.output_dir}/08_Visualizations"
        if os.path.exists(viz_dir):
            charts = [f for f in os.listdir(viz_dir) if f.endswith('.png')]
            if charts:
                print(f"\nVisualizations:")
                for chart in sorted(charts):
                    print(f"   - 08_Visualizations/{chart}")
        
        print(f"\nNext Steps:")
        print(f"   1. Review executive summary: {self.output_dir}/09_Reports/EXECUTIVE_SUMMARY.md")
        print(f"   2. Check pattern comparison: {self.output_dir}/07_Comparison_Tables/pattern_comparison_table.csv")
        print(f"   3. View visualizations: {self.output_dir}/08_Visualizations/")
        print(f"   4. Explore raw data: {self.output_dir}/[pattern folders]/")
        
        print(f"\n{'='*80}\n")
    
    def run_complete_pipeline(self):
        """Execute complete analysis pipeline"""
        start_time = datetime.now()
        
        self.print_banner()
        
        # Step 1: Pattern Analysis (required)
        if not self.run_pattern_analysis():
            print(f"\n Pipeline failed at pattern analysis step")
            return False
        
        # Step 2: Statistical Analysis (optional)
        if not self.run_statistical_analysis():
            print(f"\n Pipeline failed at statistical analysis step")
            return False
        
        # Step 3: Fundamental Analysis (always run if data available)
        if not self.run_fundamental_analysis():
            print(f"\n Pipeline failed at fundamental analysis step")
            return False
        
        # Step 4: Visualization (optional)
        if not self.run_visualization():
            print(f"\n Pipeline failed at visualization step")
            return False
        
        # Step 5: Report Generation (optional)
        if not self.run_report_generation():
            print(f"\n Pipeline failed at report generation step")
            return False
        
        # Summary
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        self.print_summary()
        
        print(f"Total Time: {duration:.1f} seconds ({duration/60:.1f} minutes)\n")
        
        return True


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Universal Stock Analyzer - Complete Analysis Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full analysis
  python analyze_stock.py --file "Infosys.csv" --company "Infosys"
  
  # Pattern analysis only (fastest)
  python analyze_stock.py --file "TCS.csv" --company "TCS" --skip-stats --skip-viz --skip-reports
  
  # Analysis with visualizations but no statistical indicators
  python analyze_stock.py --file "HDFC.csv" --company "HDFC Bank" --skip-stats

Input CSV Requirements:
  - Must have columns: Date, Open, High, Low, Close, Volume
  - Date format: YYYY-MM-DD (or parseable format)
  - Data should be sorted by date (oldest to newest)

Output:
  Creates a directory: [Company_Name]_Analysis_Complete/
  Contains:
    - Pattern analysis data (35+ CSV files)
    - Statistical analysis (if not skipped)
    - Visualizations (if not skipped)
    - Comprehensive reports (if not skipped)
        """
    )
    
    parser.add_argument('--file', '-f', required=True,
                       help='Path to stock data CSV file')
    parser.add_argument('--company', '-c', required=True,
                       help='Company name for reports')
    parser.add_argument('--skip-stats', action='store_true',
                       help='Skip statistical analysis (faster)')
    parser.add_argument('--skip-viz', action='store_true',
                       help='Skip visualization generation (faster)')
    parser.add_argument('--skip-reports', action='store_true',
                       help='Skip report generation (faster)')
    parser.add_argument('--all', action='store_true',
                       help='Run complete analysis (default, overrides skip flags)')
    
    args = parser.parse_args()
    
    # Validate file exists
    if not os.path.exists(args.file):
        print(f" ERROR: File not found: {args.file}")
        sys.exit(1)
    
    # Override skip flags if --all is set
    skip_stats = args.skip_stats and not args.all
    skip_viz = args.skip_viz and not args.all
    skip_reports = args.skip_reports and not args.all
    
    # Run pipeline
    pipeline = StockAnalysisPipeline(
        csv_file=args.file,
        company_name=args.company,
        skip_stats=skip_stats,
        skip_viz=skip_viz,
        skip_reports=skip_reports
    )
    
    success = pipeline.run_complete_pipeline()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

