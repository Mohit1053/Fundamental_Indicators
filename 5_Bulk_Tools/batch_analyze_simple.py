"""
Simple batch analyzer for NIFTY50 stocks
Runs each stock through the analyzer one by one
"""

import os
import sys
import time
import subprocess
from pathlib import Path

# Get all extracted stock files
stock_dir = "4_NIFTY50_Individual_Stocks"
output_dir = "5_NIFTY50_Complete_Analyses"

stock_files = sorted([f for f in os.listdir(stock_dir) if f.endswith('.csv') and not f.startswith('_')])

print(f"\nFound {len(stock_files)} stocks to analyze")
print(f"Output directory: {output_dir}")
print(f"\nStarting batch analysis...")
print("="*80)

os.makedirs(output_dir, exist_ok=True)

start_time = time.time()
success_count = 0
failed_count = 0

for idx, stock_file in enumerate(stock_files, 1):
    stock_name = stock_file.replace('.csv', '')
    stock_path = os.path.join(stock_dir, stock_file)
    
    print(f"\n[{idx}/{len(stock_files)}] {stock_name}")
    print("="*60)
    
    # Build command - use full Python path to ensure correct environment
    python_exe = r"C:\Users\mohit1\AppData\Local\Programs\Python\Python313\python.exe"
    analyzer_script = r"2_Generic_Stock_Analyzer\analyze_stock.py"
    
    # Run analysis using subprocess
    result = subprocess.run(
        [python_exe, analyzer_script, "--file", stock_path, "--company", stock_name, "--all"],
        cwd=os.getcwd(),
        capture_output=False,
        text=True
    )
    
    if result.returncode == 0:
        success_count += 1
        print(f"  SUCCESS")
    else:
        failed_count += 1
        print(f"  FAILED (exit code: {result.returncode})")

total_time = time.time() - start_time

print("\n" + "="*80)
print("BATCH ANALYSIS COMPLETE")
print("="*80)
print(f"Total: {len(stock_files)}")
print(f"Success: {success_count}")
print(f"Failed: {failed_count}")
print(f"Time: {total_time:.2f}s ({total_time/60:.2f} min)")
print(f"Avg per stock: {total_time/len(stock_files):.2f}s")
