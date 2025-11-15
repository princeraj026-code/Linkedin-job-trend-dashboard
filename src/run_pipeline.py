"""
Master Script - Run Complete Pipeline
Executes all processing scripts in sequence
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def run_script(script_path, script_name):
    """Run a Python script and handle errors"""
    print(f"🚀 Running: {script_name}...")
    print(f"   Script: {script_path}")
    print("-" * 70)
    
    start_time = datetime.now()
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=False,
            text=True,
            check=True
        )
        
        elapsed = (datetime.now() - start_time).total_seconds()
        print(f"\n✅ {script_name} completed successfully in {elapsed:.1f}s")
        return True
        
    except subprocess.CalledProcessError as e:
        elapsed = (datetime.now() - start_time).total_seconds()
        print(f"\n❌ {script_name} failed after {elapsed:.1f}s")
        print(f"   Error code: {e.returncode}")
        return False

def main():
    """Main pipeline execution"""
    print_header("🎯 JOB TRENDS ANALYZER - FULL PIPELINE")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Define pipeline scripts
    src_dir = Path(__file__).parent
    
    scripts = [
        (src_dir / '01_ingest_clean.py', 'Data Ingestion & Cleaning'),
        (src_dir / '02_extract_skills.py', 'Skill Extraction'),
        (src_dir / '03_role_stats.py', 'Analytics Generation'),
        (src_dir / '04_generate_charts.py', 'Chart Generation')
    ]
    
    # Track results
    results = []
    total_start = datetime.now()
    
    # Run each script
    for script_path, script_name in scripts:
        if not script_path.exists():
            print(f"❌ Script not found: {script_path}")
            results.append((script_name, False))
            continue
        
        success = run_script(script_path, script_name)
        results.append((script_name, success))
        
        if not success:
            print("\n⚠️  Pipeline halted due to error")
            break
    
    # Summary
    total_elapsed = (datetime.now() - total_start).total_seconds()
    
    print_header("📊 PIPELINE SUMMARY")
    
    for script_name, success in results:
        status = "✅ SUCCESS" if success else "❌ FAILED"
        print(f"{status:12} - {script_name}")
    
    print(f"\nTotal execution time: {total_elapsed:.1f}s")
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Final status
    all_success = all(success for _, success in results)
    
    if all_success:
        print("\n🎉 Pipeline completed successfully!")
        print("\n📌 Next Steps:")
        print("   Run: streamlit run app/streamlit_app.py")
        print("   Or use VS Code task: 'Start Streamlit Dashboard'")
    else:
        print("\n⚠️  Pipeline completed with errors")
        print("   Please check the error messages above")
        sys.exit(1)

if __name__ == "__main__":
    main()
