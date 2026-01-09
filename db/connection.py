import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

def engine_init():
    load_dotenv()
    db_url = os.getenv('DATABASE_URL')
    engine = create_engine(db_url)

    return engine

def connection_test():
    """
    Connects gets the Postgres version from supabase
    """
    engine = engine_init()

    with engine.connect() as conn:
        result = conn.execute(text("SELECT version ();"))
    
    return result.fetchone()

def create_table(df, table_name):
    engine = engine_init()
    with engine.connect() as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
