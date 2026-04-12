# shared/utils.py
# Reusable helper functions including Claude AI integration

import os
import pandas as pd
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv(override=True)

# Initialize Claude client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# ── Claude helpers ───────────────────────────────────────────

def ask_claude(prompt, context=None, model="claude-sonnet-4-20250514"):
    """
    Ask Claude a question with optional data context.
    
    Usage:
        ask_claude("What patterns do you see?", context=df.describe().to_string())
    """
    full_prompt = prompt
    if context is not None:
        full_prompt = f"Here is my data:\n{context}\n\n{prompt}"
    
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": full_prompt}]
    )
    return message.content[0].text


def analyze_dataframe(df, question):
    """
    Ask Claude to analyze a DataFrame.
    
    Usage:
        analyze_dataframe(shots_df, "What patterns do you see in Arsenal's shot locations?")
    """
    context = f"""
    Shape: {df.shape}
    Columns: {df.columns.tolist()}
    Data types: {df.dtypes.to_dict()}
    Sample (5 rows): {df.head().to_string()}
    Summary stats: {df.describe().to_string()}
    """
    return ask_claude(question, context=context)


def get_sql_query(description, schema_context=None):
    """
    Ask Claude to write a SQL query from a plain English description.
    
    Usage:
        get_sql_query("Get all Arsenal shots in the final third where the outcome was a goal")
    """
    schema = schema_context or """
    Tables:
    - match_events: id, event_id, minute, second, team_id, player_id, x, y, end_x, end_y,
                    qualifiers, is_touch, blocked_x, blocked_y, goal_mouth_z, goal_mouth_y,
                    is_shot, card_type, is_goal, type_display_name, outcome_type_display_name,
                    period_display_name, match_id
    - matches: match_id, home_team_id, away_team_id, home_team_name, away_team_name,
               scraped_url, match_date, venue_name, attendance, referee_id
    - players: player_id, shirt_no, name, age, position, height, weight, team_id
    - teams: team_id, name, country_name, manager_name
    """
    
    prompt = f"""
    Write a PostgreSQL query for the following:
    {description}
    
    Database schema:
    {schema}
    
    Return only the SQL query, no explanation.
    """
    return ask_claude(prompt)


def debug_code(code, error):
    """
    Ask Claude to debug a code error.
    
    Usage:
        debug_code(my_function_code, str(e))
    """
    prompt = f"""
    Help me debug this Python code error.
    
    Code:
    {code}
    
    Error:
    {error}
    
    Explain what's wrong and provide the fix.
    """
    return ask_claude(prompt)


def write_blog_post(analysis_summary, audience="general sports fans"):
    """
    Ask Claude to write a blog post from an analysis summary.
    
    Usage:
        write_blog_post("Arsenal's xG was 2.3 vs 0.8, dominated possession...")
    """
    prompt = f"""
    Write a engaging sports analytics blog post based on this analysis:
    {analysis_summary}
    
    Target audience: {audience}
    Style: Insightful, data-driven but accessible, conversational
    Length: 400-600 words
    """
    return ask_claude(prompt)


# ── Data helpers ─────────────────────────────────────────────

def load_table(table_name, engine, query=None):
    """
    Load a Supabase table into a pandas DataFrame.
    
    Usage:
        df = load_table("match_events", engine)
        df = load_table("match_events", engine, query="SELECT * FROM match_events WHERE is_shot = true")
    """
    sql = query or f"SELECT * FROM {table_name}"
    return pd.read_sql(sql, engine)


def summarize_df(df):
    """Quick summary of a DataFrame."""
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"Nulls:\n{df.isnull().sum()}")
    print(f"\nSample:\n{df.head()}")