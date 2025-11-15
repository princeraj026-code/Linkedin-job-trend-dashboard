# Job Trends & Skill-Gap Analyzer

**One-line Summary:** Analyze 7,927+ LinkedIn job postings to identify trending roles, in-demand skills, and regional market gaps across India's tech landscape.

---

## 📋 Task Tracking

### ✅ [Setup]

- [x] **Example: Initialize project structure** `High` ⏱️ 0.5h 👤 @yourname
  - Create base folders (src/, app/, data/, outputs/, docs/)
- [ ] **Install dependencies & create requirements.txt** `High` ⏱️ 1h 👤 @yourname
  - Add: pandas, numpy, matplotlib, seaborn, plotly, streamlit, nltk, spacy, wordcloud
- [ ] **Set up virtual environment** `High` ⏱️ 0.5h 👤 @yourname
  - Create venv and activate; document in README
- [ ] **Create .gitignore** `Medium` ⏱️ 0.25h 👤 @yourname
  - Exclude venv/, __pycache__/, *.pyc, .env, outputs/temp/
- [ ] **Download NLP models** `Medium` ⏱️ 1h 👤 @yourname
  - spaCy: en_core_web_sm, NLTK stopwords, punkt tokenizer
- [ ] **Create config.py for centralized settings** `Low` ⏱️ 0.5h 👤 @yourname
  - Paths, color schemes, default parameters
- [ ] **Set up logging framework** `Low` ⏱️ 1h 👤 @yourname
  - Create logger.py with file and console handlers
- [ ] **Create .env.example file** `Low` ⏱️ 0.25h 👤 @yourname
  - Template for API keys if needed later

---

### 📥 [Data Ingest]

- [ ] **Load and validate CSV (7,927 records)** `High` ⏱️ 1.5h 👤 @yourname
  - Check for encoding issues, validate all 16 columns
- [ ] **Handle missing values** `High` ⏱️ 2h 👤 @yourname
  - Strategy for: company_id (100%), alumni (39%), linkedin_followers (39%), hiring_person (28%)
- [ ] **Clean and standardize location data** `High` ⏱️ 2h 👤 @yourname
  - Normalize 151 unique locations, extract city/state, map "India" to unknown
- [ ] **Parse and clean work_type field** `Medium` ⏱️ 1h 👤 @yourname
  - Standardize On-site (3,258), Remote (2,999), Hybrid (1,479), handle 191 nulls
- [ ] **Extract numeric features** `Medium` ⏱️ 1.5h 👤 @yourname
  - Clean no_of_employ (parse "1,001-5,000 employees"), no_of_application, posted_day_ago
- [ ] **Remove duplicate job postings** `Medium` ⏱️ 1h 👤 @yourname
  - Check for duplicate job_ID and similar job_details
- [ ] **Create data quality report** `Low` ⏱️ 1h 👤 @yourname
  - Generate summary stats, null counts, outliers
- [ ] **Export cleaned dataset** `Low` ⏱️ 0.5h 👤 @yourname
  - Save to data/processed/cleaned_jobs.csv

---

### 🔍 [Role & Skill Extraction]

- [ ] **Extract job categories from titles** `High` ⏱️ 3h 👤 @yourname
  - Classify 2,991 unique titles into: Developer, Analyst, Engineer, Tester, Manager, etc.
- [ ] **Build technical skills dictionary** `High` ⏱️ 2h 👤 @yourname
  - Languages: Python, Java, JavaScript, SQL, C++, Scala, etc.
  - Frameworks: React, Angular, Django, Spring, etc.
  - Tools: AWS, Azure, Docker, Kubernetes, Salesforce, etc.
- [ ] **Parse job_details for skill mentions** `High` ⏱️ 4h 👤 @yourname
  - Use regex + NLP to extract skills from descriptions
- [ ] **Identify experience levels** `Medium` ⏱️ 2h 👤 @yourname
  - Extract: Fresher, Junior, Senior, Lead, Principal from titles and descriptions
- [ ] **Extract required certifications** `Medium` ⏱️ 2h 👤 @yourname
  - Find: AWS Certified, Salesforce PD1, ITIL, Scrum Master, etc.
- [ ] **Build company-to-skills mapping** `Medium` ⏱️ 1.5h 👤 @yourname
  - Top companies (EPAM: 1,517, TCS: 378, Uplers: 295) and their tech stacks
- [ ] **Create skill co-occurrence matrix** `Low` ⏱️ 2h 👤 @yourname
  - Which skills appear together (e.g., AWS + Python, Salesforce + Apex)
- [ ] **Tag domain/industry from descriptions** `Low` ⏱️ 2h 👤 @yourname
  - FinTech, HealthTech, E-commerce, Cloud, AI/ML, etc.

---

### 📊 [Analysis & Charts]

- [ ] **Top 20 in-demand job roles** `High` ⏱️ 1h 👤 @yourname
  - Bar chart with counts (Java Engineer: 172, Data Engineer: 153, etc.)
- [ ] **Top 30 required skills** `High` ⏱️ 1.5h 👤 @yourname
  - Horizontal bar chart sorted by frequency
- [ ] **Skills by job category heatmap** `High` ⏱️ 2h 👤 @yourname
  - Category vs. Skill frequency matrix
- [ ] **Geographic distribution map** `Medium` ⏱️ 2.5h 👤 @yourname
  - Choropleth/bubble map of jobs by city (Bengaluru: 1,324, Hyderabad: 671, etc.)
- [ ] **Work type distribution pie chart** `Medium` ⏱️ 1h 👤 @yourname
  - On-site: 41%, Remote: 38%, Hybrid: 19%, Unknown: 2%
- [ ] **Company size vs. skill requirements** `Medium` ⏱️ 2h 👤 @yourname
  - Scatter or box plot analysis
- [ ] **Salary insights (if extractable)** `Medium` ⏱️ 3h 👤 @yourname
  - Parse salary mentions from job_details, visualize ranges
- [ ] **Experience level distribution** `Medium` ⏱️ 1.5h 👤 @yourname
  - Fresher vs. Mid vs. Senior vs. Lead
- [ ] **Posting timeline analysis** `Low` ⏱️ 1.5h 👤 @yourname
  - Jobs posted by day/week, recency trends
- [ ] **Skill gap identification** `High` ⏱️ 2.5h 👤 @yourname
  - Compare demand vs. supply indicators, emerging vs. declining skills
- [ ] **Top hiring companies analysis** `Low` ⏱️ 1h 👤 @yourname
  - Top 10 companies with job counts and primary roles
- [ ] **Remote vs. On-site skill differences** `Low` ⏱️ 1.5h 👤 @yourname
  - Compare skill requirements for different work types
- [ ] **Word cloud for job descriptions** `Low` ⏱️ 1h 👤 @yourname
  - Visual representation of most common terms

---

### 🎨 [Streamlit Dashboard]

- [ ] **Create app structure** `High` ⏱️ 1.5h 👤 @yourname
  - app/streamlit_app.py with multipage layout
- [ ] **Build Home/Overview page** `High` ⏱️ 2h 👤 @yourname
  - Key metrics: Total jobs, companies, locations, top categories
- [ ] **Create Job Trends page** `High` ⏱️ 3h 👤 @yourname
  - Interactive charts for roles, work types, locations
- [ ] **Build Skills Explorer page** `High` ⏱️ 3h 👤 @yourname
  - Searchable skills, filtering by category/experience/location
- [ ] **Add Company Insights page** `Medium` ⏱️ 2.5h 👤 @yourname
  - Company profiles, tech stacks, hiring patterns
- [ ] **Create Geographic Analysis page** `Medium` ⏱️ 2h 👤 @yourname
  - Interactive map with filters
- [ ] **Implement filters and search** `Medium` ⏱️ 2.5h 👤 @yourname
  - Sidebar filters for all pages: location, work_type, experience, company
- [ ] **Add data download functionality** `Low` ⏱️ 1h 👤 @yourname
  - Export filtered results as CSV
- [ ] **Style with custom CSS** `Low` ⏱️ 1.5h 👤 @yourname
  - Professional color scheme, responsive layout
- [ ] **Add caching for performance** `Low` ⏱️ 1h 👤 @yourname
  - Use @st.cache_data for expensive operations

---

### 📤 [Export & Publish]

- [ ] **Generate PDF report** `Medium` ⏱️ 3h 👤 @yourname
  - Top insights, charts, summary tables using reportlab/matplotlib
- [ ] **Export all charts as PNG/SVG** `Medium` ⏱️ 1h 👤 @yourname
  - Save to outputs/charts/ with high resolution
- [ ] **Create summary JSON API** `Low` ⏱️ 2h 👤 @yourname
  - outputs/api/summary.json with key metrics
- [ ] **Build Excel workbook with multiple sheets** `Low` ⏱️ 2h 👤 @yourname
  - Sheets: Overview, Top Skills, Companies, Locations, Raw Data
- [ ] **Deploy Streamlit app** `Medium` ⏱️ 2h 👤 @yourname
  - Deploy to Streamlit Cloud or Heroku
- [ ] **Create shareable dashboard link** `Low` ⏱️ 0.5h 👤 @yourname
  - Configure for public access

---

### 🎯 [Polish & Docs]

- [ ] **Write comprehensive README.md** `High` ⏱️ 2h 👤 @yourname
  - Project overview, setup instructions, usage, screenshots
- [ ] **Create CONTRIBUTING.md** `Low` ⏱️ 1h 👤 @yourname
  - Guidelines for contributors
- [ ] **Add inline code documentation** `Medium` ⏱️ 2h 👤 @yourname
  - Docstrings for all functions and classes
- [ ] **Create usage examples** `Low` ⏱️ 1.5h 👤 @yourname
  - docs/examples/ with Jupyter notebooks
- [ ] **Add project presentation slides** `Medium` ⏱️ 2h 👤 @yourname
  - 10-15 slides summarizing findings
- [ ] **Record demo video** `Low` ⏱️ 1h 👤 @yourname
  - 3-5 minute walkthrough of dashboard
- [ ] **Write blog post/article** `Low` ⏱️ 3h 👤 @yourname
  - Medium/Dev.to article about insights found
- [ ] **Final code cleanup and refactoring** `Medium` ⏱️ 2h 👤 @yourname
  - Remove unused code, optimize performance

---

## 📝 Notes

### Data Files
- **Source CSV:** `n:\Hackathon\Job-Trend\linkdin_Job_data.csv` (7,927 rows × 16 columns)
- **Processed Data:** `data/processed/cleaned_jobs.csv`
- **Skill Mappings:** `data/processed/skills_extracted.csv`
- **Analytics Results:** `data/processed/analytics_summary.json`

### Scripts
- **Data Ingestion:** `src/01_ingest_clean.py`
- **Skill Extraction:** `src/02_extract_skills.py`
- **Role Statistics:** `src/03_role_stats.py`
- **Chart Generation:** `src/04_generate_charts.py`
- **Report Builder:** `src/05_build_report.py`

### Output Locations
- **Charts:** `outputs/charts/` (PNG, SVG)
- **Reports:** `outputs/reports/` (PDF, XLSX)
- **API Data:** `outputs/api/` (JSON)
- **Temp Files:** `outputs/temp/` (excluded from git)

### Key Statistics (from CSV analysis)
- Total Jobs: **7,927**
- Unique Job Titles: **2,991**
- Companies: **2,495**
- Locations: **151** (primarily India)
- Work Types: On-site (41%), Remote (38%), Hybrid (19%)
- Top Roles: Java Engineer, Data Engineer, Automation Tester, Business Analyst
- Top Companies: EPAM Anywhere (1,517), TCS (378), Uplers (295)
- Top Cities: Bengaluru (1,324), Hyderabad (671), Chennai (477)

### Resources
- [Project Repository](#)
- [Streamlit Dashboard](#)
- [Final Presentation](#)
- [Blog Article](#)

---

**Last Updated:** November 14, 2025  
**Total Estimated Time:** ~100+ hours  
**Priority Distribution:** High: 45%, Medium: 40%, Low: 15%
