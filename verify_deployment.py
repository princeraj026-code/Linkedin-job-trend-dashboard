"""
Pre-Deployment Verification for Streamlit Cloud
Checks all critical files and configurations
"""

import sys
from pathlib import Path
import importlib.util

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def check_file(file_path, description):
    """Check if a file exists"""
    exists = Path(file_path).exists()
    status = f"{GREEN}✓{RESET}" if exists else f"{RED}✗{RESET}"
    print(f"{status} {description:.<50} {file_path}")
    return exists

def check_import(module_name):
    """Check if a module can be imported"""
    try:
        __import__(module_name)
        print(f"{GREEN}✓{RESET} {module_name:.<50} Installed")
        return True
    except ImportError:
        print(f"{RED}✗{RESET} {module_name:.<50} NOT INSTALLED")
        return False

def main():
    print(f"\n{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}🚀 STREAMLIT CLOUD DEPLOYMENT VERIFICATION{RESET}")
    print(f"{BLUE}{'='*70}{RESET}\n")
    
    # Check critical files
    print(f"{YELLOW}📁 Checking Files:{RESET}\n")
    
    files_ok = True
    files_ok &= check_file("app/streamlit_app.py", "Main App")
    files_ok &= check_file("requirements.txt", "Dependencies")
    files_ok &= check_file("setup.sh", "Setup Script")
    files_ok &= check_file("packages.txt", "System Packages")
    files_ok &= check_file(".streamlit/config.toml", "Streamlit Config")
    files_ok &= check_file("data/processed/jobs_with_skills.csv", "Jobs Data")
    files_ok &= check_file("data/processed/analytics_summary.json", "Analytics Data")
    files_ok &= check_file("data/processed/skills_extracted.csv", "Skills Data")
    files_ok &= check_file("data/raw/linkdin_Job_data.csv", "Raw Data")
    
    # Check requirements.txt
    print(f"\n{YELLOW}📦 Checking Requirements File:{RESET}\n")
    
    packages_ok = True
    req_file = Path("requirements.txt")
    if req_file.exists():
        with open(req_file, 'r') as f:
            content = f.read()
            critical_packages = ['pandas', 'streamlit', 'plotly', 'spacy']
            for pkg in critical_packages:
                if pkg in content.lower():
                    print(f"{GREEN}✓{RESET} {pkg:.<50} Listed in requirements.txt")
                else:
                    print(f"{RED}✗{RESET} {pkg:.<50} NOT in requirements.txt")
                    packages_ok = False
    else:
        print(f"{RED}✗{RESET} requirements.txt not found")
        packages_ok = False
    
    # Check data file sizes
    print(f"\n{YELLOW}📊 Data File Sizes:{RESET}\n")
    
    data_files = [
        "data/raw/linkdin_Job_data.csv",
        "data/processed/jobs_with_skills.csv",
        "data/processed/analytics_summary.json"
    ]
    
    for file_path in data_files:
        path = Path(file_path)
        if path.exists():
            size_mb = path.stat().st_size / (1024 * 1024)
            status = f"{GREEN}✓{RESET}" if size_mb < 50 else f"{YELLOW}⚠{RESET}"
            print(f"{status} {file_path:.<50} {size_mb:.2f} MB")
    
    # Final verdict
    print(f"\n{BLUE}{'='*70}{RESET}")
    
    if files_ok and packages_ok:
        print(f"{GREEN}✅ ALL CHECKS PASSED - READY FOR DEPLOYMENT!{RESET}")
        print(f"\n{BLUE}Next Steps:{RESET}")
        print(f"1. Visit: https://share.streamlit.io/")
        print(f"2. Click 'New app'")
        print(f"3. Repository: princeraj026-code/Linkedin-job-trend-dashboard")
        print(f"4. Branch: main")
        print(f"5. Main file: app/streamlit_app.py")
        print(f"6. Click 'Deploy!'")
        print(f"\n{GREEN}📖 Full guide: Open STREAMLIT_DEPLOY_NOW.md{RESET}")
        return 0
    else:
        print(f"{RED}❌ SOME CHECKS FAILED{RESET}")
        if not files_ok:
            print(f"{YELLOW}→ Some required files are missing{RESET}")
        if not packages_ok:
            print(f"{YELLOW}→ Some Python packages need to be installed{RESET}")
            print(f"   Run: pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())
