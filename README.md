# 📊 Job Trends & Skill-Gap Analyzer

> Comprehensive analysis of 7,927+ LinkedIn job postings to identify trending roles, in-demand skills, and regional market gaps across India's tech landscape.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 🎯 Project Overview

This project analyzes job market trends from LinkedIn job postings using **AI-powered analytics** to help:
- **Job Seekers** - Get personalized career recommendations and skill gap analysis
- **Recruiters** - Access real-time market intelligence and competitive insights
- **Educators** - Align curriculum with industry requirements
- **Researchers** - Study employment trends and skill evolution

### Key Insights
- 📈 **5,819 job postings** analyzed (cleaned from 7,927 records) across **2,496 companies**
- 🏆 Top roles: Lead Java Software Engineer, Senior Automation Tester, Data Engineer
- 🌏 **151 locations** with Bengaluru leading (905 jobs)
- 💼 Work distribution: 40.7% Remote, 40.5% On-site, 16.9% Hybrid
- 🔧 **78 unique skills** tracked with AI-powered extraction
- 🤖 **AI Career Recommender** with personalized skill gap analysis
- 📈 **Real-Time Market Intelligence** with trend predictions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- (Optional) Virtual environment tool

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/job-trend.git
cd job-trend
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download NLP models**
```bash
python -m spacy download en_core_web_sm
python -m nltk.downloader stopwords punkt
```

### Running the Analysis

**Option 1: VS Code Tasks (Recommended)**
- Press `Ctrl+Shift+B` and select "Run Full Pipeline"
- Or `Ctrl+Shift+P` → "Tasks: Run Task" → "Start Streamlit Dashboard"

**Option 2: Command Line**
```bash
# Run complete pipeline
python src/01_ingest_clean.py
python src/02_extract_skills.py
python src/03_role_stats.py

# Launch dashboard
streamlit run app/streamlit_app.py
```

## 📁 Project Structure

```
Job-Trend/
├── 📄 TODO.md                  # Comprehensive task tracking
├── 📄 README.md                # This file
├── 📄 requirements.txt         # Python dependencies
├── 📄 .gitignore              # Git ignore rules
│
├── 📂 data/
│   ├── raw/                    # Original CSV data
│   │   └── linkdin_Job_data.csv
│   └── processed/              # Cleaned & processed data
│       ├── cleaned_jobs.csv
│       ├── skills_extracted.csv
│       └── analytics_summary.json
│
├── 📂 src/                     # Python scripts
│   ├── 01_ingest_clean.py     # Data loading & cleaning
│   ├── 02_extract_skills.py   # Skill extraction (NLP)
│   ├── 03_role_stats.py       # Role statistics
│   ├── 04_generate_charts.py  # Visualization generation
│   ├── 05_build_report.py     # Report builder
│   ├── config.py              # Configuration
│   ├── logger.py              # Logging framework
│   └── utils.py               # Utility functions
│
├── 📂 app/                     # Streamlit dashboard
│   ├── streamlit_app.py       # Main app
│   ├── pages/                 # Multi-page sections
│   ├── components/            # Reusable UI components
│   └── styles/                # Custom CSS
│
├── 📂 outputs/
│   ├── charts/                # Generated visualizations
│   ├── reports/               # PDF/Excel reports
│   ├── api/                   # JSON data exports
│   └── temp/                  # Temporary files
│
├── 📂 docs/
│   ├── examples/              # Jupyter notebooks
│   └── methodology/           # Technical documentation
│
├── 📂 .vscode/
│   └── tasks.json            # VS Code automation tasks
│
└── 📂 .github/
    └── ISSUE_TEMPLATE/
        └── task_request.md    # GitHub issue template
```

## 📊 Data Schema

### Source Dataset: `linkdin_Job_data.csv`

| Column | Description | Example |
|--------|-------------|---------|
| `job_ID` | Unique identifier | 3471657636 |
| `job` | Job title | "Data Analyst, Trilogy (Remote)" |
| `location` | Job location | "Bengaluru, Karnataka, India" |
| `company_name` | Hiring company | "EPAM Anywhere" |
| `work_type` | Work arrangement | "Remote" / "On-site" / "Hybrid" |
| `full_time_remote` | Employment details | "Full-time · Associate" |
| `no_of_employ` | Company size | "1,001-5,000 employees" |
| `no_of_application` | Applicant count | 200 |
| `posted_day_ago` | Posting recency | "8 hours" |
| `job_details` | Full description | (Long text with requirements) |

**Statistics:**
- Total Records: **7,927**
- Date Collected: November 2025
- Geographic Focus: India (primarily)
- Missing Values: Varies by column (see data quality report)

## 🔬 Analysis Pipeline

### 1. Data Ingestion & Cleaning (`01_ingest_clean.py`)
- Load raw CSV with encoding detection
- Handle missing values (imputation/removal)
- Standardize locations, work types, company sizes
- Remove duplicates
- Output: `cleaned_jobs.csv`

### 2. Skill Extraction (`02_extract_skills.py`)
- NLP-based skill extraction using spaCy
- Technical skills dictionary (500+ terms)
- Job category classification
- Experience level detection
- Certification identification
- Output: `skills_extracted.csv`

### 3. Role Statistics (`03_role_stats.py`)
- Aggregate statistics by role, location, company
- Skill frequency analysis
- Co-occurrence matrix generation
- Trend identification
- Output: `analytics_summary.json`

### 4. Visualization (`04_generate_charts.py`)
- Top roles bar chart
- Skills frequency analysis
- Geographic heatmaps
- Work type distribution
- Company insights
- Word clouds
- Output: `outputs/charts/*.png`

### 5. Report Generation (`05_build_report.py`)
- PDF comprehensive report
- Excel workbook (multi-sheet)
- PowerPoint presentation
- Output: `outputs/reports/`

## 📈 Key Features

### Interactive Dashboard (Streamlit)
- **🏠 Overview:** Real-time metrics with key market indicators
- **🔍 Skills Explorer:** Searchable skills database with demand analytics
- **🏢 Company Insights:** Top hiring companies and tech stack analysis
- **🌍 Geographic Analysis:** Interactive maps and regional trends
- **📋 Job Categories:** Role distribution and experience level analysis
- **🔎 Data Explorer:** Advanced filtering and CSV export
- **🎯 AI Career Recommender:** Personalized career path recommendations
- **📈 Market Intelligence:** Real-time trending skills and market predictions
- **📊 About:** Project documentation and creator information

### 🤖 AI-Powered Features

#### Career Path Recommender
- ✅ Personalized job matching based on your skills
- ✅ Match score calculation for 5,800+ job postings
- ✅ Skills gap analysis with visual charts
- ✅ Customized learning path recommendations
- ✅ Experience level-based filtering
- ✅ Work preference customization
- ✅ Top 10 role recommendations with detailed insights

#### Real-Time Market Intelligence
- ✅ Live market health score (0-100)
- ✅ Trending skills with growth indicators
- ✅ Supply vs Demand analysis with interactive charts
- ✅ Emerging technologies alerts
- ✅ 30-day AI predictions
- ✅ Custom alert configuration
- ✅ Auto-refresh capabilities

### Analytics Capabilities
- ✅ Top 20 in-demand roles with statistics
- ✅ Top 30 required skills with frequency analysis
- ✅ Skills by job category heatmap
- ✅ Geographic distribution analysis
- ✅ Work type trends (Remote vs On-site vs Hybrid)
- ✅ Skill gap identification
- ✅ Company hiring patterns
- ✅ Experience level distribution
- ✅ AI-powered trend predictions

## 🛠️ Technologies Used

**Data Processing:**
- pandas, numpy

**NLP & Text Analysis:**
- spaCy (en_core_web_sm), NLTK, textblob

**Visualization:**
- matplotlib, seaborn, plotly, wordcloud

**Dashboard:**
- Streamlit with custom CSS animations

**AI & Analytics:**
- Custom recommendation algorithms
- Real-time trend analysis
- Supply-demand modeling

**Reporting:**
- reportlab (PDF), openpyxl (Excel), python-pptx (PowerPoint)

**Real-Time Data (Optional):**
- RapidAPI integration ready
- GitHub Actions automation
- Supabase database support

## 📝 Task Management

All project tasks are tracked in **[TODO.md](TODO.md)** with:
- ✅ Checkboxes for completion tracking
- 🏷️ Priority tags (High/Medium/Low)
- ⏱️ Time estimates
- 👤 Assignee placeholders
- 📂 Organized by project phase

Use GitHub Issues with our [task request template](.github/ISSUE_TEMPLATE/task_request.md) for collaborative work.

## 📤 Pushing Code to GitHub

**Quick Command Reference:** See [PUSH_COMMANDS.md](PUSH_COMMANDS.md) for essential git commands

**Automated Scripts:**
- Windows PowerShell: `.\push_to_github.ps1`
- Windows Command Prompt: `push_to_github.bat`
- Linux/Mac: `./push_to_github.sh`

**Detailed Guides:**
- [PUSH_INSTRUCTIONS.md](PUSH_INSTRUCTIONS.md) - Complete push instructions with authentication setup
- [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md) - Step-by-step GitHub setup guide

**Basic Commands:**
```bash
# Daily workflow
git add .
git commit -m "Your commit message"
git push

# First time setup - see PUSH_COMMANDS.md for full details
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 👥 Team

- **Prince Raj** - BTech CSE 2nd Year - Project Lead & Creator
  - Data Science Enthusiast | Full-Stack Developer | AI/ML Explorer

## 🚀 Future Enhancements

- 🔄 Real-time LinkedIn API integration
- 📊 Time-series trend analysis
- 💰 Salary prediction model
- 📝 PDF career report generator
- 📚 Learning resource integration
- 🔔 Email alert notifications
- 🌐 Multi-language support

## 🙏 Acknowledgments

- LinkedIn for job posting data inspiration
- Open-source community for amazing libraries
- Streamlit team for the incredible framework
- spaCy and NLTK for NLP capabilities

## 📧 Contact

For questions or feedback:
- GitHub Issues: [Create an issue](https://github.com/yourusername/job-trend/issues)
- Project Creator: Prince Raj (BTech CSE - 2nd Year)

---

**Built with ❤️ by Prince Raj | Powered by AI & Data Science | Hackathon 2025**

*Transforming Job Market Data into Career Opportunities*

*Last Updated: November 14, 2025*
