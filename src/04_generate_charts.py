"""
Chart Generation Script
Creates comprehensive visualizations from analytics data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import json
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))
from config import (
    ANALYTICS_JSON_FILE, PROCESSED_DATA_DIR, CHARTS_DIR,
    COLOR_PALETTE
)

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette(COLOR_PALETTE)

def load_data():
    """Load processed data and analytics"""
    print("📂 Loading data...")
    
    # Load analytics
    if not ANALYTICS_JSON_FILE.exists():
        print("❌ Error: Analytics file not found!")
        print(f"   Please run 03_role_stats.py first")
        sys.exit(1)
    
    with open(ANALYTICS_JSON_FILE, 'r', encoding='utf-8') as f:
        analytics = json.load(f)
    
    # Load jobs data
    jobs_file = PROCESSED_DATA_DIR / 'jobs_with_skills.csv'
    df = pd.read_csv(jobs_file)
    df['skills'] = df['skills'].apply(lambda x: x.split('|') if pd.notna(x) and x else [])
    
    # Load skill mappings
    skills_file = PROCESSED_DATA_DIR / 'skill_mappings.csv'
    skill_df = pd.read_csv(skills_file) if skills_file.exists() else None
    
    print(f"✅ Data loaded successfully")
    return analytics, df, skill_df

def create_top_skills_chart(analytics):
    """Create top skills bar chart"""
    print("\n📊 Creating top skills chart...")
    
    skills_data = analytics['skills']['top_skills'][:20]
    
    # Create DataFrame
    df_skills = pd.DataFrame(skills_data)
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(df_skills['skill'], df_skills['count'], color=COLOR_PALETTE)
    
    ax.set_xlabel('Number of Job Postings', fontsize=12, fontweight='bold')
    ax.set_ylabel('Technical Skills', fontsize=12, fontweight='bold')
    ax.set_title('Top 20 Most Demanded Technical Skills', fontsize=14, fontweight='bold', pad=20)
    ax.invert_yaxis()
    
    # Add value labels
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, 
                f'{int(width):,}', 
                ha='left', va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    output_file = CHARTS_DIR / 'top_skills.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_file.name}")

def create_top_roles_chart(analytics):
    """Create top roles bar chart"""
    print("📊 Creating top roles chart...")
    
    roles_data = analytics['roles']['top_roles'][:15]
    
    df_roles = pd.DataFrame(roles_data)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(df_roles['role'], df_roles['count'], color=sns.color_palette('viridis', len(df_roles)))
    
    ax.set_xlabel('Number of Openings', fontsize=12, fontweight='bold')
    ax.set_ylabel('Job Roles', fontsize=12, fontweight='bold')
    ax.set_title('Top 15 Most Posted Job Roles', fontsize=14, fontweight='bold', pad=20)
    ax.invert_yaxis()
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, 
                f'{int(width):,}', 
                ha='left', va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    output_file = CHARTS_DIR / 'top_roles.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_file.name}")

def create_work_type_pie_chart(analytics):
    """Create work type distribution pie chart"""
    print("📊 Creating work type distribution chart...")
    
    work_data = analytics['work_types']['distribution']
    
    df_work = pd.DataFrame(work_data)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = sns.color_palette('Set2', len(df_work))
    wedges, texts, autotexts = ax.pie(
        df_work['count'], 
        labels=df_work['work_type'],
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        textprops={'fontsize': 11, 'fontweight': 'bold'}
    )
    
    ax.set_title('Work Type Distribution', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    output_file = CHARTS_DIR / 'work_type_distribution.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_file.name}")

def create_top_companies_chart(analytics):
    """Create top companies chart"""
    print("📊 Creating top companies chart...")
    
    company_data = analytics['companies']['top_companies'][:15]
    
    df_companies = pd.DataFrame(company_data)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(df_companies['company'], df_companies['job_count'], 
                   color=sns.color_palette('rocket', len(df_companies)))
    
    ax.set_xlabel('Number of Job Postings', fontsize=12, fontweight='bold')
    ax.set_ylabel('Companies', fontsize=12, fontweight='bold')
    ax.set_title('Top 15 Hiring Companies', fontsize=14, fontweight='bold', pad=20)
    ax.invert_yaxis()
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, 
                f'{int(width):,}', 
                ha='left', va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    output_file = CHARTS_DIR / 'top_companies.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_file.name}")

def create_top_locations_chart(analytics):
    """Create top locations chart"""
    print("📊 Creating top locations chart...")
    
    location_data = analytics['locations']['top_locations'][:15]
    
    df_locations = pd.DataFrame(location_data)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(df_locations['city'], df_locations['job_count'], 
                   color=sns.color_palette('mako', len(df_locations)))
    
    ax.set_xlabel('Number of Job Postings', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cities', fontsize=12, fontweight='bold')
    ax.set_title('Top 15 Cities by Job Postings', fontsize=14, fontweight='bold', pad=20)
    ax.invert_yaxis()
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, 
                f'{int(width):,}', 
                ha='left', va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    output_file = CHARTS_DIR / 'top_locations.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_file.name}")

def create_job_category_chart(analytics):
    """Create job category distribution chart"""
    print("📊 Creating job category chart...")
    
    category_data = analytics['job_categories']['distribution']
    
    df_categories = pd.DataFrame(category_data)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(df_categories['category'], df_categories['count'], 
                   color=sns.color_palette('coolwarm', len(df_categories)))
    
    ax.set_xlabel('Number of Jobs', fontsize=12, fontweight='bold')
    ax.set_ylabel('Job Categories', fontsize=12, fontweight='bold')
    ax.set_title('Job Category Distribution', fontsize=14, fontweight='bold', pad=20)
    ax.invert_yaxis()
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, 
                f'{int(width):,}', 
                ha='left', va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    output_file = CHARTS_DIR / 'job_categories.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_file.name}")

def create_experience_level_chart(analytics):
    """Create experience level distribution chart"""
    print("📊 Creating experience level chart...")
    
    exp_data = analytics['experience']['level_distribution']
    
    df_exp = pd.DataFrame(exp_data)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['#2ecc71', '#3498db', '#e74c3c']
    bars = ax.bar(df_exp['level'], df_exp['count'], color=colors)
    
    ax.set_xlabel('Experience Level', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Jobs', fontsize=12, fontweight='bold')
    ax.set_title('Experience Level Distribution', fontsize=14, fontweight='bold', pad=20)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, 
                f'{int(height):,}', 
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    output_file = CHARTS_DIR / 'experience_levels.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_file.name}")

def create_skills_wordcloud(analytics):
    """Create word cloud of skills"""
    print("📊 Creating skills word cloud...")
    
    skills_data = analytics['skills']['top_skills']
    
    # Create word frequency dictionary
    word_freq = {item['skill']: item['count'] for item in skills_data}
    
    # Create word cloud
    wordcloud = WordCloud(
        width=1600, 
        height=800, 
        background_color='white',
        colormap='viridis',
        relative_scaling=0.5,
        min_font_size=10
    ).generate_from_frequencies(word_freq)
    
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Skills Word Cloud', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    output_file = CHARTS_DIR / 'skills_wordcloud.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Saved: {output_file.name}")

def create_interactive_charts(analytics, df):
    """Create interactive Plotly charts"""
    print("📊 Creating interactive charts...")
    
    # Top Skills Interactive
    skills_data = pd.DataFrame(analytics['skills']['top_skills'][:20])
    fig1 = px.bar(
        skills_data, 
        x='count', 
        y='skill', 
        orientation='h',
        title='Top 20 Most Demanded Skills (Interactive)',
        labels={'count': 'Number of Jobs', 'skill': 'Skill'},
        color='count',
        color_continuous_scale='Viridis'
    )
    fig1.update_layout(height=600, showlegend=False)
    fig1.write_html(str(CHARTS_DIR / 'interactive_skills.html'))
    
    # Work Type Distribution Interactive
    work_data = pd.DataFrame(analytics['work_types']['distribution'])
    fig2 = px.pie(
        work_data,
        values='count',
        names='work_type',
        title='Work Type Distribution (Interactive)',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    fig2.write_html(str(CHARTS_DIR / 'interactive_work_type.html'))
    
    # Top Locations Map-style
    location_data = pd.DataFrame(analytics['locations']['top_locations'][:15])
    fig3 = px.bar(
        location_data,
        x='job_count',
        y='city',
        orientation='h',
        title='Top 15 Cities by Job Postings (Interactive)',
        labels={'job_count': 'Number of Jobs', 'city': 'City'},
        color='job_count',
        color_continuous_scale='Blues'
    )
    fig3.update_layout(height=600, showlegend=False)
    fig3.write_html(str(CHARTS_DIR / 'interactive_locations.html'))
    
    print(f"   ✅ Created 3 interactive HTML charts")

def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("📊 JOB TRENDS ANALYZER - CHART GENERATION")
    print("="*60)
    
    # Ensure output directory exists
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load data
    analytics, df, skill_df = load_data()
    
    # Create all charts
    print("\n🎨 Generating visualizations...")
    
    create_top_skills_chart(analytics)
    create_top_roles_chart(analytics)
    create_work_type_pie_chart(analytics)
    create_top_companies_chart(analytics)
    create_top_locations_chart(analytics)
    create_job_category_chart(analytics)
    create_experience_level_chart(analytics)
    create_skills_wordcloud(analytics)
    create_interactive_charts(analytics, df)
    
    print("\n✅ Chart generation completed successfully!")
    print(f"📁 Charts saved to: {CHARTS_DIR}")
    print(f"   Total charts created: 11 (8 PNG + 3 HTML)")
    print("="*60 + "\n")
    
    print("📌 Next Steps:")
    print("   Run: streamlit run app/streamlit_app.py")
    print()

if __name__ == "__main__":
    main()
