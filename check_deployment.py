"""
Deployment Readiness Check
Verifies all required files exist before deploying to Streamlit Cloud
"""

import sys
from pathlib import Path
import json

# Base directory
BASE_DIR = Path(__file__).parent

# Required files for deployment
REQUIRED_FILES = {
    'Main App': 'app/streamlit_app.py',
    'Requirements': 'requirements.txt',
    'Setup Script': 'setup.sh',
    'Jobs Data': 'data/processed/jobs_with_skills.csv',
    'Analytics': 'data/processed/analytics_summary.json',
    'Skills Data': 'data/processed/skills_extracted.csv',
}

def check_files():
    """Check if all required files exist"""
    print("=" * 60)
    print("🔍 STREAMLIT DEPLOYMENT READINESS CHECK")
    print("=" * 60)
    print()
    
    all_exist = True
    
    for name, file_path in REQUIRED_FILES.items():
        full_path = BASE_DIR / file_path
        exists = full_path.exists()
        
        status = "✅" if exists else "❌"
        print(f"{status} {name:.<30} {file_path}")
        
        if not exists:
            all_exist = False
    
    print()
    print("=" * 60)
    
    if all_exist:
        print("✅ ALL FILES READY FOR DEPLOYMENT!")
        print()
        print("Next steps:")
        print("1. Commit and push to GitHub:")
        print("   git add .")
        print("   git commit -m 'Ready for deployment'")
        print("   git push origin main")
        print()
        print("2. Deploy on Streamlit Cloud:")
        print("   Visit: https://share.streamlit.io/")
        print("   Click 'New app' and follow DEPLOYMENT.md")
        print()
        return 0
    else:
        print("❌ SOME FILES ARE MISSING!")
        print()
        print("Please run the pipeline to generate data files:")
        print("   python src/run_pipeline.py")
        print()
        return 1

if __name__ == "__main__":
    sys.exit(check_files())
