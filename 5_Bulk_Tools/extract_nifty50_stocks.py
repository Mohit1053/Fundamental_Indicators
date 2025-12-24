"""
NIFTY50 Stock Extractor
Extracts individual stock data from NIFTY50.csv portfolio file
Converts wide format (50 stocks horizontal) to long format (1 stock per file)
"""

import pandas as pd
from datetime import datetime, timedelta
import os
import re

def excel_serial_to_date(serial):
    """Convert Excel serial number to datetime"""
    try:
        base_date = datetime(1899, 12, 30)
        return base_date + timedelta(days=int(float(serial)))
    except:
        return None

def clean_company_name(name):
    """Convert company name to valid filename"""
    # Remove Ltd., Inc., etc.
    name = re.sub(r'\s+(Ltd\.|Limited|Inc\.|Corporation|Corp\.)?\s*$', '', name, flags=re.IGNORECASE)
    # Replace special characters with underscores
    name = re.sub(r'[^\w\s-]', '', name)
    # Replace spaces with underscores
    name = re.sub(r'\s+', '_', name)
    # Remove multiple underscores
    name = re.sub(r'_+', '_', name)
    return name.strip('_')

def extract_nifty50_stocks(input_file='NIFTY50.csv', output_dir='4_NIFTY50_Individual_Stocks'):
    """
    Extract all 50 stocks from NIFTY50.csv into individual CSV files
    
    Args:
        input_file: Path to NIFTY50.csv
        output_dir: Directory to save extracted stock files
    """
    
    print("\n" + "="*80)
    print("🚀 NIFTY50 STOCK EXTRACTION UTILITY")
    print("="*80)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n📁 Output Directory: {output_dir}")
    
    # Read file manually to handle multi-row headers
    print(f"\n📂 Reading: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Parse headers
    header1 = lines[0].strip().split(',')  # Exchange type
    header2 = lines[1].strip().split(',')  # Company names
    header3 = lines[2].strip().split(',')  # Column names
    
    print(f"✅ File loaded: {len(lines)} lines")
    print(f"✅ Data rows: {len(lines) - 3}")
    
    # Identify company column groups (each company has 12 columns)
    companies = []
    company_positions = []
    
    for i, company_name in enumerate(header2):
        if company_name and company_name.strip() and company_name != 'EQNXTH':
            companies.append(company_name.strip())
            # Each company starts at position i and spans 11 data columns + 1 separator
            company_positions.append(i)
    
    print(f"\n📊 Detected Companies: {len(companies)}")
    print("="*80)
    
    extraction_summary = []
    
    # Extract each company
    for idx, (company_name, start_col) in enumerate(zip(companies, company_positions), 1):
        try:
            print(f"\n[{idx}/{len(companies)}] Processing: {company_name}")
            
            # Extract columns for this company (11 data columns)
            # DATE, ADJCLOSE, ADJHIGH, ADJLOW, ADJOPEN, MCAP, NO_TRADES, PRICE_BV, VOLUME, VALUE, PE_CONS
            col_indices = list(range(start_col, start_col + 11))
            
            # Extract data
            company_data = []
            for line in lines[3:]:  # Skip 3 header rows
                values = line.strip().split(',')
                if len(values) > max(col_indices):
                    row_data = [values[i] for i in col_indices]
                    company_data.append(row_data)
            
            # Create DataFrame
            df = pd.DataFrame(company_data, columns=[
                'DATE', 'ADJCLOSE', 'ADJHIGH', 'ADJLOW', 'ADJOPEN', 
                'MCAP', 'NO_TRADES', 'PRICE_BV', 'VOLUME', 'VALUE', 'PE_CONS'
            ])
            
            # Convert date from Excel serial to datetime
            df['DATE'] = df['DATE'].apply(excel_serial_to_date)
            
            # Drop rows with invalid dates
            df = df.dropna(subset=['DATE'])
            
            # Convert numeric columns
            numeric_cols = ['ADJCLOSE', 'ADJHIGH', 'ADJLOW', 'ADJOPEN', 'VOLUME']
            for col in numeric_cols:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            
            # Drop rows where all price data is missing
            df = df.dropna(subset=numeric_cols, how='all')
            
            # Rename columns to match Generic Stock Analyzer expectations
            df_standard = pd.DataFrame({
                'Date': df['DATE'].dt.strftime('%Y-%m-%d'),
                'Open': df['ADJOPEN'],
                'High': df['ADJHIGH'],
                'Low': df['ADJLOW'],
                'Close': df['ADJCLOSE'],
                'Volume': df['VOLUME'],
                'MCAP': df['MCAP'],
                'NO_TRADES': df['NO_TRADES'],
                'PRICE_BV': df['PRICE_BV'],
                'VALUE': df['VALUE'],
                'PE_CONS': df['PE_CONS']
            })
            
            # Generate filename
            clean_name = clean_company_name(company_name)
            filename = f"{clean_name}.csv"
            filepath = os.path.join(output_dir, filename)
            
            # Save to CSV
            df_standard.to_csv(filepath, index=False)
            
            # Get date range
            if len(df_standard) > 0:
                date_range = f"{df_standard['Date'].iloc[-1]} to {df_standard['Date'].iloc[0]}"
                days = len(df_standard)
            else:
                date_range = "No valid data"
                days = 0
            
            print(f"   ✅ Saved: {filename}")
            print(f"   📅 Date Range: {date_range}")
            print(f"   📊 Rows: {days}")
            
            extraction_summary.append({
                'Company': company_name,
                'Filename': filename,
                'Rows': days,
                'Status': '✅ Success'
            })
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            extraction_summary.append({
                'Company': company_name,
                'Filename': 'N/A',
                'Rows': 0,
                'Status': f'❌ Failed: {str(e)[:50]}'
            })
    
    # Summary Report
    print("\n" + "="*80)
    print("📊 EXTRACTION SUMMARY")
    print("="*80)
    
    success_count = sum(1 for s in extraction_summary if s['Status'].startswith('✅'))
    total_rows = sum(s['Rows'] for s in extraction_summary)
    
    print(f"\n✅ Successfully Extracted: {success_count}/{len(companies)} companies")
    print(f"📊 Total Data Rows: {total_rows:,}")
    print(f"📁 Output Location: {os.path.abspath(output_dir)}")
    
    # Create extraction report
    report_file = os.path.join(output_dir, '_EXTRACTION_REPORT.txt')
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("NIFTY50 STOCK EXTRACTION REPORT\n")
        f.write("="*80 + "\n\n")
        f.write(f"Extraction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Source File: {input_file}\n")
        f.write(f"Output Directory: {output_dir}\n\n")
        f.write(f"Total Companies: {len(companies)}\n")
        f.write(f"Successfully Extracted: {success_count}\n")
        f.write(f"Failed: {len(companies) - success_count}\n")
        f.write(f"Total Data Rows: {total_rows:,}\n\n")
        f.write("="*80 + "\n")
        f.write("INDIVIDUAL COMPANY DETAILS\n")
        f.write("="*80 + "\n\n")
        
        for i, summary in enumerate(extraction_summary, 1):
            f.write(f"{i:2d}. {summary['Company']}\n")
            f.write(f"    Filename: {summary['Filename']}\n")
            f.write(f"    Rows: {summary['Rows']:,}\n")
            f.write(f"    Status: {summary['Status']}\n\n")
    
    print(f"\n📄 Detailed Report: {report_file}")
    print("\n" + "="*80)
    print("✅ EXTRACTION COMPLETE!")
    print("="*80)
    
    return extraction_summary, output_dir

if __name__ == "__main__":
    # Run extraction
    summary, output_dir = extract_nifty50_stocks()
    
    print(f"\n🎯 Next Step: Run Generic Stock Analyzer on each file in '{output_dir}/'")
    print(f"   Example: python 2_Generic_Stock_Analyzer/analyze_stock.py {output_dir}/HDFC_Bank.csv")
