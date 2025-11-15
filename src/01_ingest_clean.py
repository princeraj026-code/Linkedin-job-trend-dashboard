"""
Data Ingestion and Cleaning Script
Loads the raw LinkedIn job data CSV and performs cleaning operations
"""

import pandas as pd
import numpy as np
from pathlib import Path
import re
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))
from config import (
    RAW_CSV_FILE, CLEANED_CSV_FILE, PROCESSED_DATA_DIR,
    MIN_JOB_TITLE_LENGTH
)

def load_data():
    """Load raw CSV data with proper encoding"""
    print("📂 Loading raw data...")
    try:
        df = pd.read_csv(RAW_CSV_FILE, encoding='utf-8')
        print(f"✅ Loaded {len(df):,} records with {len(df.columns)} columns")
        return df
    except UnicodeDecodeError:
        df = pd.read_csv(RAW_CSV_FILE, encoding='latin-1')
        print(f"✅ Loaded {len(df):,} records (latin-1 encoding)")
        return df

def clean_job_titles(df):
    """Clean and standardize job titles"""
    print("\n🔧 Cleaning job titles...")
    
    # Remove rows with missing job titles
    initial_count = len(df)
    df = df.dropna(subset=['job'])
    
    # Remove very short titles
    df = df[df['job'].str.len() >= MIN_JOB_TITLE_LENGTH]
    
    # Strip whitespace
    df['job'] = df['job'].str.strip()
    
    print(f"   Removed {initial_count - len(df):,} invalid job titles")
    return df

def clean_locations(df):
    """Standardize location data"""
    print("\n🌍 Cleaning locations...")
    
    # Fill missing locations
    df['location'] = df['location'].fillna('Unknown')
    
    # Standardize location format
    df['location'] = df['location'].str.strip()
    
    # Extract city and state
    def parse_location(loc):
        if pd.isna(loc) or loc == 'Unknown':
            return 'Unknown', 'Unknown', 'Unknown'
        
        parts = [p.strip() for p in str(loc).split(',')]
        
        if len(parts) >= 3:
            return parts[0], parts[1], parts[2]  # City, State, Country
        elif len(parts) == 2:
            return parts[0], parts[1], 'India'
        elif len(parts) == 1:
            return parts[0], 'Unknown', 'India'
        else:
            return 'Unknown', 'Unknown', 'Unknown'
    
    df[['city', 'state', 'country']] = df['location'].apply(
        lambda x: pd.Series(parse_location(x))
    )
    
    print(f"   Parsed {df['city'].nunique()} unique cities")
    return df

def clean_work_type(df):
    """Standardize work type field"""
    print("\n💼 Cleaning work types...")
    
    # Fill missing work types
    df['work_type'] = df['work_type'].fillna('Not Specified')
    
    # Standardize values
    work_type_map = {
        'remote': 'Remote',
        'on-site': 'On-site',
        'hybrid': 'Hybrid',
        'onsite': 'On-site',
        'work from home': 'Remote',
        'wfh': 'Remote'
    }
    
    df['work_type'] = df['work_type'].str.lower().str.strip()
    df['work_type'] = df['work_type'].replace(work_type_map)
    df['work_type'] = df['work_type'].str.title()
    
    print(f"   Work type distribution:")
    print(df['work_type'].value_counts().to_string())
    return df

def clean_company_data(df):
    """Clean company-related fields"""
    print("\n🏢 Cleaning company data...")
    
    # Fill missing company names
    df['company_name'] = df['company_name'].fillna('Unknown Company')
    df['company_name'] = df['company_name'].str.strip()
    
    # Clean employee count
    df['no_of_employ'] = df['no_of_employ'].fillna('Not Specified')
    
    print(f"   {df['company_name'].nunique()} unique companies")
    return df

def parse_numeric_fields(df):
    """Parse and clean numeric fields"""
    print("\n🔢 Parsing numeric fields...")
    
    # Clean application count
    df['no_of_application'] = pd.to_numeric(
        df['no_of_application'].astype(str).str.replace(',', ''),
        errors='coerce'
    ).fillna(0).astype(int)
    
    # Parse posted_day_ago to numeric days
    def parse_posted_days(value):
        if pd.isna(value):
            return None
        
        value = str(value).lower()
        
        if 'hour' in value or 'hr' in value:
            hours = re.findall(r'\d+', value)
            return float(hours[0]) / 24 if hours else 0
        elif 'day' in value:
            days = re.findall(r'\d+', value)
            return float(days[0]) if days else 1
        elif 'week' in value:
            weeks = re.findall(r'\d+', value)
            return float(weeks[0]) * 7 if weeks else 7
        elif 'month' in value:
            months = re.findall(r'\d+', value)
            return float(months[0]) * 30 if months else 30
        else:
            return 1
    
    df['days_since_posted'] = df['posted_day_ago'].apply(parse_posted_days)
    
    print(f"   Parsed application counts and posting dates")
    return df

def remove_duplicates(df):
    """Remove duplicate job postings"""
    print("\n🔍 Removing duplicates...")
    
    initial_count = len(df)
    
    # Remove exact duplicates based on job_ID
    df = df.drop_duplicates(subset=['job_ID'], keep='first')
    
    duplicates_removed = initial_count - len(df)
    print(f"   Removed {duplicates_removed:,} duplicate records")
    
    return df

def create_additional_features(df):
    """Create additional useful features"""
    print("\n✨ Creating additional features...")
    
    # Extract experience level from job title
    def extract_experience_level(title):
        if pd.isna(title):
            return 'Unknown'
        
        title_lower = str(title).lower()
        
        if any(word in title_lower for word in ['senior', 'sr.', 'lead', 'principal', 'staff']):
            return 'Senior'
        elif any(word in title_lower for word in ['junior', 'jr.', 'entry', 'fresher', 'trainee']):
            return 'Junior'
        elif any(word in title_lower for word in ['mid', 'intermediate', 'associate']):
            return 'Mid-Level'
        else:
            return 'Mid-Level'  # Default
    
    df['experience_level'] = df['job'].apply(extract_experience_level)
    
    # Determine if job is full-time
    df['is_full_time'] = df['full_time_remote'].str.contains(
        'full-time', case=False, na=False
    ).astype(int)
    
    print(f"   Created experience_level and is_full_time features")
    return df

def generate_summary_stats(df):
    """Generate and print summary statistics"""
    print("\n" + "="*60)
    print("📊 DATA CLEANING SUMMARY")
    print("="*60)
    
    print(f"\n✅ Total Records: {len(df):,}")
    print(f"✅ Unique Companies: {df['company_name'].nunique():,}")
    print(f"✅ Unique Locations: {df['location'].nunique():,}")
    print(f"✅ Unique Job Titles: {df['job'].nunique():,}")
    
    print(f"\n📍 Top 5 Cities:")
    print(df['city'].value_counts().head().to_string())
    
    print(f"\n🏢 Top 5 Companies:")
    print(df['company_name'].value_counts().head().to_string())
    
    print(f"\n💼 Work Type Distribution:")
    print(df['work_type'].value_counts().to_string())
    
    print(f"\n📈 Experience Level Distribution:")
    print(df['experience_level'].value_counts().to_string())
    
    print(f"\n⚠️ Missing Values:")
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    if len(missing) > 0:
        print(missing.to_string())
    else:
        print("   No missing values!")
    
    print("\n" + "="*60)

def save_cleaned_data(df):
    """Save cleaned data to CSV"""
    print(f"\n💾 Saving cleaned data...")
    
    # Ensure output directory exists
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save cleaned data
    df.to_csv(CLEANED_CSV_FILE, index=False, encoding='utf-8')
    
    print(f"✅ Saved to: {CLEANED_CSV_FILE}")
    print(f"   {len(df):,} records × {len(df.columns)} columns")

def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("🚀 JOB TRENDS ANALYZER - DATA CLEANING PIPELINE")
    print("="*60)
    
    # Load data
    df = load_data()
    
    # Cleaning steps
    df = clean_job_titles(df)
    df = clean_locations(df)
    df = clean_work_type(df)
    df = clean_company_data(df)
    df = parse_numeric_fields(df)
    df = remove_duplicates(df)
    df = create_additional_features(df)
    
    # Generate summary
    generate_summary_stats(df)
    
    # Save cleaned data
    save_cleaned_data(df)
    
    print("\n✅ Data cleaning completed successfully!")
    print("="*60 + "\n")
    
    return df

if __name__ == "__main__":
    df = main()
