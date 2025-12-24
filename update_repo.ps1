# Quick Update Script for Fundamental Indicators Repository
# This script helps you quickly commit and push changes to GitHub

# Colors for output
$Green = "Green"
$Cyan = "Cyan"
$Yellow = "Yellow"
$Red = "Red"

Write-Host "`n🚀 Git Quick Update Script`n" -ForegroundColor $Cyan

# Check if we're in a git repository
if (-not (Test-Path ".git")) {
    Write-Host "❌ Error: Not a git repository!" -ForegroundColor $Red
    Write-Host "Please run this script from the repository root.`n" -ForegroundColor $Yellow
    exit 1
}

# Show current status
Write-Host "📋 Current Status:" -ForegroundColor $Yellow
git status --short

# Count changes
$changes = git status --short
if (-not $changes) {
    Write-Host "`n✅ No changes to commit. Working directory is clean.`n" -ForegroundColor $Green
    exit 0
}

$changeCount = ($changes | Measure-Object).Count
Write-Host "`n📊 Found $changeCount file(s) with changes`n" -ForegroundColor $Cyan

# Ask for commit message
Write-Host "💬 Enter commit message (or press Enter for default):" -ForegroundColor $Yellow
$commitMessage = Read-Host

if ([string]::IsNullOrWhiteSpace($commitMessage)) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    $commitMessage = "Update: Changes on $timestamp"
    Write-Host "Using default message: $commitMessage`n" -ForegroundColor $Yellow
}

# Stage all changes
Write-Host "`n📦 Staging changes..." -ForegroundColor $Cyan
git add -A

# Commit
Write-Host "💾 Creating commit..." -ForegroundColor $Cyan
git commit -m $commitMessage

# Push to GitHub
Write-Host "`n🌐 Pushing to GitHub..." -ForegroundColor $Cyan
git push origin main

# Verify
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Successfully pushed to GitHub!`n" -ForegroundColor $Green
    Write-Host "🔗 View at: https://github.com/Mohit1053/Fundamental_Indicators`n" -ForegroundColor $Cyan
} else {
    Write-Host "`n❌ Push failed! Please check the error message above.`n" -ForegroundColor $Red
    exit 1
}

# Show latest commit
Write-Host "📝 Latest commit:" -ForegroundColor $Yellow
git log --oneline -1

Write-Host "`n🎉 Done!`n" -ForegroundColor $Green
