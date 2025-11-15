# Job Trends & Skill-Gap Analyzer - Quick Start Guide

## 🚀 Run the Project in 3 Simple Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Data Pipeline
```bash
# Option A: Run complete pipeline at once
python src/run_pipeline.py

# Option B: Run scripts individually
python src/01_ingest_clean.py
python src/02_extract_skills.py
python src/03_role_stats.py
python src/04_generate_charts.py
```

### Step 3: Launch Dashboard
```bash
streamlit run app/streamlit_app.py
```

The dashboard will open in your browser at `http://localhost:8501`

---

## 📊 What Each Script Does

| Script | Purpose | Output |
|--------|---------|--------|
| `01_ingest_clean.py` | Loads and cleans CSV data | `data/processed/cleaned_jobs.csv` |
| `02_extract_skills.py` | Extracts skills using NLP | `data/processed/skills_extracted.csv` |
| `03_role_stats.py` | Generates analytics | `data/processed/analytics_summary.json` |
| `04_generate_charts.py` | Creates visualizations | `outputs/charts/*.png` |

---

## 🎯 Using VS Code Tasks

Press `Ctrl+Shift+P` → Type "Run Task" → Select:

- **Run Full Pipeline** - Runs all scripts sequentially
- **Start Streamlit Dashboard** - Launches the dashboard
- **Run Data Cleaning** - Just step 1
- **Run Skill Extraction** - Just step 2

---

## 📁 Expected Outputs

After running the pipeline, you'll have:

```
data/processed/
  ├── cleaned_jobs.csv          # Cleaned job data
  ├── jobs_with_skills.csv      # Jobs with extracted skills
  ├── skill_mappings.csv        # Skill-to-job mappings
  └── analytics_summary.json    # Complete analytics

outputs/charts/
  ├── top_skills.png
  ├── top_roles.png
  ├── work_type_distribution.png
  ├── top_companies.png
  ├── top_locations.png
  ├── job_categories.png
  ├── experience_levels.png
  ├── skills_wordcloud.png
  ├── interactive_skills.html
  ├── interactive_work_type.html
  └── interactive_locations.html
```

---

## 🐛 Troubleshooting

### CSV Encoding Error
If you see encoding errors:
- The scripts automatically try `utf-8` then `latin-1`
- Data is in `linkdin_Job_data.csv` at project root

### Import Errors
```bash
# Make sure you're in the project root directory
cd n:\Hackathon\Job-Trend

# Install all dependencies
pip install -r requirements.txt
```

### Missing Data Files
- Ensure `linkdin_Job_data.csv` exists in project root
- Run scripts in order (01 → 02 → 03 → 04)

### Streamlit Port Already in Use
```bash
streamlit run app/streamlit_app.py --server.port 8502
```

---

## 💡 Tips

1. **First time setup**: Run `python src/run_pipeline.py` once
2. **Quick dashboard launch**: Use VS Code task "Start Streamlit Dashboard"
3. **View charts**: Check `outputs/charts/` folder
4. **Export data**: Use download buttons in dashboard
5. **Check logs**: See `logs/` folder for detailed execution logs

---

## 📞 Need Help?

Check the main [README.md](README.md) for detailed documentation.
