import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


def connection_test():
    """
    Connects gets the Postgres version from supabase
    """
    load_dotenv()
    db_url = os.getenv('DATABASE_URL')
    engine = create_engine(db_url)

    with engine.connect() as conn:
        result = conn.execute(text("SELECT version ();"))
    
    return result.fetchone()

