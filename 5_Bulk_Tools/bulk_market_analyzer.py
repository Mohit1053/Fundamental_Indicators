"""
Bulk Market Analyzer
Analyzes multiple companies from Ace Equity data
Supports batch processing for entire market/index analysis
"""

import pandas as pd
import numpy as np
from typing import List, Dict
import os
from pathlib import Path
from metric_calculator import FundamentalMetricsCalculator
from scoring_engine import FundamentalScorer
from datetime import datetime
import json


class BulkMarketAnalyzer:
    """Analyze multiple companies and rank them"""
    
    def __init__(self, output_dir: str = "market_analysis"):
        """
        Initialize bulk analyzer
        
        Args:
            output_dir: Directory to save analysis results
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.results = []
        
    def analyze_company(self, company_data: Dict) -> Dict:
        """
        Analyze a single company
        
        Args:
            company_data: Financial data dictionary for one company
            
        Returns:
            Dictionary with company info, metrics, and scores
        """
        try:
            # Calculate metrics
            calculator = FundamentalMetricsCalculator(company_data)
            metrics = calculator.calculate_all_metrics()
            
            # Calculate scores
            scorer = FundamentalScorer(metrics)
            normalized_scores = scorer.calculate_normalized_scores()
            category_scores, final_score, rating = scorer.calculate_final_score(normalized_scores)
            
            # Prepare result
            result = {
                'company_info': company_data['company_info'],
                'final_score': final_score,
                'rating': rating,
                'category_scores': category_scores,
                'metrics': metrics,
                'normalized_scores': normalized_scores,
                'analysis_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            return result
            
        except Exception as e:
            print(f"❌ Error analyzing {company_data['company_info']['company_name']}: {str(e)}")
            return None
    
    def analyze_market(self, companies_data: List[Dict]) -> pd.DataFrame:
        """
        Analyze multiple companies
        
        Args:
            companies_data: List of company financial data dictionaries
            
        Returns:
            DataFrame with all companies ranked by score
        """
        print("\n" + "="*80)
        print("BULK MARKET ANALYSIS")
        print("="*80)
        print(f"\nAnalyzing {len(companies_data)} companies...")
        
        self.results = []
        successful = 0
        failed = 0
        
        for i, company_data in enumerate(companies_data, 1):
            company_name = company_data['company_info']['company_name']
            print(f"\n[{i}/{len(companies_data)}] Analyzing: {company_name}")
            
            result = self.analyze_company(company_data)
            
            if result:
                self.results.append(result)
                successful += 1
                print(f"✓ Score: {result['final_score']:.2f}/100 - {result['rating']}")
            else:
                failed += 1
        
        print("\n" + "="*80)
        print(f"ANALYSIS COMPLETE: {successful} successful, {failed} failed")
        print("="*80)
        
        # Create summary DataFrame
        return self.create_summary_dataframe()
    
    def create_summary_dataframe(self) -> pd.DataFrame:
        """Create summary DataFrame from results"""
        if not self.results:
            return pd.DataFrame()
        
        summary_data = []
        
        for result in self.results:
            info = result['company_info']
            cat_scores = result['category_scores']
            
            row = {
                'Rank': 0,  # Will be filled after sorting
                'Company': info['company_name'],
                'Symbol': info.get('symbol', 'N/A'),
                'Sector': info.get('sector', 'N/A'),
                'Industry': info.get('industry', 'N/A'),
                'Current Price': info.get('current_price', 0),
                'Market Cap (Cr)': info.get('market_cap', 0),
                'Final Score': result['final_score'],
                'Rating': result['rating'],
                'Financial Health': cat_scores['Financial Health']['score'],
                'Profitability': cat_scores['Profitability']['score'],
                'Growth': cat_scores['Growth']['score'],
                'Valuation': cat_scores['Valuation']['score'],
                'Efficiency': cat_scores['Efficiency']['score'],
            }
            
            summary_data.append(row)
        
        # Create DataFrame and sort by score
        df = pd.DataFrame(summary_data)
        df = df.sort_values('Final Score', ascending=False).reset_index(drop=True)
        df['Rank'] = range(1, len(df) + 1)
        
        # Reorder columns
        cols = ['Rank', 'Company', 'Symbol', 'Sector', 'Industry', 'Current Price', 
                'Market Cap (Cr)', 'Final Score', 'Rating', 'Financial Health', 
                'Profitability', 'Growth', 'Valuation', 'Efficiency']
        df = df[cols]
        
        return df
    
    def save_results(self, summary_df: pd.DataFrame, prefix: str = "market"):
        """
        Save analysis results to files
        
        Args:
            summary_df: Summary DataFrame
            prefix: Prefix for output files
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save summary CSV
        csv_path = os.path.join(self.output_dir, f"{prefix}_summary_{timestamp}.csv")
        summary_df.to_csv(csv_path, index=False)
        print(f"\n✓ Summary saved: {csv_path}")
        
        # Save detailed results as JSON
        json_path = os.path.join(self.output_dir, f"{prefix}_detailed_{timestamp}.json")
        with open(json_path, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)
        print(f"✓ Detailed results saved: {json_path}")
        
        # Save top performers Excel
        excel_path = os.path.join(self.output_dir, f"{prefix}_analysis_{timestamp}.xlsx")
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            # Summary sheet
            summary_df.to_excel(writer, sheet_name='Market Summary', index=False)
            
            # Top 20 companies
            top20 = summary_df.head(20)
            top20.to_excel(writer, sheet_name='Top 20', index=False)
            
            # By sector
            sector_summary = summary_df.groupby('Sector').agg({
                'Final Score': 'mean',
                'Company': 'count'
            }).round(2).sort_values('Final Score', ascending=False)
            sector_summary.columns = ['Average Score', 'Number of Companies']
            sector_summary.to_excel(writer, sheet_name='Sector Analysis')
            
            # Rating distribution
            rating_dist = summary_df['Rating'].value_counts().sort_index()
            rating_dist.to_excel(writer, sheet_name='Rating Distribution')
        
        print(f"✓ Excel report saved: {excel_path}")
        
        return csv_path, json_path, excel_path
    
    def get_top_companies(self, n: int = 10, sector: str = None) -> pd.DataFrame:
        """
        Get top N companies overall or by sector
        
        Args:
            n: Number of top companies to return
            sector: Optional sector filter
            
        Returns:
            DataFrame with top companies
        """
        df = self.create_summary_dataframe()
        
        if sector:
            df = df[df['Sector'] == sector]
        
        return df.head(n)
    
    def get_sector_leaders(self) -> pd.DataFrame:
        """Get the top company from each sector"""
        df = self.create_summary_dataframe()
        
        # Get highest scored company per sector
        leaders = df.loc[df.groupby('Sector')['Final Score'].idxmax()]
        leaders = leaders.sort_values('Final Score', ascending=False).reset_index(drop=True)
        leaders['Rank'] = range(1, len(leaders) + 1)
        
        return leaders


def load_companies_from_csv(csv_path: str) -> List[Dict]:
    """
    Load company data from CSV file exported from Ace Equity
    
    CSV should have columns matching the financial data structure
    See: ace_equity_template.csv for format
    
    Args:
        csv_path: Path to CSV file
        
    Returns:
        List of company data dictionaries
    """
    print(f"\nLoading companies from: {csv_path}")
    
    df = pd.read_csv(csv_path)
    companies_data = []
    
    for idx, row in df.iterrows():
        try:
            company_data = {
                'company_info': {
                    'symbol': row['Symbol'],
                    'company_name': row['Company Name'],
                    'sector': row.get('Sector', 'N/A'),
                    'industry': row.get('Industry', 'N/A'),
                    'current_price': float(row['Current Price']),
                    'market_cap': float(row['Market Cap']),
                },
                'balance_sheet': {
                    'fy_2024': {
                        'total_assets': float(row['Total Assets FY24']),
                        'current_assets': float(row['Current Assets FY24']),
                        'cash_and_equivalents': float(row['Cash FY24']),
                        'inventory': float(row.get('Inventory FY24', 0)),
                        'current_liabilities': float(row['Current Liabilities FY24']),
                        'total_debt': float(row['Total Debt FY24']),
                        'shareholders_equity': float(row['Equity FY24']),
                    },
                    'fy_2023': {
                        'total_assets': float(row['Total Assets FY23']),
                        'shareholders_equity': float(row['Equity FY23']),
                        'total_debt': float(row.get('Total Debt FY23', 0)),
                    },
                    'fy_2022': {
                        'total_assets': float(row.get('Total Assets FY22', 0)),
                        'shareholders_equity': float(row.get('Equity FY22', 0)),
                    },
                    'fy_2021': {
                        'total_assets': float(row.get('Total Assets FY21', 0)),
                        'shareholders_equity': float(row.get('Equity FY21', 0)),
                    },
                },
                'income_statement': {
                    'fy_2024': {
                        'total_revenue': float(row['Revenue FY24']),
                        'cost_of_revenue': float(row['COGS FY24']),
                        'operating_income': float(row['EBIT FY24']),
                        'interest_expense': float(row['Interest FY24']),
                        'pretax_income': float(row['PBT FY24']),
                        'income_tax_expense': float(row['Tax FY24']),
                        'net_income': float(row['Net Profit FY24']),
                    },
                    'fy_2023': {
                        'total_revenue': float(row['Revenue FY23']),
                        'operating_income': float(row.get('EBIT FY23', 0)),
                        'net_income': float(row['Net Profit FY23']),
                    },
                    'fy_2022': {
                        'total_revenue': float(row.get('Revenue FY22', 0)),
                        'net_income': float(row.get('Net Profit FY22', 0)),
                    },
                    'fy_2021': {
                        'total_revenue': float(row.get('Revenue FY21', 0)),
                        'net_income': float(row.get('Net Profit FY21', 0)),
                    },
                },
                'cash_flow': {
                    'fy_2024': {
                        'operating_cash_flow': float(row['OCF FY24']),
                        'capital_expenditure': float(row.get('CapEx FY24', 0)),
                        'free_cash_flow': float(row.get('FCF FY24', 0)),
                    },
                    'fy_2023': {
                        'free_cash_flow': float(row.get('FCF FY23', 0)),
                    },
                },
                'per_share_data': {
                    'fy_2024': {
                        'eps': float(row['EPS FY24']),
                        'book_value_per_share': float(row['BVPS FY24']),
                    },
                    'fy_2023': {
                        'eps': float(row.get('EPS FY23', 0)),
                    },
                    'fy_2022': {
                        'eps': float(row.get('EPS FY22', 0)),
                    },
                    'fy_2021': {
                        'eps': float(row.get('EPS FY21', 0)),
                    },
                },
            }
            
            companies_data.append(company_data)
            
        except Exception as e:
            print(f"❌ Error loading {row.get('Company Name', 'Unknown')}: {str(e)}")
            continue
    
    print(f"✓ Loaded {len(companies_data)} companies successfully")
    return companies_data


if __name__ == "__main__":
    # Example usage
    print("="*80)
    print("BULK MARKET ANALYZER")
    print("="*80)
    print("\nThis tool analyzes multiple companies from Ace Equity data.")
    print("\nUsage:")
    print("1. Export data from Ace Equity to CSV (use ace_equity_template.csv format)")
    print("2. Load and analyze:")
    print("   companies = load_companies_from_csv('your_data.csv')")
    print("   analyzer = BulkMarketAnalyzer()")
    print("   results = analyzer.analyze_market(companies)")
    print("   analyzer.save_results(results)")
    print("\n" + "="*80)
