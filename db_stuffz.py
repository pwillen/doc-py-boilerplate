"""
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
"""
import pandas as pd
import psycopg
# Connect to DB

# This does not connect.
# Unable to find a sample database and not really worth my time to set one up just for this
with psycopg.connect("postgresql://demo:demo@demo.cloudbeaver.io/pagila") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM actor")
        rows = cur.fetchall()
        for row in rows:
            print(row)

# ======================================================================================================================
# With Pandas instead

with psycopg.connect("postgresql://demo:demo@demo.cloudbeaver.io/pagila") as conn:
    # Can read from DB api connection or sqlalchemy engine
    df = pd.read_sql("SELECT * FROM actor", conn)
    print(df)