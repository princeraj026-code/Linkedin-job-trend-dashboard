"""
Configuration settings for Job Trends & Skill-Gap Analyzer
Centralized configuration for paths, constants, and parameters
"""

import os
from pathlib import Path

# ============================================================================
# PROJECT PATHS
# ============================================================================

# Root directory (project base)
ROOT_DIR = Path(__file__).parent.parent.absolute()

# Data directories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Output directories
OUTPUT_DIR = ROOT_DIR / "outputs"
CHARTS_DIR = OUTPUT_DIR / "charts"
REPORTS_DIR = OUTPUT_DIR / "reports"
API_DIR = OUTPUT_DIR / "api"
TEMP_DIR = OUTPUT_DIR / "temp"

# Source code directory
SRC_DIR = ROOT_DIR / "src"

# App directory
APP_DIR = ROOT_DIR / "app"

# ============================================================================
# DATA FILES
# ============================================================================

# Raw data
RAW_CSV_FILE = RAW_DATA_DIR / "linkdin_Job_data.csv"

# Processed data
CLEANED_CSV_FILE = PROCESSED_DATA_DIR / "cleaned_jobs.csv"
SKILLS_CSV_FILE = PROCESSED_DATA_DIR / "skills_extracted.csv"
ROLE_CATEGORIES_FILE = PROCESSED_DATA_DIR / "role_categories.csv"
ANALYTICS_JSON_FILE = PROCESSED_DATA_DIR / "analytics_summary.json"

# ============================================================================
# ANALYSIS PARAMETERS
# ============================================================================

# Data cleaning
MIN_JOB_TITLE_LENGTH = 3
MAX_DESCRIPTION_LENGTH = 10000
DUPLICATE_THRESHOLD = 0.95  # Similarity threshold for duplicate detection

# Skill extraction
MIN_SKILL_FREQUENCY = 2  # Minimum occurrences to be considered
MAX_SKILLS_PER_JOB = 50
SKILL_EXTRACTION_CONFIDENCE = 0.6

# NLP settings
NLP_MODEL = "en_core_web_sm"  # spaCy model
MAX_TOKENS_PER_DOC = 1000000

# ============================================================================
# VISUALIZATION SETTINGS
# ============================================================================

# Chart dimensions
CHART_WIDTH = 12
CHART_HEIGHT = 8
DPI = 300

# Color schemes
COLOR_PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
                 "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
CUSTOM_COLORS = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e",
    "success": "#2ca02c",
    "warning": "#d62728",
    "info": "#9467bd"
}

# Top N items to display
TOP_N_ROLES = 20
TOP_N_SKILLS = 30
TOP_N_COMPANIES = 10
TOP_N_LOCATIONS = 10

# ============================================================================
# STREAMLIT DASHBOARD SETTINGS
# ============================================================================

DASHBOARD_TITLE = "Job Trends & Skill-Gap Analyzer"
PAGE_ICON = "📊"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Cache TTL (in seconds)
CACHE_TTL = 3600  # 1 hour

# ============================================================================
# REPORT SETTINGS
# ============================================================================

# PDF Report
PDF_TITLE = "Job Market Trends Analysis Report"
PDF_AUTHOR = "Job Trends Analyzer Team"
PDF_MARGIN = 72  # points (1 inch)

# Excel Report
EXCEL_SHEET_NAMES = [
    "Overview",
    "Top Skills",
    "Top Roles", 
    "Companies",
    "Locations",
    "Raw Data"
]

# ============================================================================
# SKILL CATEGORIES
# ============================================================================

SKILL_CATEGORIES = {
    "Programming Languages": [
        "Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go", "Rust",
        "PHP", "Swift", "Kotlin", "Scala", "R", "MATLAB", "TypeScript"
    ],
    "Web Frameworks": [
        "React", "Angular", "Vue.js", "Django", "Flask", "Spring", "Express",
        "Node.js", "Laravel", "Ruby on Rails", "ASP.NET", "FastAPI"
    ],
    "Databases": [
        "MySQL", "PostgreSQL", "MongoDB", "Redis", "Oracle", "SQL Server",
        "Cassandra", "DynamoDB", "Neo4j", "SQLite", "MariaDB", "Snowflake"
    ],
    "Cloud Platforms": [
        "AWS", "Azure", "Google Cloud", "GCP", "Heroku", "DigitalOcean",
        "IBM Cloud", "Oracle Cloud", "Alibaba Cloud"
    ],
    "DevOps & Tools": [
        "Docker", "Kubernetes", "Jenkins", "Git", "CI/CD", "Terraform",
        "Ansible", "Chef", "Puppet", "GitLab", "GitHub Actions", "CircleCI"
    ],
    "Data Science & ML": [
        "TensorFlow", "PyTorch", "scikit-learn", "Keras", "Pandas", "NumPy",
        "Spark", "Hadoop", "Tableau", "Power BI", "Machine Learning", "Deep Learning"
    ],
    "Business Tools": [
        "Salesforce", "SAP", "Oracle ERP", "ServiceNow", "JIRA", "Confluence",
        "Tableau", "Power BI", "Excel", "MS Office"
    ]
}

# ============================================================================
# JOB CATEGORIES
# ============================================================================

JOB_CATEGORIES = {
    "Developer": ["developer", "programmer", "coder", "software engineer"],
    "Data Professional": ["data analyst", "data scientist", "data engineer", "ML engineer"],
    "QA/Testing": ["tester", "QA", "quality assurance", "automation tester"],
    "DevOps": ["devops", "SRE", "infrastructure", "cloud engineer"],
    "Business Analyst": ["business analyst", "BA", "product analyst"],
    "Project Manager": ["project manager", "PM", "program manager", "scrum master"],
    "Designer": ["designer", "UI/UX", "graphic designer", "product designer"],
    "Database": ["DBA", "database admin", "database developer"],
    "Security": ["security", "cybersecurity", "infosec", "security engineer"],
    "Support": ["support engineer", "technical support", "help desk"]
}

# ============================================================================
# EXPERIENCE LEVELS
# ============================================================================

EXPERIENCE_LEVELS = {
    "Fresher": ["fresher", "entry level", "junior", "trainee", "intern"],
    "Mid-Level": ["mid-level", "associate", "professional", "2-5 years"],
    "Senior": ["senior", "sr.", "lead", "principal", "5-10 years"],
    "Expert": ["expert", "architect", "director", "10+ years", "staff"]
}

# ============================================================================
# LOGGING SETTINGS
# ============================================================================

LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = ROOT_DIR / "app.log"

# ============================================================================
# API SETTINGS (if needed)
# ============================================================================

API_VERSION = "v1"
API_RATE_LIMIT = 100  # requests per minute

# ============================================================================
# Create directories if they don't exist
# ============================================================================

def ensure_directories():
    """Create all required directories if they don't exist"""
    directories = [
        DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR,
        OUTPUT_DIR, CHARTS_DIR, REPORTS_DIR, API_DIR, TEMP_DIR
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
    print("✅ All directories ensured")

if __name__ == "__main__":
    ensure_directories()
    print(f"Project Root: {ROOT_DIR}")
    print(f"Raw Data: {RAW_CSV_FILE}")
    print(f"Cleaned Data: {CLEANED_CSV_FILE}")
