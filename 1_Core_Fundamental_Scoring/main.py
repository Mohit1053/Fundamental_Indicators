"""
Main Entry Point for Fundamental Stock Analysis System
Analyzes Eternal Ltd / Zomato Limited (Indian Stock)
"""

# Import real Eternal Ltd data
from eternal_ltd_real_data import ETERNAL_DATA
from metric_calculator import FundamentalMetricsCalculator
from scoring_engine import ScoringEngine
from report_generator import ReportGenerator


def print_data_summary():
    """Print summary of the financial data being analyzed"""
    company = ETERNAL_DATA['company_info']
    fy24_income = ETERNAL_DATA['income_statement']['fy_2024']
    fy24_balance = ETERNAL_DATA['balance_sheet']['fy_2024']
    fy24_ps = ETERNAL_DATA['per_share_data']['fy_2024']
    
    print("\n" + "="*70)
    print("ETERNAL LTD (ZOMATO) - REAL FINANCIAL DATA")
    print("="*70)
    print(f"\nCompany: {company['company_name']}")
    print(f"Ticker: {company['ticker']}")
    print(f"Sector: {company['sector']}")
    print(f"Current Price: Rs.{company['current_price']:.2f}")
    print(f"Market Cap: Rs.{company['market_cap']:.0f} Cr")
    
    print(f"\nFY 2024 Financials (in Crores):")
    print(f"  Revenue: Rs.{fy24_income['total_revenue']:.0f} Cr")
    print(f"  Net Income: Rs.{fy24_income['net_income']:.0f} Cr")
    print(f"  Total Assets: Rs.{fy24_balance['total_assets']:.0f} Cr")
    print(f"  Shareholders Equity: Rs.{fy24_balance['shareholders_equity']:.0f} Cr")
    
    print(f"\nPer Share Metrics:")
    print(f"  EPS (FY24): Rs.{fy24_ps['eps']:.2f}")
    print(f"  Book Value Per Share: Rs.{fy24_ps['book_value_per_share']:.2f}")
    
    print("\n" + "="*70)
    print("DATA SOURCE: Screener.in (Real Verified Data)")
    print("="*70)


def main():
    """Main execution function"""
    print("\n" + "="*80)
    print(" " * 15 + "FUNDAMENTAL STOCK ANALYSIS SYSTEM")
    print(" " * 20 + "For Indian Markets (NSE/BSE)")
    print("="*80)
    
    # Display data summary
    print_data_summary()
    
    # Step 1: Calculate Metrics
    print("\n" + "="*80)
    print("STEP 1: CALCULATING FUNDAMENTAL METRICS")
    print("="*80)
    
    calculator = FundamentalMetricsCalculator(ETERNAL_DATA)
    metrics = calculator.calculate_all_metrics()
    
    # Step 2: Calculate Scores
    print("\n" + "="*80)
    print("STEP 2: CALCULATING NORMALIZED SCORES")
    print("="*80)
    
    scorer = ScoringEngine(metrics)
    scores = scorer.calculate_scores()
    category_scores = scorer.calculate_category_scores()
    final_score = scorer.calculate_final_score()
    
    # Step 3: Generate Report
    print("\n" + "="*80)
    print("STEP 3: GENERATING COMPREHENSIVE REPORT")
    print("="*80)
    
    report = ReportGenerator(
        company_info=ETERNAL_DATA['company_info'],
        metrics=metrics,
        scores=scores,
        category_scores=category_scores,
        final_score=final_score
    )
    
    report.generate_complete_report()
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE!")
    print("="*80)
    print("\nYou can now:")
    print("  1. View the visualization: eternal_analysis.png")
    print("  2. Open the Excel report: eternal_fundamental_analysis.xlsx")
    print("  3. Review the terminal output for detailed analysis")
    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    main()
