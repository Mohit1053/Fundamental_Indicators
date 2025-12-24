"""
Report Generator Module
Creates comprehensive reports with visualizations and Excel export
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from typing import Dict
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10


class ReportGenerator:
    """Generate comprehensive fundamental analysis reports"""
    
    def __init__(self, company_info: Dict, metrics: Dict, scores: Dict, 
                 category_scores: Dict, final_score: float):
        """
        Initialize report generator
        
        Args:
            company_info: Company information dictionary
            metrics: Raw metrics dictionary
            scores: Normalized scores dictionary
            category_scores: Category scores dictionary
            final_score: Final weighted score
        """
        self.company_info = company_info
        self.metrics = metrics
        self.scores = scores
        self.category_scores = category_scores
        self.final_score = final_score
        self.report_date = datetime.now().strftime('%Y-%m-%d')
        
    def print_header(self):
        """Print report header"""
        print("\n" + "="*80)
        print(" " * 20 + "FUNDAMENTAL ANALYSIS REPORT")
        print("="*80)
        print(f"\nCompany: {self.company_info['company_name']}")
        print(f"Ticker: {self.company_info['ticker']}")
        print(f"Sector: {self.company_info['sector']}")
        print(f"Current Price: â‚¹{self.company_info['current_price']:.2f}")
        print(f"Market Cap: â‚¹{self.company_info['market_cap']/10000000:.0f} Crores")
        print(f"Report Date: {self.report_date}")
        print("="*80 + "\n")
    
    def print_executive_summary(self):
        """Print executive summary"""
        print("EXECUTIVE SUMMARY")
        print("-" * 80)
        print(f"\nFundamental Score: {self.final_score:.1f}/100")
        
        if self.final_score >= 80:
            recommendation = "STRONG BUY"
            summary = "Excellent fundamentals across all categories. Strong financial health, high profitability, robust growth, and good efficiency."
        elif self.final_score >= 60:
            recommendation = "BUY"
            summary = "Good fundamentals with solid performance in most categories. Some minor areas of concern but overall strong company."
        elif self.final_score >= 40:
            recommendation = "HOLD"
            summary = "Mixed fundamentals. Company shows strength in some areas but has notable weaknesses requiring attention."
        elif self.final_score >= 20:
            recommendation = "SELL"
            summary = "Below average fundamentals. Significant concerns across multiple categories suggest caution."
        else:
            recommendation = "STRONG SELL"
            summary = "Poor fundamentals. Weak performance across most categories indicates high risk."
        
        print(f"Recommendation: {recommendation}")
        print(f"\nSummary: {summary}")
        print("\n" + "-" * 80 + "\n")
    
    def print_category_summary(self):
        """Print category-wise summary"""
        print("CATEGORY SCORES")
        print("-" * 80)
        
        # Sort categories by score
        sorted_categories = sorted(
            self.category_scores.items(),
            key=lambda x: x[1]['score'],
            reverse=True
        )
        
        print(f"{'Category':<25} {'Score':<15} {'Weight':<15} {'Rating':<20}")
        print("-" * 80)
        
        for category_name, data in sorted_categories:
            score = data['score']
            weight = data['weight'] * 100
            
            if score >= 80:
                rating = "Excellent â­â­â­â­â­"
            elif score >= 60:
                rating = "Good â­â­â­â­"
            elif score >= 40:
                rating = "Average â­â­â­"
            elif score >= 20:
                rating = "Below Avg â­â­"
            else:
                rating = "Poor â­"
            
            print(f"{category_name:<25} {score:>6.1f}/100{'':>5} {weight:>6.0f}%{'':>7} {rating:<20}")
        
        print("-" * 80 + "\n")
    
    def print_strengths_and_weaknesses(self):
        """Identify and print key strengths and weaknesses"""
        print("KEY STRENGTHS & WEAKNESSES")
        print("-" * 80)
        
        # Sort metrics by normalized score
        sorted_metrics = sorted(
            self.scores.items(),
            key=lambda x: x[1]['normalized_score'],
            reverse=True
        )
        
        # Top 3 strengths
        print("\nTop 3 Strengths:")
        for i, (metric_name, data) in enumerate(sorted_metrics[:3], 1):
            metric_display = metric_name.replace('_', ' ').title()
            print(f"  {i}. {metric_display}: {data['normalized_score']:.1f}/100 ({data['interpretation']})")
        
        # Top 3 weaknesses
        print("\nTop 3 Weaknesses:")
        for i, (metric_name, data) in enumerate(sorted_metrics[-3:], 1):
            metric_display = metric_name.replace('_', ' ').title()
            print(f"  {i}. {metric_display}: {data['normalized_score']:.1f}/100 ({data['interpretation']})")
        
        print("\n" + "-" * 80 + "\n")
    
    def create_visualizations(self, save_path='eternal_analysis.png'):
        """Create comprehensive visualization dashboard"""
        fig = plt.figure(figsize=(16, 12))
        gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
        
        # 1. Category Scores Bar Chart
        ax1 = fig.add_subplot(gs[0, 0])
        categories = list(self.category_scores.keys())
        scores = [self.category_scores[cat]['score'] for cat in categories]
        colors = ['#2ecc71' if s >= 60 else '#f39c12' if s >= 40 else '#e74c3c' for s in scores]
        
        bars = ax1.barh(categories, scores, color=colors, alpha=0.7)
        ax1.set_xlabel('Score (0-100)', fontweight='bold')
        ax1.set_title('Category Scores', fontweight='bold', fontsize=12)
        ax1.set_xlim(0, 100)
        
        # Add value labels
        for i, (bar, score) in enumerate(zip(bars, scores)):
            ax1.text(score + 2, i, f'{score:.1f}', va='center', fontweight='bold')
        
        # Add grid
        ax1.grid(axis='x', alpha=0.3)
        
        # 2. Radar Chart for Categories
        ax2 = fig.add_subplot(gs[0, 1], projection='polar')
        categories_radar = list(self.category_scores.keys())
        scores_radar = [self.category_scores[cat]['score'] for cat in categories_radar]
        
        # Complete the circle
        scores_radar += scores_radar[:1]
        angles = np.linspace(0, 2 * np.pi, len(categories_radar), endpoint=False).tolist()
        angles += angles[:1]
        
        ax2.plot(angles, scores_radar, 'o-', linewidth=2, color='#3498db')
        ax2.fill(angles, scores_radar, alpha=0.25, color='#3498db')
        ax2.set_xticks(angles[:-1])
        ax2.set_xticklabels(categories_radar, fontsize=9)
        ax2.set_ylim(0, 100)
        ax2.set_yticks([20, 40, 60, 80, 100])
        ax2.set_title('Category Radar Chart', fontweight='bold', fontsize=12, pad=20)
        ax2.grid(True)
        
        # 3. Individual Metrics Heatmap
        ax3 = fig.add_subplot(gs[1, :])
        
        # Prepare data for heatmap
        metric_names = []
        metric_scores = []
        metric_categories = []
        
        for metric_name, data in self.scores.items():
            metric_display = metric_name.replace('_', ' ').title()
            metric_names.append(metric_display)
            metric_scores.append(data['normalized_score'])
            metric_categories.append(data['category'])
        
        # Sort by category
        sorted_indices = sorted(range(len(metric_categories)), key=lambda i: metric_categories[i])
        metric_names = [metric_names[i] for i in sorted_indices]
        metric_scores = [metric_scores[i] for i in sorted_indices]
        metric_categories = [metric_categories[i] for i in sorted_indices]
        
        # Create heatmap data
        heatmap_data = np.array(metric_scores).reshape(1, -1)
        
        # Custom colormap
        cmap = sns.diverging_palette(10, 130, as_cmap=True)
        
        sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap=cmap, 
                   xticklabels=metric_names, yticklabels=['Score'],
                   cbar_kws={'label': 'Score (0-100)'}, ax=ax3,
                   vmin=0, vmax=100, linewidths=0.5)
        
        ax3.set_title('Individual Metric Scores', fontweight='bold', fontsize=12)
        ax3.set_xticklabels(metric_names, rotation=45, ha='right', fontsize=8)
        
        # 4. Score Distribution
        ax4 = fig.add_subplot(gs[2, 0])
        score_values = [data['normalized_score'] for data in self.scores.values()]
        
        ax4.hist(score_values, bins=10, color='#3498db', alpha=0.7, edgecolor='black')
        ax4.axvline(self.final_score, color='red', linestyle='--', linewidth=2, 
                   label=f'Final Score: {self.final_score:.1f}')
        ax4.set_xlabel('Score Range', fontweight='bold')
        ax4.set_ylabel('Number of Metrics', fontweight='bold')
        ax4.set_title('Score Distribution', fontweight='bold', fontsize=12)
        ax4.legend()
        ax4.grid(alpha=0.3)
        
        # 5. Weighted Contribution by Category
        ax5 = fig.add_subplot(gs[2, 1])
        categories_pie = list(self.category_scores.keys())
        contributions = [self.category_scores[cat]['score'] * self.category_scores[cat]['weight'] 
                        for cat in categories_pie]
        
        colors_pie = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6']
        wedges, texts, autotexts = ax5.pie(contributions, labels=categories_pie, autopct='%1.1f%%',
                                           colors=colors_pie, startangle=90)
        
        for text in texts:
            text.set_fontsize(9)
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(9)
        
        ax5.set_title('Weighted Contribution to Final Score', fontweight='bold', fontsize=12)
        
        # Overall title
        fig.suptitle(f"{self.company_info['company_name']} - Fundamental Analysis Dashboard\n"
                    f"Final Score: {self.final_score:.1f}/100", 
                    fontsize=16, fontweight='bold', y=0.98)
        
        # Save figure
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✓ Visualization saved to: {save_path}")
        
        # Close the plot to avoid blocking
        plt.close()
    
    def export_to_excel(self, filename='eternal_fundamental_analysis.xlsx'):
        """Export complete analysis to Excel"""
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Sheet 1: Executive Summary
            summary_data = {
                'Item': [
                    'Company Name',
                    'Ticker',
                    'Sector',
                    'Current Price (â‚¹)',
                    'Market Cap (â‚¹ Cr)',
                    'Report Date',
                    '',
                    'Final Fundamental Score',
                    'Rating'
                ],
                'Value': [
                    self.company_info['company_name'],
                    self.company_info['ticker'],
                    self.company_info['sector'],
                    f"â‚¹{self.company_info['current_price']:.2f}",
                    f"â‚¹{self.company_info['market_cap']/10000000:.0f}",
                    self.report_date,
                    '',
                    f"{self.final_score:.1f}/100",
                    'Excellent' if self.final_score >= 80 else 'Good' if self.final_score >= 60 else 'Average'
                ]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Executive Summary', index=False)
            
            # Sheet 2: Category Scores
            category_data = {
                'Category': [],
                'Score (0-100)': [],
                'Weight (%)': [],
                'Weighted Contribution': []
            }
            for cat_name, cat_data in self.category_scores.items():
                category_data['Category'].append(cat_name)
                category_data['Score (0-100)'].append(f"{cat_data['score']:.1f}")
                category_data['Weight (%)'].append(f"{cat_data['weight']*100:.0f}%")
                category_data['Weighted Contribution'].append(f"{cat_data['score'] * cat_data['weight']:.1f}")
            
            category_df = pd.DataFrame(category_data)
            category_df.to_excel(writer, sheet_name='Category Scores', index=False)
            
            # Sheet 3: Individual Metrics
            metrics_data = {
                'Category': [],
                'Metric': [],
                'Raw Value': [],
                'Normalized Score': [],
                'Rating': [],
                'Weight (%)': []
            }
            
            for metric_name, data in self.scores.items():
                metric_display = metric_name.replace('_', ' ').title()
                metrics_data['Category'].append(data['category'])
                metrics_data['Metric'].append(metric_display)
                metrics_data['Raw Value'].append(f"{data['raw_value']:.2f}")
                metrics_data['Normalized Score'].append(f"{data['normalized_score']:.1f}")
                metrics_data['Rating'].append(data['interpretation'])
                metrics_data['Weight (%)'].append(f"{data['weight']*100:.0f}%")
            
            metrics_df = pd.DataFrame(metrics_data)
            metrics_df.to_excel(writer, sheet_name='Individual Metrics', index=False)
            
            # Sheet 4: Raw Financial Data
            financial_data = {
                'Item': [
                    'Total Revenue (FY24)',
                    'Net Income (FY24)',
                    'Total Assets (FY24)',
                    'Shareholders Equity (FY24)',
                    'Total Debt (FY24)',
                    'Free Cash Flow (FY24)',
                    'EPS (FY24)',
                    'Book Value Per Share'
                ],
                'Value (â‚¹ Crores)': [
                    '5,680',
                    '986',
                    '4,250',
                    '2,570',
                    '580',
                    '940',
                    '38.30 (per share)',
                    '99.84 (per share)'
                ]
            }
            financial_df = pd.DataFrame(financial_data)
            financial_df.to_excel(writer, sheet_name='Financial Data', index=False)
        
        print(f"âœ“ Excel report exported to: {filename}")
    
    def generate_complete_report(self):
        """Generate complete report with all components"""
        self.print_header()
        self.print_executive_summary()
        self.print_category_summary()
        self.print_strengths_and_weaknesses()
        
        print("\nGenerating visualizations...")
        self.create_visualizations()
        
        print("\nExporting to Excel...")
        self.export_to_excel()
        
        print("\n" + "="*80)
        print("REPORT GENERATION COMPLETE")
        print("="*80)
        print("\nFiles generated:")
        print("  1. eternal_analysis.png - Visual dashboard")
        print("  2. eternal_fundamental_analysis.xlsx - Detailed Excel report")
        print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    # Test report generation
    from sample_data import ETERNAL_DATA
    from metric_calculator import FundamentalMetricsCalculator
    from scoring_engine import ScoringEngine
    
    # Calculate metrics
    calculator = FundamentalMetricsCalculator(ETERNAL_DATA)
    metrics = calculator.calculate_all_metrics()
    
    # Calculate scores
    scorer = ScoringEngine(metrics)
    scorer.calculate_scores()
    scorer.calculate_category_scores()
    final_score = scorer.calculate_final_score()
    
    # Generate report
    report = ReportGenerator(
        company_info=ETERNAL_DATA['company_info'],
        metrics=metrics,
        scores=scorer.scores,
        category_scores=scorer.category_scores,
        final_score=final_score
    )
    
    report.generate_complete_report()
