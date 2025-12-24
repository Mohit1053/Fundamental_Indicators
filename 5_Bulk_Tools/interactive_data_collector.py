"""
Interactive Financial Data Collection Tool for Eternal Ltd
Allows manual input of financial data with validation
"""

import json
import os
from datetime import datetime


def get_float_input(prompt, allow_zero=True, allow_negative=False):
    """Get validated float input from user"""
    while True:
        try:
            value = input(f"{prompt}: ").strip()
            if value == '':
                return 0.0
            
            num = float(value)
            
            if not allow_negative and num < 0:
                print("  ⚠ Value cannot be negative. Please try again.")
                continue
            
            if not allow_zero and num == 0:
                print("  ⚠ Value cannot be zero. Please try again.")
                continue
            
            return num
        except ValueError:
            print("  ⚠ Invalid input. Please enter a number.")


def collect_company_info():
    """Collect basic company information"""
    print("\n" + "="*70)
    print("STEP 1: COMPANY INFORMATION")
    print("="*70)
    
    data = {}
    data['symbol'] = input("Stock Symbol (e.g., ETERNAL): ").strip().upper() or 'ETERNAL'
    data['exchange'] = input("Exchange (NSE/BSE): ").strip().upper() or 'NSE'
    data['ticker'] = f"{data['symbol']}.{data['exchange']}"
    data['bse_code'] = input("BSE Code (e.g., 543320): ").strip() or '543320'
    data['company_name'] = input("Company Name: ").strip() or 'Eternal Ltd'
    data['sector'] = input("Sector: ").strip() or 'E-commerce / Technology'
    data['industry'] = input("Industry: ").strip() or 'Technology Services'
    
    print("\n📊 Current Market Data:")
    data['current_price'] = get_float_input("Current Stock Price (Rs.)", allow_zero=False)
    data['market_cap'] = get_float_input("Market Cap (Rs. Crores)", allow_zero=False)
    data['shares_outstanding'] = get_float_input("Shares Outstanding (Crores)", allow_zero=False)
    
    return data


def collect_balance_sheet(year_label):
    """Collect balance sheet data for a year"""
    print(f"\n📋 Balance Sheet Data for {year_label}:")
    data = {}
    
    print("\n  Assets:")
    data['total_assets'] = get_float_input("    Total Assets (Cr)", allow_zero=False)
    data['current_assets'] = get_float_input("    Current Assets (Cr)")
    data['cash_and_equivalents'] = get_float_input("    Cash & Cash Equivalents (Cr)")
    data['accounts_receivable'] = get_float_input("    Accounts Receivable (Cr)")
    data['inventory'] = get_float_input("    Inventory (Cr)")
    
    print("\n  Liabilities:")
    data['current_liabilities'] = get_float_input("    Current Liabilities (Cr)")
    data['accounts_payable'] = get_float_input("    Accounts Payable (Cr)")
    data['short_term_debt'] = get_float_input("    Short-term Debt (Cr)")
    data['long_term_debt'] = get_float_input("    Long-term Debt (Cr)")
    data['total_debt'] = data['short_term_debt'] + data['long_term_debt']
    print(f"    Total Debt (Auto-calculated): {data['total_debt']:.2f} Cr")
    data['total_liabilities'] = get_float_input("    Total Liabilities (Cr)")
    
    print("\n  Equity:")
    data['shareholders_equity'] = get_float_input("    Shareholders Equity (Cr)", allow_zero=False)
    data['common_stock'] = get_float_input("    Common Stock (Cr)")
    data['retained_earnings'] = get_float_input("    Retained Earnings (Cr)")
    
    return data


def collect_income_statement(year_label):
    """Collect income statement data for a year"""
    print(f"\n💰 Income Statement Data for {year_label}:")
    data = {}
    
    data['total_revenue'] = get_float_input("  Total Revenue (Cr)", allow_zero=False)
    data['cost_of_revenue'] = get_float_input("  Cost of Revenue/COGS (Cr)")
    data['gross_profit'] = get_float_input("  Gross Profit (Cr)")
    data['operating_expenses'] = get_float_input("  Operating Expenses (Cr)")
    data['operating_income'] = get_float_input("  Operating Income/EBIT (Cr)", allow_negative=True)
    data['interest_expense'] = get_float_input("  Interest Expense (Cr)")
    data['other_income'] = get_float_input("  Other Income (Cr)", allow_negative=True)
    data['pretax_income'] = get_float_input("  Pre-tax Income (Cr)", allow_negative=True)
    data['income_tax_expense'] = get_float_input("  Income Tax Expense (Cr)")
    data['net_income'] = get_float_input("  Net Income (Cr)", allow_negative=True)
    
    return data


def collect_cash_flow(year_label):
    """Collect cash flow data for a year"""
    print(f"\n💵 Cash Flow Data for {year_label}:")
    data = {}
    
    data['operating_cash_flow'] = get_float_input("  Operating Cash Flow (Cr)", allow_negative=True)
    data['capital_expenditure'] = get_float_input("  Capital Expenditure (Cr, enter positive)", allow_negative=True)
    
    # Make CapEx negative if user entered positive
    if data['capital_expenditure'] > 0:
        data['capital_expenditure'] = -data['capital_expenditure']
    
    data['free_cash_flow'] = data['operating_cash_flow'] + data['capital_expenditure']
    print(f"  Free Cash Flow (Auto-calculated): {data['free_cash_flow']:.2f} Cr")
    
    data['financing_activities'] = get_float_input("  Financing Activities (Cr)", allow_negative=True)
    data['investing_activities'] = get_float_input("  Investing Activities (Cr)", allow_negative=True)
    
    return data


def collect_per_share_data(year_label, shares_outstanding):
    """Collect per-share data"""
    print(f"\n📈 Per-Share Data for {year_label}:")
    data = {}
    
    data['eps'] = get_float_input("  EPS (Rs.)", allow_negative=True)
    data['book_value_per_share'] = get_float_input("  Book Value Per Share (Rs.)")
    data['bvps'] = data['book_value_per_share']  # Alias
    data['dividend_per_share'] = get_float_input("  Dividend Per Share (Rs.)")
    
    return data


def collect_all_data_interactive():
    """Main function to collect all financial data interactively"""
    print("\n" + "="*70)
    print("INTERACTIVE FINANCIAL DATA COLLECTION FOR ETERNAL LTD")
    print("="*70)
    print("\nThis tool will guide you through entering all required financial data.")
    print("Press Enter to skip optional fields (will default to 0).")
    print("\nData should be from:")
    print("  - Annual Reports")
    print("  - Screener.in")
    print("  - MoneyControl")
    print("  - BSE/NSE Filings")
    print("="*70)
    
    # Collect company info
    company_info = collect_company_info()
    
    # Collect financial data for multiple years
    print("\n" + "="*70)
    print("STEP 2: FINANCIAL STATEMENTS (Last 4 Years)")
    print("="*70)
    
    balance_sheets = {}
    income_statements = {}
    cash_flows = {}
    per_share_data = {}
    
    years = ['fy_2024', 'fy_2023', 'fy_2022', 'fy_2021']
    year_labels = ['FY 2024 (Most Recent)', 'FY 2023', 'FY 2022', 'FY 2021']
    
    for year, label in zip(years, year_labels):
        print(f"\n{'='*70}")
        print(f"COLLECTING DATA FOR {label}")
        print('='*70)
        
        # Full data for recent years
        if year in ['fy_2024', 'fy_2023']:
            balance_sheets[year] = collect_balance_sheet(label)
            income_statements[year] = collect_income_statement(label)
            if year in ['fy_2024', 'fy_2023', 'fy_2022']:
                cash_flows[year] = collect_cash_flow(label)
            per_share_data[year] = collect_per_share_data(label, company_info['shares_outstanding'])
        else:
            # Minimal data for older years
            print(f"\n📋 Minimal data needed for {label}:")
            balance_sheets[year] = {
                'total_assets': get_float_input("  Total Assets (Cr)"),
                'shareholders_equity': get_float_input("  Shareholders Equity (Cr)"),
                'total_debt': get_float_input("  Total Debt (Cr)"),
            }
            income_statements[year] = {
                'total_revenue': get_float_input("  Total Revenue (Cr)"),
                'cost_of_revenue': get_float_input("  Cost of Revenue (Cr)"),
                'operating_income': get_float_input("  Operating Income (Cr)", allow_negative=True),
                'interest_expense': get_float_input("  Interest Expense (Cr)"),
                'net_income': get_float_input("  Net Income (Cr)", allow_negative=True),
            }
            if year == 'fy_2022':
                cash_flows[year] = collect_cash_flow(label)
            per_share_data[year] = {
                'eps': get_float_input("  EPS (Rs.)", allow_negative=True),
                'bvps': get_float_input("  Book Value Per Share (Rs.)"),
            }
    
    # Analyst estimates (optional)
    print("\n" + "="*70)
    print("STEP 3: ANALYST ESTIMATES (Optional)")
    print("="*70)
    
    estimates = {
        'expected_eps_growth_5y': get_float_input("Expected EPS Growth (5Y %) [Optional]"),
        'analyst_target_price': get_float_input("Analyst Target Price (Rs.) [Optional]"),
        'number_of_analysts': int(get_float_input("Number of Analysts Covering [Optional]")),
        'recommendation': input("Recommendation (Buy/Hold/Sell) [Optional]: ").strip() or 'N/A',
    }
    
    # Compile all data
    eternal_data = {
        'company_info': company_info,
        'balance_sheet': balance_sheets,
        'income_statement': income_statements,
        'cash_flow': cash_flows,
        'per_share_data': per_share_data,
        'estimates': estimates,
    }
    
    # Save to file
    output_file = 'eternal_ltd_real_data.py'
    save_data_to_file(eternal_data, output_file)
    
    print("\n" + "="*70)
    print("✓ DATA COLLECTION COMPLETE!")
    print("="*70)
    print(f"\nData saved to: {output_file}")
    print("\nYou can now run the analysis using this data:")
    print("  python main.py")
    
    return eternal_data


def save_data_to_file(data, filename):
    """Save collected data to a Python file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('Real Financial Data for Eternal Ltd\n')
        f.write(f'Data collected on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        f.write('Source: Manual Entry via Interactive Tool\n')
        f.write('"""\n\n')
        f.write('ETERNAL_DATA = ')
        f.write(format_dict(data, indent=0))
        f.write('\n\n')
        f.write('if __name__ == "__main__":\n')
        f.write('    print(f"Company: {ETERNAL_DATA[\'company_info\'][\'company_name\']}")\n')
        f.write('    print(f"Ticker: {ETERNAL_DATA[\'company_info\'][\'ticker\']}")\n')
        f.write('    print(f"Current Price: Rs.{ETERNAL_DATA[\'company_info\'][\'current_price\']:.2f}")\n')
        f.write('    print(f"Market Cap: Rs.{ETERNAL_DATA[\'company_info\'][\'market_cap\']:.0f} Cr")\n')


def format_dict(d, indent=0):
    """Format dictionary for Python file output"""
    lines = ['{\n']
    indent_str = '    ' * (indent + 1)
    
    for key, value in d.items():
        if isinstance(value, dict):
            lines.append(f"{indent_str}'{key}': {format_dict(value, indent + 1)},\n")
        elif isinstance(value, str):
            lines.append(f"{indent_str}'{key}': '{value}',\n")
        elif isinstance(value, (int, float)):
            lines.append(f"{indent_str}'{key}': {value},\n")
        else:
            lines.append(f"{indent_str}'{key}': {repr(value)},\n")
    
    lines.append('    ' * indent + '}')
    return ''.join(lines)


if __name__ == "__main__":
    print("\n🚀 Starting Interactive Data Collection...")
    print("\nNOTE: Have your financial data ready from:")
    print("  - Annual Report PDF")
    print("  - Screener.in page")
    print("  - MoneyControl page")
    print("\nPress Ctrl+C anytime to cancel.\n")
    
    try:
        data = collect_all_data_interactive()
        print("\n✓ Success! Data collection completed.")
    except KeyboardInterrupt:
        print("\n\n⚠ Data collection cancelled by user.")
    except Exception as e:
        print(f"\n\n✗ Error: {str(e)}")
