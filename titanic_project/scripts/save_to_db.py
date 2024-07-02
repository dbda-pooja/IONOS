import sqlite3

def save_to_db(df, db_name):
    """
    Save DataFrame to SQLite database.

    Parameters:
    - df (pd.DataFrame): DataFrame to save.
    - db_name (str): Path to SQLite database file.
    """
    conn = sqlite3.connect(db_name)
    df.to_sql('titanic', conn, if_exists='replace', index=False)
    conn.close()