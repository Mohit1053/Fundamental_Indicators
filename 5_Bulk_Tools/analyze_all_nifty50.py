"""
NIFTY50 Batch Analyzer
Extracts all 50 stocks from NIFTY50.csv and analyzes each using Generic Stock Analyzer
"""

import os
import sys
import subprocess
import time
from datetime import datetime
from pathlib import Path

# Add Generic Stock Analyzer to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '2_Generic_Stock_Analyzer'))

def analyze_all_nifty50():
    """
    Complete pipeline:
    1. Extract all 50 stocks from NIFTY50.csv
    2. Analyze each stock using Generic Stock Analyzer
    3. Generate master summary report
    """
    
    print("\n" + "="*80)
    print("🚀 NIFTY50 COMPLETE ANALYSIS PIPELINE")
    print("="*80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    start_time = time.time()
    
    # Step 1: Extract stocks
    print("\n" + "─"*80)
    print("STEP 1: EXTRACTING INDIVIDUAL STOCKS FROM NIFTY50.csv")
    print("─"*80)
    
    from extract_nifty50_stocks import extract_nifty50_stocks
    
    extraction_summary, stock_dir = extract_nifty50_stocks()
    
    extraction_time = time.time() - start_time
    print(f"\n✅ Extraction completed in {extraction_time:.2f} seconds")
    
    # Get list of extracted CSV files
    stock_files = sorted([f for f in os.listdir(stock_dir) if f.endswith('.csv')])
    
    if not stock_files:
        print("\n❌ No stock files found. Exiting.")
        return
    
    print(f"\n📊 Found {len(stock_files)} stock files to analyze")
    
    # Step 2: Analyze each stock
    print("\n" + "─"*80)
    print("STEP 2: ANALYZING EACH STOCK WITH GENERIC STOCK ANALYZER")
    print("─"*80)
    
    analysis_results = []
    analysis_start = time.time()
    
    # Create master output directory
    master_output_dir = '5_NIFTY50_Complete_Analyses'
    os.makedirs(master_output_dir, exist_ok=True)
    
    for idx, stock_file in enumerate(stock_files, 1):
        stock_path = os.path.join(stock_dir, stock_file)
        stock_name = stock_file.replace('.csv', '')
        
        print(f"\n[{idx}/{len(stock_files)}] Analyzing: {stock_name}")
        print("─"*60)
        
        stock_start = time.time()
        
        try:
            # Create output directory for this stock
            output_subdir = os.path.join(master_output_dir, f"{stock_name}_Analysis")
            os.makedirs(output_subdir, exist_ok=True)
            
            # Change to output directory for analysis
            original_dir = os.getcwd()
            os.chdir(output_subdir)
            
            # Run analyzer as subprocess
            analyzer_script = os.path.join(original_dir, '2_Generic_Stock_Analyzer', 'analyze_stock.py')
            result = subprocess.run(
                [sys.executable, analyzer_script, '--file', stock_path, '--company', stock_name, '--all'],
                capture_output=True,
                text=True
            )
            
            os.chdir(original_dir)
            
            stock_time = time.time() - stock_start
            
            if result.returncode == 0:
                # Count generated files (recursively)
                file_count = sum([len(files) for _, _, files in os.walk(output_subdir)])
                
                analysis_results.append({
                    'stock': stock_name,
                    'status': '✅ Success',
                    'time': stock_time,
                    'files': file_count,
                    'output_dir': output_subdir
                })
                
                print(f"   ✅ Analysis complete: {file_count} files generated in {stock_time:.2f}s")
            else:
                analysis_results.append({
                    'stock': stock_name,
                    'status': '❌ Failed',
                    'time': stock_time,
                    'files': 0,
                    'output_dir': output_subdir
                })
                print(f"   ❌ Analysis failed after {stock_time:.2f}s")
                if result.stderr:
                    print(f"   Error: {result.stderr[:200]}")
                
        except Exception as e:
            stock_time = time.time() - stock_start
            analysis_results.append({
                'stock': stock_name,
                'status': f'❌ Error: {str(e)[:50]}',
                'time': stock_time,
                'files': 0,
                'output_dir': None
            })
            print(f"   ❌ Error: {str(e)}")
    
    analysis_time = time.time() - analysis_start
    total_time = time.time() - start_time
    
    # Step 3: Generate Master Summary Report
    print("\n" + "─"*80)
    print("STEP 3: GENERATING MASTER SUMMARY REPORT")
    print("─"*80)
    
    success_count = sum(1 for r in analysis_results if r['status'].startswith('✅'))
    failed_count = len(analysis_results) - success_count
    total_files = sum(r['files'] for r in analysis_results)
    avg_time = sum(r['time'] for r in analysis_results) / len(analysis_results) if analysis_results else 0
    
    # Create master report
    report_path = os.path.join(master_output_dir, 'NIFTY50_MASTER_ANALYSIS_REPORT.md')
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# 📊 NIFTY50 COMPLETE ANALYSIS REPORT\n\n")
        f.write(f"**Analysis Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
        f.write(f"**Total Stocks**: {len(stock_files)}  \n")
        f.write(f"**Successfully Analyzed**: {success_count}  \n")
        f.write(f"**Failed**: {failed_count}  \n\n")
        
        f.write("---\n\n")
        f.write("## ⏱️ Performance Metrics\n\n")
        f.write(f"- **Total Execution Time**: {total_time:.2f} seconds ({total_time/60:.2f} minutes)\n")
        f.write(f"- **Extraction Time**: {extraction_time:.2f} seconds\n")
        f.write(f"- **Analysis Time**: {analysis_time:.2f} seconds\n")
        f.write(f"- **Average Time per Stock**: {avg_time:.2f} seconds\n")
        f.write(f"- **Total Files Generated**: {total_files:,}\n\n")
        
        f.write("---\n\n")
        f.write("## 📈 Analysis Results by Stock\n\n")
        f.write("| # | Stock Name | Status | Time (s) | Files | Output Directory |\n")
        f.write("|---|------------|--------|----------|-------|------------------|\n")
        
        for i, result in enumerate(analysis_results, 1):
            status_icon = "✅" if result['status'].startswith('✅') else "❌"
            f.write(f"| {i} | {result['stock']} | {status_icon} | {result['time']:.2f} | {result['files']} | `{result['output_dir']}` |\n")
        
        f.write("\n---\n\n")
        f.write("## 🎯 Successfully Analyzed Companies\n\n")
        
        for i, result in enumerate([r for r in analysis_results if r['status'].startswith('✅')], 1):
            f.write(f"{i}. **{result['stock']}** - {result['files']} files in {result['time']:.2f}s\n")
        
        if failed_count > 0:
            f.write("\n---\n\n")
            f.write("## ❌ Failed Analyses\n\n")
            
            for i, result in enumerate([r for r in analysis_results if not r['status'].startswith('✅')], 1):
                f.write(f"{i}. **{result['stock']}** - {result['status']}\n")
        
        f.write("\n---\n\n")
        f.write("## 📁 Directory Structure\n\n")
        f.write("```\n")
        f.write("Fundamental_Indicators/\n")
        f.write("├── NIFTY50.csv (source file)\n")
        f.write("├── 4_NIFTY50_Individual_Stocks/ (50 extracted CSVs)\n")
        f.write("└── 5_NIFTY50_Complete_Analyses/ (this directory)\n")
        f.write("    ├── NIFTY50_MASTER_ANALYSIS_REPORT.md (this file)\n")
        
        for result in analysis_results[:3]:  # Show first 3 as examples
            if result['status'].startswith('✅'):
                f.write(f"    ├── {result['stock']}_Analysis/\n")
                f.write(f"    │   ├── {result['stock']}_Executive_Summary.md\n")
                f.write(f"    │   ├── {result['stock']}_Trading_Strategies.md\n")
                f.write(f"    │   ├── Pattern_Analysis/\n")
                f.write(f"    │   ├── Statistical_Analysis/\n")
                f.write(f"    │   └── Visualizations/\n")
        
        if len(analysis_results) > 3:
            f.write(f"    ├── ... ({len(analysis_results) - 3} more stock analyses)\n")
        
        f.write("```\n\n")
        
        f.write("---\n\n")
        f.write("## 🔍 Analysis Components Per Stock\n\n")
        f.write("Each successfully analyzed stock contains:\n\n")
        f.write("### 📄 Reports\n")
        f.write("- Executive Summary (key metrics, recommendations)\n")
        f.write("- Trading Strategies (entry/exit signals)\n")
        f.write("- Master Analysis Index (complete overview)\n\n")
        
        f.write("### 📊 Pattern Analysis\n")
        f.write("- Weekday patterns\n")
        f.write("- Monthly patterns\n")
        f.write("- Special date patterns\n")
        f.write("- Cyclical patterns\n\n")
        
        f.write("### 📈 Statistical Analysis\n")
        f.write("- Moving averages (SMA, EMA)\n")
        f.write("- Technical indicators (RSI, MACD, Bollinger Bands)\n")
        f.write("- Performance metrics (returns, volatility, Sharpe ratio)\n")
        f.write("- Correlation analysis\n\n")
        
        f.write("### 📉 Visualizations\n")
        f.write("- Price charts with indicators\n")
        f.write("- Volume analysis\n")
        f.write("- Pattern distributions\n")
        f.write("- Performance comparisons\n\n")
        
        f.write("---\n\n")
        f.write("## ✅ Conclusion\n\n")
        f.write(f"Successfully completed comprehensive analysis of **{success_count} out of {len(stock_files)} NIFTY50 stocks** ")
        f.write(f"in **{total_time/60:.2f} minutes**, generating **{total_files:,} analysis files**.\n\n")
        
        f.write("All analysis outputs are available in their respective subdirectories within ")
        f.write("`5_NIFTY50_Complete_Analyses/`.\n")
    
    print(f"\n✅ Master report generated: {report_path}")
    
    # Final Summary
    print("\n" + "="*80)
    print("🎉 NIFTY50 ANALYSIS PIPELINE COMPLETE!")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"   • Total Stocks: {len(stock_files)}")
    print(f"   • Successfully Analyzed: {success_count}")
    print(f"   • Failed: {failed_count}")
    print(f"   • Total Files Generated: {total_files:,}")
    print(f"   • Total Time: {total_time:.2f}s ({total_time/60:.2f} min)")
    print(f"   • Average Time per Stock: {avg_time:.2f}s")
    print(f"\n📁 Output Location: {os.path.abspath(master_output_dir)}")
    print(f"📄 Master Report: {report_path}")
    print("\n" + "="*80)
    
    return analysis_results

if __name__ == "__main__":
    results = analyze_all_nifty50()
