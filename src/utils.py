"""
Utility Functions
Common helper functions used across the project
"""

import pandas as pd
from pathlib import Path
import re
from typing import List, Dict, Any

def ensure_dir(path: Path) -> None:
    """Ensure directory exists, create if it doesn't"""
    path.mkdir(parents=True, exist_ok=True)

def safe_read_csv(file_path: Path, encoding: str = 'utf-8') -> pd.DataFrame:
    """Safely read CSV with fallback encoding"""
    try:
        return pd.read_csv(file_path, encoding=encoding)
    except UnicodeDecodeError:
        return pd.read_csv(file_path, encoding='latin-1')

def clean_text(text: str) -> str:
    """Clean and normalize text"""
    if pd.isna(text):
        return ''
    
    # Convert to string
    text = str(text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove special characters
    text = re.sub(r'[^\w\s\-\.]', ' ', text)
    
    return text.strip()

def extract_numbers(text: str) -> List[int]:
    """Extract all numbers from text"""
    if pd.isna(text):
        return []
    
    return [int(n) for n in re.findall(r'\d+', str(text))]

def parse_employee_count(text: str) -> int:
    """Parse employee count ranges to approximate number"""
    if pd.isna(text):
        return 0
    
    text = str(text).lower()
    
    # Common patterns
    if '10,000+' in text or '10000+' in text:
        return 10000
    elif '5,001-10,000' in text or '5001-10000' in text:
        return 7500
    elif '1,001-5,000' in text or '1001-5000' in text:
        return 3000
    elif '501-1,000' in text or '501-1000' in text:
        return 750
    elif '201-500' in text:
        return 350
    elif '51-200' in text:
        return 125
    elif '11-50' in text:
        return 30
    elif '1-10' in text:
        return 5
    else:
        # Try to extract numbers
        nums = extract_numbers(text)
        return nums[0] if nums else 0

def format_large_number(num: int) -> str:
    """Format large numbers with K, M suffixes"""
    if num >= 1_000_000:
        return f"{num/1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num/1_000:.1f}K"
    else:
        return str(num)

def calculate_percentage(part: int, total: int) -> float:
    """Calculate percentage with error handling"""
    if total == 0:
        return 0.0
    return round((part / total) * 100, 2)

def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to max length with ellipsis"""
    if pd.isna(text):
        return ''
    
    text = str(text)
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length-3] + '...'

def standardize_location(location: str) -> Dict[str, str]:
    """Parse and standardize location string"""
    if pd.isna(location):
        return {'city': 'Unknown', 'state': 'Unknown', 'country': 'Unknown'}
    
    parts = [p.strip() for p in str(location).split(',')]
    
    if len(parts) >= 3:
        return {'city': parts[0], 'state': parts[1], 'country': parts[2]}
    elif len(parts) == 2:
        return {'city': parts[0], 'state': parts[1], 'country': 'India'}
    elif len(parts) == 1:
        return {'city': parts[0], 'state': 'Unknown', 'country': 'India'}
    else:
        return {'city': 'Unknown', 'state': 'Unknown', 'country': 'Unknown'}

def create_summary_dict(df: pd.DataFrame, column: str, top_n: int = 10) -> List[Dict[str, Any]]:
    """Create summary dictionary for a column"""
    value_counts = df[column].value_counts().head(top_n)
    
    return [
        {
            'value': str(val),
            'count': int(count),
            'percentage': calculate_percentage(count, len(df))
        }
        for val, count in value_counts.items()
    ]

def filter_dataframe(df: pd.DataFrame, filters: Dict[str, Any]) -> pd.DataFrame:
    """Apply multiple filters to dataframe"""
    filtered = df.copy()
    
    for column, value in filters.items():
        if value and value != 'All':
            filtered = filtered[filtered[column] == value]
    
    return filtered

def validate_data_quality(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate data quality and return report"""
    return {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'missing_values': df.isnull().sum().to_dict(),
        'duplicate_rows': df.duplicated().sum(),
        'memory_usage': f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB"
    }

def export_to_excel(df: pd.DataFrame, file_path: Path, sheet_name: str = 'Data') -> None:
    """Export dataframe to Excel with formatting"""
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Auto-adjust column widths
        worksheet = writer.sheets[sheet_name]
        for idx, col in enumerate(df.columns):
            max_length = max(
                df[col].astype(str).apply(len).max(),
                len(str(col))
            )
            worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)

if __name__ == "__main__":
    # Test utilities
    print("✅ Utility functions loaded successfully")
    print(f"   format_large_number(12500): {format_large_number(12500)}")
    print(f"   calculate_percentage(75, 300): {calculate_percentage(75, 300)}%")
