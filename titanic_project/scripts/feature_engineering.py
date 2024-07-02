import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def feature_engineering(df):
    """
    Perform feature engineering on the DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.

    Returns:
    - pd.DataFrame: DataFrame with engineered features.
    """
    # Extract titles from names
    df['Title'] = df['Name'].str.extract(r',\s*([^\.]*)\s*\.', expand=False)
    df['Title'] = df['Title'].replace(['Lady', 'Countess', 'Capt', 'Col',
                                       'Don', 'Dr', 'Major', 'Rev', 'Sir',
                                       'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')

    # Create new features
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    # Bin Age into categorical groups
    bins = [0, 18, 30, 50, float('inf')]
    labels = ['Child', 'Young Adult', 'Adult', 'Senior']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    # Bin Fare into categories
    fare_bins = [0, 10, 30, 100, float('inf')]
    fare_labels = ['Low', 'Medium', 'High', 'Very High']
    df['FareCategory'] = pd.cut(df['Fare'], bins=fare_bins, labels=fare_labels, right=False)

    df['Age*Pclass'] = df['Age'] * df['Pclass']

    # Normalize numerical values (Fare)
    scaler = MinMaxScaler()
    df[['Fare']] = scaler.fit_transform(df[['Fare']])

    return df