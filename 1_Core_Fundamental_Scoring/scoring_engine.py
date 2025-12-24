"""
Scoring Engine Module
Normalizes metrics to 0-100 scale and applies weighted scoring
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple


class ScoringEngine:
    """Score and normalize fundamental metrics"""
    
    # Define ideal ranges and scoring direction for each metric
    METRIC_CONFIG = {
        # Financial Health (20%)
        'debt_to_equity': {
            'category': 'Financial Health',
            'weight': 0.07,
            'direction': 'lower',  # Lower is better
            'ideal_min': 0.0,
            'ideal_max': 0.5,
            'acceptable_max': 2.0,
        },
        'current_ratio': {
            'category': 'Financial Health',
            'weight': 0.07,
            'direction': 'higher',  # Higher is better
            'ideal_min': 1.5,
            'ideal_max': 3.0,
            'acceptable_min': 0.5,
        },
        'interest_coverage': {
            'category': 'Financial Health',
            'weight': 0.06,
            'direction': 'higher',
            'ideal_min': 5.0,
            'ideal_max': 20.0,
            'acceptable_min': 1.0,
        },
        
        # Profitability (25%)
        'roe': {
            'category': 'Profitability',
            'weight': 0.08,
            'direction': 'higher',
            'ideal_min': 15.0,
            'ideal_max': 30.0,
            'acceptable_min': 5.0,
        },
        'roic': {
            'category': 'Profitability',
            'weight': 0.09,
            'direction': 'higher',
            'ideal_min': 15.0,
            'ideal_max': 35.0,
            'acceptable_min': 5.0,
        },
        'net_profit_margin': {
            'category': 'Profitability',
            'weight': 0.08,
            'direction': 'higher',
            'ideal_min': 10.0,
            'ideal_max': 25.0,
            'acceptable_min': 3.0,
        },
        
        # Growth (25%)
        'revenue_growth_3y': {
            'category': 'Growth',
            'weight': 0.10,
            'direction': 'higher',
            'ideal_min': 15.0,
            'ideal_max': 30.0,
            'acceptable_min': 5.0,
        },
        'eps_growth_3y': {
            'category': 'Growth',
            'weight': 0.10,
            'direction': 'higher',
            'ideal_min': 15.0,
            'ideal_max': 30.0,
            'acceptable_min': 5.0,
        },
        'fcf_growth': {
            'category': 'Growth',
            'weight': 0.05,
            'direction': 'higher',
            'ideal_min': 10.0,
            'ideal_max': 25.0,
            'acceptable_min': 0.0,
        },
        
        # Valuation (20%)
        'pe_ratio': {
            'category': 'Valuation',
            'weight': 0.07,
            'direction': 'lower',
            'ideal_min': 10.0,
            'ideal_max': 20.0,
            'acceptable_max': 40.0,
        },
        'pb_ratio': {
            'category': 'Valuation',
            'weight': 0.07,
            'direction': 'lower',
            'ideal_min': 1.0,
            'ideal_max': 4.0,
            'acceptable_max': 10.0,
        },
        'peg_ratio': {
            'category': 'Valuation',
            'weight': 0.06,
            'direction': 'lower',
            'ideal_min': 0.5,
            'ideal_max': 1.5,
            'acceptable_max': 3.0,
        },
        
        # Efficiency (10%)
        'asset_turnover': {
            'category': 'Efficiency',
            'weight': 0.05,
            'direction': 'higher',
            'ideal_min': 1.0,
            'ideal_max': 2.5,
            'acceptable_min': 0.5,
        },
        'inventory_turnover': {
            'category': 'Efficiency',
            'weight': 0.05,
            'direction': 'higher',
            'ideal_min': 6.0,
            'ideal_max': 12.0,
            'acceptable_min': 2.0,
        },
    }
    
    def __init__(self, metrics: Dict):
        """
        Initialize scoring engine with calculated metrics
        
        Args:
            metrics: Dictionary of calculated fundamental metrics
        """
        self.metrics = metrics
        self.scores = {}
        self.category_scores = {}
        self.final_score = 0.0
        
    def normalize_metric(self, metric_name: str, value: float) -> Tuple[float, str]:
        """
        Normalize a metric to 0-100 scale
        
        Args:
            metric_name: Name of the metric
            value: Raw metric value
            
        Returns:
            Tuple of (normalized_score, interpretation)
        """
        config = self.METRIC_CONFIG[metric_name]
        direction = config['direction']
        
        # CRITICAL: Treat zero as missing data - always score as 0
        # This prevents missing valuation data from getting perfect scores
        if value == 0:
            return 0.0, 'Missing Data'
        
        # Handle infinity values
        if value == float('inf'):
            if direction == 'higher':
                return 100.0, 'Excellent'
            else:
                return 0.0, 'Poor'
        
        if direction == 'higher':
            # Higher is better (e.g., ROE, Current Ratio)
            ideal_min = config['ideal_min']
            ideal_max = config['ideal_max']
            acceptable_min = config.get('acceptable_min', 0)
            
            if value >= ideal_max:
                score = 100.0
                interpretation = 'Excellent'
            elif value >= ideal_min:
                # Linear interpolation between ideal_min (80) and ideal_max (100)
                score = 80 + ((value - ideal_min) / (ideal_max - ideal_min)) * 20
                interpretation = 'Very Good'
            elif value >= acceptable_min:
                # Linear interpolation between acceptable_min (40) and ideal_min (80)
                score = 40 + ((value - acceptable_min) / (ideal_min - acceptable_min)) * 40
                interpretation = 'Good' if score >= 60 else 'Average'
            else:
                # Below acceptable minimum
                if acceptable_min > 0:
                    score = max(0, (value / acceptable_min) * 40)
                else:
                    score = 0  # If acceptable_min is 0, can't calculate ratio
                interpretation = 'Below Average' if score >= 20 else 'Poor'
        
        else:  # direction == 'lower'
            # Lower is better (e.g., P/E, Debt-to-Equity)
            ideal_min = config['ideal_min']
            ideal_max = config['ideal_max']
            acceptable_max = config.get('acceptable_max', ideal_max * 2)
            
            if value <= ideal_min:
                score = 100.0
                interpretation = 'Excellent'
            elif value <= ideal_max:
                # Linear interpolation between ideal_min (100) and ideal_max (80)
                score = 80 + ((ideal_max - value) / (ideal_max - ideal_min)) * 20
                interpretation = 'Very Good'
            elif value <= acceptable_max:
                # Linear interpolation between ideal_max (80) and acceptable_max (40)
                score = 40 + ((acceptable_max - value) / (acceptable_max - ideal_max)) * 40
                interpretation = 'Good' if score >= 60 else 'Average'
            else:
                # Above acceptable maximum
                score = max(0, 40 * (1 - (value - acceptable_max) / acceptable_max))
                interpretation = 'Below Average' if score >= 20 else 'Poor'
        
        # Ensure score is between 0 and 100
        score = max(0, min(100, score))
        
        return score, interpretation
    
    def calculate_scores(self) -> Dict:
        """Calculate normalized scores for all metrics"""
        print("\n" + "="*70)
        print("CALCULATING NORMALIZED SCORES (0-100 scale)")
        print("="*70 + "\n")
        
        for metric_name, value in self.metrics.items():
            if metric_name in self.METRIC_CONFIG:
                score, interpretation = self.normalize_metric(metric_name, value)
                self.scores[metric_name] = {
                    'raw_value': value,
                    'normalized_score': score,
                    'interpretation': interpretation,
                    'weight': self.METRIC_CONFIG[metric_name]['weight'],
                    'category': self.METRIC_CONFIG[metric_name]['category']
                }
                
                metric_display = metric_name.replace('_', ' ').title()
                print(f"{metric_display}:")
                print(f"  Raw Value: {value:.2f}")
                print(f"  Normalized Score: {score:.1f}/100")
                print(f"  Rating: {interpretation}")
                print()
        
        return self.scores
    
    def calculate_category_scores(self) -> Dict:
        """
        Calculate category scores for informational/visualization purposes
        
        NOTE: Category scores do NOT affect final score calculation.
        Final score = direct sum of individual weighted metrics.
        Category scores shown here are for understanding performance by category.
        """
        print("\n" + "="*70)
        print("CATEGORY SCORES (Informational Only)")
        print("="*70 + "\n")
        
        categories = {
            'Financial Health': {'weight': 0.20, 'metrics': []},
            'Profitability': {'weight': 0.25, 'metrics': []},
            'Growth': {'weight': 0.25, 'metrics': []},
            'Valuation': {'weight': 0.20, 'metrics': []},
            'Efficiency': {'weight': 0.10, 'metrics': []}
        }
        
        # Group metrics by category
        for metric_name, score_data in self.scores.items():
            category = score_data['category']
            categories[category]['metrics'].append(score_data)
        
        # Calculate ACTUAL weighted contribution for each category
        for category_name, category_data in categories.items():
            total_weighted_contribution = 0
            
            for metric in category_data['metrics']:
                # This is the actual contribution to final score
                weighted_contribution = metric['normalized_score'] * metric['weight']
                total_weighted_contribution += weighted_contribution
            
            # Store actual contribution (not averaged, but summed)
            category_score = total_weighted_contribution
            
            self.category_scores[category_name] = {
                'score': category_score,  # This is the contribution, not a 0-100 score
                'weight': category_data['weight'],
                'num_metrics': len(category_data['metrics']),
                'max_possible': category_data['weight'] * 100  # Max if all metrics = 100
            }
            
            # Determine rating based on percentage of max possible
            max_possible = category_data['weight'] * 100
            percentage = (category_score / max_possible * 100) if max_possible > 0 else 0
            
            if percentage >= 80:
                rating = 'Excellent'
            elif percentage >= 60:
                rating = 'Good'
            elif percentage >= 40:
                rating = 'Average'
            elif percentage >= 20:
                rating = 'Below Average'
            else:
                rating = 'Poor'
            
            print(f"{category_name} ({category_data['weight']*100:.0f}% weight):")
            print(f"  Contribution to Final Score: {category_score:.2f}")
            print(f"  Max Possible Contribution: {max_possible:.2f}")
            print(f"  Performance: {percentage:.1f}% of maximum")
            print(f"  Rating: {rating}")
            print(f"  Number of Metrics: {len(category_data['metrics'])}")
            print()
        
        return self.category_scores
    
    def calculate_final_score(self) -> float:
        """
        Calculate the final weighted score
        
        METHOD: Direct weighted sum of all 14 normalized scores
        Formula: Sum(Normalized_Score_i × Weight_i) for all i from 1 to 14
        
        This is NOT category-based averaging, but individual metric weighting.
        """
        if not self.scores:
            self.calculate_scores()
        
        # Calculate final score as direct sum of all weighted individual metrics
        total_score = 0
        
        print("\n" + "="*70)
        print("FINAL SCORE CALCULATION (Direct Weighted Sum)")
        print("="*70)
        print(f"{'Metric':<30} {'Norm Score':<12} {'Weight':<10} {'Contribution':<15}")
        print("-" * 70)
        
        for metric_name, score_data in self.scores.items():
            normalized_score = score_data['normalized_score']
            weight = score_data['weight']
            contribution = normalized_score * weight
            total_score += contribution
            
            metric_display = metric_name.replace('_', ' ').title()
            print(f"{metric_display:<30} {normalized_score:>6.2f}/100   {weight*100:>5.1f}%     {contribution:>6.2f}")
        
        print("-" * 70)
        print(f"{'TOTAL FINAL SCORE':<30} {' '*12} {' '*10} {total_score:>6.2f}/100")
        print("=" * 70)
        
        self.final_score = total_score
        
        # Determine overall rating
        if self.final_score >= 80:
            rating = 'Excellent - Strong fundamentals across the board'
        elif self.final_score >= 60:
            rating = 'Good - Solid company with minor weaknesses'
        elif self.final_score >= 40:
            rating = 'Average - Mixed signals, requires deeper analysis'
        elif self.final_score >= 20:
            rating = 'Below Average - Significant concerns'
        else:
            rating = 'Poor - Weak fundamentals'
        
        print("\n" + "="*70)
        print("FINAL FUNDAMENTAL SCORE")
        print("="*70)
        print(f"\nOverall Score: {self.final_score:.1f}/100")
        print(f"Rating: {rating}")
        print("="*70 + "\n")
        
        return self.final_score
    
    def get_score_breakdown(self) -> pd.DataFrame:
        """Get detailed score breakdown as a DataFrame"""
        if not self.scores:
            self.calculate_scores()
        
        data = {
            'Metric': [],
            'Raw Value': [],
            'Score (0-100)': [],
            'Rating': [],
            'Weight': [],
            'Category': []
        }
        
        for metric_name, score_data in self.scores.items():
            metric_display = metric_name.replace('_', ' ').title()
            data['Metric'].append(metric_display)
            data['Raw Value'].append(f"{score_data['raw_value']:.2f}")
            data['Score (0-100)'].append(f"{score_data['normalized_score']:.1f}")
            data['Rating'].append(score_data['interpretation'])
            data['Weight'].append(f"{score_data['weight']*100:.0f}%")
            data['Category'].append(score_data['category'])
        
        return pd.DataFrame(data)
    
    def get_category_breakdown(self) -> pd.DataFrame:
        """Get category score breakdown as a DataFrame"""
        if not self.category_scores:
            self.calculate_category_scores()
        
        data = {
            'Category': [],
            'Score (0-100)': [],
            'Weight': [],
            'Weighted Contribution': []
        }
        
        for category_name, category_data in self.category_scores.items():
            data['Category'].append(category_name)
            data['Score (0-100)'].append(f"{category_data['score']:.1f}")
            data['Weight'].append(f"{category_data['weight']*100:.0f}%")
            contribution = category_data['score'] * category_data['weight']
            data['Weighted Contribution'].append(f"{contribution:.1f}")
        
        return pd.DataFrame(data)


if __name__ == "__main__":
    # Test with sample data
    from sample_data import ETERNAL_DATA
    from metric_calculator import FundamentalMetricsCalculator
    
    # Calculate metrics
    calculator = FundamentalMetricsCalculator(ETERNAL_DATA)
    metrics = calculator.calculate_all_metrics()
    
    # Calculate scores
    scorer = ScoringEngine(metrics)
    scores = scorer.calculate_scores()
    category_scores = scorer.calculate_category_scores()
    final_score = scorer.calculate_final_score()
    
    # Display breakdown
    print("\nDetailed Score Breakdown:")
    print("-" * 70)
    print(scorer.get_score_breakdown().to_string(index=False))
    
    print("\n\nCategory Breakdown:")
    print("-" * 70)
    print(scorer.get_category_breakdown().to_string(index=False))
