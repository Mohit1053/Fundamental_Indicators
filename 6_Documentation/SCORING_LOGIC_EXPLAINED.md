# EXACT SCORING METHODOLOGY - As Per Your Requirements

## Overview
This document explains the EXACT scoring formula implemented for the Fundamental Stock Analysis System.

---

## ✅ CORRECT FORMULA (As You Specified)

### Final Score Calculation:
```
Final Score = Σ (Normalized_Score_i × Weight_i)

Where:
- i = 1 to 14 (all individual metrics)
- Normalized_Score_i = Score for metric i on 0-100 scale
- Weight_i = Individual weight for metric i
```

### This is a **DIRECT WEIGHTED SUM**, NOT category-based averaging!

---

## Weight Distribution (Your Exact Specifications)

### Category 1: Financial Health (Total: 20%)
| Metric | Weight | Calculation |
|--------|--------|-------------|
| Debt-to-Equity Ratio | 7% (0.07) | Lower is better |
| Current Ratio | 7% (0.07) | Higher is better |
| Interest Coverage Ratio | 6% (0.06) | Higher is better |
| **Category Total** | **20%** | |

### Category 2: Profitability (Total: 25%)
| Metric | Weight | Calculation |
|--------|--------|-------------|
| Return on Equity (ROE) | 8% (0.08) | Higher is better |
| Return on Invested Capital (ROIC) | 9% (0.09) | Higher is better |
| Net Profit Margin | 8% (0.08) | Higher is better |
| **Category Total** | **25%** | |

### Category 3: Growth (Total: 25%)
| Metric | Weight | Calculation |
|--------|--------|-------------|
| Revenue Growth (3-Year Avg) | 10% (0.10) | Higher is better |
| EPS Growth (3-Year Avg) | 10% (0.10) | Higher is better |
| Free Cash Flow Growth | 5% (0.05) | Higher is better |
| **Category Total** | **25%** | |

### Category 4: Valuation (Total: 20%)
| Metric | Weight | Calculation |
|--------|--------|-------------|
| Price-to-Earnings (P/E) Ratio | 7% (0.07) | Lower is better |
| Price-to-Book (P/B) Ratio | 7% (0.07) | Lower is better |
| PEG Ratio | 6% (0.06) | Lower is better |
| **Category Total** | **20%** | |

### Category 5: Efficiency (Total: 10%)
| Metric | Weight | Calculation |
|--------|--------|-------------|
| Asset Turnover Ratio | 5% (0.05) | Higher is better |
| Inventory Turnover | 5% (0.05) | Higher is better |
| **Category Total** | **10%** | |

### **Grand Total: 100%** ✓

---

## Step-by-Step Calculation Example

### Step 1: Calculate Raw Metrics
Example for Debt-to-Equity:
```
Total Debt = Rs. 500 Cr
Shareholders Equity = Rs. 2,000 Cr
Debt-to-Equity Ratio = 500 / 2,000 = 0.25
```

### Step 2: Normalize to 0-100 Scale
Each metric is normalized based on ideal ranges:

**For "Lower is Better" metrics (e.g., Debt-to-Equity):**
- If value ≤ Ideal Min (0.0) → Score = 100
- If value between Ideal Min and Ideal Max (0.0 to 0.5) → Score = 80-100 (linear)
- If value between Ideal Max and Acceptable Max (0.5 to 2.0) → Score = 40-80 (linear)
- If value > Acceptable Max → Score < 40 (declining)

**For "Higher is Better" metrics (e.g., ROE):**
- If value ≥ Ideal Max (30%) → Score = 100
- If value between Ideal Min and Ideal Max (15% to 30%) → Score = 80-100 (linear)
- If value between Acceptable Min and Ideal Min (5% to 15%) → Score = 40-80 (linear)
- If value < Acceptable Min → Score < 40 (declining)

**Example:**
```
Debt-to-Equity = 0.25
Ideal range: 0.0 to 0.5 (lower is better)
Position in range: 0.25 / 0.5 = 50%
Normalized Score = 100 - (50% of 20) = 90/100
```

### Step 3: Apply Individual Weight
```
Weighted Contribution = Normalized Score × Weight
= 90 × 0.07
= 6.30
```

### Step 4: Repeat for All 14 Metrics
```
Metric 1 (D/E):           90 × 0.07 = 6.30
Metric 2 (Current Ratio): 85 × 0.07 = 5.95
Metric 3 (Interest Cov):  95 × 0.06 = 5.70
Metric 4 (ROE):          100 × 0.08 = 8.00
Metric 5 (ROIC):         100 × 0.09 = 9.00
Metric 6 (NPM):           88 × 0.08 = 7.04
Metric 7 (Rev Growth):    82 × 0.10 = 8.20
Metric 8 (EPS Growth):    86 × 0.10 = 8.60
Metric 9 (FCF Growth):    92 × 0.05 = 4.60
Metric 10 (P/E):          94 × 0.07 = 6.58
Metric 11 (P/B):          74 × 0.07 = 5.18
Metric 12 (PEG):          97 × 0.06 = 5.82
Metric 13 (Asset Turn):   85 × 0.05 = 4.25
Metric 14 (Inv Turn):    100 × 0.05 = 5.00
```

### Step 5: Sum All Contributions
```
Final Score = 6.30 + 5.95 + 5.70 + 8.00 + 9.00 + 7.04 
            + 8.20 + 8.60 + 4.60 + 6.58 + 5.18 + 5.82 
            + 4.25 + 5.00
            = 90.22/100
```

---

## Important Notes

### ❌ INCORRECT Method (What We're NOT Doing):
```
Step 1: Calculate category averages
Financial Health = (90 + 85 + 95) / 3 = 90
Profitability = (100 + 100 + 88) / 3 = 96
...

Step 2: Apply category weights
Final = (90 × 0.20) + (96 × 0.25) + ...
```

### ✅ CORRECT Method (What We ARE Doing):
```
Final Score = (90 × 0.07) + (85 × 0.07) + (95 × 0.06) 
            + (100 × 0.08) + (100 × 0.09) + (88 × 0.08)
            + ... (all 14 metrics)
```

---

## Category Scores (For Information Only)

Category scores are shown for visualization and understanding, but they **DO NOT** affect the final calculation.

**Category Contribution Calculation:**
```
Category Contribution = Sum of (Normalized Score × Weight) for all metrics in that category

Example for Financial Health:
= (90 × 0.07) + (85 × 0.07) + (95 × 0.06)
= 6.30 + 5.95 + 5.70
= 17.95 out of maximum possible 20
```

**Category Performance:**
```
Performance % = (Actual Contribution / Max Possible) × 100
= (17.95 / 20) × 100
= 89.75%
```

---

## Verification

### Sum of All Weights = 100% ✓
```
Financial Health: 7% + 7% + 6% = 20%
Profitability:    8% + 9% + 8% = 25%
Growth:          10% + 10% + 5% = 25%
Valuation:        7% + 7% + 6% = 20%
Efficiency:       5% + 5% = 10%
TOTAL:                            100%
```

### Maximum Possible Score = 100
```
If all 14 metrics score 100/100:
Final Score = (100 × 0.07) + (100 × 0.07) + ... + (100 × 0.05)
            = 100 × (0.07 + 0.07 + 0.06 + ... + 0.05)
            = 100 × 1.00
            = 100 ✓
```

### Minimum Possible Score = 0
```
If all 14 metrics score 0/100:
Final Score = (0 × 0.07) + (0 × 0.07) + ... + (0 × 0.05)
            = 0 ✓
```

---

## Output Format

The system will show:

1. **Individual Metric Scores:**
   ```
   Debt-to-Equity Ratio:
     Raw Value: 0.25
     Normalized Score: 90.0/100
     Weight: 7%
     Contribution to Final Score: 6.30
   ```

2. **Category Summary (Informational):**
   ```
   Financial Health (20% weight):
     Total Contribution: 17.95
     Max Possible: 20.00
     Performance: 89.75%
   ```

3. **Final Score Calculation Table:**
   ```
   Metric                    Normalized   Weight   Contribution
   -----------------------------------------------------------
   Debt-to-Equity Ratio         90.00      7.0%       6.30
   Current Ratio                85.00      7.0%       5.95
   ...
   -----------------------------------------------------------
   TOTAL FINAL SCORE                                 90.22/100
   ```

---

## Next Steps

Once you provide the actual financial data for **Eternal Ltd (ETERNAL.NS)**, the system will:

1. ✅ Calculate all 14 raw metrics from financial statements
2. ✅ Normalize each to 0-100 scale using ideal ranges
3. ✅ Multiply by individual weights (exactly as you specified)
4. ✅ Sum all 14 weighted contributions = Final Score
5. ✅ Show detailed breakdown for transparency

**Please provide the financial data, and I'll run the complete analysis!**
