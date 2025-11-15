"""
Skill Extraction Script
Extracts technical skills, certifications, and job categories from job descriptions
"""

import pandas as pd
import re
from pathlib import Path
from collections import Counter
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))
from config import (
    CLEANED_CSV_FILE, SKILLS_CSV_FILE, PROCESSED_DATA_DIR,
    SKILL_CATEGORIES, JOB_CATEGORIES, MIN_SKILL_FREQUENCY
)

def load_cleaned_data():
    """Load cleaned data from previous step"""
    print("📂 Loading cleaned data...")
    
    if not CLEANED_CSV_FILE.exists():
        print("❌ Error: Cleaned data not found!")
        print(f"   Please run 01_ingest_clean.py first")
        sys.exit(1)
    
    df = pd.read_csv(CLEANED_CSV_FILE)
    print(f"✅ Loaded {len(df):,} records")
    return df

def build_skill_dictionary():
    """Build comprehensive skill dictionary from config"""
    print("\n📚 Building skill dictionary...")
    
    all_skills = {}
    
    for category, skills in SKILL_CATEGORIES.items():
        for skill in skills:
            # Add skill and common variations
            all_skills[skill.lower()] = {
                'name': skill,
                'category': category
            }
            
            # Add variations
            variations = [
                skill.lower(),
                skill.replace('.', ''),
                skill.replace(' ', ''),
                skill.replace('-', '')
            ]
            
            for var in variations:
                if var and var not in all_skills:
                    all_skills[var] = {
                        'name': skill,
                        'category': category
                    }
    
    print(f"   Built dictionary with {len(set(s['name'] for s in all_skills.values()))} unique skills")
    return all_skills

def extract_skills_from_text(text, skill_dict):
    """Extract skills from job description text"""
    if pd.isna(text):
        return []
    
    text_lower = str(text).lower()
    found_skills = set()
    
    # Search for each skill
    for skill_key, skill_info in skill_dict.items():
        # Use word boundaries for better matching
        pattern = r'\b' + re.escape(skill_key) + r'\b'
        
        if re.search(pattern, text_lower):
            found_skills.add(skill_info['name'])
    
    return list(found_skills)

def categorize_job_role(title):
    """Categorize job based on title"""
    if pd.isna(title):
        return 'Other'
    
    title_lower = str(title).lower()
    
    for category, keywords in JOB_CATEGORIES.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
    
    return 'Other'

def extract_certifications(text):
    """Extract certifications mentioned in job description"""
    if pd.isna(text):
        return []
    
    certifications = []
    text_lower = str(text).lower()
    
    # Common certifications
    cert_patterns = {
        'AWS Certified': r'aws\s+certified',
        'Azure Certified': r'azure\s+certified',
        'GCP Certified': r'gcp\s+certified|google\s+cloud\s+certified',
        'Salesforce PD1': r'pd1|platform\s+developer\s+1',
        'Salesforce PD2': r'pd2|platform\s+developer\s+2',
        'Salesforce Admin': r'salesforce\s+admin|salesforce\s+certified\s+administrator',
        'ITIL': r'\bitil\b',
        'Scrum Master': r'csm|certified\s+scrum\s+master',
        'PMP': r'\bpmp\b|project\s+management\s+professional',
        'Oracle Certified': r'oracle\s+certified',
        'CISSP': r'\bcissp\b'
    }
    
    for cert_name, pattern in cert_patterns.items():
        if re.search(pattern, text_lower):
            certifications.append(cert_name)
    
    return certifications

def extract_experience_years(text, title):
    """Extract required years of experience"""
    if pd.isna(text) and pd.isna(title):
        return None
    
    combined_text = str(text) + ' ' + str(title)
    
    # Pattern: X+ years, X-Y years, X to Y years
    patterns = [
        r'(\d+)\+?\s*years?',
        r'(\d+)\s*-\s*(\d+)\s*years?',
        r'(\d+)\s*to\s*(\d+)\s*years?'
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, combined_text.lower())
        if matches:
            if isinstance(matches[0], tuple):
                # Range found, take average
                return (int(matches[0][0]) + int(matches[0][1])) / 2
            else:
                # Single number
                return int(matches[0])
    
    return None

def analyze_skills(df, skill_dict):
    """Perform skill extraction and analysis"""
    print("\n🔍 Extracting skills from job descriptions...")
    
    # Extract skills
    df['skills'] = df['job_details'].apply(
        lambda x: extract_skills_from_text(x, skill_dict)
    )
    
    # Count skills per job
    df['skill_count'] = df['skills'].apply(len)
    
    # Extract certifications
    df['certifications'] = df['job_details'].apply(extract_certifications)
    
    # Categorize jobs
    df['job_category'] = df['job'].apply(categorize_job_role)
    
    # Extract experience requirements
    df['required_experience_years'] = df.apply(
        lambda row: extract_experience_years(row['job_details'], row['job']),
        axis=1
    )
    
    print(f"   Processed {len(df):,} job descriptions")
    print(f"   Average skills per job: {df['skill_count'].mean():.1f}")
    
    return df

def generate_skill_statistics(df):
    """Generate statistics about skills"""
    print("\n📊 Generating skill statistics...")
    
    # Count skill frequencies
    all_skills = []
    for skills in df['skills']:
        all_skills.extend(skills)
    
    skill_freq = Counter(all_skills)
    
    # Top skills
    print(f"\n🔥 Top 20 Most Demanded Skills:")
    for skill, count in skill_freq.most_common(20):
        percentage = (count / len(df)) * 100
        print(f"   {skill:.<30} {count:>5} ({percentage:>5.1f}%)")
    
    # Job category distribution
    print(f"\n📋 Job Category Distribution:")
    print(df['job_category'].value_counts().head(10).to_string())
    
    # Certification statistics
    all_certs = []
    for certs in df['certifications']:
        all_certs.extend(certs)
    
    if all_certs:
        cert_freq = Counter(all_certs)
        print(f"\n🎓 Top Certifications Mentioned:")
        for cert, count in cert_freq.most_common(10):
            print(f"   {cert:.<30} {count:>5}")
    
    # Experience requirements
    exp_data = df['required_experience_years'].dropna()
    if len(exp_data) > 0:
        print(f"\n💼 Experience Requirements:")
        print(f"   Average: {exp_data.mean():.1f} years")
        print(f"   Median: {exp_data.median():.1f} years")
        print(f"   Range: {exp_data.min():.0f} - {exp_data.max():.0f} years")

def create_skill_mapping_table(df):
    """Create a separate table for skill mappings"""
    print("\n🗂️ Creating skill mapping table...")
    
    skill_mappings = []
    
    for idx, row in df.iterrows():
        job_id = row['job_ID']
        skills = row['skills']
        
        for skill in skills:
            skill_mappings.append({
                'job_ID': job_id,
                'skill': skill,
                'job_title': row['job'],
                'company_name': row['company_name'],
                'location': row['location'],
                'job_category': row['job_category']
            })
    
    skill_df = pd.DataFrame(skill_mappings)
    print(f"   Created {len(skill_df):,} skill mappings")
    
    return skill_df

def save_results(df, skill_mapping_df):
    """Save extraction results"""
    print(f"\n💾 Saving results...")
    
    # Ensure output directory exists
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Convert list columns to string for CSV
    df_to_save = df.copy()
    df_to_save['skills'] = df_to_save['skills'].apply(lambda x: '|'.join(x) if x else '')
    df_to_save['certifications'] = df_to_save['certifications'].apply(lambda x: '|'.join(x) if x else '')
    
    # Save main file with skills
    skills_file = PROCESSED_DATA_DIR / 'jobs_with_skills.csv'
    df_to_save.to_csv(skills_file, index=False, encoding='utf-8')
    print(f"✅ Saved jobs with skills: {skills_file}")
    
    # Save skill mappings
    skill_mapping_df.to_csv(SKILLS_CSV_FILE, index=False, encoding='utf-8')
    print(f"✅ Saved skill mappings: {SKILLS_CSV_FILE}")
    
    print(f"   {len(df):,} jobs × {len(df.columns)} columns")
    print(f"   {len(skill_mapping_df):,} skill mappings")

def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("🔍 JOB TRENDS ANALYZER - SKILL EXTRACTION PIPELINE")
    print("="*60)
    
    # Load data
    df = load_cleaned_data()
    
    # Build skill dictionary
    skill_dict = build_skill_dictionary()
    
    # Extract skills and analyze
    df = analyze_skills(df, skill_dict)
    
    # Generate statistics
    generate_skill_statistics(df)
    
    # Create skill mapping table
    skill_mapping_df = create_skill_mapping_table(df)
    
    # Save results
    save_results(df, skill_mapping_df)
    
    print("\n✅ Skill extraction completed successfully!")
    print("="*60 + "\n")
    
    return df, skill_mapping_df

if __name__ == "__main__":
    df, skill_df = main()
