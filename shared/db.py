# shared/db.py
# Database connection - connects project to Supabase

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from supabase import create_client, Client
from urllib.parse import quote_plus

# Load credentials from .env
load_dotenv(override=True)

# ── Supabase client ──────────────────────────────────────────
# Used for upserts, inserts, and real-time operations
def get_supabase_client() -> Client:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY in .env")
    
    return create_client(url, key)

# ── SQLAlchemy engine ────────────────────────────────────────
# Used for pandas read_sql queries and raw SQL operations
def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    name = os.getenv("DB_NAME")
    
    if not all([user, password, host, port, name]):
        raise ValueError("Missing database credentials in .env")
    
    connection_string = f"postgresql://{user}:{quote_plus(password)}@{host}:{port}/{name}"
    return create_engine(connection_string)

# ── Connection test ──────────────────────────────────────────
def test_connection():
    try:
        engine = get_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM match_events"))
            count = result.scalar()
            print(f"✅ Connected to Supabase successfully")
            print(f"✅ match_events table has {count:,} rows")
            return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    test_connection()