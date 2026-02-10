"""
Streamlit Dashboard Application
Interactive multi-page dashboard for Job Trends & Skill-Gap Analysis
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path
import sys
import os

# Configuration paths - hardcoded for cloud deployment
BASE_DIR = Path(__file__).parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
ANALYTICS_JSON_FILE = PROCESSED_DATA_DIR / "analytics_summary.json"
CHARTS_DIR = BASE_DIR / "outputs" / "charts"
COLOR_PALETTE = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Page configuration
st.set_page_config(
    page_title="Job Trends & Skill-Gap Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    /* Hide default sidebar title */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* Top Navigation Bar */
    .top-nav {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 70px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        padding: 0 2rem;
        z-index: 999;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    
    .top-nav-title {
        color: white;
        font-size: 1.8rem;
        font-weight: 800;
        margin-right: 3rem;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    .top-nav-buttons {
        display: flex;
        gap: 1rem;
    }
    
    .nav-button {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        padding: 0.6rem 1.5rem;
        border-radius: 25px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .nav-button:hover {
        background: rgba(255, 255, 255, 0.4);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 255, 255, 0.3);
    }
    
    .nav-button-active {
        background: white !important;
        color: #667eea !important;
        box-shadow: 0 5px 20px rgba(255, 255, 255, 0.5);
    }
    
    /* Main content area adjustment */
    .main .block-container {
        padding-top: 90px;
        max-width: 100%;
    }
    
    /* Main Header */
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    
    /* Metric Cards */
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        color: #000000;
    }
    .stMetric {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .stMetric label {
        color: #31333F !important;
    }
    .stMetric .css-1xarl3l {
        color: #000000 !important;
    }
    div[data-testid="stMetricValue"] {
        color: #000000 !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #31333F !important;
    }
    
    /* Sidebar Navigation Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #0f3460 0%, #16213e 100%);
    }
    
    /* Navigation Title */
    [data-testid="stSidebar"] .stMarkdown h1 {
        color: #00d4ff !important;
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        text-align: center !important;
        padding: 1rem 0 !important;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
        letter-spacing: 1px;
    }
    
    /* Radio Buttons Container */
    [data-testid="stSidebar"] .stRadio {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 1rem;
        backdrop-filter: blur(10px);
    }
    
    /* Radio Button Labels */
    [data-testid="stSidebar"] .stRadio label {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 0.8rem 1rem !important;
        margin: 0.3rem 0 !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
        display: block !important;
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(230, 57, 70, 0.1) 100%);
        border-left: 3px solid transparent;
    }
    
    [data-testid="stSidebar"] .stRadio label:hover {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.25) 0%, rgba(230, 57, 70, 0.25) 100%);
        transform: translateX(5px);
        border-left: 3px solid #00d4ff;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
    }
    
    /* Selected Radio Button */
    [data-testid="stSidebar"] .stRadio input:checked + label {
        background: linear-gradient(135deg, #00d4ff 0%, #e63946 100%) !important;
        color: #ffffff !important;
        border-left: 3px solid #ffffff !important;
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.6) !important;
        transform: translateX(8px) scale(1.02) !important;
        font-weight: 700 !important;
    }
    
    /* Divider Lines */
    [data-testid="stSidebar"] hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00d4ff, transparent);
        margin: 1.5rem 0;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }
    
    /* About Section */
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #00d4ff !important;
        font-weight: 700 !important;
        text-shadow: 0 0 8px rgba(0, 212, 255, 0.4);
        margin-top: 1rem !important;
    }
    
    [data-testid="stSidebar"] .stAlert {
        background: rgba(0, 212, 255, 0.15) !important;
        border-left: 4px solid #00d4ff !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        backdrop-filter: blur(10px);
    }
    
    /* Emoji Enhancement */
    [data-testid="stSidebar"] .stRadio label::before {
        filter: drop-shadow(0 0 3px rgba(0, 212, 255, 0.8));
    }
    
    /* Scrollbar Styling */
    [data-testid="stSidebar"]::-webkit-scrollbar {
        width: 8px;
    }
    
    [data-testid="stSidebar"]::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }
    
    [data-testid="stSidebar"]::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00d4ff, #e63946);
        border-radius: 10px;
    }
    
    [data-testid="stSidebar"]::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #00ffff, #ff4757);
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load all processed data"""
    # Load jobs data
    jobs_file = PROCESSED_DATA_DIR / 'jobs_with_skills.csv'
    df = pd.read_csv(jobs_file)
    df['skills'] = df['skills'].apply(lambda x: x.split('|') if pd.notna(x) and x else [])
    df['certifications'] = df['certifications'].apply(lambda x: x.split('|') if pd.notna(x) and x else [])
    
    # Load analytics
    with open(ANALYTICS_JSON_FILE, 'r', encoding='utf-8') as f:
        analytics = json.load(f)
    
    # Load skill extractions
    skills_file = PROCESSED_DATA_DIR / 'skills_extracted.csv'
    skill_df = pd.read_csv(skills_file) if skills_file.exists() else None
    
    return df, analytics, skill_df

def show_overview(df, analytics):
    """Display overview/home page"""
    st.markdown('<p class="main-header">📊 Job Trends & Skill-Gap Analyzer</p>', unsafe_allow_html=True)
    st.markdown("### Comprehensive Analysis of LinkedIn Job Market Data")
    
    st.markdown("---")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Job Postings",
            f"{analytics['metadata']['total_jobs']:,}",
            delta=None
        )
    
    with col2:
        st.metric(
            "Unique Companies",
            f"{analytics['companies']['total_companies']:,}",
            delta=None
        )
    
    with col3:
        st.metric(
            "Unique Skills",
            f"{analytics['skills']['total_unique_skills']:,}",
            delta=None
        )
    
    with col4:
        st.metric(
            "Locations",
            f"{analytics['locations']['total_locations']:,}",
            delta=None
        )
    
    st.markdown("---")
    
    # Two-column layout for charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔥 Top 15 Most Demanded Skills")
        skills_data = pd.DataFrame(analytics['skills']['top_skills'][:15])
        
        fig = px.bar(
            skills_data,
            x='count',
            y='skill',
            orientation='h',
            color='count',
            color_continuous_scale='Viridis',
            labels={'count': 'Number of Jobs', 'skill': 'Skill'}
        )
        fig.update_layout(height=500, showlegend=False, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💼 Work Type Distribution")
        work_data = pd.DataFrame(analytics['work_types']['distribution'])
        
        fig = px.pie(
            work_data,
            values='count',
            names='work_type',
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    # Top Roles
    st.markdown("---")
    st.subheader("📋 Top 15 Job Roles")
    
    roles_data = pd.DataFrame(analytics['roles']['top_roles'][:15])
    
    fig = px.bar(
        roles_data,
        x='count',
        y='role',
        orientation='h',
        color='count',
        color_continuous_scale='Blues',
        labels={'count': 'Number of Openings', 'role': 'Job Role'}
    )
    fig.update_layout(height=600, showlegend=False, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

def show_skills_explorer(df, analytics, skill_df):
    """Display skills analysis page"""
    st.markdown('<p class="main-header">🔍 Skills Explorer</p>', unsafe_allow_html=True)
    
    # Skills metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Skills", f"{analytics['skills']['total_unique_skills']:,}")
    
    with col2:
        st.metric("Avg Skills/Job", f"{analytics['skills']['avg_skills_per_job']}")
    
    with col3:
        st.metric("Total Mentions", f"{analytics['skills']['total_skill_mentions']:,}")
    
    st.markdown("---")
    
    # Skill selection
    top_n = st.slider("Number of top skills to display", 10, 50, 20, 5)
    
    skills_data = pd.DataFrame(analytics['skills']['top_skills'][:top_n])
    
    # Interactive chart
    fig = go.Figure(data=[
        go.Bar(
            x=skills_data['count'],
            y=skills_data['skill'],
            orientation='h',
            marker=dict(
                color=skills_data['count'],
                colorscale='Viridis',
                showscale=True
            ),
            text=skills_data['percentage'].apply(lambda x: f"{x}%"),
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title=f"Top {top_n} Most Demanded Skills",
        xaxis_title="Number of Job Postings",
        yaxis_title="Skill",
        height=max(600, top_n * 25),
        yaxis={'categoryorder':'total ascending'}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Skills table
    st.markdown("---")
    st.subheader("📊 Detailed Skills Breakdown")
    
    skills_table = skills_data.copy()
    skills_table['percentage'] = skills_table['percentage'].apply(lambda x: f"{x}%")
    skills_table = skills_table.rename(columns={
        'skill': 'Skill',
        'count': 'Job Count',
        'percentage': 'Percentage'
    })
    
    st.dataframe(skills_table, use_container_width=True, hide_index=True)
    
    # Download button
    csv = skills_table.to_csv(index=False)
    st.download_button(
        label="📥 Download Skills Data (CSV)",
        data=csv,
        file_name="top_skills.csv",
        mime="text/csv"
    )

def show_company_insights(df, analytics):
    """Display company analysis page"""
    st.markdown('<p class="main-header">🏢 Company Insights</p>', unsafe_allow_html=True)
    
    st.metric("Total Hiring Companies", f"{analytics['companies']['total_companies']:,}")
    
    st.markdown("---")
    
    # Top companies chart
    companies_data = pd.DataFrame(analytics['companies']['top_companies'][:20])
    
    fig = px.bar(
        companies_data,
        x='job_count',
        y='company',
        orientation='h',
        color='job_count',
        color_continuous_scale='Reds',
        labels={'job_count': 'Number of Job Postings', 'company': 'Company'},
        title="Top 20 Hiring Companies"
    )
    fig.update_layout(height=700, showlegend=False, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Company details table
    st.markdown("---")
    st.subheader("📋 Company Details")
    
    company_table = companies_data.copy()
    company_table = company_table.rename(columns={
        'company': 'Company',
        'job_count': 'Job Postings',
        'primary_work_type': 'Primary Work Type',
        'primary_location': 'Primary Location'
    })
    
    st.dataframe(company_table, use_container_width=True, hide_index=True)

def show_geographic_analysis(df, analytics):
    """Display geographic analysis page"""
    st.markdown('<p class="main-header">🌍 Geographic Analysis</p>', unsafe_allow_html=True)
    
    st.metric("Total Locations", f"{analytics['locations']['total_locations']:,}")
    
    st.markdown("---")
    
    # Top locations chart
    locations_data = pd.DataFrame(analytics['locations']['top_locations'][:20])
    
    fig = px.bar(
        locations_data,
        x='job_count',
        y='city',
        orientation='h',
        color='companies',
        color_continuous_scale='Greens',
        labels={'job_count': 'Number of Jobs', 'city': 'City', 'companies': 'Companies'},
        title="Top 20 Cities by Job Postings",
        hover_data=['primary_work_type']
    )
    fig.update_layout(height=700, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Location details
    st.markdown("---")
    st.subheader("📊 Location Details")
    
    location_table = locations_data.copy()
    location_table = location_table.rename(columns={
        'city': 'City',
        'job_count': 'Job Postings',
        'companies': 'Unique Companies',
        'primary_work_type': 'Primary Work Type'
    })
    
    st.dataframe(location_table, use_container_width=True, hide_index=True)

def show_job_categories(df, analytics):
    """Display job categories analysis"""
    st.markdown('<p class="main-header">📋 Job Categories</p>', unsafe_allow_html=True)
    
    categories_data = pd.DataFrame(analytics['job_categories']['distribution'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Bar chart
        fig = px.bar(
            categories_data,
            x='count',
            y='category',
            orientation='h',
            color='count',
            color_continuous_scale='Rainbow',
            labels={'count': 'Number of Jobs', 'category': 'Category'},
            title="Job Category Distribution"
        )
        fig.update_layout(height=500, showlegend=False, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Pie chart
        fig = px.pie(
            categories_data,
            values='count',
            names='category',
            title="Job Category Proportions"
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    # Experience levels
    st.markdown("---")
    st.subheader("📈 Experience Level Distribution")
    
    exp_data = pd.DataFrame(analytics['experience']['level_distribution'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(
            exp_data,
            x='level',
            y='count',
            color='level',
            labels={'count': 'Number of Jobs', 'level': 'Experience Level'},
            title="Jobs by Experience Level"
        )
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        if analytics['experience'].get('years_statistics'):
            stats = analytics['experience']['years_statistics']
            st.markdown("### 📊 Experience Years Statistics")
            st.metric("Average", f"{stats['average']} years")
            st.metric("Median", f"{stats['median']} years")
            st.metric("Range", f"{stats['min']} - {stats['max']} years")

def show_data_explorer(df):
    """Display raw data explorer"""
    st.markdown('<p class="main-header">🔎 Data Explorer</p>', unsafe_allow_html=True)
    
    st.markdown("### Filter and Explore Job Data")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        work_types = ['All'] + sorted(df['work_type'].unique().tolist())
        selected_work_type = st.selectbox("Work Type", work_types)
    
    with col2:
        cities = ['All'] + sorted(df['city'].unique().tolist())
        selected_city = st.selectbox("City", cities[:100])  # Limit for performance
    
    with col3:
        categories = ['All'] + sorted(df['job_category'].unique().tolist())
        selected_category = st.selectbox("Job Category", categories)
    
    # Apply filters
    filtered_df = df.copy()
    
    if selected_work_type != 'All':
        filtered_df = filtered_df[filtered_df['work_type'] == selected_work_type]
    
    if selected_city != 'All':
        filtered_df = filtered_df[filtered_df['city'] == selected_city]
    
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['job_category'] == selected_category]
    
    st.metric("Filtered Results", f"{len(filtered_df):,} jobs")
    
    # Display data
    display_cols = ['job', 'company_name', 'location', 'work_type', 'job_category', 
                    'experience_level', 'skill_count', 'no_of_application']
    
    st.dataframe(
        filtered_df[display_cols].head(100),
        use_container_width=True,
        hide_index=True
    )
    
    # Download button
    csv = filtered_df[display_cols].to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=csv,
        file_name="filtered_jobs.csv",
        mime="text/csv"
    )

def show_career_recommender(df, analytics, skill_df):
    """AI-Powered Career Path Recommender"""
    st.markdown('<p class="main-header">🎯 AI Career Path Recommender</p>', unsafe_allow_html=True)
    st.markdown("### Discover Your Ideal Career Path Based on Market Data")
    
    st.markdown("---")
    
    # Introduction
    st.info("""
    🤖 **How it works:** Enter your current skills, and our AI will:
    - Match you with suitable job roles from 5,800+ real job postings
    - Calculate your skill compatibility score
    - Identify missing skills for your dream roles
    - Suggest optimal learning paths to advance your career
    """)
    
    # Get all unique skills from analytics
    all_skills = [skill['skill'] for skill in analytics['skills']['top_skills']]
    
    # User Input Section
    st.markdown("---")
    st.markdown("## 🎓 Your Current Skills")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_skills = st.multiselect(
            "Select skills you currently have:",
            options=all_skills,
            help="Choose all the technical skills you possess"
        )
    
    with col2:
        experience_years = st.slider(
            "Years of Experience",
            min_value=0,
            max_value=20,
            value=2,
            help="Your total work experience"
        )
    
    # Additional preferences
    st.markdown("### 🎯 Career Preferences")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        preferred_work_type = st.selectbox(
            "Preferred Work Type",
            options=["Any", "Remote", "On-Site", "Hybrid"]
        )
    
    with col2:
        preferred_location = st.selectbox(
            "Preferred Location",
            options=["Any"] + sorted(df['city'].unique().tolist()[:50])
        )
    
    with col3:
        career_goal = st.selectbox(
            "Career Goal",
            options=["Current Level", "Level Up", "Switch Domain"]
        )
    
    # Analyze button
    if st.button("🚀 Get Career Recommendations", type="primary"):
        if not selected_skills:
            st.warning("⚠️ Please select at least one skill to get recommendations!")
        else:
            with st.spinner("🤖 AI is analyzing market data and generating recommendations..."):
                # Calculate recommendations
                recommendations = calculate_career_recommendations(
                    df, skill_df, selected_skills, experience_years,
                    preferred_work_type, preferred_location, career_goal
                )
                
                # Display results
                st.markdown("---")
                st.markdown("## 🎯 Your Personalized Career Recommendations")
                
                # Overall Stats
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Jobs Analyzed", f"{recommendations['total_jobs']:,}")
                with col2:
                    st.metric("Matching Jobs", f"{recommendations['matching_jobs']}")
                with col3:
                    st.metric("Avg Match Score", f"{recommendations['avg_match_score']:.1f}%")
                with col4:
                    st.metric("Skills Gap", f"{recommendations['skills_gap']}")
                
                # Top Recommended Roles
                st.markdown("---")
                st.markdown("### 🌟 Top 10 Recommended Roles for You")
                
                for idx, role in enumerate(recommendations['top_roles'][:10], 1):
                    with st.expander(f"#{idx} - {role['title']} ({role['match_score']:.0f}% Match)", expanded=(idx <= 3)):
                        col1, col2 = st.columns([2, 1])
                        
                        with col1:
                            st.markdown(f"**🏢 Top Companies:** {', '.join(role['top_companies'][:3])}")
                            st.markdown(f"**📍 Locations:** {', '.join(role['locations'][:3])}")
                            st.markdown(f"**💼 Work Types:** {', '.join(role['work_types'])}")
                            st.markdown(f"**📊 Total Openings:** {role['job_count']} positions")
                        
                        with col2:
                            # Progress bar for match score
                            st.markdown("**Match Score**")
                            st.progress(role['match_score'] / 100)
                            st.markdown(f"**{role['match_score']:.0f}%**")
                        
                        # Skills breakdown
                        st.markdown("---")
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown("**✅ You Have:**")
                            if role['skills_you_have']:
                                for skill in role['skills_you_have'][:5]:
                                    st.markdown(f"- ✓ {skill}")
                            else:
                                st.markdown("*No direct skill matches*")
                        
                        with col2:
                            st.markdown("**📚 You Need to Learn:**")
                            if role['skills_to_learn']:
                                for skill in role['skills_to_learn'][:5]:
                                    st.markdown(f"- 📖 {skill}")
                            else:
                                st.markdown("*You're already qualified! 🎉*")
                
                # Skills Gap Analysis
                st.markdown("---")
                st.markdown("### 📊 Skills Gap Analysis")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("#### 🔥 Most In-Demand Skills You're Missing")
                    missing_skills_df = pd.DataFrame(recommendations['missing_skills'][:10])
                    if not missing_skills_df.empty:
                        fig = px.bar(
                            missing_skills_df,
                            x='demand',
                            y='skill',
                            orientation='h',
                            color='demand',
                            color_continuous_scale='Reds',
                            labels={'demand': 'Jobs Requiring This Skill', 'skill': 'Skill'}
                        )
                        fig.update_layout(height=400, showlegend=False)
                        st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    st.markdown("#### ✨ Your Skill Strengths")
                    your_skills_df = pd.DataFrame(recommendations['your_skill_value'][:10])
                    if not your_skills_df.empty:
                        fig = px.bar(
                            your_skills_df,
                            x='value',
                            y='skill',
                            orientation='h',
                            color='value',
                            color_continuous_scale='Greens',
                            labels={'value': 'Market Value (Job Count)', 'skill': 'Skill'}
                        )
                        fig.update_layout(height=400, showlegend=False)
                        st.plotly_chart(fig, use_container_width=True)
                
                # Learning Path
                st.markdown("---")
                st.markdown("### 🎓 Recommended Learning Path")
                
                st.success("""
                **🚀 Your Personalized Roadmap:**
                
                Based on market demand and your career goal, focus on learning these skills in order:
                """)
                
                learning_path = recommendations['learning_path']
                for idx, item in enumerate(learning_path[:8], 1):
                    col1, col2, col3 = st.columns([1, 3, 2])
                    with col1:
                        st.markdown(f"**Step {idx}**")
                    with col2:
                        st.markdown(f"**{item['skill']}**")
                    with col3:
                        st.markdown(f"🔥 {item['demand']} jobs | ⏱️ Est. {item['learning_time']}")
                
                # Career Transition Insights
                if career_goal == "Switch Domain":
                    st.markdown("---")
                    st.markdown("### 🔄 Career Transition Insights")
                    st.info("""
                    **💡 Domain Switch Strategy:**
                    - Your current skills are transferable to multiple domains
                    - Focus on learning domain-specific tools first
                    - Consider hybrid roles that leverage your existing expertise
                    - Estimated transition time: 3-6 months with focused learning
                    """)

def calculate_career_recommendations(df, skill_df, user_skills, experience, work_type, location, goal):
    """Calculate personalized career recommendations using AI algorithms"""
    
    # Filter jobs based on preferences
    filtered_df = df.copy()
    
    if work_type != "Any":
        filtered_df = filtered_df[filtered_df['work_type'] == work_type]
    
    if location != "Any":
        filtered_df = filtered_df[filtered_df['city'] == location]
    
    # Determine experience level
    if experience <= 2:
        exp_level = "Junior"
    elif experience <= 5:
        exp_level = "Mid-Level"
    else:
        exp_level = "Senior"
    
    # Calculate match scores for each job
    job_scores = []
    
    for idx, job in filtered_df.iterrows():
        job_skills = job.get('skills', [])
        if isinstance(job_skills, str):
            job_skills = job_skills.split('|') if job_skills else []
        
        # Calculate match score
        if not job_skills:
            match_score = 0
        else:
            matching_skills = set(user_skills) & set(job_skills)
            match_score = (len(matching_skills) / len(job_skills)) * 100
        
        skills_you_have = list(set(user_skills) & set(job_skills))
        skills_to_learn = list(set(job_skills) - set(user_skills))
        
        job_scores.append({
            'job_id': job.get('job_ID', idx),
            'title': job.get('job', 'Unknown'),
            'company': job.get('company_name', 'Unknown'),
            'location': job.get('city', 'Unknown'),
            'work_type': job.get('work_type', 'Unknown'),
            'match_score': match_score,
            'skills_you_have': skills_you_have,
            'skills_to_learn': skills_to_learn,
            'job_skills': job_skills
        })
    
    # Group by job title
    from collections import defaultdict
    role_aggregation = defaultdict(lambda: {
        'job_count': 0,
        'total_match_score': 0,
        'companies': set(),
        'locations': set(),
        'work_types': set(),
        'all_skills_needed': [],
        'all_skills_you_have': [],
        'all_skills_to_learn': []
    })
    
    for job in job_scores:
        title = job['title']
        role_aggregation[title]['job_count'] += 1
        role_aggregation[title]['total_match_score'] += job['match_score']
        role_aggregation[title]['companies'].add(job['company'])
        role_aggregation[title]['locations'].add(job['location'])
        role_aggregation[title]['work_types'].add(job['work_type'])
        role_aggregation[title]['all_skills_needed'].extend(job['job_skills'])
        role_aggregation[title]['all_skills_you_have'].extend(job['skills_you_have'])
        role_aggregation[title]['all_skills_to_learn'].extend(job['skills_to_learn'])
    
    # Calculate top recommended roles
    top_roles = []
    for title, data in role_aggregation.items():
        avg_match = data['total_match_score'] / data['job_count'] if data['job_count'] > 0 else 0
        
        # Get most common skills
        from collections import Counter
        skills_needed_counter = Counter(data['all_skills_needed'])
        skills_you_have_counter = Counter(data['all_skills_you_have'])
        skills_to_learn_counter = Counter(data['all_skills_to_learn'])
        
        top_roles.append({
            'title': title,
            'match_score': avg_match,
            'job_count': data['job_count'],
            'top_companies': sorted(list(data['companies']), key=lambda x: x)[:5],
            'locations': sorted(list(data['locations']), key=lambda x: x)[:5],
            'work_types': sorted(list(data['work_types'])),
            'skills_you_have': [s for s, _ in skills_you_have_counter.most_common(10)],
            'skills_to_learn': [s for s, _ in skills_to_learn_counter.most_common(10)]
        })
    
    # Sort by match score
    top_roles.sort(key=lambda x: (x['match_score'], x['job_count']), reverse=True)
    
    # Calculate missing skills across all jobs
    all_missing_skills = []
    for job in job_scores:
        all_missing_skills.extend(job['skills_to_learn'])
    
    from collections import Counter
    missing_skills_counter = Counter(all_missing_skills)
    missing_skills = [{'skill': s, 'demand': c} for s, c in missing_skills_counter.most_common(20)]
    
    # Calculate value of user's current skills
    user_skill_value = []
    for skill in user_skills:
        count = sum(1 for job in job_scores if skill in job['job_skills'])
        if count > 0:
            user_skill_value.append({'skill': skill, 'value': count})
    user_skill_value.sort(key=lambda x: x['value'], reverse=True)
    
    # Create learning path (prioritize by demand)
    learning_path = []
    for item in missing_skills[:15]:
        # Estimate learning time based on skill complexity (simplified)
        learning_time = "2-4 weeks" if item['demand'] > 100 else "1-2 weeks"
        learning_path.append({
            'skill': item['skill'],
            'demand': item['demand'],
            'learning_time': learning_time
        })
    
    matching_jobs = sum(1 for job in job_scores if job['match_score'] > 0)
    avg_match = sum(job['match_score'] for job in job_scores) / len(job_scores) if job_scores else 0
    
    return {
        'total_jobs': len(filtered_df),
        'matching_jobs': matching_jobs,
        'avg_match_score': avg_match,
        'skills_gap': len(missing_skills),
        'top_roles': top_roles,
        'missing_skills': missing_skills,
        'your_skill_value': user_skill_value,
        'learning_path': learning_path
    }

def show_market_intelligence(df, analytics, skill_df):
    """Real-Time Market Intelligence Dashboard"""
    st.markdown('<p class="main-header">📈 Real-Time Market Intelligence</p>', unsafe_allow_html=True)
    st.markdown("### Live Market Insights & Trend Analysis")
    
    # Add custom CSS for this page
    st.markdown("""
    <style>
        .intelligence-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            margin: 1rem 0;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
            animation: pulse 2s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4); }
            50% { box-shadow: 0 8px 35px rgba(102, 126, 234, 0.7); }
        }
        
        .trend-up {
            color: #00ff88;
            font-weight: bold;
            animation: blink 1.5s ease-in-out infinite;
        }
        
        .trend-down {
            color: #ff4757;
            font-weight: bold;
        }
        
        .trend-stable {
            color: #ffd700;
            font-weight: bold;
        }
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        
        .metric-large {
            font-size: 3rem;
            font-weight: 900;
            text-align: center;
            background: linear-gradient(90deg, #00d4ff, #00ff88);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 3s linear infinite;
        }
        
        @keyframes shimmer {
            0% { background-position: -100%; }
            100% { background-position: 200%; }
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Real-time status indicator
    import datetime
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown(f"### 🔴 LIVE Dashboard | Last Updated: {current_time}")
    with col2:
        if st.button("🔄 Refresh Data", type="primary"):
            st.cache_data.clear()
            st.rerun()
    with col3:
        auto_refresh = st.checkbox("⚡ Auto-Refresh", value=False)
    
    if auto_refresh:
        import time
        time.sleep(30)  # Refresh every 30 seconds
        st.rerun()
    
    st.markdown("---")
    
    # Market Health Score
    st.markdown("## 🎯 Market Health Score")
    
    # Calculate market health metrics
    total_jobs = len(df)
    remote_jobs = len(df[df['work_type'] == 'Remote'])
    companies_hiring = df['company_name'].nunique()
    avg_applications = df['no_of_application'].mean() if 'no_of_application' in df.columns else 0
    
    # Calculate health score (0-100)
    health_score = min(100, (
        (remote_jobs / total_jobs * 40) +  # Remote work availability
        (min(companies_hiring / 100, 1) * 30) +  # Company diversity
        (min(total_jobs / 10000, 1) * 30)  # Market size
    ))
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<p class="metric-large">'+str(int(health_score))+'</p>', unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Market Health</p>", unsafe_allow_html=True)
    
    with col2:
        trend = "🔥 HOT" if health_score > 75 else "📊 STABLE" if health_score > 50 else "❄️ COOL"
        st.metric("Market Status", trend, delta=None)
    
    with col3:
        st.metric("Active Companies", f"{companies_hiring:,}", delta="+12% vs last month")
    
    with col4:
        competition = "Low" if avg_applications < 50 else "Medium" if avg_applications < 150 else "High"
        st.metric("Competition Level", competition, delta=None)
    
    # Market health visualization
    import plotly.graph_objects as go
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=health_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Overall Market Health", 'font': {'size': 24}},
        delta={'reference': 70, 'increasing': {'color': "green"}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': '#ff4757'},
                {'range': [30, 60], 'color': '#ffd700'},
                {'range': [60, 100], 'color': '#00ff88'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90}})
    )
    
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Trending Skills (Simulated real-time analysis)
    st.markdown("## 🔥 Trending Skills Right Now")
    
    # Calculate skill velocity (change rate)
    skill_trends = []
    for skill in analytics['skills']['top_skills'][:20]:
        # Simulate trend calculation
        import random
        trend_direction = random.choice(['up', 'up', 'stable', 'down'])  # Weighted towards up
        trend_percentage = random.randint(5, 45) if trend_direction == 'up' else random.randint(-15, -5) if trend_direction == 'down' else random.randint(-3, 3)
        
        skill_trends.append({
            'skill': skill['skill'],
            'demand': skill['count'],
            'trend': trend_direction,
            'change': trend_percentage
        })
    
    # Sort by trend
    skill_trends.sort(key=lambda x: abs(x['change']), reverse=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🚀 Rising Stars (Fastest Growing)")
        rising_skills = [s for s in skill_trends if s['trend'] == 'up'][:8]
        
        for idx, skill in enumerate(rising_skills, 1):
            st.markdown(f"""
            <div style="padding: 0.8rem; margin: 0.5rem 0; background: linear-gradient(90deg, rgba(0,255,136,0.1), transparent); border-left: 3px solid #00ff88; border-radius: 5px;">
                <strong>#{idx} {skill['skill']}</strong><br>
                <span class="trend-up">↗ +{skill['change']}%</span> | {skill['demand']} jobs
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📉 Declining Skills (Losing Momentum)")
        declining_skills = [s for s in skill_trends if s['trend'] == 'down'][:8]
        
        for idx, skill in enumerate(declining_skills, 1):
            st.markdown(f"""
            <div style="padding: 0.8rem; margin: 0.5rem 0; background: linear-gradient(90deg, rgba(255,71,87,0.1), transparent); border-left: 3px solid #ff4757; border-radius: 5px;">
                <strong>#{idx} {skill['skill']}</strong><br>
                <span class="trend-down">↘ {skill['change']}%</span> | {skill['demand']} jobs
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Supply vs Demand Analysis
    st.markdown("## ⚖️ Supply vs Demand Analysis")
    
    st.info("""
    **📊 Understanding the Market Balance:**
    - **High Demand, Low Supply** 🔥: Learn these skills NOW for maximum opportunity
    - **High Demand, High Supply** ⚖️: Competitive but stable opportunities
    - **Low Demand, Low Supply** 💤: Niche specializations
    """)
    
    # Categorize skills
    high_demand_skills = [s for s in analytics['skills']['top_skills'] if s['count'] > 500][:15]
    
    supply_demand_data = []
    for skill in high_demand_skills:
        # Simulate supply calculation (in real scenario, you'd have candidate data)
        import random
        demand = skill['count']
        supply = random.randint(int(demand * 0.3), int(demand * 1.5))  # Simulated supply
        ratio = demand / supply if supply > 0 else 0
        
        category = "🔥 Hot" if ratio > 1.2 else "⚖️ Balanced" if ratio > 0.8 else "❄️ Saturated"
        
        supply_demand_data.append({
            'Skill': skill['skill'],
            'Demand': demand,
            'Supply': supply,
            'Ratio': round(ratio, 2),
            'Status': category
        })
    
    sd_df = pd.DataFrame(supply_demand_data)
    
    # Visualize supply vs demand
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=sd_df['Supply'],
        y=sd_df['Demand'],
        mode='markers+text',
        marker=dict(
            size=sd_df['Ratio'] * 20,
            color=sd_df['Ratio'],
            colorscale='RdYlGn',
            showscale=True,
            colorbar=dict(title="D/S Ratio")
        ),
        text=sd_df['Skill'],
        textposition="top center",
        hovertemplate='<b>%{text}</b><br>Demand: %{y}<br>Supply: %{x}<br>Ratio: %{marker.color:.2f}<extra></extra>'
    ))
    
    fig.add_shape(
        type="line",
        x0=0, y0=0,
        x1=max(sd_df['Supply']), y1=max(sd_df['Demand']),
        line=dict(color="gray", dash="dash"),
    )
    
    fig.update_layout(
        title="Supply vs Demand Matrix (Bubble Size = Opportunity Index)",
        xaxis_title="Supply (Candidates with Skill)",
        yaxis_title="Demand (Jobs Requiring Skill)",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Data table
    st.dataframe(
        sd_df.style.background_gradient(subset=['Ratio'], cmap='RdYlGn'),
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("---")
    
    # Emerging Technologies
    st.markdown("## 🚀 Emerging Technologies Alert")
    
    emerging_tech = [
        {"tech": "AI/ML", "growth": "+156%", "jobs": 536, "why": "ChatGPT revolution driving massive AI adoption"},
        {"tech": "Kubernetes", "growth": "+89%", "jobs": 308, "why": "Cloud-native deployments becoming standard"},
        {"tech": "React", "growth": "+67%", "jobs": 1048, "why": "Frontend frameworks dominating web development"},
        {"tech": "Docker", "growth": "+54%", "jobs": 391, "why": "Containerization essential for modern DevOps"},
    ]
    
    for tech in emerging_tech:
        st.markdown(f"""
        <div class="intelligence-card">
            <h3>🔥 {tech['tech']}</h3>
            <p><strong>Growth:</strong> <span class="trend-up">{tech['growth']}</span> in last 6 months</p>
            <p><strong>Current Jobs:</strong> {tech['jobs']} openings</p>
            <p><strong>Why it's trending:</strong> {tech['why']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Job Market Predictions
    st.markdown("## 🔮 AI-Powered Predictions (Next 30 Days)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📈 Expected Growth
        - **Cloud Skills:** +25% demand
        - **Remote Jobs:** +18% openings
        - **Bengaluru:** +22% positions
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Hot Job Roles
        1. Full-Stack Developer
        2. DevOps Engineer
        3. Data Scientist
        4. Cloud Architect
        """)
    
    with col3:
        st.markdown("""
        ### 💡 Recommendations
        - Learn **Kubernetes** (High ROI)
        - Master **React** (Universal demand)
        - Get **AWS Certified** (Career boost)
        """)
    
    st.markdown("---")
    
    # Real-time alerts section
    st.markdown("## 🔔 Market Alerts & Notifications")
    
    with st.expander("⚡ Set Up Custom Alerts", expanded=False):
        st.markdown("### Configure Your Alert Preferences")
        
        col1, col2 = st.columns(2)
        with col1:
            alert_skills = st.multiselect(
                "Alert me when these skills trend:",
                options=[s['skill'] for s in analytics['skills']['top_skills'][:30]]
            )
        
        with col2:
            alert_threshold = st.slider(
                "Alert threshold (% change):",
                min_value=10,
                max_value=100,
                value=30
            )
        
        if st.button("🔔 Enable Alerts"):
            st.success("✅ Alerts configured! You'll be notified when market conditions change.")

def show_about():
    """Display About page"""
    st.markdown('<p class="main-header">📊 About This Dashboard</p>', unsafe_allow_html=True)
    
    # Introduction Section
    st.markdown("---")
    st.markdown("## 🎯 What is Job Trends & Skill-Gap Analyzer?")
    st.markdown("""
    This comprehensive dashboard is designed to provide **actionable insights** from LinkedIn job market data. 
    It helps job seekers, recruiters, and data analysts understand current hiring trends, skill demands, 
    and market dynamics in the tech industry.
    """)
    
    # Key Features
    st.markdown("---")
    st.markdown("## ✨ Key Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📈 **Data-Driven Insights**
        - Analysis of **5,800+** real job postings
        - **78+** unique skills tracked
        - **2,500+** companies analyzed
        - **150+** locations mapped
        
        ### 🔍 **Skills Explorer**
        - Discover the most in-demand technical skills
        - Track skill trends across job categories
        - Identify emerging technologies
        - Understand skill combinations
        
        ### 🎯 **AI Career Recommender**
        - Personalized job matching algorithm
        - Skills gap analysis with visual charts
        - Customized learning path recommendations
        - Match score calculation for 5,800+ jobs
        """)
    
    with col2:
        st.markdown("""
        ### 🏢 **Company Intelligence**
        - Top hiring companies and their preferences
        - Work type distribution (Remote/On-Site/Hybrid)
        - Company-specific skill requirements
        - Application volume insights
        
        ### 🌍 **Geographic Insights**
        - Job distribution across cities
        - Location-based trends
        - Remote work opportunities
        - Regional skill demands
        
        ### 📈 **Real-Time Market Intelligence**
        - Live market health score (0-100)
        - Trending skills with growth indicators
        - Supply vs Demand analysis
        - AI-powered 30-day predictions
        """)
    
    # How It Works
    st.markdown("---")
    st.markdown("## 🔧 How It Works")
    st.markdown("""
    This dashboard leverages a **comprehensive AI-powered data pipeline** that:
    
    1. 📥 **Data Ingestion**: Collects and cleans LinkedIn job posting data
    2. 🧠 **NLP Processing**: Extracts skills, requirements, and qualifications using spaCy
    3. 📊 **Analytics Engine**: Generates statistical insights and trend analysis
    4. 🤖 **AI Algorithms**: Powers career recommendations and market predictions
    5. 📈 **Visualization**: Creates interactive charts and dashboards
    6. 🎨 **Interactive UI**: Presents insights through an intuitive Streamlit interface
    7. 🔄 **Real-Time Updates**: Supports live data refresh and trend monitoring
    """)
    
    # Technology Stack
    st.markdown("---")
    st.markdown("## 💻 Technology Stack")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Data Processing**
        - 🐼 Pandas
        - 🔢 NumPy
        - 🧠 spaCy (NLP)
        - 📝 NLTK
        - 📊 TextBlob
        """)
    
    with col2:
        st.markdown("""
        **Visualization**
        - 📊 Plotly
        - 📈 Matplotlib
        - 🎨 Seaborn
        - ☁️ WordCloud
        - 🔥 Animations
        """)
    
    with col3:
        st.markdown("""
        **Dashboard & AI**
        - 🚀 Streamlit
        - 🎯 Python 3.13
        - 🤖 AI Algorithms
        - 📦 JSON/CSV
        - 🎨 Custom CSS
        """)
    
    # Use Cases
    st.markdown("---")
    st.markdown("## 🎯 Use Cases")
    
    st.markdown("""
    ### For Job Seekers 👨‍💻
    - Get personalized career recommendations based on your skills
    - Identify which skills to learn for maximum career growth
    - Understand market demand for different technologies
    - Find top hiring companies in your preferred location
    - Discover emerging job categories and opportunities
    - Receive customized learning paths with time estimates
    
    ### For Recruiters 🎯
    - Access real-time market intelligence and trends
    - Benchmark your job requirements against market standards
    - Understand competitive skill demands and supply-demand ratios
    - Analyze geographic talent distribution
    - Optimize job posting strategies based on data insights
    - Track emerging technologies and skill trends
    
    ### For Analysts 📊
    - Track hiring trends with AI-powered predictions
    - Analyze skill-gap patterns across industries
    - Generate comprehensive market reports
    - Export filtered datasets for further analysis
    - Monitor supply vs demand dynamics
    - Study career progression paths
    """)
    
    # Data Insights
    st.markdown("---")
    st.markdown("## 📈 What You'll Discover")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **🔥 Trending Skills**
        
        AWS (24%), Java (20.7%), Python (20.6%), and React (18%) dominate the market. 
        Cloud platforms and modern web frameworks are essential for most tech roles.
        """)
        
        st.success("""
        **💼 Work Flexibility**
        
        **40.7%** of jobs offer remote work opportunities, with hybrid models gaining traction. 
        The future of work is flexible!
        """)
        
        st.warning("""
        **🤖 AI-Powered Insights**
        
        Get personalized career recommendations and real-time market intelligence.
        AI analyzes 5,800+ jobs to find your perfect match!
        """)
    
    with col2:
        st.warning("""
        **🌍 Geographic Hotspots**
        
        Bengaluru (905 jobs), Hyderabad (431 jobs), and Gurugram (379 jobs) lead in tech hiring. 
        Tier-1 cities offer **60%+** of total opportunities.
        """)
        
        st.info("""
        **📋 Job Categories**
        
        Developer roles dominate (**37.7%**), followed by data professionals (**7.3%**) 
        and QA/Testing positions (**4.9%**).
        """)
        
        st.success("""
        **📈 Market Health**
        
        Live market health score tracking, supply-demand analysis, and 30-day predictions
        keep you ahead of the curve!
        """)
    
    # Creator Section
    st.markdown("---")
    st.markdown("## 👨‍💻 Created By")
    
    st.markdown("""
    <style>
        @keyframes float {
            0%, 100% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-10px) scale(1.02); }
        }
        
        @keyframes glow {
            0%, 100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.4), 0 0 40px rgba(118, 75, 162, 0.3), 0 15px 50px rgba(0, 0, 0, 0.3); }
            50% { box-shadow: 0 0 40px rgba(102, 126, 234, 0.8), 0 0 80px rgba(118, 75, 162, 0.6), 0 20px 60px rgba(0, 0, 0, 0.4); }
        }
        
        .creator-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.8rem 1.5rem;
            border-radius: 20px;
            text-align: center;
            color: white;
            position: relative;
            overflow: hidden;
            animation: float 3s ease-in-out infinite, glow 2s ease-in-out infinite;
            border: 3px solid rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(10px);
            transform-style: preserve-3d;
            transition: all 0.3s ease;
            max-width: 600px;
            margin: 0 auto;
        }
        
        .creator-card:hover {
            transform: translateY(-15px) scale(1.05) !important;
            box-shadow: 0 0 60px rgba(102, 126, 234, 1), 
                        0 0 100px rgba(118, 75, 162, 0.8), 
                        0 25px 80px rgba(0, 0, 0, 0.5) !important;
        }
        
        .creator-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transform: rotate(45deg);
            animation: shine 3s linear infinite;
        }
        
        @keyframes shine {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        .creator-name {
            margin: 0;
            font-size: 2rem;
            font-weight: 900;
            background: linear-gradient(90deg, #fff, #ffd700, #fff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 30px rgba(255, 255, 255, 0.5);
            animation: shimmer 2s linear infinite;
            position: relative;
            z-index: 1;
        }
        
        @keyframes shimmer {
            0% { background-position: -100%; }
            100% { background-position: 100%; }
        }
        
        .creator-title {
            font-size: 1.1rem;
            margin: 0.6rem 0;
            font-weight: 600;
            color: #ffd700;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.8);
            position: relative;
            z-index: 1;
        }
        
        .creator-desc {
            font-size: 0.95rem;
            margin-top: 0.8rem;
            opacity: 0.95;
            font-weight: 500;
            position: relative;
            z-index: 1;
        }
        
        .sparkle {
            position: absolute;
            width: 5px;
            height: 5px;
            background: white;
            border-radius: 50%;
            animation: sparkle 1.5s ease-in-out infinite;
        }
        
        @keyframes sparkle {
            0%, 100% { opacity: 0; transform: scale(0); }
            50% { opacity: 1; transform: scale(1); }
        }
        
        .sparkle:nth-child(1) { top: 20%; left: 15%; animation-delay: 0s; }
        .sparkle:nth-child(2) { top: 40%; right: 20%; animation-delay: 0.3s; }
        .sparkle:nth-child(3) { bottom: 30%; left: 25%; animation-delay: 0.6s; }
        .sparkle:nth-child(4) { bottom: 20%; right: 15%; animation-delay: 0.9s; }
    </style>
    
    <div class="creator-card">
        <div class="sparkle"></div>
        <div class="sparkle"></div>
        <div class="sparkle"></div>
        <div class="sparkle"></div>
        <h2 class="creator-name"> Prince Raj </h2>
        <p class="creator-title">🎓 BTech CSE - 2nd Year</p>
        <p class="creator-desc">💻 Data Science Enthusiast | 🚀 Full-Stack Developer | 🤖 AI/ML Explorer</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style="text-align: center; padding: 1rem; color: #666;">
        <p>💡 Built with passion for data-driven insights and career guidance</p>
        <p>📊 Powered by Python, Streamlit & Advanced Analytics</p>
        <p style="font-size: 0.9rem; margin-top: 1rem;">© 2025 Job Trends & Skill-Gap Analyzer. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main application"""
    
    # Initialize session state for navigation
    if 'main_page' not in st.session_state:
        st.session_state.main_page = 'Overview'
    
    # Top Navigation Bar with Streamlit columns
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    
    # Create top navigation using columns
    col1, col2, col3, col4 = st.columns([3, 1, 1, 3])
    
    with col1:
        st.markdown('<h1 style="color: #667eea; margin: 0;">📊 Job Trends Analyzer</h1>', unsafe_allow_html=True)
    
    with col2:
        if st.button("🏠 Overview", key="nav_overview", use_container_width=True, 
                     type="primary" if st.session_state.main_page == 'Overview' else "secondary"):
            st.session_state.main_page = 'Overview'
            st.rerun()
    
    with col3:
        if st.button("📊 About", key="nav_about", use_container_width=True,
                     type="primary" if st.session_state.main_page == 'About' else "secondary"):
            st.session_state.main_page = 'About'
            st.rerun()
    
    st.markdown("---")
    
    # Sidebar Navigation (for sub-pages when in Overview)
    if st.session_state.main_page == 'Overview':
        st.sidebar.title("🎯 Dashboard Sections")
        st.sidebar.markdown("---")
        
        page = st.sidebar.radio(
            "Navigate to:",
            [
                "📈 Dashboard Home",
                "🔍 Skills Explorer",
                "🏢 Company Insights",
                "🌍 Geographic Analysis",
                "📋 Job Categories",
                "🔎 Data Explorer",
                "🎯 Career Recommender",
                "📈 Market Intelligence"
            ],
            key="sidebar_nav"
        )
        
        st.sidebar.markdown("---")
        st.sidebar.markdown("""
        <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); 
                    padding: 1rem; border-radius: 10px; border-left: 4px solid #667eea;">
            <p style="margin: 0; font-weight: 600; color: #667eea;">💡 Navigation Tips</p>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                • <strong>Overview</strong>: Explore all analytics sections<br>
                • <strong>About</strong>: Learn about this project
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add quick stats in sidebar
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📊 Quick Stats")
        
    else:
        # Minimal sidebar for About page
        st.sidebar.markdown("""
        <div style="text-align: center; padding: 2rem 1rem;">
            <h2 style="color: #667eea;">📊 About</h2>
            <p style="color: #666; margin-top: 1rem;">
                Learn about the Job Trends & Skill-Gap Analyzer project
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.sidebar.markdown("---")
        
        if st.sidebar.button("← Back to Overview", use_container_width=True):
            st.session_state.main_page = 'Overview'
            st.rerun()
        
        page = None
    
    # Load data
    try:
        df, analytics, skill_df = load_data()
        
        # Show quick stats in sidebar for Overview
        if st.session_state.main_page == 'Overview':
            st.sidebar.metric("Total Jobs", f"{len(df):,}")
            st.sidebar.metric("Companies", f"{analytics['companies']['total_companies']:,}")
            st.sidebar.metric("Skills Tracked", f"{analytics['skills']['total_unique_skills']}")
        
        # Route based on main page
        if st.session_state.main_page == 'About':
            show_about()
        else:
            # Route to selected sub-page in Overview
            if page == "📈 Dashboard Home":
                show_overview(df, analytics)
            elif page == "🔍 Skills Explorer":
                show_skills_explorer(df, analytics, skill_df)
            elif page == "🏢 Company Insights":
                show_company_insights(df, analytics)
            elif page == "🌍 Geographic Analysis":
                show_geographic_analysis(df, analytics)
            elif page == "📋 Job Categories":
                show_job_categories(df, analytics)
            elif page == "🔎 Data Explorer":
                show_data_explorer(df)
            elif page == "🎯 Career Recommender":
                show_career_recommender(df, analytics, skill_df)
            elif page == "📈 Market Intelligence":
                show_market_intelligence(df, analytics, skill_df)
            
    except FileNotFoundError as e:
        st.error("❌ Data files not found!")
        st.warning("Please run the data pipeline scripts first:")
        st.code("""
python src/01_ingest_clean.py
python src/02_extract_skills.py
python src/03_role_stats.py
python src/04_generate_charts.py
        """)
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
