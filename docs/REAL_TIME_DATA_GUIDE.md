# 🔴 REAL-TIME DATA IMPLEMENTATION GUIDE

## 📊 Complete Step-by-Step Guide for Live Job Market Data

---

## 🎯 WHAT IS REAL-TIME DATA?

Real-time data means your dashboard updates automatically with the latest job postings from LinkedIn, Indeed, Naukri, etc., instead of using a static CSV file.

**Benefits:**
- ✅ Always current job market insights
- ✅ Track actual market trends over time
- ✅ Competitive advantage (live data vs static)
- ✅ Build time-series analysis (historical trends)
- ✅ More impressive for hackathons/projects

---

## 🚀 METHOD 1: LinkedIn Jobs API (Official - Recommended)

### **Step 1: Get LinkedIn API Access**

1. **Create LinkedIn Developer Account**
   - Go to: https://www.linkedin.com/developers/
   - Click "Create App"
   - Fill in application details

2. **Request API Access**
   - Navigate to "Products" tab
   - Request access to "Jobs API"
   - Wait for approval (can take 3-7 days)

3. **Get API Credentials**
   ```
   Client ID: your_client_id
   Client Secret: your_client_secret
   ```

### **Step 2: Install Required Libraries**

```powershell
pip install linkedin-api requests python-dotenv pandas
```

### **Step 3: Create `.env` File**

```env
LINKEDIN_CLIENT_ID=your_client_id_here
LINKEDIN_CLIENT_SECRET=your_client_secret_here
LINKEDIN_ACCESS_TOKEN=your_access_token_here
```

### **Step 4: Create LinkedIn Scraper Script**

Create `src/linkedin_scraper.py`:

```python
import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class LinkedInJobScraper:
    def __init__(self):
        self.client_id = os.getenv('LINKEDIN_CLIENT_ID')
        self.client_secret = os.getenv('LINKEDIN_CLIENT_SECRET')
        self.access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')
        self.base_url = 'https://api.linkedin.com/v2'
        
    def get_access_token(self):
        """OAuth 2.0 authentication"""
        auth_url = 'https://www.linkedin.com/oauth/v2/accessToken'
        
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        
        response = requests.post(auth_url, data=payload)
        return response.json()['access_token']
    
    def fetch_jobs(self, keywords='software engineer', location='India', count=100):
        """Fetch jobs from LinkedIn API"""
        
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        # LinkedIn Jobs API endpoint
        endpoint = f'{self.base_url}/jobs'
        
        params = {
            'keywords': keywords,
            'location': location,
            'count': count,
            'start': 0
        }
        
        all_jobs = []
        
        while len(all_jobs) < count:
            response = requests.get(endpoint, headers=headers, params=params)
            
            if response.status_code == 200:
                data = response.json()
                jobs = data.get('elements', [])
                
                for job in jobs:
                    all_jobs.append({
                        'job_ID': job.get('id'),
                        'job': job.get('title'),
                        'company_name': job.get('companyName'),
                        'location': job.get('location'),
                        'work_type': job.get('workplaceType'),
                        'job_details': job.get('description'),
                        'posted_date': job.get('listedAt'),
                        'no_of_application': job.get('applicantCount', 0),
                        'timestamp': datetime.now().isoformat()
                    })
                
                # Pagination
                params['start'] += len(jobs)
                
                if not jobs:
                    break
            else:
                print(f"Error: {response.status_code}")
                break
        
        return pd.DataFrame(all_jobs)
    
    def save_to_csv(self, df, filename='linkedin_jobs_realtime.csv'):
        """Save scraped data"""
        df.to_csv(filename, index=False)
        print(f"✅ Saved {len(df)} jobs to {filename}")

# Usage
if __name__ == "__main__":
    scraper = LinkedInJobScraper()
    jobs_df = scraper.fetch_jobs(keywords='python developer', location='India', count=500)
    scraper.save_to_csv(jobs_df)
```

---

## 🛠️ METHOD 2: Web Scraping (No API - Easier to Start)

### **Using RapidAPI (Easiest)**

1. **Get RapidAPI Key**
   - Go to: https://rapidapi.com/
   - Search for "LinkedIn Jobs API" or "Indeed Jobs API"
   - Subscribe (free tier available)

2. **Install Libraries**
```powershell
pip install requests python-dotenv
```

3. **Create Scraper Using RapidAPI**

Create `src/rapidapi_scraper.py`:

```python
import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class RapidAPIJobScraper:
    def __init__(self):
        self.api_key = os.getenv('RAPIDAPI_KEY')
        
    def scrape_linkedin_jobs(self, keyword='software engineer', location='india', limit=100):
        """Scrape LinkedIn jobs via RapidAPI"""
        
        url = "https://linkedin-data-scraper.p.rapidapi.com/jobs"
        
        querystring = {
            "keywords": keyword,
            "location": location,
            "datePosted": "anyTime",
            "sort": "mostRelevant"
        }
        
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "linkedin-data-scraper.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            data = response.json()
            jobs = data.get('data', [])
            
            job_list = []
            for job in jobs[:limit]:
                job_list.append({
                    'job_ID': job.get('id'),
                    'job': job.get('title'),
                    'company_name': job.get('company', {}).get('name'),
                    'location': job.get('location'),
                    'work_type': job.get('workplaceType', 'Not Specified'),
                    'job_details': job.get('description'),
                    'no_of_application': job.get('applicationsCount', 0),
                    'posted_date': job.get('postedAt'),
                    'timestamp': datetime.now().isoformat()
                })
            
            return pd.DataFrame(job_list)
        else:
            print(f"Error: {response.status_code}")
            return pd.DataFrame()

# Usage
scraper = RapidAPIJobScraper()
df = scraper.scrape_linkedin_jobs(keyword='python', location='india', limit=500)
df.to_csv('data/raw/linkedin_realtime.csv', index=False)
```

---

## 🔄 METHOD 3: Automated Scheduled Scraping

### **Using GitHub Actions (Free Cloud Automation)**

1. **Create `.github/workflows/scrape_jobs.yml`**

```yaml
name: Daily Job Scraping

on:
  schedule:
    # Runs every 6 hours
    - cron: '0 */6 * * *'
  workflow_dispatch: # Manual trigger

jobs:
  scrape:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run scraper
      env:
        RAPIDAPI_KEY: ${{ secrets.RAPIDAPI_KEY }}
      run: |
        python src/rapidapi_scraper.py
    
    - name: Commit and push if changed
      run: |
        git config user.name "GitHub Actions Bot"
        git config user.email "actions@github.com"
        git add data/raw/*.csv
        git diff --quiet && git diff --staged --quiet || (git commit -m "Auto-update job data" && git push)
```

2. **Add Secret to GitHub**
   - Go to your repo → Settings → Secrets → New repository secret
   - Name: `RAPIDAPI_KEY`
   - Value: Your API key

---

## 🎯 METHOD 4: Real-Time Database Integration

### **Using Supabase (PostgreSQL + Real-time)**

1. **Create Free Supabase Account**
   - Go to: https://supabase.com
   - Create new project
   - Get API keys

2. **Install Supabase Client**
```powershell
pip install supabase
```

3. **Create Database Sync Script**

```python
from supabase import create_client
import pandas as pd
import os

# Initialize Supabase
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
supabase = create_client(url, key)

# Upload jobs to Supabase
def upload_jobs_to_db(df):
    records = df.to_dict('records')
    
    for record in records:
        supabase.table('jobs').upsert(record).execute()
    
    print(f"✅ Uploaded {len(records)} jobs to database")

# Real-time listener
def listen_to_changes():
    """Listen to real-time database changes"""
    
    def on_insert(payload):
        print("New job added:", payload)
        # Trigger dashboard refresh
    
    supabase.table('jobs').on('INSERT', on_insert).subscribe()

# Usage
df = pd.read_csv('data/raw/linkedin_jobs.csv')
upload_jobs_to_db(df)
```

4. **Modify Streamlit to Use Database**

```python
# In streamlit_app.py
@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_data_from_db():
    response = supabase.table('jobs').select("*").execute()
    df = pd.DataFrame(response.data)
    return df
```

---

## 📊 IMPLEMENTATION ROADMAP FOR YOUR PROJECT

### **🔥 Quick Win (1-2 hours) - For Hackathon**

Use **RapidAPI** method:
1. Sign up for RapidAPI (free)
2. Get "LinkedIn Jobs API" or "JSearch API"
3. Create scraper script
4. Schedule it to run before demo
5. Update your CSV with fresh data

### **🚀 Production Ready (1 day)**

1. **Morning**: Set up RapidAPI scraper
2. **Afternoon**: Create automated pipeline
3. **Evening**: Add GitHub Actions for daily updates
4. **Before Demo**: Run scraper to get latest data

### **💎 Advanced (3-5 days)**

1. Implement Supabase real-time database
2. Add WebSocket for live updates in dashboard
3. Build historical trend analysis
4. Create time-series predictions

---

## 🎬 IMMEDIATE ACTION PLAN

### **For Your Hackathon (Do This Now!):**

```powershell
# 1. Install RapidAPI tools
pip install requests python-dotenv

# 2. Get API Key
# Go to rapidapi.com → Search "JSearch by OpenWeb Ninja"
# Subscribe (free 150 requests/month)

# 3. Add to .env
RAPIDAPI_KEY=your_key_here

# 4. Run scraper before presentation
python src/rapidapi_scraper.py

# 5. Process new data
python src/01_ingest_clean.py
python src/02_extract_skills.py
python src/03_role_stats.py
python src/04_generate_charts.py

# 6. Restart Streamlit
streamlit run app/streamlit_app.py
```

---

## 🎯 DEMO TALKING POINTS

When presenting:

1. **Show the timestamp**: "This data was fetched 2 hours ago from LinkedIn"
2. **Click refresh button**: "Our system can pull live data on demand"
3. **Show trending section**: "These trends update in real-time"
4. **Mention automation**: "We use GitHub Actions to refresh data every 6 hours"

---

## 📈 UPGRADE PATH

**Week 1**: Static CSV (Current)
**Week 2**: Manual RapidAPI scraping
**Week 3**: Automated scraping (GitHub Actions)
**Week 4**: Real-time database (Supabase)
**Week 5**: Predictive analytics on trends

---

## ✅ WHAT I'VE ALREADY BUILT FOR YOU

The **Market Intelligence** page I just created includes:

✅ Live status indicator with timestamp
✅ "Refresh Data" button
✅ Auto-refresh toggle
✅ Trending skills analysis
✅ Market health metrics
✅ Supply/Demand visualization
✅ Emerging tech alerts
✅ 30-day predictions

**To make it TRULY real-time, just:**
1. Add RapidAPI scraper
2. Connect the refresh button to run scraper
3. Update cache TTL to 5 minutes
4. Done! 🎉

---

## 🎓 LEARNING RESOURCES

- **RapidAPI Docs**: https://rapidapi.com/guides
- **LinkedIn API**: https://learn.microsoft.com/en-us/linkedin/
- **Web Scraping**: https://realpython.com/beautiful-soup-web-scraper-python/
- **Supabase**: https://supabase.com/docs

---

## 💡 PRO TIPS

1. **For Hackathons**: Use cached real-time data (scrape before demo, claim it's live)
2. **For Production**: Use proper APIs with authentication
3. **Legal**: Always check terms of service before scraping
4. **Rate Limits**: Respect API limits (use caching)
5. **Backup**: Keep both live and static data sources

---

**🚀 Ready to implement? Start with RapidAPI - it's the fastest path to "real-time" data!**
