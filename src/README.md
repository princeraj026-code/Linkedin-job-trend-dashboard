# Source Code

This directory contains all Python scripts for the data pipeline.

## Scripts

- `01_ingest_clean.py` - Load and clean the LinkedIn job data CSV
- `02_extract_skills.py` - Extract skills and role categories from job descriptions
- `03_role_stats.py` - Generate role statistics and analytics
- `04_generate_charts.py` - Create all visualization charts
- `05_build_report.py` - Generate PDF/Excel reports

## Helper Modules

- `config.py` - Centralized configuration settings
- `logger.py` - Logging framework
- `utils.py` - Utility functions for data processing
- `skill_dictionary.py` - Technical skills mapping and categories
