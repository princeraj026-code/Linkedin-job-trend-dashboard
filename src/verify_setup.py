"""
Environment Verification Script
Checks if all dependencies and files are properly set up
"""

import sys
from pathlib import Path
import importlib

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def check_python_version():
    """Check Python version"""
    print("\n🐍 Python Version Check")
    version = sys.version_info
    print(f"   Current: Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Python version is compatible (3.8+)")
        return True
    else:
        print("   ❌ Python 3.8+ required")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    print("\n📦 Dependency Check")
    
    required_packages = [
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'plotly',
        'streamlit',
        'wordcloud',
        'openpyxl'
    ]
    
    missing = []
    installed = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            installed.append(package)
            print(f"   ✅ {package}")
        except ImportError:
            missing.append(package)
            print(f"   ❌ {package} - NOT INSTALLED")
    
    print(f"\n   Installed: {len(installed)}/{len(required_packages)}")
    
    if missing:
        print(f"\n   ⚠️  Missing packages: {', '.join(missing)}")
        print("   Run: pip install -r requirements.txt")
        return False
    
    return True

def check_project_structure():
    """Check if project directories exist"""
    print("\n📁 Project Structure Check")
    
    base_dir = Path(__file__).parent.parent
    
    required_dirs = [
        'src',
        'app',
        'data/raw',
        'data/processed',
        'outputs/charts',
        'outputs/reports',
        'docs'
    ]
    
    all_exist = True
    
    for dir_path in required_dirs:
        full_path = base_dir / dir_path
        if full_path.exists():
            print(f"   ✅ {dir_path}/")
        else:
            print(f"   ❌ {dir_path}/ - MISSING")
            all_exist = False
    
    return all_exist

def check_csv_file():
    """Check if data CSV exists"""
    print("\n📄 Data File Check")
    
    base_dir = Path(__file__).parent.parent
    csv_file = base_dir / 'linkdin_Job_data.csv'
    
    if csv_file.exists():
        size_mb = csv_file.stat().st_size / (1024 * 1024)
        print(f"   ✅ linkdin_Job_data.csv found")
        print(f"   📊 File size: {size_mb:.2f} MB")
        return True
    else:
        print(f"   ❌ linkdin_Job_data.csv NOT FOUND")
        print(f"   Expected location: {csv_file}")
        return False

def check_scripts():
    """Check if all Python scripts exist"""
    print("\n🔧 Script Files Check")
    
    base_dir = Path(__file__).parent
    
    scripts = [
        'config.py',
        '01_ingest_clean.py',
        '02_extract_skills.py',
        '03_role_stats.py',
        '04_generate_charts.py',
        'run_pipeline.py',
        'utils.py',
        'logger.py'
    ]
    
    all_exist = True
    
    for script in scripts:
        script_path = base_dir / script
        if script_path.exists():
            print(f"   ✅ {script}")
        else:
            print(f"   ❌ {script} - MISSING")
            all_exist = False
    
    # Check streamlit app
    app_file = base_dir.parent / 'app' / 'streamlit_app.py'
    if app_file.exists():
        print(f"   ✅ app/streamlit_app.py")
    else:
        print(f"   ❌ app/streamlit_app.py - MISSING")
        all_exist = False
    
    return all_exist

def check_config():
    """Check if config.py is properly set up"""
    print("\n⚙️  Configuration Check")
    
    try:
        sys.path.append(str(Path(__file__).parent))
        import config
        
        print(f"   ✅ config.py loaded successfully")
        print(f"   📊 {len(config.SKILL_CATEGORIES)} skill categories defined")
        print(f"   📋 {len(config.JOB_CATEGORIES)} job categories defined")
        return True
        
    except Exception as e:
        print(f"   ❌ Error loading config: {str(e)}")
        return False

def main():
    """Main verification function"""
    print_header("🔍 JOB TRENDS ANALYZER - Environment Verification")
    print("\nThis script verifies that your environment is properly set up.\n")
    
    # Run all checks
    checks = [
        ("Python Version", check_python_version()),
        ("Dependencies", check_dependencies()),
        ("Project Structure", check_project_structure()),
        ("Data File", check_csv_file()),
        ("Script Files", check_scripts()),
        ("Configuration", check_config())
    ]
    
    # Summary
    print_header("📊 VERIFICATION SUMMARY")
    
    passed = sum(1 for _, result in checks if result)
    total = len(checks)
    
    for check_name, result in checks:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} - {check_name}")
    
    print(f"\nResults: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 All checks passed! Your environment is ready.")
        print("\n📌 Next Steps:")
        print("   1. Run: python src/run_pipeline.py")
        print("   2. Run: streamlit run app/streamlit_app.py")
        print("\n   Or use VS Code tasks (Ctrl+Shift+P → Run Task)")
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
        print("\n💡 Common fixes:")
        print("   • Install dependencies: pip install -r requirements.txt")
        print("   • Ensure CSV file is in project root directory")
        print("   • Check that all project files are present")
        
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    print()
    sys.exit(exit_code)
