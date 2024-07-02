import pandas as pd

def load_data(csv_file):
    """
    Load data from CSV file.

    Parameters:
    - csv_file (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded data as a DataFrame.
    """
    return pd.read_csv(csv_file)