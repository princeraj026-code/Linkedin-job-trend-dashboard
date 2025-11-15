# 🚀 Quick Start Guide

## First Time Setup (5 minutes)

### Step 1: Install Dependencies
Open terminal in VS Code (`` Ctrl+` ``) and run:

```powershell
# Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\activate

# Install all packages
pip install -r requirements.txt

# Download NLP models
python -m spacy download en_core_web_sm
python -m nltk.downloader stopwords punkt
```

### Step 2: Verify Installation
```powershell
# Run config to ensure directories exist
python src/config.py
```

You should see: `✅ All directories ensured`

---

## Using VS Code Tasks (Easiest Method)

### Run Tasks via Keyboard
1. Press **`Ctrl+Shift+B`** (or `Ctrl+Shift+P` → "Tasks: Run Task")
2. Select from:
   - **Run Full Pipeline** - Process all data
   - **Start Streamlit Dashboard** - Launch interactive app
   - **Install Dependencies** - Set up environment
   - **Clean Output Files** - Reset outputs

### Quick Access
- **Command Palette**: `Ctrl+Shift+P`
- **Terminal**: `` Ctrl+` ``
- **File Explorer**: `Ctrl+Shift+E`

---

## Manual Workflow

### 1. Data Processing
```powershell
# Clean and prepare data
python src/01_ingest_clean.py

# Extract skills from job descriptions
python src/02_extract_skills.py

# Generate statistics
python src/03_role_stats.py
```

### 2. Create Visualizations
```powershell
python src/04_generate_charts.py
```

### 3. Launch Dashboard
```powershell
streamlit run app/streamlit_app.py
```

Opens in browser at `http://localhost:8501`

---

## Project Workflow

### Starting a New Task

1. **Check TODO.md** - Find your task
2. **Mark as in-progress** - Update checkbox
3. **Create feature branch** (optional):
   ```bash
   git checkout -b feature/your-feature
   ```
4. **Write code** - Follow CONTRIBUTING.md
5. **Test locally** - Run your script
6. **Mark complete** - Update TODO.md with `[x]`
7. **Commit changes**:
   ```bash
   git add .
   git commit -m "feat: your feature description"
   ```

### Creating GitHub Issues

Use the template at `.github/ISSUE_TEMPLATE/task_request.md`:
- Fill in task description
- Set priority (High/Medium/Low)
- Estimate time
- Link related tasks

---

## Common Commands Reference

### Python Environment
```powershell
# Activate venv
.\venv\Scripts\activate

# Deactivate
deactivate

# Install new package
pip install package-name
pip freeze > requirements.txt  # Update file
```

### Data Analysis
```powershell
# Quick data preview
python analyze_csv.py

# Check config paths
python src/config.py
```

### Git Workflow
```bash
# Check status
git status

# Stage changes
git add .
git add specific-file.py

# Commit with message
git commit -m "feat: add new feature"

# Push to GitHub
git push origin main
```

---

## File Locations Quick Reference

| What | Where |
|------|-------|
| Raw data | `data/raw/linkdin_Job_data.csv` |
| Cleaned data | `data/processed/cleaned_jobs.csv` |
| Python scripts | `src/*.py` |
| Dashboard | `app/streamlit_app.py` |
| Charts | `outputs/charts/*.png` |
| Reports | `outputs/reports/*.pdf` |
| Configuration | `src/config.py` |
| Task list | `TODO.md` |

---

## Troubleshooting

### "Module not found"
```powershell
# Make sure venv is activated
.\venv\Scripts\activate

# Reinstall requirements
pip install -r requirements.txt
```

### "File not found"
```powershell
# Check you're in project root
cd N:\Hackathon\Job-Trend

# Verify file paths in config
python src/config.py
```

### Streamlit not starting
```powershell
# Check Streamlit installed
pip show streamlit

# Run with verbose output
streamlit run app/streamlit_app.py --logger.level=debug
```

### VS Code tasks not working
- Make sure you're in the workspace folder
- Check `.vscode/tasks.json` exists
- Restart VS Code

---

## Next Steps After Setup

1. ✅ **Start with data cleaning** (`TODO.md` → Data Ingest section)
2. ✅ **Build skill extraction** (Use config.py skill categories)
3. ✅ **Create first visualizations** (Top roles, skills)
4. ✅ **Build basic dashboard** (Home page + one analysis page)
5. ✅ **Iterate and improve** (Add more features from TODO.md)

---

## Getting Help

- 📖 **Full documentation**: See `README.md`
- 📋 **Task breakdown**: See `TODO.md`
- 🤝 **Contributing guide**: See `CONTRIBUTING.md`
- 📊 **Setup summary**: See `PROJECT_SETUP_SUMMARY.md`
- ⚙️ **Configuration**: See `src/config.py`

---

## Tips for Success

💡 **Use VS Code Tasks** - Automate repetitive work  
💡 **Commit often** - Small, focused commits  
💡 **Follow TODO.md** - Stay organized  
💡 **Read the data** - Understand what you're analyzing  
💡 **Test incrementally** - Don't wait to test at the end  

---

**Ready to start? Run your first task!** 🎯

```powershell
# Verify everything works
python src/config.py

# Then start with data cleaning
python src/01_ingest_clean.py
```

**Good luck!** 🚀
