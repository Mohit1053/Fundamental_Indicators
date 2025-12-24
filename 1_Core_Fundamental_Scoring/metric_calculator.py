"""
Metric Calculator Module
Calculates all 14 fundamental indicators for stock analysis
"""

import pandas as pd
import numpy as np
from typing import Dict, Optional, Tuple


class FundamentalMetricsCalculator:
    """Calculate fundamental metrics from financial data"""
    
    def __init__(self, financial_data: Dict):
        """
        Initialize calculator with financial data
        
        Args:
            financial_data: Dictionary containing balance sheet, income statement,
                          cash flow, and company info
        """
        self.data = financial_data
        self.metrics = {}
        
    def calculate_all_metrics(self) -> Dict:
        """Calculate all 14 fundamental metrics"""
        print("\n" + "="*70)
        print("CALCULATING FUNDAMENTAL METRICS")
        print("="*70 + "\n")
        
        # Financial Health Metrics (20%)
        print("1. Financial Health Metrics")
        print("-" * 40)
        self.metrics['debt_to_equity'] = self.calculate_debt_to_equity()
        self.metrics['current_ratio'] = self.calculate_current_ratio()
        self.metrics['interest_coverage'] = self.calculate_interest_coverage()
        
        # Profitability Metrics (25%)
        print("\n2. Profitability Metrics")
        print("-" * 40)
        self.metrics['roe'] = self.calculate_roe()
        self.metrics['roic'] = self.calculate_roic()
        self.metrics['net_profit_margin'] = self.calculate_net_profit_margin()
        
        # Growth Metrics (25%)
        print("\n3. Growth Metrics")
        print("-" * 40)
        self.metrics['revenue_growth_3y'] = self.calculate_revenue_growth_3y()
        self.metrics['eps_growth_3y'] = self.calculate_eps_growth_3y()
        self.metrics['fcf_growth'] = self.calculate_fcf_growth()
        
        # Valuation Metrics (20%)
        print("\n4. Valuation Metrics")
        print("-" * 40)
        self.metrics['pe_ratio'] = self.calculate_pe_ratio()
        self.metrics['pb_ratio'] = self.calculate_pb_ratio()
        self.metrics['peg_ratio'] = self.calculate_peg_ratio()
        
        # Efficiency Metrics (10%)
        print("\n5. Efficiency Metrics")
        print("-" * 40)
        self.metrics['asset_turnover'] = self.calculate_asset_turnover()
        self.metrics['inventory_turnover'] = self.calculate_inventory_turnover()
        
        print("\n" + "="*70)
        print("âœ“ ALL METRICS CALCULATED SUCCESSFULLY")
        print("="*70 + "\n")
        
        return self.metrics
    
    # ==================== FINANCIAL HEALTH METRICS ====================
    
    def calculate_debt_to_equity(self) -> float:
        """Calculate Debt-to-Equity Ratio (Lower is better)"""
        bs_2024 = self.data['balance_sheet']['fy_2024']
        total_debt = bs_2024['total_debt']
        shareholders_equity = bs_2024['shareholders_equity']
        
        ratio = total_debt / shareholders_equity
        print(f"  Debt-to-Equity Ratio: {ratio:.2f}")
        print(f"    Total Debt: â‚¹{total_debt:.0f} Cr")
        print(f"    Shareholders Equity: â‚¹{shareholders_equity:.0f} Cr")
        return ratio
    
    def calculate_current_ratio(self) -> float:
        """Calculate Current Ratio (Higher is better)"""
        bs_2024 = self.data['balance_sheet']['fy_2024']
        current_assets = bs_2024['current_assets']
        current_liabilities = bs_2024['current_liabilities']
        
        ratio = current_assets / current_liabilities
        print(f"  Current Ratio: {ratio:.2f}")
        print(f"    Current Assets: â‚¹{current_assets:.0f} Cr")
        print(f"    Current Liabilities: â‚¹{current_liabilities:.0f} Cr")
        return ratio
    
    def calculate_interest_coverage(self) -> float:
        """Calculate Interest Coverage Ratio (Higher is better)"""
        inc_2024 = self.data['income_statement']['fy_2024']
        ebit = inc_2024['operating_income']
        interest_expense = inc_2024['interest_expense']
        
        if interest_expense == 0:
            ratio = float('inf')  # No interest expense
        else:
            ratio = ebit / interest_expense
        
        print(f"  Interest Coverage Ratio: {ratio:.2f}x")
        print(f"    EBIT: â‚¹{ebit:.0f} Cr")
        print(f"    Interest Expense: â‚¹{interest_expense:.0f} Cr")
        return ratio
    
    # ==================== PROFITABILITY METRICS ====================
    
    def calculate_roe(self) -> float:
        """Calculate Return on Equity (Higher is better)"""
        inc_2024 = self.data['income_statement']['fy_2024']
        bs_2024 = self.data['balance_sheet']['fy_2024']
        bs_2023 = self.data['balance_sheet']['fy_2023']
        
        net_income = inc_2024['net_income']
        equity_current = bs_2024['shareholders_equity']
        equity_previous = bs_2023['shareholders_equity']
        avg_equity = (equity_current + equity_previous) / 2
        
        roe = (net_income / avg_equity) * 100
        print(f"  Return on Equity (ROE): {roe:.2f}%")
        print(f"    Net Income: â‚¹{net_income:.0f} Cr")
        print(f"    Average Equity: â‚¹{avg_equity:.0f} Cr")
        return roe
    
    def calculate_roic(self) -> float:
        """Calculate Return on Invested Capital (Higher is better)"""
        inc_2024 = self.data['income_statement']['fy_2024']
        bs_2024 = self.data['balance_sheet']['fy_2024']
        
        # Calculate NOPAT (Net Operating Profit After Tax)
        ebit = inc_2024['operating_income']
        tax_rate = inc_2024['income_tax_expense'] / inc_2024['pretax_income']
        nopat = ebit * (1 - tax_rate)
        
        # Calculate Invested Capital
        total_equity = bs_2024['shareholders_equity']
        total_debt = bs_2024['total_debt']
        cash = bs_2024['cash_and_equivalents']
        invested_capital = total_equity + total_debt - cash
        
        roic = (nopat / invested_capital) * 100
        print(f"  Return on Invested Capital (ROIC): {roic:.2f}%")
        print(f"    NOPAT: â‚¹{nopat:.0f} Cr")
        print(f"    Invested Capital: â‚¹{invested_capital:.0f} Cr")
        return roic
    
    def calculate_net_profit_margin(self) -> float:
        """Calculate Net Profit Margin (Higher is better)"""
        inc_2024 = self.data['income_statement']['fy_2024']
        net_income = inc_2024['net_income']
        total_revenue = inc_2024['total_revenue']
        
        npm = (net_income / total_revenue) * 100
        print(f"  Net Profit Margin: {npm:.2f}%")
        print(f"    Net Income: â‚¹{net_income:.0f} Cr")
        print(f"    Total Revenue: â‚¹{total_revenue:.0f} Cr")
        return npm
    
    # ==================== GROWTH METRICS ====================
    
    def calculate_revenue_growth_3y(self) -> float:
        """Calculate 3-Year Average Revenue Growth (Higher is better)"""
        inc_2024 = self.data['income_statement']['fy_2024']
        inc_2023 = self.data['income_statement']['fy_2023']
        inc_2022 = self.data['income_statement']['fy_2022']
        inc_2021 = self.data['income_statement']['fy_2021']
        
        revenues = [
            inc_2024['total_revenue'],
            inc_2023['total_revenue'],
            inc_2022['total_revenue'],
            inc_2021['total_revenue']
        ]
        
        # Calculate year-over-year growth rates
        growth_rates = []
        for i in range(len(revenues) - 1):
            growth = ((revenues[i] - revenues[i+1]) / revenues[i+1]) * 100
            growth_rates.append(growth)
        
        avg_growth = sum(growth_rates) / len(growth_rates)
        print(f"  3-Year Average Revenue Growth: {avg_growth:.2f}%")
        print(f"    FY24 Revenue: â‚¹{revenues[0]:.0f} Cr")
        print(f"    FY23 Revenue: â‚¹{revenues[1]:.0f} Cr")
        print(f"    FY22 Revenue: â‚¹{revenues[2]:.0f} Cr")
        print(f"    FY21 Revenue: â‚¹{revenues[3]:.0f} Cr")
        print(f"    YoY Growth Rates: {[f'{g:.1f}%' for g in growth_rates]}")
        return avg_growth
    
    def calculate_eps_growth_3y(self) -> float:
        """Calculate 3-Year Average EPS Growth (Higher is better)"""
        eps_data = self.data['per_share_data']
        eps_values = [
            eps_data['fy_2024']['eps'],
            eps_data['fy_2023']['eps'],
            eps_data['fy_2022']['eps'],
            eps_data['fy_2021']['eps']
        ]
        
        # Calculate year-over-year growth rates
        growth_rates = []
        for i in range(len(eps_values) - 1):
            growth = ((eps_values[i] - eps_values[i+1]) / eps_values[i+1]) * 100
            growth_rates.append(growth)
        
        avg_growth = sum(growth_rates) / len(growth_rates)
        print(f"  3-Year Average EPS Growth: {avg_growth:.2f}%")
        print(f"    FY24 EPS: â‚¹{eps_values[0]:.2f}")
        print(f"    FY23 EPS: â‚¹{eps_values[1]:.2f}")
        print(f"    FY22 EPS: â‚¹{eps_values[2]:.2f}")
        print(f"    FY21 EPS: â‚¹{eps_values[3]:.2f}")
        print(f"    YoY Growth Rates: {[f'{g:.1f}%' for g in growth_rates]}")
        return avg_growth
    
    def calculate_fcf_growth(self) -> float:
        """Calculate Free Cash Flow Growth (Higher is better)"""
        cf_2024 = self.data['cash_flow']['fy_2024']
        cf_2023 = self.data['cash_flow']['fy_2023']
        
        fcf_current = cf_2024['free_cash_flow']
        fcf_previous = cf_2023['free_cash_flow']
        
        fcf_growth = ((fcf_current - fcf_previous) / fcf_previous) * 100
        print(f"  Free Cash Flow Growth: {fcf_growth:.2f}%")
        print(f"    FY24 FCF: â‚¹{fcf_current:.0f} Cr")
        print(f"    FY23 FCF: â‚¹{fcf_previous:.0f} Cr")
        return fcf_growth
    
    # ==================== VALUATION METRICS ====================
    
    def calculate_pe_ratio(self) -> float:
        """Calculate Price-to-Earnings Ratio (Lower is better)"""
        current_price = self.data['company_info']['current_price']
        eps = self.data['per_share_data']['fy_2024']['eps']
        
        pe_ratio = current_price / eps
        print(f"  Price-to-Earnings (P/E) Ratio: {pe_ratio:.2f}x")
        print(f"    Current Price: â‚¹{current_price:.2f}")
        print(f"    EPS (TTM): â‚¹{eps:.2f}")
        return pe_ratio
    
    def calculate_pb_ratio(self) -> float:
        """Calculate Price-to-Book Ratio (Lower is better)"""
        current_price = self.data['company_info']['current_price']
        book_value_per_share = self.data['per_share_data']['fy_2024']['book_value_per_share']
        
        pb_ratio = current_price / book_value_per_share
        print(f"  Price-to-Book (P/B) Ratio: {pb_ratio:.2f}x")
        print(f"    Current Price: â‚¹{current_price:.2f}")
        print(f"    Book Value Per Share: â‚¹{book_value_per_share:.2f}")
        return pb_ratio
    
    def calculate_peg_ratio(self) -> float:
        """Calculate PEG Ratio (Lower is better)"""
        pe_ratio = self.metrics.get('pe_ratio') or self.calculate_pe_ratio()
        eps_growth = self.metrics.get('eps_growth_3y') or self.calculate_eps_growth_3y()
        
        if eps_growth <= 0:
            peg_ratio = float('inf')  # No growth or negative growth
        else:
            peg_ratio = pe_ratio / eps_growth
        
        print(f"  PEG Ratio: {peg_ratio:.2f}")
        print(f"    P/E Ratio: {pe_ratio:.2f}x")
        print(f"    EPS Growth Rate: {eps_growth:.2f}%")
        return peg_ratio
    
    # ==================== EFFICIENCY METRICS ====================
    
    def calculate_asset_turnover(self) -> float:
        """Calculate Asset Turnover Ratio (Higher is better)"""
        inc_2024 = self.data['income_statement']['fy_2024']
        bs_2024 = self.data['balance_sheet']['fy_2024']
        bs_2023 = self.data['balance_sheet']['fy_2023']
        
        revenue = inc_2024['total_revenue']
        assets_current = bs_2024['total_assets']
        assets_previous = bs_2023['total_assets']
        avg_assets = (assets_current + assets_previous) / 2
        
        asset_turnover = revenue / avg_assets
        print(f"  Asset Turnover Ratio: {asset_turnover:.2f}x")
        print(f"    Revenue: â‚¹{revenue:.0f} Cr")
        print(f"    Average Total Assets: â‚¹{avg_assets:.0f} Cr")
        return asset_turnover
    
    def calculate_inventory_turnover(self) -> float:
        """Calculate Inventory Turnover (Higher is better)"""
        inc_2024 = self.data['income_statement']['fy_2024']
        bs_2024 = self.data['balance_sheet']['fy_2024']
        bs_2023 = self.data['balance_sheet']['fy_2023']
        
        cogs = inc_2024['cost_of_revenue']
        inventory_current = bs_2024['inventory']
        inventory_previous = bs_2023['inventory']
        avg_inventory = (inventory_current + inventory_previous) / 2
        
        if avg_inventory == 0:
            inventory_turnover = float('inf')  # Service company with no inventory
            print(f"  Inventory Turnover: N/A (Service Company)")
        else:
            inventory_turnover = cogs / avg_inventory
            print(f"  Inventory Turnover: {inventory_turnover:.2f}x")
            print(f"    COGS: â‚¹{cogs:.0f} Cr")
            print(f"    Average Inventory: â‚¹{avg_inventory:.0f} Cr")
        
        return inventory_turnover
    
    def get_metrics_summary(self) -> pd.DataFrame:
        """Get a summary of all metrics as a DataFrame"""
        if not self.metrics:
            self.calculate_all_metrics()
        
        summary_data = {
            'Category': [],
            'Metric': [],
            'Value': [],
            'Weight': []
        }
        
        # Financial Health
        summary_data['Category'].extend(['Financial Health'] * 3)
        summary_data['Metric'].extend(['Debt-to-Equity Ratio', 'Current Ratio', 'Interest Coverage Ratio'])
        summary_data['Value'].extend([
            f"{self.metrics['debt_to_equity']:.2f}",
            f"{self.metrics['current_ratio']:.2f}",
            f"{self.metrics['interest_coverage']:.2f}x"
        ])
        summary_data['Weight'].extend(['7%', '7%', '6%'])
        
        # Profitability
        summary_data['Category'].extend(['Profitability'] * 3)
        summary_data['Metric'].extend(['Return on Equity (ROE)', 'Return on Invested Capital (ROIC)', 'Net Profit Margin'])
        summary_data['Value'].extend([
            f"{self.metrics['roe']:.2f}%",
            f"{self.metrics['roic']:.2f}%",
            f"{self.metrics['net_profit_margin']:.2f}%"
        ])
        summary_data['Weight'].extend(['8%', '9%', '8%'])
        
        # Growth
        summary_data['Category'].extend(['Growth'] * 3)
        summary_data['Metric'].extend(['Revenue Growth (3Y Avg)', 'EPS Growth (3Y Avg)', 'FCF Growth'])
        summary_data['Value'].extend([
            f"{self.metrics['revenue_growth_3y']:.2f}%",
            f"{self.metrics['eps_growth_3y']:.2f}%",
            f"{self.metrics['fcf_growth']:.2f}%"
        ])
        summary_data['Weight'].extend(['10%', '10%', '5%'])
        
        # Valuation
        summary_data['Category'].extend(['Valuation'] * 3)
        summary_data['Metric'].extend(['P/E Ratio', 'P/B Ratio', 'PEG Ratio'])
        summary_data['Value'].extend([
            f"{self.metrics['pe_ratio']:.2f}x",
            f"{self.metrics['pb_ratio']:.2f}x",
            f"{self.metrics['peg_ratio']:.2f}"
        ])
        summary_data['Weight'].extend(['7%', '7%', '6%'])
        
        # Efficiency
        summary_data['Category'].extend(['Efficiency'] * 2)
        summary_data['Metric'].extend(['Asset Turnover Ratio', 'Inventory Turnover'])
        summary_data['Value'].extend([
            f"{self.metrics['asset_turnover']:.2f}x",
            f"{self.metrics['inventory_turnover']:.2f}x" if self.metrics['inventory_turnover'] != float('inf') else "N/A"
        ])
        summary_data['Weight'].extend(['5%', '5%'])
        
        return pd.DataFrame(summary_data)


if __name__ == "__main__":
    # Test with sample data
    from sample_data import ETERNAL_DATA
    
    calculator = FundamentalMetricsCalculator(ETERNAL_DATA)
    metrics = calculator.calculate_all_metrics()
    
    print("\n" + "="*70)
    print("METRICS SUMMARY")
    print("="*70)
    summary_df = calculator.get_metrics_summary()
    print(summary_df.to_string(index=False))
