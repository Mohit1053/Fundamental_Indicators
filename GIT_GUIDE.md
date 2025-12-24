# 🚀 Quick Start - Updating Your Repository

This guide shows you how to keep your GitHub repository up-to-date with your local changes.

---

## 📦 Method 1: Using the Quick Update Script (Easiest)

We've created a PowerShell script to make updates super easy:

```powershell
.\update_repo.ps1
```

**What it does:**
1. Shows you what files have changed
2. Asks for a commit message (optional)
3. Stages all changes
4. Creates a commit
5. Pushes to GitHub automatically

---

## 📝 Method 2: Manual Git Commands

### Step 1: Check what changed
```powershell
git status
```

### Step 2: Add your changes
```powershell
# Add all changes
git add .

# Or add specific files
git add path/to/file.py
```

### Step 3: Commit with a message
```powershell
git commit -m "Your commit message here"
```

### Step 4: Push to GitHub
```powershell
git push origin main
```

---

## 🔄 Common Workflows

### After Adding a New Analysis
```powershell
git add .
git commit -m "feat: Add HDFC Bank analysis results"
git push origin main
```

### After Fixing a Bug
```powershell
git add .
git commit -m "fix: Correct ROE calculation for negative equity"
git push origin main
```

### After Updating Documentation
```powershell
git add .
git commit -m "docs: Update README with new examples"
git push origin main
```

### After Adding New Features
```powershell
git add .
git commit -m "feat: Add dividend yield calculator"
git push origin main
```

---

## 📋 Commit Message Conventions

Use these prefixes for clear commit messages:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks
- `style:` - Formatting changes

**Examples:**
```
feat: Add MACD indicator to statistical analyzer
fix: Handle division by zero in metric calculator
docs: Update installation instructions
refactor: Simplify scoring engine logic
```

---

## 🔍 Checking Status Before Commit

### See what files changed
```powershell
git status
```

### See the actual changes
```powershell
git diff
```

### See changes in a specific file
```powershell
git diff path/to/file.py
```

---

## ⚠️ Before You Push

### 1. Test your changes
```powershell
# Test core functionality
cd 1_Core_Fundamental_Scoring
python main.py

# Test analyzers
cd 2_Generic_Stock_Analyzer
python analyze_stock.py test_data.csv
```

### 2. Check for large files
```powershell
# Don't commit files larger than 50MB
# GitHub has a 100MB file limit
Get-ChildItem -Recurse | Where-Object {$_.Length -gt 50MB}
```

### 3. Verify .gitignore is working
```powershell
# These should NOT appear in git status:
# - __pycache__/
# - *.pyc
# - .env
# - credentials.json
git status
```

---

## 🚨 If You Made a Mistake

### Undo last commit (keep changes)
```powershell
git reset --soft HEAD~1
```

### Undo changes in a file (before commit)
```powershell
git checkout -- path/to/file.py
```

### Undo all changes (before commit)
```powershell
git reset --hard
```

---

## 🌐 Viewing Your Repository

After pushing, view your repository at:
**https://github.com/Mohit1053/Fundamental_Indicators**

GitHub Actions will automatically:
- ✅ Run code quality checks
- ✅ Test your code on multiple Python versions
- ✅ Generate reports

---

## 📊 Repository Statistics

Your repository includes:
- **180 files** in initial commit
- **144,718 lines** of code and data
- **Automatic CI/CD** via GitHub Actions
- **Professional documentation**
- **Issue and PR templates**

---

## 🎯 Quick Reference

| Task | Command |
|------|---------|
| Check status | `git status` |
| Add all changes | `git add .` |
| Commit | `git commit -m "message"` |
| Push to GitHub | `git push origin main` |
| Pull latest | `git pull origin main` |
| View history | `git log --oneline` |
| View remote | `git remote -v` |

---

## 🤝 Collaborating

### Clone on another computer
```powershell
git clone https://github.com/Mohit1053/Fundamental_Indicators.git
cd Fundamental_Indicators
pip install -r requirements.txt
```

### Pull latest changes
```powershell
git pull origin main
```

---

## 💡 Pro Tips

1. **Commit often** - Small, focused commits are better than large ones
2. **Write clear messages** - Future you will thank present you
3. **Test before pushing** - Catch errors early
4. **Use branches for experiments** - `git checkout -b feature-name`
5. **Review changes before committing** - `git diff`

---

## 📞 Need Help?

- **Git Issues:** Check [GitHub Docs](https://docs.github.com/)
- **Repository Issues:** Open an issue at [Issues Page](https://github.com/Mohit1053/Fundamental_Indicators/issues)

---

**🎉 Happy Coding!**
