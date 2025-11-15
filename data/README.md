# Data Directory

## Structure

### raw/
Contains the original, unmodified data files.
- `linkdin_Job_data.csv` - Original LinkedIn job postings (7,927 records)

### processed/
Contains cleaned and processed data files ready for analysis.
- `cleaned_jobs.csv` - Cleaned and standardized job data
- `skills_extracted.csv` - Extracted skills with job mappings
- `role_categories.csv` - Job categorization results
- `analytics_summary.json` - Pre-computed analytics and metrics

## Data Sources

**Primary Dataset:** LinkedIn Job Postings  
**Date Range:** Various (captured from LinkedIn)  
**Geography:** Primarily India (151 unique locations)  
**Record Count:** 7,927 job postings  
**Companies:** 2,495 unique companies  
**Job Titles:** 2,991 unique titles  

## Columns in Raw Data

1. `job_ID` - Unique job identifier
2. `job` - Job title
3. `location` - Job location (city, state, country)
4. `company_id` - Company identifier (mostly null)
5. `company_name` - Name of hiring company
6. `work_type` - On-site / Remote / Hybrid
7. `full_time_remote` - Employment type details
8. `no_of_employ` - Company size
9. `no_of_application` - Number of applications
10. `posted_day_ago` - Posting recency
11. `alumni` - Alumni count
12. `Hiring_person` - Recruiter name
13. `linkedin_followers` - Company followers
14. `hiring_person_link` - Recruiter profile link
15. `job_details` - Full job description
16. `Column1` - Empty column
