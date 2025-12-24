"""
Quick Start Script for Bulk Market Analysis
Run this after exporting data from Ace Equity
"""

from bulk_market_analyzer import BulkMarketAnalyzer, load_companies_from_csv
import os


def main():
    print("\n" + "="*80)
    print("QUICK START: BULK MARKET ANALYSIS")
    print("="*80)
    
    # Step 1: Check if data file exists
    data_file = input("\nEnter CSV file path from Ace Equity (or press Enter for template): ").strip()
    
    if not data_file:
        data_file = "ace_equity_template.csv"
        print(f"\nUsing template file: {data_file}")
    
    if not os.path.exists(data_file):
        print(f"\n❌ Error: File not found: {data_file}")
        print("\nPlease:")
        print("1. Export data from Ace Equity")
        print("2. Save as CSV file")
        print("3. Run this script again with the correct path")
        return
    
    # Step 2: Load companies
    print("\n" + "-"*80)
    print("STEP 1: LOADING COMPANIES")
    print("-"*80)
    
    try:
        companies = load_companies_from_csv(data_file)
        
        if not companies:
            print("\n❌ No companies loaded. Please check CSV format.")
            return
        
        print(f"\n✓ Successfully loaded {len(companies)} companies")
        
    except Exception as e:
        print(f"\n❌ Error loading CSV: {str(e)}")
        print("\nPlease check:")
        print("1. CSV format matches ace_equity_template.csv")
        print("2. All required columns are present")
        print("3. No special characters in data")
        return
    
    # Step 3: Analyze
    print("\n" + "-"*80)
    print("STEP 2: ANALYZING COMPANIES")
    print("-"*80)
    print(f"\nThis will analyze {len(companies)} companies...")
    print("Estimated time: ~2 seconds per company")
    
    proceed = input("\nProceed with analysis? (y/n): ").lower()
    
    if proceed != 'y':
        print("\nAnalysis cancelled.")
        return
    
    try:
        analyzer = BulkMarketAnalyzer(output_dir='market_analysis')
        results_df = analyzer.analyze_market(companies)
        
        # Step 4: Save results
        print("\n" + "-"*80)
        print("STEP 3: SAVING RESULTS")
        print("-"*80)
        
        prefix = input("\nEnter prefix for output files (default: 'market'): ").strip()
        if not prefix:
            prefix = 'market'
        
        csv_path, json_path, excel_path = analyzer.save_results(results_df, prefix=prefix)
        
        # Step 5: Display summary
        print("\n" + "="*80)
        print("ANALYSIS COMPLETE!")
        print("="*80)
        
        print("\n📊 SUMMARY STATISTICS")
        print("-"*80)
        print(f"Total Companies Analyzed: {len(results_df)}")
        print(f"Average Score: {results_df['Final Score'].mean():.2f}/100")
        print(f"Highest Score: {results_df['Final Score'].max():.2f}/100")
        print(f"Lowest Score: {results_df['Final Score'].min():.2f}/100")
        
        print("\n📈 RATING DISTRIBUTION")
        print("-"*80)
        rating_counts = results_df['Rating'].value_counts()
        for rating, count in rating_counts.items():
            print(f"{rating}: {count} companies ({count/len(results_df)*100:.1f}%)")
        
        print("\n🏆 TOP 10 COMPANIES")
        print("-"*80)
        top10 = results_df.head(10)
        print(top10[['Rank', 'Company', 'Symbol', 'Final Score', 'Rating']].to_string(index=False))
        
        print("\n📁 OUTPUT FILES")
        print("-"*80)
        print(f"1. Summary CSV: {csv_path}")
        print(f"2. Detailed JSON: {json_path}")
        print(f"3. Excel Report: {excel_path}")
        
        print("\n💡 NEXT STEPS")
        print("-"*80)
        print("1. Open Excel report for detailed analysis")
        print("2. Review top companies for investment")
        print("3. Filter by sector/rating in CSV file")
        print("4. Compare scores across time periods")
        
        # Optional: Show sector leaders
        show_sectors = input("\nShow top company by sector? (y/n): ").lower()
        if show_sectors == 'y':
            print("\n🎯 SECTOR LEADERS")
            print("-"*80)
            leaders = analyzer.get_sector_leaders()
            print(leaders[['Rank', 'Sector', 'Company', 'Final Score', 'Rating']].to_string(index=False))
        
        print("\n" + "="*80)
        print("✓ ANALYSIS COMPLETE")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error during analysis: {str(e)}")
        print("\nPlease check:")
        print("1. Data quality in CSV file")
        print("2. All required financial years present")
        print("3. No negative/zero equity values")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAnalysis interrupted by user.")
    except Exception as e:
        print(f"\n\nUnexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
