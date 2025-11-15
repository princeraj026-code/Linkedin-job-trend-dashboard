"""
Role Statistics and Analytics Script
Generates comprehensive statistics and analytics from processed job data
"""

import pandas as pd
import json
from pathlib import Path
from collections import Counter
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))
from config import (
    SKILLS_CSV_FILE, ANALYTICS_JSON_FILE, PROCESSED_DATA_DIR,
    TOP_N_ROLES, TOP_N_SKILLS, TOP_N_COMPANIES, TOP_N_LOCATIONS
)

def load_processed_data():
    """Load processed data from previous steps"""
    print("📂 Loading processed data...")
    
    jobs_file = PROCESSED_DATA_DIR / 'jobs_with_skills.csv'
    
    if not jobs_file.exists():
        print("❌ Error: Processed data not found!")
        print(f"   Please run 01_ingest_clean.py and 02_extract_skills.py first")
        sys.exit(1)
    
    df = pd.read_csv(jobs_file)
    
    # Convert pipe-separated skills back to lists
    df['skills'] = df['skills'].apply(lambda x: x.split('|') if pd.notna(x) and x else [])
    df['certifications'] = df['certifications'].apply(lambda x: x.split('|') if pd.notna(x) and x else [])
    
    print(f"✅ Loaded {len(df):,} records")
    
    # Load skill mappings if available
    skill_df = None
    if SKILLS_CSV_FILE.exists():
        skill_df = pd.read_csv(SKILLS_CSV_FILE)
        print(f"✅ Loaded {len(skill_df):,} skill mappings")
    
    return df, skill_df

def analyze_top_roles(df):
    """Analyze top job roles"""
    print("\n📊 Analyzing top roles...")
    
    top_roles = df['job'].value_counts().head(TOP_N_ROLES)
    
    results = {
        'total_unique_roles': df['job'].nunique(),
        'top_roles': [
            {
                'role': role,
                'count': int(count),
                'percentage': round((count / len(df)) * 100, 2)
            }
            for role, count in top_roles.items()
        ]
    }
    
    print(f"   Found {results['total_unique_roles']:,} unique roles")
    print(f"\n   Top {TOP_N_ROLES} Roles:")
    for item in results['top_roles'][:10]:
        print(f"   {item['role']:.<50} {item['count']:>5} ({item['percentage']:>5.1f}%)")
    
    return results

def analyze_top_skills(df, skill_df):
    """Analyze most demanded skills"""
    print("\n🔥 Analyzing top skills...")
    
    # Count all skills
    all_skills = []
    for skills in df['skills']:
        all_skills.extend(skills)
    
    skill_freq = Counter(all_skills)
    top_skills = skill_freq.most_common(TOP_N_SKILLS)
    
    results = {
        'total_unique_skills': len(skill_freq),
        'total_skill_mentions': len(all_skills),
        'avg_skills_per_job': round(len(all_skills) / len(df), 2),
        'top_skills': [
            {
                'skill': skill,
                'count': count,
                'percentage': round((count / len(df)) * 100, 2)
            }
            for skill, count in top_skills
        ]
    }
    
    print(f"   Found {results['total_unique_skills']:,} unique skills")
    print(f"   Average {results['avg_skills_per_job']} skills per job")
    print(f"\n   Top {TOP_N_SKILLS} Skills:")
    for item in results['top_skills'][:15]:
        print(f"   {item['skill']:.<30} {item['count']:>5} ({item['percentage']:>5.1f}%)")
    
    return results

def analyze_companies(df):
    """Analyze top hiring companies"""
    print("\n🏢 Analyzing companies...")
    
    company_stats = df.groupby('company_name').agg({
        'job_ID': 'count',
        'work_type': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'Unknown',
        'city': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'Unknown'
    }).reset_index()
    
    company_stats.columns = ['company', 'job_count', 'primary_work_type', 'primary_location']
    company_stats = company_stats.sort_values('job_count', ascending=False)
    
    results = {
        'total_companies': df['company_name'].nunique(),
        'top_companies': [
            {
                'company': row['company'],
                'job_count': int(row['job_count']),
                'primary_work_type': row['primary_work_type'],
                'primary_location': row['primary_location']
            }
            for _, row in company_stats.head(TOP_N_COMPANIES).iterrows()
        ]
    }
    
    print(f"   Found {results['total_companies']:,} unique companies")
    print(f"\n   Top {TOP_N_COMPANIES} Hiring Companies:")
    for item in results['top_companies']:
        print(f"   {item['company']:.<35} {item['job_count']:>4} jobs ({item['primary_work_type']})")
    
    return results

def analyze_locations(df):
    """Analyze geographic distribution"""
    print("\n🌍 Analyzing locations...")
    
    location_stats = df.groupby('city').agg({
        'job_ID': 'count',
        'work_type': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'Unknown',
        'company_name': 'nunique'
    }).reset_index()
    
    location_stats.columns = ['city', 'job_count', 'primary_work_type', 'unique_companies']
    location_stats = location_stats.sort_values('job_count', ascending=False)
    
    results = {
        'total_locations': df['city'].nunique(),
        'top_locations': [
            {
                'city': row['city'],
                'job_count': int(row['job_count']),
                'companies': int(row['unique_companies']),
                'primary_work_type': row['primary_work_type']
            }
            for _, row in location_stats.head(TOP_N_LOCATIONS).iterrows()
        ]
    }
    
    print(f"   Found {results['total_locations']:,} unique locations")
    print(f"\n   Top {TOP_N_LOCATIONS} Locations:")
    for item in results['top_locations']:
        print(f"   {item['city']:.<30} {item['job_count']:>5} jobs, {item['companies']:>3} companies")
    
    return results

def analyze_work_types(df):
    """Analyze work type distribution"""
    print("\n💼 Analyzing work types...")
    
    work_type_dist = df['work_type'].value_counts()
    
    results = {
        'distribution': [
            {
                'work_type': wt,
                'count': int(count),
                'percentage': round((count / len(df)) * 100, 2)
            }
            for wt, count in work_type_dist.items()
        ]
    }
    
    print(f"\n   Work Type Distribution:")
    for item in results['distribution']:
        print(f"   {item['work_type']:.<20} {item['count']:>5} ({item['percentage']:>5.1f}%)")
    
    return results

def analyze_job_categories(df):
    """Analyze job category distribution"""
    print("\n📋 Analyzing job categories...")
    
    category_dist = df['job_category'].value_counts()
    
    results = {
        'total_categories': df['job_category'].nunique(),
        'distribution': [
            {
                'category': cat,
                'count': int(count),
                'percentage': round((count / len(df)) * 100, 2)
            }
            for cat, count in category_dist.items()
        ]
    }
    
    print(f"   Found {results['total_categories']} job categories")
    print(f"\n   Category Distribution:")
    for item in results['distribution'][:10]:
        print(f"   {item['category']:.<25} {item['count']:>5} ({item['percentage']:>5.1f}%)")
    
    return results

def analyze_experience_levels(df):
    """Analyze experience level distribution"""
    print("\n📈 Analyzing experience levels...")
    
    exp_dist = df['experience_level'].value_counts()
    
    # Experience years statistics
    exp_years = df['required_experience_years'].dropna()
    
    results = {
        'level_distribution': [
            {
                'level': level,
                'count': int(count),
                'percentage': round((count / len(df)) * 100, 2)
            }
            for level, count in exp_dist.items()
        ],
        'years_statistics': {
            'average': round(exp_years.mean(), 1) if len(exp_years) > 0 else None,
            'median': round(exp_years.median(), 1) if len(exp_years) > 0 else None,
            'min': round(exp_years.min(), 1) if len(exp_years) > 0 else None,
            'max': round(exp_years.max(), 1) if len(exp_years) > 0 else None
        } if len(exp_years) > 0 else {}
    }
    
    print(f"\n   Experience Level Distribution:")
    for item in results['level_distribution']:
        print(f"   {item['level']:.<20} {item['count']:>5} ({item['percentage']:>5.1f}%)")
    
    if results['years_statistics']:
        print(f"\n   Experience Years Statistics:")
        print(f"   Average: {results['years_statistics']['average']} years")
        print(f"   Median: {results['years_statistics']['median']} years")
    
    return results

def create_summary_analytics(df, skill_df):
    """Create comprehensive analytics summary"""
    print("\n" + "="*60)
    print("📊 GENERATING COMPREHENSIVE ANALYTICS")
    print("="*60)
    
    analytics = {
        'metadata': {
            'total_jobs': len(df),
            'generation_date': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data_source': 'LinkedIn Job Postings'
        },
        'roles': analyze_top_roles(df),
        'skills': analyze_top_skills(df, skill_df),
        'companies': analyze_companies(df),
        'locations': analyze_locations(df),
        'work_types': analyze_work_types(df),
        'job_categories': analyze_job_categories(df),
        'experience': analyze_experience_levels(df)
    }
    
    return analytics

def save_analytics(analytics):
    """Save analytics to JSON file"""
    print(f"\n💾 Saving analytics...")
    
    # Ensure output directory exists
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save to JSON
    with open(ANALYTICS_JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(analytics, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved analytics to: {ANALYTICS_JSON_FILE}")
    
    # Calculate file size
    file_size = ANALYTICS_JSON_FILE.stat().st_size
    print(f"   File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")

def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("📊 JOB TRENDS ANALYZER - ANALYTICS GENERATION")
    print("="*60)
    
    # Load data
    df, skill_df = load_processed_data()
    
    # Generate analytics
    analytics = create_summary_analytics(df, skill_df)
    
    # Save results
    save_analytics(analytics)
    
    print("\n✅ Analytics generation completed successfully!")
    print("="*60 + "\n")
    
    print("📌 Next Steps:")
    print("   1. Run: python src/04_generate_charts.py (to create visualizations)")
    print("   2. Run: streamlit run app/streamlit_app.py (to view dashboard)")
    print()
    
    return analytics

if __name__ == "__main__":
    analytics = main()
