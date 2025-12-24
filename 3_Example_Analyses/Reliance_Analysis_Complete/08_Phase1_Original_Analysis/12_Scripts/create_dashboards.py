"""
PHASE 1 VISUALIZATION - Technical & Statistical Dashboards
===========================================================
Creates comprehensive visualization dashboards for:
- Technical indicators (Price, MAs, RSI, MACD, Bollinger Bands, Volume, ATR)
- Statistical analysis (Distributions, Drawdowns, Returns, Risk metrics)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (20, 24)
plt.rcParams['font.size'] = 9

print("=" * 80)
print("CREATING TECHNICAL & STATISTICAL VISUALIZATIONS")
print("=" * 80)
print()

# Setup paths
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load data
print("📂 Loading enhanced data...")
df = pd.read_csv(os.path.join(base_dir, 'Reliance_Complete_Analysis', '1_Data', 'Reliance_Industries_Enhanced.csv'))
df['Date'] = pd.to_datetime(df['Date'])
print(f"✓ Loaded {len(df):,} rows")
print()

# ============================================================================
# TECHNICAL ANALYSIS DASHBOARD
# ============================================================================
print("📊 Creating Technical Analysis Dashboard...")

fig1 = plt.figure(figsize=(24, 28))
gs = gridspec.GridSpec(7, 2, figure=fig1, hspace=0.4, wspace=0.3)

# Chart 1: Price with Moving Averages (Full history)
ax1 = fig1.add_subplot(gs[0, :])
ax1.plot(df['Date'], df['Close'], label='Close Price', color='black', linewidth=1.5, alpha=0.7)
ax1.plot(df['Date'], df['MA_20'], label='MA 20', color='blue', linewidth=1, alpha=0.7)
ax1.plot(df['Date'], df['MA_50'], label='MA 50', color='orange', linewidth=1, alpha=0.7)
ax1.plot(df['Date'], df['MA_100'], label='MA 100', color='green', linewidth=1, alpha=0.7)
ax1.plot(df['Date'], df['MA_200'], label='MA 200', color='red', linewidth=1.5, alpha=0.7)

# Mark Golden/Death crosses
golden_crosses = df[df['Golden_Cross'] == 1]
death_crosses = df[df['Death_Cross'] == 1]
ax1.scatter(golden_crosses['Date'], golden_crosses['Close'], color='green', marker='^', s=100, label='Golden Cross', zorder=5)
ax1.scatter(death_crosses['Date'], death_crosses['Close'], color='red', marker='v', s=100, label='Death Cross', zorder=5)

ax1.set_title('Reliance Industries - Price Action with Moving Averages (2000-2025)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price (₹)')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_yscale('log')  # Log scale for better visualization

# Chart 2: Price with Moving Averages (Last 2 years)
ax2 = fig1.add_subplot(gs[1, :])
df_recent = df.tail(504)  # ~2 years
ax2.plot(df_recent['Date'], df_recent['Close'], label='Close Price', color='black', linewidth=2)
ax2.plot(df_recent['Date'], df_recent['MA_20'], label='MA 20', color='blue', linewidth=1.5)
ax2.plot(df_recent['Date'], df_recent['MA_50'], label='MA 50', color='orange', linewidth=1.5)
ax2.plot(df_recent['Date'], df_recent['MA_200'], label='MA 200', color='red', linewidth=1.5)
ax2.fill_between(df_recent['Date'], df_recent['Close'], df_recent['MA_20'], where=(df_recent['Close'] >= df_recent['MA_20']), color='green', alpha=0.1)
ax2.fill_between(df_recent['Date'], df_recent['Close'], df_recent['MA_20'], where=(df_recent['Close'] < df_recent['MA_20']), color='red', alpha=0.1)
ax2.set_title('Recent Price Action (Last 2 Years)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Date')
ax2.set_ylabel('Price (₹)')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Chart 3: RSI (Relative Strength Index)
ax3 = fig1.add_subplot(gs[2, 0])
ax3.plot(df_recent['Date'], df_recent['RSI_14'], color='purple', linewidth=1.5)
ax3.axhline(y=70, color='red', linestyle='--', label='Overbought (70)')
ax3.axhline(y=30, color='green', linestyle='--', label='Oversold (30)')
ax3.axhline(y=50, color='gray', linestyle=':', alpha=0.5)
ax3.fill_between(df_recent['Date'], 70, df_recent['RSI_14'], where=(df_recent['RSI_14'] >= 70), color='red', alpha=0.3)
ax3.fill_between(df_recent['Date'], 30, df_recent['RSI_14'], where=(df_recent['RSI_14'] <= 30), color='green', alpha=0.3)
ax3.set_title('RSI (14-period) - Recent', fontsize=11, fontweight='bold')
ax3.set_xlabel('Date')
ax3.set_ylabel('RSI')
ax3.legend(loc='upper right')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(0, 100)

# Chart 4: MACD
ax4 = fig1.add_subplot(gs[2, 1])
ax4.plot(df_recent['Date'], df_recent['MACD'], label='MACD', color='blue', linewidth=1.5)
ax4.plot(df_recent['Date'], df_recent['MACD_Signal'], label='Signal', color='red', linewidth=1.5)
ax4.bar(df_recent['Date'], df_recent['MACD_Histogram'], label='Histogram', color='gray', alpha=0.3)
ax4.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax4.set_title('MACD - Recent', fontsize=11, fontweight='bold')
ax4.set_xlabel('Date')
ax4.set_ylabel('MACD')
ax4.legend()
ax4.grid(True, alpha=0.3)

# Chart 5: Bollinger Bands (Recent)
ax5 = fig1.add_subplot(gs[3, :])
ax5.plot(df_recent['Date'], df_recent['Close'], label='Close', color='black', linewidth=2)
ax5.plot(df_recent['Date'], df_recent['BB_Upper'], label='Upper Band', color='red', linestyle='--', linewidth=1)
ax5.plot(df_recent['Date'], df_recent['BB_Middle'], label='Middle (MA20)', color='blue', linestyle='--', linewidth=1)
ax5.plot(df_recent['Date'], df_recent['BB_Lower'], label='Lower Band', color='green', linestyle='--', linewidth=1)
ax5.fill_between(df_recent['Date'], df_recent['BB_Upper'], df_recent['BB_Lower'], alpha=0.1, color='gray')
ax5.set_title('Bollinger Bands (20, 2) - Recent', fontsize=12, fontweight='bold')
ax5.set_xlabel('Date')
ax5.set_ylabel('Price (₹)')
ax5.legend()
ax5.grid(True, alpha=0.3)

# Chart 6: Volume Analysis
ax6 = fig1.add_subplot(gs[4, :])
colors = ['green' if df_recent['Daily_Return'].iloc[i] >= 0 else 'red' for i in range(len(df_recent))]
ax6.bar(df_recent['Date'], df_recent['Volume'], color=colors, alpha=0.6)
ax6.plot(df_recent['Date'], df_recent['Volume_MA_20'], label='Volume MA 20', color='blue', linewidth=2)
ax6.set_title('Volume Analysis (Green=Up day, Red=Down day)', fontsize=12, fontweight='bold')
ax6.set_xlabel('Date')
ax6.set_ylabel('Volume (000s)')
ax6.legend()
ax6.grid(True, alpha=0.3, axis='y')

# Chart 7: ATR (Average True Range)
ax7 = fig1.add_subplot(gs[5, 0])
ax7.plot(df_recent['Date'], df_recent['ATR_Percent'], color='darkorange', linewidth=1.5)
ax7.axhline(y=df['ATR_Percent'].mean(), color='blue', linestyle='--', label=f'Avg: {df["ATR_Percent"].mean():.2f}%')
ax7.set_title('ATR % (Volatility)', fontsize=11, fontweight='bold')
ax7.set_xlabel('Date')
ax7.set_ylabel('ATR %')
ax7.legend()
ax7.grid(True, alpha=0.3)

# Chart 8: Bollinger Band Width
ax8 = fig1.add_subplot(gs[5, 1])
ax8.plot(df_recent['Date'], df_recent['BB_Width'], color='purple', linewidth=1.5)
ax8.axhline(y=df['BB_Width'].mean(), color='blue', linestyle='--', label=f'Avg: {df["BB_Width"].mean():.2f}%')
ax8.fill_between(df_recent['Date'], df_recent['BB_Width'], alpha=0.3, color='purple')
ax8.set_title('Bollinger Band Width (Volatility)', fontsize=11, fontweight='bold')
ax8.set_xlabel('Date')
ax8.set_ylabel('BB Width %')
ax8.legend()
ax8.grid(True, alpha=0.3)

# Chart 9: Cumulative Returns
ax9 = fig1.add_subplot(gs[6, 0])
ax9.plot(df['Date'], df['Cumulative_Return'], color='darkgreen', linewidth=1.5)
ax9.fill_between(df['Date'], 1, df['Cumulative_Return'], alpha=0.3, color='green')
ax9.set_title('Cumulative Returns (₹1 invested in 2000)', fontsize=11, fontweight='bold')
ax9.set_xlabel('Date')
ax9.set_ylabel('Cumulative Return')
ax9.grid(True, alpha=0.3)
ax9.set_yscale('log')

# Chart 10: Drawdown
ax10 = fig1.add_subplot(gs[6, 1])
ax10.fill_between(df['Date'], 0, df['Drawdown'], color='red', alpha=0.4)
ax10.plot(df['Date'], df['Drawdown'], color='darkred', linewidth=1)
ax10.axhline(y=df['Drawdown'].min(), color='red', linestyle='--', label=f'Max DD: {df["Drawdown"].min():.2f}%')
ax10.set_title('Drawdown from Peak (%)', fontsize=11, fontweight='bold')
ax10.set_xlabel('Date')
ax10.set_ylabel('Drawdown %')
ax10.legend()
ax10.grid(True, alpha=0.3)

plt.suptitle('RELIANCE INDUSTRIES - TECHNICAL ANALYSIS DASHBOARD', fontsize=18, fontweight='bold', y=0.995)

output_path = os.path.join(base_dir, 'Reliance_Complete_Analysis', '10_Visualizations', 'technical_analysis_dashboard.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✓ Saved Technical Dashboard: 10_Visualizations/technical_analysis_dashboard.png")
plt.close()

# ============================================================================
# STATISTICAL ANALYSIS DASHBOARD
# ============================================================================
print("📊 Creating Statistical Analysis Dashboard...")

fig2 = plt.figure(figsize=(24, 28))
gs2 = gridspec.GridSpec(7, 2, figure=fig2, hspace=0.4, wspace=0.3)

# Prepare return data
returns = df['Daily_Return'].dropna()

# Chart 1: Return Distribution Histogram
ax1 = fig2.add_subplot(gs2[0, 0])
ax1.hist(returns, bins=100, color='steelblue', alpha=0.7, edgecolor='black')
ax1.axvline(returns.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {returns.mean():.4f}%')
ax1.axvline(returns.median(), color='green', linestyle='--', linewidth=2, label=f'Median: {returns.median():.4f}%')
ax1.set_title('Daily Return Distribution', fontsize=12, fontweight='bold')
ax1.set_xlabel('Daily Return (%)')
ax1.set_ylabel('Frequency')
ax1.legend()
ax1.grid(True, alpha=0.3, axis='y')

# Chart 2: Q-Q Plot (Normality Test)
ax2 = fig2.add_subplot(gs2[0, 1])
from scipy import stats
stats.probplot(returns, dist="norm", plot=ax2)
ax2.set_title('Q-Q Plot (Normality Test)', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)

# Chart 3: Return Distribution Box Plot by Year
ax3 = fig2.add_subplot(gs2[1, :])
yearly_returns = []
years = []
for year in sorted(df['Year'].unique()):
    year_data = df[df['Year'] == year]['Daily_Return'].dropna()
    if len(year_data) > 0:
        yearly_returns.append(year_data.values)
        years.append(int(year))

bp = ax3.boxplot(yearly_returns, labels=years, patch_artist=True)
for patch in bp['boxes']:
    patch.set_facecolor('lightblue')
ax3.axhline(y=0, color='red', linestyle='--', linewidth=1)
ax3.set_title('Daily Returns Distribution by Year', fontsize=12, fontweight='bold')
ax3.set_xlabel('Year')
ax3.set_ylabel('Daily Return (%)')
ax3.grid(True, alpha=0.3, axis='y')
ax3.tick_params(axis='x', rotation=45)

# Chart 4: Cumulative Return by Year
ax4 = fig2.add_subplot(gs2[2, :])
yearly_perf = pd.read_csv(os.path.join(base_dir, 'Reliance_Complete_Analysis', '8_Performance_Attribution', 'yearly_returns.csv'))
colors = ['green' if x > 0 else 'red' for x in yearly_perf['Return (%)']]
ax4.bar(yearly_perf['Year'], yearly_perf['Return (%)'], color=colors, alpha=0.7, edgecolor='black')
ax4.axhline(y=0, color='black', linewidth=1)
ax4.set_title('Annual Returns (%)', fontsize=12, fontweight='bold')
ax4.set_xlabel('Year')
ax4.set_ylabel('Return (%)')
ax4.grid(True, alpha=0.3, axis='y')
ax4.tick_params(axis='x', rotation=45)

# Chart 5: Rolling Volatility
ax5 = fig2.add_subplot(gs2[3, :])
df['Rolling_Vol_30'] = df['Daily_Return'].rolling(window=30).std() * np.sqrt(252)
df['Rolling_Vol_90'] = df['Daily_Return'].rolling(window=90).std() * np.sqrt(252)
ax5.plot(df['Date'], df['Rolling_Vol_30'], label='30-day Annualized Vol', color='blue', linewidth=1, alpha=0.7)
ax5.plot(df['Date'], df['Rolling_Vol_90'], label='90-day Annualized Vol', color='red', linewidth=1.5)
ax5.axhline(y=df['Daily_Return'].std() * np.sqrt(252), color='green', linestyle='--', label='Overall Ann. Vol')
ax5.set_title('Rolling Volatility (Annualized)', fontsize=12, fontweight='bold')
ax5.set_xlabel('Date')
ax5.set_ylabel('Volatility (%)')
ax5.legend()
ax5.grid(True, alpha=0.3)

# Chart 6: Win/Loss Heatmap by Month and Year
ax6 = fig2.add_subplot(gs2[4, :])
df_copy = df.copy()
df_copy['YearMonth'] = df_copy['Date'].dt.to_period('M')
monthly_returns = df_copy.groupby('YearMonth')['Daily_Return'].apply(lambda x: ((1 + x/100).prod() - 1) * 100)
monthly_returns_df = monthly_returns.reset_index()
monthly_returns_df['Year'] = monthly_returns_df['YearMonth'].dt.year
monthly_returns_df['Month'] = monthly_returns_df['YearMonth'].dt.month

pivot_table = monthly_returns_df.pivot(index='Year', columns='Month', values='Daily_Return')
sns.heatmap(pivot_table, cmap='RdYlGn', center=0, annot=False, fmt='.1f', cbar_kws={'label': 'Return (%)'}, ax=ax6)
ax6.set_title('Monthly Returns Heatmap (Year x Month)', fontsize=12, fontweight='bold')
ax6.set_xlabel('Month')
ax6.set_ylabel('Year')

# Chart 7: Drawdown Over Time
ax7 = fig2.add_subplot(gs2[5, :])
ax7.fill_between(df['Date'], 0, df['Drawdown'], color='red', alpha=0.4)
ax7.plot(df['Date'], df['Drawdown'], color='darkred', linewidth=1)
ax7.set_title('Drawdown from Peak Over Time', fontsize=12, fontweight='bold')
ax7.set_xlabel('Date')
ax7.set_ylabel('Drawdown %')
ax7.grid(True, alpha=0.3)

# Chart 8: Return Percentiles
ax8 = fig2.add_subplot(gs2[6, 0])
dist_data = pd.read_csv(os.path.join(base_dir, 'Reliance_Complete_Analysis', '5_Statistical_Analysis', 'distribution_analysis.csv'))
ax8.plot(dist_data['Percentile'], dist_data['Return (%)'], marker='o', color='darkblue', linewidth=2)
ax8.axhline(y=0, color='red', linestyle='--')
ax8.fill_between(dist_data['Percentile'], 0, dist_data['Return (%)'], alpha=0.3, color='blue')
ax8.set_title('Return Percentiles', fontsize=11, fontweight='bold')
ax8.set_xlabel('Percentile')
ax8.set_ylabel('Return (%)')
ax8.grid(True, alpha=0.3)

# Chart 9: Risk Metrics Summary
ax9 = fig2.add_subplot(gs2[6, 1])
risk_data = pd.read_csv(os.path.join(base_dir, 'Reliance_Complete_Analysis', '5_Statistical_Analysis', 'risk_metrics.csv'))

# Display key metrics
key_metrics = risk_data[risk_data['Metric'].isin([
    'Annualized Return (%)', 'Annualized Volatility (%)', 'Sharpe Ratio', 
    'Sortino Ratio', 'Max Drawdown (%)', 'Win Rate (%)', 'CAGR (%)'
])]

y_pos = np.arange(len(key_metrics))
colors = ['green' if v > 0 else 'red' for v in key_metrics['Value']]

ax9.barh(y_pos, key_metrics['Value'], color=colors, alpha=0.7, edgecolor='black')
ax9.set_yticks(y_pos)
ax9.set_yticklabels(key_metrics['Metric'])
ax9.set_xlabel('Value')
ax9.set_title('Key Risk Metrics Summary', fontsize=11, fontweight='bold')
ax9.grid(True, alpha=0.3, axis='x')

# Add values on bars
for i, v in enumerate(key_metrics['Value']):
    ax9.text(v, i, f' {v:.2f}', va='center', fontweight='bold')

plt.suptitle('RELIANCE INDUSTRIES - STATISTICAL ANALYSIS DASHBOARD', fontsize=18, fontweight='bold', y=0.995)

output_path2 = os.path.join(base_dir, 'Reliance_Complete_Analysis', '10_Visualizations', 'statistical_analysis_dashboard.png')
plt.savefig(output_path2, dpi=300, bbox_inches='tight')
print(f"✓ Saved Statistical Dashboard: 10_Visualizations/statistical_analysis_dashboard.png")
plt.close()

print()
print("=" * 80)
print("✅ VISUALIZATION CREATION COMPLETE!")
print("=" * 80)
print()
print("📁 Generated Files:")
print("   • 10_Visualizations/technical_analysis_dashboard.png")
print("   • 10_Visualizations/statistical_analysis_dashboard.png")
print()
