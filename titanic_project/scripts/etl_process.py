from .load_data import load_data
from .preprocess_data import preprocess_data
from .feature_engineering import feature_engineering
from .save_to_db import save_to_db

def etl_process(csv_file, db_name):
    df = load_data(csv_file)
    df = preprocess_data(df)
    df = feature_engineering(df)
    save_to_db(df, db_name)