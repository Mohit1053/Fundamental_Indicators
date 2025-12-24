# 🔍 HOW SCORES ARE CALCULATED - DETAILED EXPLANATION

## Your Question: Why is P/E Ratio 0/100 and others 100/100?

**Short Answer:** Because Eternal Ltd's P/E ratio is **126.53x**, which is **WAY BEYOND** the acceptable maximum of 40x, scoring it as 0/100 (Poor).

Let me break down EXACTLY how each score is calculated:

---

## 📊 THE NORMALIZATION LOGIC

### Two Types of Metrics:

#### 1. **"Higher is Better"** (ROE, Growth, Margins, etc.)
- Score increases as value increases
- Examples: ROE, Revenue Growth, Current Ratio

#### 2. **"Lower is Better"** (P/E, Debt, Valuation ratios)
- Score increases as value decreases
- Examples: P/E Ratio, Debt-to-Equity, P/B Ratio

---

## 📐 SCORING FORMULA

### For "Lower is Better" Metrics (like P/E Ratio):

```
IF value ≤ ideal_min:           Score = 100 (Excellent)
IF ideal_min < value ≤ ideal_max:  Score = 80-100 (Very Good)
IF ideal_max < value ≤ acceptable_max: Score = 40-80 (Average/Good)
IF value > acceptable_max:      Score = 0-40 (Poor/Below Average)
```

### For "Higher is Better" Metrics (like ROE):

```
IF value ≥ ideal_max:           Score = 100 (Excellent)
IF ideal_min ≤ value < ideal_max:  Score = 80-100 (Very Good)
IF acceptable_min ≤ value < ideal_min: Score = 40-80 (Average/Good)
IF value < acceptable_min:      Score = 0-40 (Poor/Below Average)
```

---

## 🎯 DETAILED CALCULATIONS FOR ETERNAL LTD

### 1. P/E RATIO: 0.00/100 ⚠️

**Your Company's Value:** 126.53x  
**Direction:** Lower is better

**Thresholds:**
- Ideal Min: 10x (Score = 100)
- Ideal Max: 20x (Score = 80)
- Acceptable Max: 40x (Score = 40)
- Your Value: **126.53x**

**Calculation:**
```python
# P/E Ratio Configuration
ideal_min = 10.0
ideal_max = 20.0
acceptable_max = 40.0

# Your value
pe_ratio = 126.53

# Step 1: Check which range
# 126.53 > 40 → Way beyond acceptable max

# Step 2: Calculate score for values > acceptable_max
# Formula: max(0, 40 * (1 - (value - acceptable_max) / acceptable_max))

score = 40 * (1 - (126.53 - 40) / 40)
score = 40 * (1 - 86.53 / 40)
score = 40 * (1 - 2.163)
score = 40 * (-1.163)
score = -46.52

# Step 3: Ensure score is between 0 and 100
score = max(0, -46.52)
score = 0.0
```

**Result:** 0.00/100 (Poor)

**Why?** Your P/E of 126.53x is **3.16 times** the acceptable maximum!

**What this means:**
- Stock is trading at 126.53 times its annual earnings
- Market has priced in MASSIVE future growth expectations
- Any disappointment in growth = sharp price correction
- Very expensive by traditional valuation standards

---

### 2. EPS GROWTH 3Y: 100.00/100 ✅

**Your Company's Value:** 352.93%  
**Direction:** Higher is better

**Thresholds:**
- Acceptable Min: 5% (Score = 40)
- Ideal Min: 15% (Score = 80)
- Ideal Max: 30% (Score = 100)
- Your Value: **352.93%**

**Calculation:**
```python
# EPS Growth Configuration
acceptable_min = 5.0
ideal_min = 15.0
ideal_max = 30.0

# Your value
eps_growth = 352.93

# Step 1: Check which range
# 352.93 ≥ 30 → Way above ideal max!

# Step 2: For values ≥ ideal_max
score = 100.0
```

**Result:** 100.00/100 (Excellent)

**Why?** Your EPS growth of 352.93% is **11.76 times** the ideal maximum!

**What this means:**
- Company's earnings per share grew 353% over 3 years
- Exceptional growth trajectory
- From loss-making to highly profitable
- Justifies high P/E ratio (hence PEG ratio is excellent)

---

### 3. CURRENT RATIO: 100.00/100 ✅

**Your Company's Value:** 20.33x  
**Direction:** Higher is better

**Thresholds:**
- Acceptable Min: 0.5x (Score = 40)
- Ideal Min: 1.5x (Score = 80)
- Ideal Max: 3.0x (Score = 100)
- Your Value: **20.33x**

**Calculation:**
```python
# Current Ratio Configuration
acceptable_min = 0.5
ideal_min = 1.5
ideal_max = 3.0

# Your value
current_ratio = 20.33

# Step 1: Check which range
# 20.33 ≥ 3.0 → Above ideal max

# Step 2: For values ≥ ideal_max
score = 100.0
```

**Result:** 100.00/100 (Excellent)

**Why?** Your current ratio of 20.33x is **6.78 times** the ideal maximum!

**What this means:**
- Rs.20.33 of current assets for every Re.1 of current liabilities
- Extremely strong liquidity position
- Can easily meet short-term obligations
- Massive cash reserves (Rs.27,259 Cr in investments)

---

### 4. INTEREST COVERAGE: 100.00/100 ✅

**Your Company's Value:** 64.85x  
**Direction:** Higher is better

**Thresholds:**
- Acceptable Min: 1.0x (Score = 40)
- Ideal Min: 5.0x (Score = 80)
- Ideal Max: 20.0x (Score = 100)
- Your Value: **64.85x**

**Calculation:**
```python
# Interest Coverage Configuration
acceptable_min = 1.0
ideal_min = 5.0
ideal_max = 20.0

# Your value
interest_coverage = 64.85

# Step 1: Check which range
# 64.85 ≥ 20.0 → Above ideal max

# Step 2: For values ≥ ideal_max
score = 100.0
```

**Result:** 100.00/100 (Excellent)

**Why?** Your interest coverage of 64.85x is **3.24 times** the ideal maximum!

**What this means:**
- EBIT can cover interest expense 64.85 times over
- Virtually zero financial risk
- Can easily service debt obligations
- Debt is so small (Rs.248 Cr) compared to earnings (Rs.1,297 Cr EBIT)

---

### 5. DEBT-TO-EQUITY: 99.72/100 ✅

**Your Company's Value:** 0.01 (or 0.7%)  
**Direction:** Lower is better

**Thresholds:**
- Ideal Min: 0.0 (Score = 100)
- Ideal Max: 0.5 (Score = 80)
- Acceptable Max: 2.0 (Score = 40)
- Your Value: **0.01**

**Calculation:**
```python
# Debt-to-Equity Configuration
ideal_min = 0.0
ideal_max = 0.5
acceptable_max = 2.0

# Your value
debt_to_equity = 0.01

# Step 1: Check which range
# 0.01 is between 0.0 and 0.5 (between ideal_min and ideal_max)

# Step 2: Linear interpolation for "lower is better"
# Formula: 80 + ((ideal_max - value) / (ideal_max - ideal_min)) * 20

score = 80 + ((0.5 - 0.01) / (0.5 - 0.0)) * 20
score = 80 + (0.49 / 0.5) * 20
score = 80 + 0.98 * 20
score = 80 + 19.6
score = 99.6
```

**Result:** 99.72/100 (Very Good) - Small rounding difference in actual calculation

**Why?** Your debt is only 0.7% of equity - almost debt-free!

**What this means:**
- Total debt: Rs.248 Cr
- Total equity: Rs.35,820 Cr
- Debt/Equity = 248 ÷ 35,820 = 0.0069 = 0.69%
- Company has minimal leverage
- Very low financial risk

---

### 6. NET PROFIT MARGIN: 99.88/100 ✅

**Your Company's Value:** 24.91%  
**Direction:** Higher is better

**Thresholds:**
- Acceptable Min: 3% (Score = 40)
- Ideal Min: 10% (Score = 80)
- Ideal Max: 25% (Score = 100)
- Your Value: **24.91%**

**Calculation:**
```python
# Net Profit Margin Configuration
acceptable_min = 3.0
ideal_min = 10.0
ideal_max = 25.0

# Your value
npm = 24.91

# Step 1: Check which range
# 24.91 is between 10 and 25 (between ideal_min and ideal_max)

# Step 2: Linear interpolation
# Formula: 80 + ((value - ideal_min) / (ideal_max - ideal_min)) * 20

score = 80 + ((24.91 - 10.0) / (25.0 - 10.0)) * 20
score = 80 + (14.91 / 15.0) * 20
score = 80 + 0.994 * 20
score = 80 + 19.88
score = 99.88
```

**Result:** 99.88/100 (Very Good, almost Excellent)

**Why?** Your margin of 24.91% is just 0.09% below the ideal maximum!

**What this means:**
- For every Rs.100 of revenue, Rs.24.91 is net profit
- Excellent profitability
- Strong pricing power
- Efficient cost management

---

### 7. PEG RATIO: 100.00/100 ✅

**Your Company's Value:** 0.36  
**Direction:** Lower is better

**Thresholds:**
- Ideal Min: 0.5 (Score = 100)
- Ideal Max: 1.5 (Score = 80)
- Acceptable Max: 3.0 (Score = 40)
- Your Value: **0.36**

**Calculation:**
```python
# PEG Ratio Configuration
ideal_min = 0.5
ideal_max = 1.5
acceptable_max = 3.0

# Your value
peg_ratio = 0.36

# Step 1: Check which range
# 0.36 ≤ 0.5 → Below or equal to ideal_min

# Step 2: For values ≤ ideal_min (lower is better)
score = 100.0
```

**Result:** 100.00/100 (Excellent)

**Why?** Your PEG ratio of 0.36 is below the ideal minimum of 0.5!

**What this means:**
- PEG = P/E ÷ Growth Rate = 126.53 ÷ 352.93 = 0.36
- Stock is CHEAP relative to its growth rate
- Despite high P/E, the growth justifies it
- Traditional value investors use PEG < 1 as "good value"
- Your 0.36 means growth is 2.78x the P/E multiple

---

### 8. ROE: 47.02/100 ⚠️

**Your Company's Value:** 6.75%  
**Direction:** Higher is better

**Thresholds:**
- Acceptable Min: 5% (Score = 40)
- Ideal Min: 15% (Score = 80)
- Ideal Max: 30% (Score = 100)
- Your Value: **6.75%**

**Calculation:**
```python
# ROE Configuration
acceptable_min = 5.0
ideal_min = 15.0
ideal_max = 30.0

# Your value
roe = 6.75

# Step 1: Check which range
# 6.75 is between 5 and 15 (between acceptable_min and ideal_min)

# Step 2: Linear interpolation
# Formula: 40 + ((value - acceptable_min) / (ideal_min - acceptable_min)) * 40

score = 40 + ((6.75 - 5.0) / (15.0 - 5.0)) * 40
score = 40 + (1.75 / 10.0) * 40
score = 40 + 0.175 * 40
score = 40 + 7.0
score = 47.0
```

**Result:** 47.02/100 (Average)

**Why?** Your ROE is above minimum but well below ideal range.

**What this means:**
- ROE = Net Income ÷ Shareholders Equity = 2,362 ÷ 35,820 = 6.59%
- Generating Rs.6.75 of profit for every Rs.100 of equity
- Below industry standards (ideal is 15-30%)
- Company has huge equity base but earnings are catching up
- Growing company still optimizing capital efficiency

---

### 9. REVENUE GROWTH 3Y: 95.93/100 ✅

**Your Company's Value:** 26.95%  
**Direction:** Higher is better

**Thresholds:**
- Acceptable Min: 5% (Score = 40)
- Ideal Min: 15% (Score = 80)
- Ideal Max: 30% (Score = 100)
- Your Value: **26.95%**

**Calculation:**
```python
# Revenue Growth Configuration
acceptable_min = 5.0
ideal_min = 15.0
ideal_max = 30.0

# Your value
revenue_growth = 26.95

# Step 1: Check which range
# 26.95 is between 15 and 30 (between ideal_min and ideal_max)

# Step 2: Linear interpolation
# Formula: 80 + ((value - ideal_min) / (ideal_max - ideal_min)) * 20

score = 80 + ((26.95 - 15.0) / (30.0 - 15.0)) * 20
score = 80 + (11.95 / 15.0) * 20
score = 80 + 0.7967 * 20
score = 80 + 15.93
score = 95.93
```

**Result:** 95.93/100 (Very Good)

**Why?** Your revenue growth is in the upper range of ideal!

**What this means:**
- Revenue CAGR over 3 years: 26.95%
- FY21: Rs.4,707 Cr → FY24: Rs.9,481 Cr
- Strong business momentum
- Market share gains
- Platform scaling successfully

---

### 10. INVENTORY TURNOVER: 100.00/100 ✅

**Your Company's Value:** Infinity (∞)  
**Direction:** Higher is better

**Calculation:**
```python
# Inventory Turnover Configuration
acceptable_min = 2.0
ideal_min = 6.0
ideal_max = 12.0

# Your value
inventory_turnover = infinity  # Service company, no inventory

# Step 1: Check for infinity
if value == infinity and direction == 'higher':
    score = 100.0
```

**Result:** 100.00/100 (Excellent)

**Why?** E-commerce platform has zero/minimal inventory!

**What this means:**
- Inventory = Rs.0 Cr (food delivery platform)
- COGS ÷ Inventory = Infinity
- Asset-light business model
- No inventory holding costs
- No obsolescence risk

---

### 11. P/B RATIO: 50.96/100 ⚠️

**Your Company's Value:** 8.36x  
**Direction:** Lower is better

**Thresholds:**
- Ideal Min: 1.0x (Score = 100)
- Ideal Max: 4.0x (Score = 80)
- Acceptable Max: 10.0x (Score = 40)
- Your Value: **8.36x**

**Calculation:**
```python
# P/B Ratio Configuration
ideal_min = 1.0
ideal_max = 4.0
acceptable_max = 10.0

# Your value
pb_ratio = 8.36

# Step 1: Check which range
# 8.36 is between 4.0 and 10.0 (between ideal_max and acceptable_max)

# Step 2: Linear interpolation for "lower is better"
# Formula: 40 + ((acceptable_max - value) / (acceptable_max - ideal_max)) * 40

score = 40 + ((10.0 - 8.36) / (10.0 - 4.0)) * 40
score = 40 + (1.64 / 6.0) * 40
score = 40 + 0.2733 * 40
score = 40 + 10.93
score = 50.93
```

**Result:** 50.96/100 (Average)

**Why?** Trading above book value but within acceptable range.

**What this means:**
- P/B = Stock Price ÷ Book Value = 310 ÷ 37.1 = 8.35x
- Paying Rs.8.36 for every Re.1 of book value
- Premium to book value (common for growth stocks)
- Market values intangibles (brand, platform, network effects)
- Acceptable for asset-light tech companies

---

### 12. ASSET TURNOVER: 20.58/100 ⚠️

**Your Company's Value:** 0.26x  
**Direction:** Higher is better

**Thresholds:**
- Acceptable Min: 0.5x (Score = 40)
- Ideal Min: 1.0x (Score = 80)
- Ideal Max: 2.5x (Score = 100)
- Your Value: **0.26x**

**Calculation:**
```python
# Asset Turnover Configuration
acceptable_min = 0.5
ideal_min = 1.0
ideal_max = 2.5

# Your value
asset_turnover = 0.26

# Step 1: Check which range
# 0.26 < 0.5 → Below acceptable minimum

# Step 2: For values below acceptable_min
# Formula: max(0, (value / acceptable_min) * 40)

score = (0.26 / 0.5) * 40
score = 0.52 * 40
score = 20.8
```

**Result:** 20.58/100 (Below Average)

**Why?** Generating only Rs.0.26 of revenue per Re.1 of assets.

**What this means:**
- Asset Turnover = Revenue ÷ Assets = 9,481 ÷ 36,852 = 0.26x
- Capital intensive business (platform, tech, investments)
- Heavy upfront investment phase
- Large cash reserves (Rs.27K Cr) inflate asset base
- Not unusual for growth-stage tech companies

---

### 13. ROIC: 72.00/100 ⚠️

**Your Company's Value:** 13.00%  
**Direction:** Higher is better

**Thresholds:**
- Acceptable Min: 5% (Score = 40)
- Ideal Min: 15% (Score = 80)
- Ideal Max: 35% (Score = 100)
- Your Value: **13.00%**

**Calculation:**
```python
# ROIC Configuration
acceptable_min = 5.0
ideal_min = 15.0
ideal_max = 35.0

# Your value
roic = 13.0

# Step 1: Check which range
# 13.0 is between 5 and 15 (between acceptable_min and ideal_min)

# Step 2: Linear interpolation
# Formula: 40 + ((value - acceptable_min) / (ideal_min - acceptable_min)) * 40

score = 40 + ((13.0 - 5.0) / (15.0 - 5.0)) * 40
score = 40 + (8.0 / 10.0) * 40
score = 40 + 0.8 * 40
score = 40 + 32.0
score = 72.0
```

**Result:** 72.00/100 (Good)

**Why?** Above minimum but not yet at ideal range.

**What this means:**
- Generating 13% return on invested capital
- Better than ROE (6.75%)
- Improving capital efficiency
- Good but room for improvement

---

### 14. FCF GROWTH: 87.59/100 ✅

**Your Company's Value:** 15.69%  
**Direction:** Higher is better

**Thresholds:**
- Acceptable Min: 0% (Score = 40)
- Ideal Min: 10% (Score = 80)
- Ideal Max: 25% (Score = 100)
- Your Value: **15.69%**

**Calculation:**
```python
# FCF Growth Configuration
acceptable_min = 0.0
ideal_min = 10.0
ideal_max = 25.0

# Your value
fcf_growth = 15.69

# Step 1: Check which range
# 15.69 is between 10 and 25 (between ideal_min and ideal_max)

# Step 2: Linear interpolation
# Formula: 80 + ((value - ideal_min) / (ideal_max - ideal_min)) * 20

score = 80 + ((15.69 - 10.0) / (25.0 - 10.0)) * 20
score = 80 + (5.69 / 15.0) * 20
score = 80 + 0.3793 * 20
score = 80 + 7.59
score = 87.59
```

**Result:** 87.59/100 (Very Good)

**Why?** Solid cash generation growth.

**What this means:**
- FCF grew 15.69% YoY
- FY23: Rs.1,179 Cr → FY24: Rs.1,364 Cr
- Strong cash generation ability
- Can fund growth without external capital

---

## 📋 SUMMARY TABLE

| Metric | Value | Score | Why This Score? |
|--------|-------|-------|-----------------|
| **P/E Ratio** | 126.53x | 0/100 | **3.16x beyond acceptable max (40x)** |
| **EPS Growth** | 352.93% | 100/100 | **11.76x above ideal max (30%)** |
| **Current Ratio** | 20.33x | 100/100 | **6.78x above ideal max (3x)** |
| **Interest Coverage** | 64.85x | 100/100 | **3.24x above ideal max (20x)** |
| **Debt/Equity** | 0.01 | 99.72/100 | Very close to perfect (0) |
| **Net Margin** | 24.91% | 99.88/100 | Just 0.09% below ideal max (25%) |
| **PEG Ratio** | 0.36 | 100/100 | **Below ideal min (0.5)** |
| **Revenue Growth** | 26.95% | 95.93/100 | Upper range of ideal (15-30%) |
| **FCF Growth** | 15.69% | 87.59/100 | Mid-upper range of ideal (10-25%) |
| **ROIC** | 13.00% | 72/100 | Between acceptable and ideal |
| **P/B Ratio** | 8.36x | 50.96/100 | Between ideal max and acceptable max |
| **ROE** | 6.75% | 47.02/100 | Just above acceptable min (5%) |
| **Asset Turnover** | 0.26x | 20.58/100 | Below acceptable min (0.5x) |
| **Inventory Turnover** | ∞ | 100/100 | Service company advantage |

---

## 🎯 KEY INSIGHTS

### Why P/E = 0 Despite Great Company?

**The score is mathematically correct!**

1. **Threshold Logic:**
   - Acceptable Max for P/E: 40x
   - Your P/E: 126.53x
   - Excess: 86.53 points beyond limit

2. **The Penalty Formula:**
   ```
   Score = 40 * (1 - (126.53 - 40) / 40)
         = 40 * (1 - 2.163)
         = 40 * (-1.163)
         = -46.52
         = max(0, -46.52)
         = 0
   ```

3. **What This Tells You:**
   - **NOT that the company is bad**
   - **BUT that the stock price is expensive**
   - Market has priced in future growth
   - Valuation risk is high
   - Any growth disappointment = price drop

### Why This Makes Sense:

- ✅ **PEG Ratio = 100:** Growth justifies P/E
- ⚠️ **P/E Ratio = 0:** But traditional valuation is expensive
- ✅ **Overall Score = 77.8:** Balanced view considering all factors

---

## 💡 WHAT THE SCORES REALLY MEAN

### Scores of 100/100:
- **NOT perfect in absolute terms**
- **Exceeds ideal maximum thresholds**
- Could be even higher but capped at 100

### Scores of 0/100:
- **NOT worthless**
- **Exceeds acceptable NEGATIVE threshold**
- Extreme concern in that specific area

### The Balance:
Your **77.8/100 final score** balances:
- ✅ Exceptional growth (100 scores)
- ✅ Strong financials (99+ scores)
- ⚠️ Expensive valuation (0-50 scores)
- ⚠️ Capital efficiency concerns (20-72 scores)

---

## 🎓 HOW TO INTERPRET YOUR RESULTS

### High P/E (0/100) + High PEG (100/100) = Growth Stock

**Translation:**
- Stock is expensive by traditional metrics
- But growth justifies the premium
- Risk: Must maintain hypergrowth
- Reward: Could compound if execution continues

### Recommendation: BUY
**Because:**
- Growth (95.9%) > Valuation concerns (47.8%)
- Financial Health (99.9%) provides downside protection
- Profitability improving (72.9%)

---

## 📊 WANT TO ADJUST SCORING?

If you think P/E ratio threshold is too strict, you can modify in `scoring_engine.py`:

```python
'pe_ratio': {
    'ideal_min': 10.0,
    'ideal_max': 20.0,
    'acceptable_max': 40.0,  # Change to 150.0 for growth stocks
},
```

This would make 126.53 score higher!

---

**Hope this clarifies how every single score is calculated! 📈**

Any metric you want me to explain in even more detail?
