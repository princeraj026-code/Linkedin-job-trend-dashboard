# 🚀 Quick Start: Push to GitHub

## Your Repository Details
- **GitHub URL**: https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git
- **Username**: princeraj026-code
- **Email**: rajputprincesingh026@gmail.com

---

## ⚡ EASIEST METHOD: Run the Automated Script

I've created scripts that will do everything for you automatically!

### Option 1: PowerShell Script (Recommended)
```powershell
cd N:\Hackathon\Job-Trend
.\push_to_github.ps1
```

### Option 2: Batch File
```cmd
cd N:\Hackathon\Job-Trend
push_to_github.bat
```

**The scripts will:**
1. ✓ Find Git on your system
2. ✓ Configure your GitHub username and email
3. ✓ Initialize the repository
4. ✓ Stage all your files
5. ✓ Create the initial commit
6. ✓ Add your GitHub repository as remote
7. ✓ Push to GitHub

---

## 🔑 Authentication Setup (Required Before Pushing)

GitHub requires authentication. Choose **ONE** method:

### Method 1: Personal Access Token (Recommended)

1. **Create Token:**
   - Go to: https://github.com/settings/tokens
   - Click **"Generate new token (classic)"**
   - Give it a name: `Job-Trends-Dashboard`
   - Select scope: ✅ **repo** (full control of private repositories)
   - Click **"Generate token"**
   - **COPY THE TOKEN** (you won't see it again!)

2. **Use Token:**
   - When the script asks for password, **paste the token** (not your GitHub password)
   - Username: `princeraj026-code`
   - Password: `<paste-your-token-here>`

### Method 2: GitHub CLI (One-Time Setup)

```powershell
# Install GitHub CLI
winget install --id GitHub.cli

# Authenticate
gh auth login

# Then run the push script
.\push_to_github.ps1
```

### Method 3: GitHub Desktop (Easiest for Beginners)

1. Download: https://desktop.github.com/
2. Install and sign in with GitHub
3. Click **"Add Local Repository"**
4. Select: `N:\Hackathon\Job-Trend`
5. Click **"Publish repository"**
6. Done! 🎉

---

## 📝 Manual Commands (If You Prefer)

If Git is installed and in your PATH, run these commands:

```powershell
# Navigate to project
cd N:\Hackathon\Job-Trend

# Configure Git
git config --global user.name "princeraj026-code"
git config --global user.email "rajputprincesingh026@gmail.com"

# Initialize repository
git init

# Stage all files
git add .

# Create commit
git commit -m "Initial commit: LinkedIn Job Trends Dashboard with AI features"

# Set branch to main
git branch -M main

# Add remote repository
git remote add origin https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git

# Push to GitHub
git push -u origin main
```

---

## 🔧 If Git is Not Found

**Install Git for Windows:**

1. **Download:**
   - Go to: https://git-scm.com/download/win
   - Download the 64-bit installer

2. **Install:**
   - Run the installer
   - Use default settings
   - **Important:** Check "Add Git to PATH"

3. **Restart VS Code:**
   - Close all VS Code windows
   - Open VS Code again

4. **Verify:**
   ```powershell
   git --version
   # Should show: git version 2.x.x
   ```

**Or install via winget:**
```powershell
winget install --id Git.Git -e --source winget
```

Then restart VS Code and run the script!

---

## ✅ After Pushing - Verify

1. Go to: https://github.com/princeraj026-code/Linkedin-job-trend-dashboard
2. You should see all your files!
3. Check that these are uploaded:
   - ✓ README.md
   - ✓ app/ folder with streamlit_app.py
   - ✓ src/ folder with all Python scripts
   - ✓ requirements.txt
   - ✓ TODO.md
   - ✓ GITHUB_SETUP_GUIDE.md

---

## 🔄 Future Updates

After making changes to your code:

```powershell
git add .
git commit -m "Add new feature: describe your changes"
git push
```

---

## 🎯 Next Steps After Pushing

### 1. Add Repository Description
- Go to your repo on GitHub
- Click **"⚙️ About"** (top right)
- Add description: "AI-Powered Job Market Intelligence Dashboard - Real-time LinkedIn job trends analysis with skill gap detection and career recommendations"
- Add topics: `python`, `streamlit`, `data-science`, `ai`, `job-market`, `analytics`

### 2. Deploy to Streamlit Cloud (Make it Live!)

1. Go to: https://share.streamlit.io/
2. Sign in with GitHub
3. Click **"New app"**
4. Select:
   - Repository: `princeraj026-code/Linkedin-job-trend-dashboard`
   - Branch: `main`
   - Main file: `app/streamlit_app.py`
5. Click **"Deploy"**
6. Wait 2-3 minutes
7. **Your dashboard is LIVE!** 🎉

You'll get a URL like: `https://linkedin-job-trend-dashboard.streamlit.app`

### 3. Update README with Live Demo

After deployment, add to your README.md:
```markdown
## 🚀 Live Demo
[Try it live!](https://your-app.streamlit.app)
```

---

## 🆘 Troubleshooting

### Error: "git is not recognized"
**Solution:** Install Git (see "If Git is Not Found" section above)

### Error: "remote origin already exists"
**Solution:**
```powershell
git remote remove origin
git remote add origin https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git
git push -u origin main
```

### Error: "Authentication failed"
**Solution:** Use a Personal Access Token, not your GitHub password

### Error: "Large files rejected"
**Solution:**
```powershell
# Check file sizes
Get-ChildItem -Recurse | Where-Object {$_.Length -gt 50MB} | Select-Object FullName, @{Name="Size(MB)";Expression={[math]::Round($_.Length/1MB, 2)}}

# If you find large files, add them to .gitignore
echo "path/to/large/file" >> .gitignore
git rm --cached path/to/large/file
git commit -m "Remove large file"
git push
```

---

## 📞 Quick Reference

**Your repository URL:**
```
https://github.com/princeraj026-code/Linkedin-job-trend-dashboard
```

**Clone your repository (on another computer):**
```powershell
git clone https://github.com/princeraj026-code/Linkedin-job-trend-dashboard.git
```

**Check status:**
```powershell
git status
```

**View commit history:**
```powershell
git log --oneline
```

---

**Ready? Run the script and push your code! 🚀**

```powershell
.\push_to_github.ps1
```
