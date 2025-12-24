"""
PHASE 1 COMPREHENSIVE ANALYSIS - Reliance Industries
====================================================
Technical Indicators + Statistical Analysis + Performance Attribution

This script implements:
- Part 2: Technical Analysis (Moving Averages, RSI, MACD, Bollinger Bands, ATR, Volume)
- Part 4: Statistical Analysis (Distributions, Risk Metrics, Sharpe, Sortino, VaR)
- Part 8: Performance Attribution (Returns, Streaks, Drawdowns, CAGR)
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("PHASE 1: COMPREHENSIVE TECHNICAL & STATISTICAL ANALYSIS")
print("=" * 80)
print()

# Load data
print("📂 Loading Reliance Industries data...")
import os
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df = pd.read_csv(os.path.join(base_dir, 'Reliance_Industries.csv'))
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y')
df = df.sort_values('Date').reset_index(drop=True)

# Rename columns for easier access
df = df.rename(columns={
    'Open (Unit Curr)': 'Open',
    'High (Unit Curr)': 'High',
    'Low (Unit Curr)': 'Low',
    'Close (Unit Curr)': 'Close',
    "Volume (000's)": 'Volume'
})

print(f"✓ Loaded {len(df):,} trading days from {df['Date'].min().date()} to {df['Date'].max().date()}")
print()

# ============================================================================
# PART 2: TECHNICAL INDICATORS
# ============================================================================
print("=" * 80)
print("PART 2: TECHNICAL INDICATORS")
print("=" * 80)
print()

# 2.1 Moving Averages
print("📊 Calculating Moving Averages...")
df['MA_20'] = df['Close'].rolling(window=20).mean()
df['MA_50'] = df['Close'].rolling(window=50).mean()
df['MA_100'] = df['Close'].rolling(window=100).mean()
df['MA_200'] = df['Close'].rolling(window=200).mean()

# Golden Cross / Death Cross
df['Golden_Cross'] = ((df['MA_50'] > df['MA_200']) & (df['MA_50'].shift(1) <= df['MA_200'].shift(1))).astype(int)
df['Death_Cross'] = ((df['MA_50'] < df['MA_200']) & (df['MA_50'].shift(1) >= df['MA_200'].shift(1))).astype(int)

golden_crosses = df['Golden_Cross'].sum()
death_crosses = df['Death_Cross'].sum()
print(f"   Golden Crosses (50 > 200): {golden_crosses}")
print(f"   Death Crosses (50 < 200): {death_crosses}")

# Current trend
current_price = df['Close'].iloc[-1]
current_ma20 = df['MA_20'].iloc[-1]
current_ma50 = df['MA_50'].iloc[-1]
current_ma200 = df['MA_200'].iloc[-1]

print(f"\n   Current Status:")
print(f"   Price: ₹{current_price:.2f}")
print(f"   MA20: ₹{current_ma20:.2f} ({'Above' if current_price > current_ma20 else 'Below'})")
print(f"   MA50: ₹{current_ma50:.2f} ({'Above' if current_price > current_ma50 else 'Below'})")
print(f"   MA200: ₹{current_ma200:.2f} ({'Above' if current_price > current_ma200 else 'Below'})")
print()

# 2.2 RSI (Relative Strength Index)
print("📊 Calculating RSI (14-period)...")

def calculate_rsi(data, period=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

df['RSI_14'] = calculate_rsi(df['Close'], 14)

# RSI analysis
rsi_overbought = (df['RSI_14'] > 70).sum()
rsi_oversold = (df['RSI_14'] < 30).sum()
current_rsi = df['RSI_14'].iloc[-1]

print(f"   Overbought days (RSI > 70): {rsi_overbought} ({rsi_overbought/len(df)*100:.2f}%)")
print(f"   Oversold days (RSI < 30): {rsi_oversold} ({rsi_oversold/len(df)*100:.2f}%)")
print(f"   Current RSI: {current_rsi:.2f}")
if current_rsi > 70:
    print(f"   Status: 🔴 OVERBOUGHT")
elif current_rsi < 30:
    print(f"   Status: 🟢 OVERSOLD")
else:
    print(f"   Status: 🟡 NEUTRAL")
print()

# 2.3 MACD (Moving Average Convergence Divergence)
print("📊 Calculating MACD...")
exp1 = df['Close'].ewm(span=12, adjust=False).mean()
exp2 = df['Close'].ewm(span=26, adjust=False).mean()
df['MACD'] = exp1 - exp2
df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
df['MACD_Histogram'] = df['MACD'] - df['MACD_Signal']

# MACD crossovers
df['MACD_Bullish_Cross'] = ((df['MACD'] > df['MACD_Signal']) & (df['MACD'].shift(1) <= df['MACD_Signal'].shift(1))).astype(int)
df['MACD_Bearish_Cross'] = ((df['MACD'] < df['MACD_Signal']) & (df['MACD'].shift(1) >= df['MACD_Signal'].shift(1))).astype(int)

macd_bullish = df['MACD_Bullish_Cross'].sum()
macd_bearish = df['MACD_Bearish_Cross'].sum()

print(f"   Bullish MACD Crossovers: {macd_bullish}")
print(f"   Bearish MACD Crossovers: {macd_bearish}")
print(f"   Current MACD: {df['MACD'].iloc[-1]:.2f}")
print(f"   Current Signal: {df['MACD_Signal'].iloc[-1]:.2f}")
print(f"   Current Histogram: {df['MACD_Histogram'].iloc[-1]:.2f}")
print()

# 2.4 Bollinger Bands
print("📊 Calculating Bollinger Bands (20-period, 2 std)...")
df['BB_Middle'] = df['Close'].rolling(window=20).mean()
bb_std = df['Close'].rolling(window=20).std()
df['BB_Upper'] = df['BB_Middle'] + (bb_std * 2)
df['BB_Lower'] = df['BB_Middle'] - (bb_std * 2)
df['BB_Width'] = ((df['BB_Upper'] - df['BB_Lower']) / df['BB_Middle']) * 100

# Bollinger Band analysis
bb_touches_upper = (df['Close'] >= df['BB_Upper']).sum()
bb_touches_lower = (df['Close'] <= df['BB_Lower']).sum()
current_bb_width = df['BB_Width'].iloc[-1]
avg_bb_width = df['BB_Width'].mean()

print(f"   Upper band touches: {bb_touches_upper} ({bb_touches_upper/len(df)*100:.2f}%)")
print(f"   Lower band touches: {bb_touches_lower} ({bb_touches_lower/len(df)*100:.2f}%)")
print(f"   Current BB Width: {current_bb_width:.2f}%")
print(f"   Average BB Width: {avg_bb_width:.2f}%")
if current_bb_width < avg_bb_width * 0.7:
    print(f"   Status: 🔵 SQUEEZE (Low Volatility)")
elif current_bb_width > avg_bb_width * 1.3:
    print(f"   Status: 🔴 EXPANSION (High Volatility)")
else:
    print(f"   Status: 🟡 NORMAL")
print()

# 2.5 ATR (Average True Range)
print("📊 Calculating ATR (14-period)...")
df['H-L'] = df['High'] - df['Low']
df['H-PC'] = abs(df['High'] - df['Close'].shift(1))
df['L-PC'] = abs(df['Low'] - df['Close'].shift(1))
df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)
df['ATR_14'] = df['TR'].rolling(window=14).mean()
df['ATR_Percent'] = (df['ATR_14'] / df['Close']) * 100

current_atr = df['ATR_14'].iloc[-1]
current_atr_pct = df['ATR_Percent'].iloc[-1]
avg_atr_pct = df['ATR_Percent'].mean()

print(f"   Current ATR: ₹{current_atr:.2f}")
print(f"   Current ATR %: {current_atr_pct:.2f}%")
print(f"   Average ATR %: {avg_atr_pct:.2f}%")
print()

# 2.6 Volume Analysis
print("📊 Calculating Volume Indicators...")
df['Volume_MA_20'] = df['Volume'].rolling(window=20).mean()
df['Volume_Ratio'] = df['Volume'] / df['Volume_MA_20']

high_volume_days = (df['Volume_Ratio'] > 2.0).sum()
print(f"   High Volume Days (2x avg): {high_volume_days} ({high_volume_days/len(df)*100:.2f}%)")
print(f"   Current Volume Ratio: {df['Volume_Ratio'].iloc[-1]:.2f}x")
print()

# Save technical indicators
print("💾 Saving technical indicators to CSV...")
technical_cols = ['Date', 'Close', 'MA_20', 'MA_50', 'MA_100', 'MA_200', 
                  'RSI_14', 'MACD', 'MACD_Signal', 'MACD_Histogram',
                  'BB_Upper', 'BB_Middle', 'BB_Lower', 'BB_Width',
                  'ATR_14', 'ATR_Percent', 'Volume', 'Volume_MA_20', 'Volume_Ratio']
technical_df = df[technical_cols].copy()
output_path = os.path.join(base_dir, 'Reliance_Complete_Analysis', '3_Technical_Analysis', 'technical_indicators.csv')
technical_df.to_csv(output_path, index=False)
print("✓ Saved to: 3_Technical_Analysis/technical_indicators.csv")
print()

# ============================================================================
# PART 4: STATISTICAL & RISK ANALYSIS
# ============================================================================
print("=" * 80)
print("PART 4: STATISTICAL & RISK ANALYSIS")
print("=" * 80)
print()

# Calculate daily returns
df['Daily_Return'] = df['Close'].pct_change() * 100

# 4.1 Return Distribution
print("📊 Return Distribution Analysis...")
returns = df['Daily_Return'].dropna()

mean_return = returns.mean()
median_return = returns.median()
std_return = returns.std()
skewness = returns.skew()
kurtosis = returns.kurtosis()

print(f"   Mean Return: {mean_return:.4f}%")
print(f"   Median Return: {median_return:.4f}%")
print(f"   Std Deviation: {std_return:.4f}%")
print(f"   Skewness: {skewness:.4f}", end="")
if skewness > 0:
    print(" (Right-tailed, more large positive returns)")
elif skewness < 0:
    print(" (Left-tailed, more large negative returns)")
else:
    print(" (Symmetric)")

print(f"   Kurtosis: {kurtosis:.4f}", end="")
if kurtosis > 0:
    print(" (Fat tails, more extreme events)")
elif kurtosis < 0:
    print(" (Thin tails, fewer extreme events)")
else:
    print(" (Normal distribution)")
print()

# Percentiles
print("   Return Percentiles:")
percentiles = [1, 5, 10, 25, 50, 75, 90, 95, 99]
for p in percentiles:
    val = np.percentile(returns, p)
    print(f"      {p}th percentile: {val:+.2f}%")
print()

# 4.2 Risk Metrics
print("📊 Risk Metrics...")

# Annualized metrics
trading_days_per_year = 252
annual_return = mean_return * trading_days_per_year
annual_volatility = std_return * np.sqrt(trading_days_per_year)

print(f"   Annualized Return: {annual_return:.2f}%")
print(f"   Annualized Volatility: {annual_volatility:.2f}%")
print()

# Sharpe Ratio (assuming 6% risk-free rate)
risk_free_rate = 6.0
sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility
print(f"   Sharpe Ratio: {sharpe_ratio:.4f}")
if sharpe_ratio > 2:
    print("      Rating: ⭐⭐⭐⭐⭐ Excellent")
elif sharpe_ratio > 1:
    print("      Rating: ⭐⭐⭐⭐ Good")
elif sharpe_ratio > 0:
    print("      Rating: ⭐⭐⭐ Acceptable")
else:
    print("      Rating: ⭐⭐ Poor")
print()

# Sortino Ratio (downside deviation)
downside_returns = returns[returns < 0]
downside_std = downside_returns.std()
annual_downside_std = downside_std * np.sqrt(trading_days_per_year)
sortino_ratio = (annual_return - risk_free_rate) / annual_downside_std

print(f"   Downside Deviation: {annual_downside_std:.2f}%")
print(f"   Sortino Ratio: {sortino_ratio:.4f}")
print()

# Maximum Drawdown
print("📊 Drawdown Analysis...")
df['Cumulative_Return'] = (1 + df['Daily_Return']/100).cumprod()
df['Running_Max'] = df['Cumulative_Return'].cummax()
df['Drawdown'] = ((df['Cumulative_Return'] - df['Running_Max']) / df['Running_Max']) * 100

max_drawdown = df['Drawdown'].min()
max_dd_date = df.loc[df['Drawdown'].idxmin(), 'Date']

print(f"   Maximum Drawdown: {max_drawdown:.2f}%")
print(f"   Max DD Date: {max_dd_date.date()}")
print()

# Calmar Ratio
calmar_ratio = annual_return / abs(max_drawdown)
print(f"   Calmar Ratio: {calmar_ratio:.4f}")
print()

# Value at Risk (VaR)
print("📊 Value at Risk (VaR)...")
var_95 = np.percentile(returns, 5)
var_99 = np.percentile(returns, 1)

print(f"   VaR (95% confidence): {var_95:.2f}%")
print(f"      → 5% chance of losing more than {abs(var_95):.2f}% in a day")
print(f"   VaR (99% confidence): {var_99:.2f}%")
print(f"      → 1% chance of losing more than {abs(var_99):.2f}% in a day")
print()

# Conditional VaR (CVaR / Expected Shortfall)
cvar_95 = returns[returns <= var_95].mean()
cvar_99 = returns[returns <= var_99].mean()

print(f"   CVaR (95%): {cvar_95:.2f}%")
print(f"      → Average loss when in worst 5% of days")
print(f"   CVaR (99%): {cvar_99:.2f}%")
print(f"      → Average loss when in worst 1% of days")
print()

# Win/Loss Statistics
positive_days = (returns > 0).sum()
negative_days = (returns < 0).sum()
flat_days = (returns == 0).sum()
win_rate = positive_days / len(returns) * 100

avg_win = returns[returns > 0].mean()
avg_loss = returns[returns < 0].mean()
win_loss_ratio = abs(avg_win / avg_loss)

print(f"📊 Win/Loss Statistics...")
print(f"   Positive Days: {positive_days} ({win_rate:.2f}%)")
print(f"   Negative Days: {negative_days} ({negative_days/len(returns)*100:.2f}%)")
print(f"   Flat Days: {flat_days}")
print(f"   Average Win: {avg_win:.2f}%")
print(f"   Average Loss: {avg_loss:.2f}%")
print(f"   Win/Loss Ratio: {win_loss_ratio:.2f}")
print()

# ============================================================================
# PART 8: PERFORMANCE ATTRIBUTION
# ============================================================================
print("=" * 80)
print("PART 8: PERFORMANCE ATTRIBUTION")
print("=" * 80)
print()

# 8.1 Period Returns
print("📊 Period-wise Returns...")

# Daily stats (already have)
daily_mean = returns.mean()
daily_median = returns.median()

# Weekly returns
df['Week'] = df['Date'].dt.to_period('W')
weekly_returns = df.groupby('Week')['Daily_Return'].apply(lambda x: ((1 + x/100).prod() - 1) * 100)
weekly_mean = weekly_returns.mean()

# Monthly returns
df['Month'] = df['Date'].dt.to_period('M')
monthly_returns = df.groupby('Month')['Daily_Return'].apply(lambda x: ((1 + x/100).prod() - 1) * 100)
monthly_mean = monthly_returns.mean()

# Yearly returns
df['Year'] = df['Date'].dt.year
yearly_returns = df.groupby('Year')['Daily_Return'].apply(lambda x: ((1 + x/100).prod() - 1) * 100)

print(f"   Daily Average: {daily_mean:.3f}%")
print(f"   Weekly Average: {weekly_mean:.3f}%")
print(f"   Monthly Average: {monthly_mean:.3f}%")
print()

print("   Yearly Returns:")
for year, ret in yearly_returns.items():
    print(f"      {year}: {ret:+.2f}%")
print()

# CAGR
first_price = df['Close'].iloc[0]
last_price = df['Close'].iloc[-1]
years = (df['Date'].iloc[-1] - df['Date'].iloc[0]).days / 365.25
cagr = (((last_price / first_price) ** (1/years)) - 1) * 100

print(f"📊 Compound Annual Growth Rate (CAGR)...")
print(f"   Start Price ({df['Date'].iloc[0].date()}): ₹{first_price:.2f}")
print(f"   End Price ({df['Date'].iloc[-1].date()}): ₹{last_price:.2f}")
print(f"   Time Period: {years:.2f} years")
print(f"   CAGR: {cagr:.2f}%")
print()

# 8.2 Streak Analysis
print("📊 Streak Analysis...")

# Calculate streaks
df['Return_Sign'] = np.where(df['Daily_Return'] > 0, 1, np.where(df['Daily_Return'] < 0, -1, 0))
df['Streak'] = df['Return_Sign'].groupby((df['Return_Sign'] != df['Return_Sign'].shift()).cumsum()).cumcount() + 1
df['Streak'] = df['Streak'] * df['Return_Sign']

# Winning streaks
winning_streaks = df[df['Streak'] > 0]['Streak']
max_win_streak = winning_streaks.max() if len(winning_streaks) > 0 else 0

# Losing streaks
losing_streaks = df[df['Streak'] < 0]['Streak']
max_loss_streak = abs(losing_streaks.min()) if len(losing_streaks) > 0 else 0

print(f"   Longest Winning Streak: {max_win_streak} days")
print(f"   Longest Losing Streak: {max_loss_streak} days")
print()

# Consecutive days probability
prob_up_after_up = len(df[(df['Return_Sign'] == 1) & (df['Return_Sign'].shift(1) == 1)]) / len(df[df['Return_Sign'].shift(1) == 1]) * 100 if len(df[df['Return_Sign'].shift(1) == 1]) > 0 else 0
prob_up_after_down = len(df[(df['Return_Sign'] == 1) & (df['Return_Sign'].shift(1) == -1)]) / len(df[df['Return_Sign'].shift(1) == -1]) * 100 if len(df[df['Return_Sign'].shift(1) == -1]) > 0 else 0

print(f"   Probability of UP after UP day: {prob_up_after_up:.2f}%")
print(f"   Probability of UP after DOWN day: {prob_up_after_down:.2f}%")
print()

# 8.3 Rolling Returns
print("📊 Rolling Returns...")
df['Rolling_30D'] = df['Daily_Return'].rolling(window=30).apply(lambda x: ((1 + x/100).prod() - 1) * 100)
df['Rolling_90D'] = df['Daily_Return'].rolling(window=90).apply(lambda x: ((1 + x/100).prod() - 1) * 100)
df['Rolling_365D'] = df['Daily_Return'].rolling(window=252).apply(lambda x: ((1 + x/100).prod() - 1) * 100)

current_30d = df['Rolling_30D'].iloc[-1]
current_90d = df['Rolling_90D'].iloc[-1]
current_365d = df['Rolling_365D'].iloc[-1]

print(f"   Current 30-day return: {current_30d:.2f}%")
print(f"   Current 90-day return: {current_90d:.2f}%")
print(f"   Current 365-day return: {current_365d:.2f}%")
print()

# Save statistical analysis
print("💾 Saving statistical analysis...")
stats_summary = {
    'Metric': [
        'Mean Daily Return (%)', 'Median Daily Return (%)', 'Std Dev (%)',
        'Skewness', 'Kurtosis', 'Annualized Return (%)', 'Annualized Volatility (%)',
        'Sharpe Ratio', 'Sortino Ratio', 'Max Drawdown (%)', 'Calmar Ratio',
        'VaR 95% (%)', 'VaR 99% (%)', 'CVaR 95% (%)', 'CVaR 99% (%)',
        'Win Rate (%)', 'Avg Win (%)', 'Avg Loss (%)', 'Win/Loss Ratio',
        'Max Win Streak', 'Max Loss Streak', 'CAGR (%)'
    ],
    'Value': [
        mean_return, median_return, std_return,
        skewness, kurtosis, annual_return, annual_volatility,
        sharpe_ratio, sortino_ratio, max_drawdown, calmar_ratio,
        var_95, var_99, cvar_95, cvar_99,
        win_rate, avg_win, avg_loss, win_loss_ratio,
        max_win_streak, max_loss_streak, cagr
    ]
}

stats_df = pd.DataFrame(stats_summary)
stats_df.to_csv(os.path.join(base_dir, 'Reliance_Complete_Analysis', '5_Statistical_Analysis', 'risk_metrics.csv'), index=False)
print("✓ Saved to: 5_Statistical_Analysis/risk_metrics.csv")
print()

# Save distribution analysis
print("💾 Saving distribution analysis...")
distribution_df = pd.DataFrame({
    'Percentile': percentiles,
    'Return (%)': [np.percentile(returns, p) for p in percentiles]
})
distribution_df.to_csv(os.path.join(base_dir, 'Reliance_Complete_Analysis', '5_Statistical_Analysis', 'distribution_analysis.csv'), index=False)
print("✓ Saved to: 5_Statistical_Analysis/distribution_analysis.csv")
print()

# Save performance attribution
print("💾 Saving performance attribution...")
performance_df = pd.DataFrame({
    'Period': ['Daily', 'Weekly', 'Monthly', 'Yearly (Avg)', 'CAGR'],
    'Average_Return (%)': [daily_mean, weekly_mean, monthly_mean, yearly_returns.mean(), cagr]
})
performance_df.to_csv(os.path.join(base_dir, 'Reliance_Complete_Analysis', '8_Performance_Attribution', 'period_returns.csv'), index=False)
print("✓ Saved to: 8_Performance_Attribution/period_returns.csv")
print()

# Save yearly returns
yearly_df = pd.DataFrame({
    'Year': yearly_returns.index,
    'Return (%)': yearly_returns.values
})
yearly_df.to_csv(os.path.join(base_dir, 'Reliance_Complete_Analysis', '8_Performance_Attribution', 'yearly_returns.csv'), index=False)
print("✓ Saved to: 8_Performance_Attribution/yearly_returns.csv")
print()

# Save complete enhanced dataset
print("💾 Saving complete enhanced dataset...")
df.to_csv(os.path.join(base_dir, 'Reliance_Complete_Analysis', '1_Data', 'Reliance_Industries_Enhanced.csv'), index=False)
print("✓ Saved to: 1_Data/Reliance_Industries_Enhanced.csv")
print()

print("=" * 80)
print("✅ PHASE 1 ANALYSIS COMPLETE!")
print("=" * 80)
print()
print("📁 Generated Files:")
print("   • 3_Technical_Analysis/technical_indicators.csv")
print("   • 5_Statistical_Analysis/risk_metrics.csv")
print("   • 5_Statistical_Analysis/distribution_analysis.csv")
print("   • 8_Performance_Attribution/period_returns.csv")
print("   • 8_Performance_Attribution/yearly_returns.csv")
print("   • 1_Data/Reliance_Industries_Enhanced.csv")
print()
print("🎯 Key Findings:")
print(f"   • CAGR (26 years): {cagr:.2f}%")
print(f"   • Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"   • Max Drawdown: {max_drawdown:.2f}%")
print(f"   • Win Rate: {win_rate:.2f}%")
print(f"   • Current RSI: {current_rsi:.2f}")
print()
print("Next: Run visualization scripts to create charts!")
