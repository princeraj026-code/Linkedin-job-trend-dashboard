# 🚀 Git Push Commands - Quick Reference

## Essential Commands to Push Code to GitHub

### First Time Setup (One-Time Only)

```bash
# 1. Configure your Git identity
git config --global user.name "princeraj026-code"
git config --global user.email "rajputprincesingh026@gmail.com"

# 2. Initialize repository (if not already initialized)
git init

# 3. Add all files
git add .

# 4. Create initial commit
git commit -m "Initial commit: LinkedIn Job Trends Dashboard"

# 5. Set default branch to main
git branch -M main

# 6. Add remote repository
git remote add origin https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git

# 7. Push to GitHub
git push -u origin main
```

---

## Daily Workflow: Push Updates

```bash
# 1. Check what changed
git status

# 2. Stage all changes
git add .

# 3. Commit with message
git commit -m "Describe your changes here"

# 4. Push to GitHub
git push
```

---

## One-Line Command (After Initial Setup)

```bash
git add . && git commit -m "Your commit message" && git push
```

---

## Automated Scripts Available

### Windows Users
- **PowerShell**: `.\push_to_github.ps1`
- **Command Prompt**: `push_to_github.bat`

### Linux/Mac Users
- **Bash**: `./push_to_github.sh`

See [`PUSH_INSTRUCTIONS.md`](PUSH_INSTRUCTIONS.md) for detailed instructions and troubleshooting.

---

## Common Git Commands

```bash
# View status
git status

# View commit history
git log --oneline

# View remote URL
git remote -v

# Pull latest changes
git pull

# Discard changes to a file
git checkout -- filename

# View what changed
git diff
```

---

## GitHub Authentication

When pushing for the first time, GitHub will ask for authentication:

**Option 1: GitHub CLI (Easiest)**
```bash
# Install GitHub CLI
winget install --id GitHub.cli  # Windows
brew install gh                  # Mac

# Login
gh auth login
```

**Option 2: Personal Access Token**
1. Go to https://github.com/settings/tokens
2. Generate new token (classic)
3. Select scope: `repo`
4. Use token as password when pushing

**Option 3: SSH Key**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "rajputprincesingh026@gmail.com"

# Add to GitHub
# Copy: ~/.ssh/id_ed25519.pub
# Paste at: https://github.com/settings/keys

# Change remote to SSH
git remote set-url origin git@github.com:princeraj026-code/Linkedin-job-trend-dashboard.git
```

---

## Quick Troubleshooting

**Error: "remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git
```

**Error: "Authentication failed"**
- Use Personal Access Token instead of password
- Or use GitHub CLI: `gh auth login`

**Error: "Large files rejected"**
```bash
# Add to .gitignore
echo "path/to/large/file" >> .gitignore
git rm --cached path/to/large/file
git commit -m "Remove large file"
git push
```

---

## Repository URL

```
https://github.com/princeraj026-code/Linkedin-job-trend-dashboard
```

---

**For detailed instructions**, see:
- [`PUSH_INSTRUCTIONS.md`](PUSH_INSTRUCTIONS.md) - Complete push guide
- [`GITHUB_SETUP_GUIDE.md`](GITHUB_SETUP_GUIDE.md) - Full GitHub setup

**Need help?** Check the troubleshooting sections in the guides above.
