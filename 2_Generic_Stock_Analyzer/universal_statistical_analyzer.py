"""
Universal Stock Statistical Analyzer
=====================================
Comprehensive statistical analysis for ANY stock data.

Calculates:
- Technical indicators (MA, RSI, MACD, Bollinger Bands, ATR)
- Statistical metrics (Sharpe, Sortino, VaR, CVaR, Max Drawdown)
- Performance attribution (CAGR, streaks, yearly returns)

Usage:
    python universal_statistical_analyzer.py --file "Company_Analysis_Complete/00_Master_Data/company_master_data_enhanced.csv" --company "Company Name"
"""

import pandas as pd
import numpy as np
import argparse
import os
import sys
from datetime import datetime

class UniversalStatisticalAnalyzer:
    """Statistical and technical analysis for any stock"""
    
    def __init__(self, csv_file, company_name):
        self.csv_file = csv_file
        self.company_name = company_name
        self.df = None
        self.output_dir = os.path.dirname(os.path.dirname(csv_file))  # Parent of 00_Master_Data
        self.stats_dir = f"{self.output_dir}/10_Statistical_Analysis"
        
    def load_data(self):
        """Load the master data file"""
        print(f"\n{'='*70}")
        print(f"UNIVERSAL STATISTICAL ANALYZER")
        print(f"{'='*70}")
        print(f"Company: {self.company_name}")
        print(f"Input File: {self.csv_file}")
        print(f"{'='*70}\n")
        
        self.df = pd.read_csv(self.csv_file)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df = self.df.sort_values('Date').reset_index(drop=True)
        
        print(f" Loaded {len(self.df):,} rows")
        print(f"  Date Range: {self.df['Date'].min().date()} to {self.df['Date'].max().date()}")
        
        # Create output directory
        os.makedirs(self.stats_dir, exist_ok=True)
        
        return self.df
    
    def calculate_moving_averages(self, periods=[20, 50, 100, 200]):
        """Calculate moving averages"""
        print(f"\n{'='*70}")
        print("CALCULATING MOVING AVERAGES")
        print(f"{'='*70}\n")
        
        for period in periods:
            col_name = f'MA_{period}'
            self.df[col_name] = self.df['Close'].rolling(window=period).mean()
            print(f" {col_name} calculated")
        
        # Save
        output_file = f"{self.stats_dir}/moving_averages.csv"
        ma_cols = ['Date', 'Close'] + [f'MA_{p}' for p in periods]
        self.df[ma_cols].to_csv(output_file, index=False)
        print(f"\n Saved to: {output_file}")
        
        return self.df
    
    def calculate_rsi(self, period=14):
        """Calculate Relative Strength Index"""
        print(f"\n{'='*70}")
        print("CALCULATING RSI (Relative Strength Index)")
        print(f"{'='*70}\n")
        
        delta = self.df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        self.df['RSI'] = 100 - (100 / (1 + rs))
        
        print(f" RSI calculated (period={period})")
        print(f"  Current RSI: {self.df['RSI'].iloc[-1]:.2f}")
        print(f"  Avg RSI: {self.df['RSI'].mean():.2f}")
        
        # Save
        output_file = f"{self.stats_dir}/rsi_data.csv"
        self.df[['Date', 'Close', 'RSI']].to_csv(output_file, index=False)
        print(f"\n Saved to: {output_file}")
        
        return self.df
    
    def calculate_macd(self, fast=12, slow=26, signal=9):
        """Calculate MACD"""
        print(f"\n{'='*70}")
        print("CALCULATING MACD")
        print(f"{'='*70}\n")
        
        exp1 = self.df['Close'].ewm(span=fast, adjust=False).mean()
        exp2 = self.df['Close'].ewm(span=slow, adjust=False).mean()
        
        self.df['MACD'] = exp1 - exp2
        self.df['MACD_Signal'] = self.df['MACD'].ewm(span=signal, adjust=False).mean()
        self.df['MACD_Histogram'] = self.df['MACD'] - self.df['MACD_Signal']
        
        print(f" MACD calculated (fast={fast}, slow={slow}, signal={signal})")
        print(f"  Current MACD: {self.df['MACD'].iloc[-1]:.2f}")
        print(f"  Current Signal: {self.df['MACD_Signal'].iloc[-1]:.2f}")
        
        # Save
        output_file = f"{self.stats_dir}/macd_data.csv"
        self.df[['Date', 'Close', 'MACD', 'MACD_Signal', 'MACD_Histogram']].to_csv(output_file, index=False)
        print(f"\n Saved to: {output_file}")
        
        return self.df
    
    def calculate_bollinger_bands(self, period=20, std_dev=2):
        """Calculate Bollinger Bands"""
        print(f"\n{'='*70}")
        print("CALCULATING BOLLINGER BANDS")
        print(f"{'='*70}\n")
        
        self.df['BB_Middle'] = self.df['Close'].rolling(window=period).mean()
        rolling_std = self.df['Close'].rolling(window=period).std()
        
        self.df['BB_Upper'] = self.df['BB_Middle'] + (rolling_std * std_dev)
        self.df['BB_Lower'] = self.df['BB_Middle'] - (rolling_std * std_dev)
        self.df['BB_Width'] = self.df['BB_Upper'] - self.df['BB_Lower']
        
        print(f" Bollinger Bands calculated (period={period}, std={std_dev})")
        
        # Save
        output_file = f"{self.stats_dir}/bollinger_bands.csv"
        bb_cols = ['Date', 'Close', 'BB_Upper', 'BB_Middle', 'BB_Lower', 'BB_Width']
        self.df[bb_cols].to_csv(output_file, index=False)
        print(f"\n Saved to: {output_file}")
        
        return self.df
    
    def calculate_atr(self, period=14):
        """Calculate Average True Range"""
        print(f"\n{'='*70}")
        print("CALCULATING ATR (Average True Range)")
        print(f"{'='*70}\n")
        
        high_low = self.df['High'] - self.df['Low']
        high_close = np.abs(self.df['High'] - self.df['Close'].shift())
        low_close = np.abs(self.df['Low'] - self.df['Close'].shift())
        
        tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        self.df['ATR'] = tr.rolling(window=period).mean()
        
        print(f" ATR calculated (period={period})")
        print(f"  Current ATR: {self.df['ATR'].iloc[-1]:.2f}")
        print(f"  Avg ATR: {self.df['ATR'].mean():.2f}")
        
        # Save
        output_file = f"{self.stats_dir}/atr_data.csv"
        self.df[['Date', 'High', 'Low', 'Close', 'ATR']].to_csv(output_file, index=False)
        print(f"\n Saved to: {output_file}")
        
        return self.df
    
    def calculate_performance_metrics(self):
        """Calculate comprehensive performance metrics"""
        print(f"\n{'='*70}")
        print("CALCULATING PERFORMANCE METRICS")
        print(f"{'='*70}\n")
        
        returns = self.df['Daily_Return'].dropna()
        
        # Basic metrics
        total_days = len(returns)
        years = (self.df['Date'].max() - self.df['Date'].min()).days / 365.25
        
        # CAGR
        start_price = self.df['Close'].iloc[0]
        end_price = self.df['Close'].iloc[-1]
        cagr = ((end_price / start_price) ** (1/years) - 1) * 100
        
        # Total return
        total_return = ((end_price - start_price) / start_price) * 100
        
        # Annualized volatility
        ann_volatility = returns.std() * np.sqrt(252)
        
        # Sharpe Ratio (assuming 0% risk-free rate)
        sharpe = (returns.mean() * 252) / (returns.std() * np.sqrt(252)) if returns.std() > 0 else 0
        
        # Sortino Ratio (downside deviation)
        downside_returns = returns[returns < 0]
        downside_std = downside_returns.std() * np.sqrt(252)
        sortino = (returns.mean() * 252) / downside_std if downside_std > 0 else 0
        
        # Maximum Drawdown
        cumulative = (1 + returns/100).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max * 100
        max_drawdown = drawdown.min()
        
        # Win/Loss streaks
        win_loss = (returns > 0).astype(int)
        streaks = []
        current_streak = 1
        for i in range(1, len(win_loss)):
            if win_loss.iloc[i] == win_loss.iloc[i-1]:
                current_streak += 1
            else:
                streaks.append(current_streak)
                current_streak = 1
        max_win_streak = max([s for i, s in enumerate(streaks) if win_loss.iloc[i] == 1], default=0)
        max_loss_streak = max([s for i, s in enumerate(streaks) if win_loss.iloc[i] == 0], default=0)
        
        # Compile metrics
        metrics = {
            'Metric': [
                'Total Trading Days',
                'Years Analyzed',
                'Starting Price',
                'Ending Price',
                'Total Return (%)',
                'CAGR (%)',
                'Annualized Volatility (%)',
                'Sharpe Ratio',
                'Sortino Ratio',
                'Maximum Drawdown (%)',
                'Best Day (%)',
                'Worst Day (%)',
                'Average Daily Return (%)',
                'Median Daily Return (%)',
                'Win Rate (%)',
                'Max Win Streak (days)',
                'Max Loss Streak (days)',
            ],
            'Value': [
                total_days,
                f"{years:.2f}",
                f"{start_price:.2f}",
                f"{end_price:.2f}",
                f"{total_return:.2f}",
                f"{cagr:.2f}",
                f"{ann_volatility:.2f}",
                f"{sharpe:.3f}",
                f"{sortino:.3f}",
                f"{max_drawdown:.2f}",
                f"{returns.max():.2f}",
                f"{returns.min():.2f}",
                f"{returns.mean():.3f}",
                f"{returns.median():.3f}",
                f"{(returns > 0).mean() * 100:.2f}",
                max_win_streak,
                max_loss_streak,
            ]
        }
        
        metrics_df = pd.DataFrame(metrics)
        
        # Print key metrics
        print(f" Performance Metrics Calculated:")
        print(f"  CAGR: {cagr:.2f}%")
        print(f"  Sharpe Ratio: {sharpe:.3f}")
        print(f"  Sortino Ratio: {sortino:.3f}")
        print(f"  Max Drawdown: {max_drawdown:.2f}%")
        print(f"  Win Rate: {(returns > 0).mean() * 100:.2f}%")
        
        # Save
        output_file = f"{self.stats_dir}/performance_metrics.csv"
        metrics_df.to_csv(output_file, index=False)
        print(f"\n Saved to: {output_file}")
        
        return metrics_df
    
    def calculate_yearly_returns(self):
        """Calculate year-by-year returns"""
        print(f"\n{'='*70}")
        print("CALCULATING YEARLY RETURNS")
        print(f"{'='*70}\n")
        
        self.df['Year'] = self.df['Date'].dt.year
        
        yearly_data = []
        for year in sorted(self.df['Year'].unique()):
            year_df = self.df[self.df['Year'] == year]
            
            if len(year_df) > 0:
                start_price = year_df['Close'].iloc[0]
                end_price = year_df['Close'].iloc[-1]
                year_return = ((end_price - start_price) / start_price) * 100
                
                yearly_data.append({
                    'Year': year,
                    'Start_Price': start_price,
                    'End_Price': end_price,
                    'Return (%)': year_return,
                    'Trading_Days': len(year_df),
                    'Win_Rate (%)': (year_df['Daily_Return'] > 0).mean() * 100,
                    'Best_Day (%)': year_df['Daily_Return'].max(),
                    'Worst_Day (%)': year_df['Daily_Return'].min(),
                })
                
                print(f" {year}: {year_return:+7.2f}% ({len(year_df)} days)")
        
        yearly_df = pd.DataFrame(yearly_data)
        
        # Save
        output_file = f"{self.stats_dir}/yearly_returns.csv"
        yearly_df.to_csv(output_file, index=False)
        print(f"\n Saved to: {output_file}")
        
        return yearly_df
    
    def calculate_var_cvar(self, confidence=0.95):
        """Calculate Value at Risk and Conditional VaR"""
        print(f"\n{'='*70}")
        print(f"CALCULATING VaR AND CVaR (Confidence: {confidence*100}%)")
        print(f"{'='*70}\n")
        
        returns = self.df['Daily_Return'].dropna()
        
        # VaR
        var = np.percentile(returns, (1 - confidence) * 100)
        
        # CVaR (expected shortfall)
        cvar = returns[returns <= var].mean()
        
        print(f" VaR ({confidence*100}%): {var:.3f}%")
        print(f" CVaR ({confidence*100}%): {cvar:.3f}%")
        print(f"\n  Interpretation:")
        print(f"  - On the worst {(1-confidence)*100}% of days, expect at least {var:.2f}% loss (VaR)")
        print(f"  - When losses exceed VaR, average loss is {cvar:.2f}% (CVaR)")
        
        risk_metrics = pd.DataFrame({
            'Metric': ['VaR (95%)', 'CVaR (95%)'],
            'Value (%)': [var, cvar]
        })
        
        # Save
        output_file = f"{self.stats_dir}/risk_metrics.csv"
        risk_metrics.to_csv(output_file, index=False)
        print(f"\n Saved to: {output_file}")
        
        return risk_metrics
    
    def save_enhanced_data(self):
        """Save the enhanced dataset with all indicators"""
        print(f"\n{'='*70}")
        print("SAVING ENHANCED DATA WITH ALL INDICATORS")
        print(f"{'='*70}\n")
        
        output_file = f"{self.stats_dir}/enhanced_data_with_indicators.csv"
        self.df.to_csv(output_file, index=False)
        
        print(f" Enhanced data saved: {output_file}")
        print(f"  Rows: {len(self.df):,}")
        print(f"  Columns: {len(self.df.columns)}")
        
    def run_complete_analysis(self):
        """Run complete statistical analysis"""
        try:
            self.load_data()
            
            # Technical indicators
            self.calculate_moving_averages([20, 50, 100, 200])
            self.calculate_rsi(14)
            self.calculate_macd(12, 26, 9)
            self.calculate_bollinger_bands(20, 2)
            self.calculate_atr(14)
            
            # Statistical metrics
            self.calculate_performance_metrics()
            self.calculate_yearly_returns()
            self.calculate_var_cvar(0.95)
            
            # Save enhanced data
            self.save_enhanced_data()
            
            print(f"\n{'='*70}")
            print(f" STATISTICAL ANALYSIS COMPLETE!")
            print(f"{'='*70}")
            print(f"\nOutput directory: {self.stats_dir}/")
            print(f"\nGenerated files:")
            print(f"   Moving averages (20, 50, 100, 200)")
            print(f"   RSI (Relative Strength Index)")
            print(f"   MACD indicators")
            print(f"   Bollinger Bands")
            print(f"   ATR (Average True Range)")
            print(f"   Performance metrics (Sharpe, Sortino, etc.)")
            print(f"   Yearly returns breakdown")
            print(f"   Risk metrics (VaR, CVaR)")
            print(f"   Enhanced data with all indicators")
            print(f"{'='*70}\n")
            
            return True
            
        except Exception as e:
            print(f"\n ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Universal Statistical Analyzer - Technical and statistical analysis for any stock',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python universal_statistical_analyzer.py --file "Infosys_Analysis_Complete/00_Master_Data/infosys_master_data_enhanced.csv" --company "Infosys"
  python universal_statistical_analyzer.py --file "TCS_Analysis_Complete/00_Master_Data/tcs_master_data_enhanced.csv" --company "TCS"
        """
    )
    
    parser.add_argument('--file', '-f', required=True,
                       help='Path to master data CSV file')
    parser.add_argument('--company', '-c', required=True,
                       help='Company name for reports')
    
    args = parser.parse_args()
    
    # Validate file exists
    if not os.path.exists(args.file):
        print(f" ERROR: File not found: {args.file}")
        sys.exit(1)
    
    # Run analysis
    analyzer = UniversalStatisticalAnalyzer(args.file, args.company)
    success = analyzer.run_complete_analysis()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

