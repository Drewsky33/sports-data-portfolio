# Sports Data Portfolio

A data science portfolio focused on soccer, NBA, and college basketball analytics.
I built this to demonstrate end-to-end data skills for sports analytics and sports gambling roles.

## Project Goals
- Build and maintain live databases for soccer (Arsenal + top 5 leagues), NBA, and CBB
- Develop predictive models for player recruitment, xG, and performance analysis
- Publish weekly data-driven sports analysis on Substack
- Create a public portfolio demonstrating production-grade data science skills

## Tech Stack
- **Language:** Python 3.11
- **Database:** Supabase (PostgreSQL)
- **Analysis:** pandas, numpy, scipy, statsmodels
- **Visualization:** mplsoccer, matplotlib, seaborn, plotly
- **Machine Learning:** scikit-learn, xgboost
- **AI Integration:** Anthropic Claude API
- **Scraping:** Selenium, BeautifulSoup4
- **Environment:** VS Code, Jupyter, Git

## Project Structure

```
sports-data-portfolio/
├── soccer/          # Arsenal + top 5 leagues analysis
├── nba/             # NBA analysis and models
├── cbb/             # College basketball analysis
├── shared/          # Shared utilities
│   ├── db.py        # Supabase database connection
│   └── utils.py     # Claude AI helpers and data utilities
├── notebooks/       # Jupyter notebooks for analysis
├── dashboards/      # Streamlit dashboards
├── blog/            # Weekly blog exports
└── data/            # Local data files

```
## Setup
```bash
# Clone the repo
git clone https://github.com/Drewsky33/sports-data-portfolio.git
cd sports-data-portfolio

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your credentials
cp .env.example .env
# Fill in your Supabase and Anthropic credentials
```

## Current Databases
- **Soccer:** Arsenal match events (73,169 rows) — WhoScored XY data
- **NBA:** Coming soon
- **CBB:** Coming soon

## Analysis & Blog
Weekly sports analytics posts coming soon on Substack.

## Author
Andrew Lujan | [GitHub](https://github.com/Drewsky33)