"""
Logging Configuration
Centralized logging setup for the entire project
"""

import logging
import sys
from pathlib import Path
from datetime import datetime

# Create logs directory
LOG_DIR = Path(__file__).parent.parent / 'logs'
LOG_DIR.mkdir(exist_ok=True)

# Log file with timestamp
LOG_FILE = LOG_DIR / f"job_analyzer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

def setup_logger(name: str = 'job_analyzer', level: int = logging.INFO):
    """
    Setup and configure logger
    
    Args:
        name: Logger name
        level: Logging level
        
    Returns:
        Configured logger instance
    """
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid duplicate handlers
    if logger.handlers:
        return logger
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    simple_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )
    
    # File handler (detailed)
    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    
    # Console handler (simple)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def log_execution_time(func):
    """Decorator to log function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('job_analyzer')
        start_time = time.time()
        
        logger.info(f"Starting {func.__name__}...")
        
        try:
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            logger.info(f"Completed {func.__name__} in {elapsed_time:.2f} seconds")
            return result
            
        except Exception as e:
            elapsed_time = time.time() - start_time
            logger.error(f"Failed {func.__name__} after {elapsed_time:.2f} seconds: {str(e)}")
            raise
    
    return wrapper

# Create default logger
logger = setup_logger()

if __name__ == "__main__":
    # Test logging
    logger.info("Logger initialized successfully")
    logger.debug("This is a debug message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    print(f"\n✅ Log file created: {LOG_FILE}")
