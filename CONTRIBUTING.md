# Contributing to Fundamental Indicators

First off, thank you for considering contributing to Fundamental Indicators! 🎉

This document provides guidelines for contributing to this project. Following these guidelines helps maintain quality and makes it easier for maintainers to review and accept your contributions.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)

---

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of experience level, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, or nationality.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Trolling, insulting comments, or personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct that could be considered inappropriate

---

## 🚀 How Can I Contribute?

### Reporting Bugs

If you find a bug, please create an issue with:

1. **Clear title** - Describe the issue in one line
2. **Description** - Detailed explanation of the bug
3. **Steps to reproduce** - How to trigger the bug
4. **Expected behavior** - What should happen
5. **Actual behavior** - What actually happens
6. **Environment** - Python version, OS, dependencies
7. **Screenshots** - If applicable

**Example:**
```markdown
## Bug: Incorrect ROE calculation for negative equity

**Description:** The ROE calculation returns positive values when equity is negative.

**Steps to reproduce:**
1. Run `python main.py` with negative equity data
2. Check the ROE value in the output

**Expected:** ROE should be negative or flagged as invalid
**Actual:** ROE shows positive percentage

**Environment:**
- Python 3.9
- Windows 10
- pandas 2.0.0
```

### Suggesting Enhancements

We welcome feature requests! Please include:

1. **Use case** - Why is this feature needed?
2. **Proposed solution** - How would it work?
3. **Alternatives considered** - Other approaches you've thought of
4. **Additional context** - Screenshots, examples, references

### Your First Code Contribution

Unsure where to start? Look for issues labeled:

- `good first issue` - Simple issues perfect for beginners
- `help wanted` - Issues where we'd appreciate contributions
- `documentation` - Improvements to docs

---

## 💻 Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/Fundamental_Indicators.git
cd Fundamental_Indicators
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install all dependencies
pip install -r requirements.txt

# Install development dependencies (if available)
pip install -r requirements-dev.txt  # If exists
```

### 4. Create a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or a bugfix branch
git checkout -b bugfix/issue-number-description
```

---

## 🔄 Pull Request Process

### Before Submitting

1. ✅ **Test your changes** - Ensure everything works
2. ✅ **Update documentation** - If you changed functionality
3. ✅ **Follow coding standards** - See below
4. ✅ **Add comments** - Explain complex logic
5. ✅ **Check for errors** - Run linters if available

### Submitting the PR

1. **Push your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request** on GitHub

3. **Fill out the PR template** with:
   - What changes you made
   - Why you made them
   - Any related issues
   - Testing performed

4. **Wait for review** - Maintainers will review and provide feedback

### PR Title Format

Use conventional commits format:

- `feat: Add new metric calculator for dividend yield`
- `fix: Correct ROE calculation for negative equity`
- `docs: Update installation instructions`
- `refactor: Simplify scoring engine logic`
- `test: Add unit tests for pattern analyzer`
- `chore: Update dependencies`

---

## 📝 Coding Standards

### Python Style Guide

Follow **PEP 8** guidelines:

```python
# Good
def calculate_roe(net_income, equity):
    """
    Calculate Return on Equity.
    
    Args:
        net_income (float): Net income value
        equity (float): Shareholder equity value
        
    Returns:
        float: ROE as a percentage
    """
    if equity == 0:
        return None
    return (net_income / equity) * 100


# Bad
def calc_roe(ni,eq):
    if eq==0:return None
    return(ni/eq)*100
```

### Key Principles

1. **Meaningful names** - Use descriptive variable and function names
2. **Docstrings** - Document all functions and classes
3. **Type hints** - Add type annotations where helpful
4. **Error handling** - Use try/except for potential failures
5. **Constants** - Use UPPER_CASE for constants
6. **Comments** - Explain why, not what

### File Organization

```python
"""Module docstring explaining purpose."""

# Standard library imports
import os
import sys

# Third-party imports
import pandas as pd
import numpy as np

# Local imports
from .metric_calculator import calculate_metrics

# Constants
DEFAULT_THRESHOLD = 0.05

# Classes
class ScoringEngine:
    """Class for scoring stocks."""
    pass

# Functions
def main():
    """Main execution function."""
    pass
```

---

## 🧪 Testing Guidelines

### Manual Testing

Before submitting, test your changes:

```bash
# Test core scoring
cd 1_Core_Fundamental_Scoring
python main.py

# Test generic analyzer
cd 2_Generic_Stock_Analyzer
python analyze_stock.py path/to/test/data.csv "Test Company"

# Test bulk tools
cd 5_Bulk_Tools
python bulk_market_analyzer.py
```

### Test Data

- Use sample data from `3_Example_Analyses/`
- Create small test CSVs with edge cases
- Test with missing data, negative values, zeros

### What to Test

1. ✅ Normal cases - Typical inputs
2. ✅ Edge cases - Empty data, single row, all zeros
3. ✅ Error cases - Invalid inputs, missing columns
4. ✅ Performance - Large datasets
5. ✅ Compatibility - Different Python versions

---

## 📚 Documentation

### Code Documentation

```python
def calculate_metric(value, benchmark, weight=1.0):
    """
    Calculate a weighted metric score.
    
    This function compares a value against a benchmark and returns
    a weighted score from 0-100.
    
    Args:
        value (float): The actual metric value
        benchmark (float): The target benchmark value
        weight (float, optional): Metric weight. Defaults to 1.0.
        
    Returns:
        float: Weighted score between 0 and 100
        
    Raises:
        ValueError: If weight is negative
        
    Examples:
        >>> calculate_metric(15, 10, 1.5)
        150.0
        
        >>> calculate_metric(5, 10, 0.5)
        25.0
    """
    if weight < 0:
        raise ValueError("Weight cannot be negative")
    return (value / benchmark) * 100 * weight
```

### README Updates

If you add new features, update:

- `README.md` - Main project README
- Module-specific READMEs in subdirectories
- `6_Documentation/` - Comprehensive guides

### Commit Messages

Write clear commit messages:

```bash
# Good
git commit -m "feat: Add dividend yield calculator

- Implemented calculate_dividend_yield() function
- Added unit tests
- Updated documentation
- Closes #123"

# Bad
git commit -m "fixed stuff"
```

---

## 🎯 Areas for Contribution

### High Priority

1. **Unit tests** - Add pytest tests
2. **Data validation** - Input validation functions
3. **Error handling** - Improve error messages
4. **Performance** - Optimize slow operations
5. **Documentation** - More examples and tutorials

### New Features

1. **Additional metrics** - More fundamental indicators
2. **Sector comparisons** - Industry-specific benchmarks
3. **Export formats** - PDF, JSON outputs
4. **Interactive dashboards** - Plotly/Streamlit interfaces
5. **API integration** - Live data fetching

### Bug Fixes

Check [Issues](https://github.com/Mohit1053/Fundamental_Indicators/issues) for bugs to fix.

---

## 📞 Questions?

- **GitHub Issues** - For bugs and features
- **Discussions** - For questions and ideas
- **Email** - Contact maintainers directly

---

## 🏆 Recognition

Contributors will be:

- Listed in `CONTRIBUTORS.md`
- Mentioned in release notes
- Credited in documentation

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers this project.

---

## 🙏 Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort! 🎉

---

**Happy Contributing! 🚀**
