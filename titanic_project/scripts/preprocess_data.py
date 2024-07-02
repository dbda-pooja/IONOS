import pandas as pd

def preprocess_data(df, missing_threshold=0.7):
    """
    Preprocess data:
    - Handle missing values in specific columns.
    - Clean up and impute missing values.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - missing_threshold (float): Threshold for dropping columns with missing values.

    Returns:
    - pd.DataFrame: Preprocessed DataFrame.
    """
    # Define columns to preprocess
    columns_to_process = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Embarked', 'SibSp', 'Parch', 'Cabin']

    for col in columns_to_process:
        if df[col].isnull().any():
            if df[col].isnull().sum() / len(df) > missing_threshold:
                df.drop(col, axis=1, inplace=True)
                print(f"Dropped column '{col}' due to more than {missing_threshold * 100}% missing values.")
                
            else:
                if col == 'Survived':
                    df['Survived'] = df['Survived'].fillna(df['Survived'].mode()[0]) # Fill Survived with mode

                elif col == 'Pclass':
                    df['Pclass'] = df['Pclass'].fillna(df['Pclass'].mode()[0])  # Fill Pclass with mode
            
                elif col == 'Name':
                    df[col] = df[col].fillna('Unknown')  # Fill Name with 'Unknown'
                    
                elif col == 'Sex':
                    df[col] = df[col].fillna(df[col].mode()[0])  # Fill Sex with mode

                elif col == 'Age':
                    # Fill Age based on average by Sex
                    avg_age_male = df[df['Sex'] == 'male']['Age'].mean().round(0)
                    avg_age_female = df[df['Sex'] == 'female']['Age'].mean().round(0)
                    df.loc[(df['Sex'] == 'male') & (df['Age'].isnull()), 'Age'] = avg_age_male
                    df.loc[(df['Sex'] == 'female') & (df['Age'].isnull()), 'Age'] = avg_age_female

                elif col == 'Embarked':
                    df[col] = df[col].fillna(df[col].mode()[0])  # Fill Embarked with mode

                elif col == 'SibSp':
                    df[col] = df[col].fillna(df[col].median())  # Fill SibSp with median

                elif col == 'Parch':
                    df[col] = df[col].fillna('unknown')  # Fill Parch with 'unknown'

                elif col == 'Cabin':
                    df[col] = df[col].fillna('Unknown')  # Fill Cabin with 'Unknown'

    return df