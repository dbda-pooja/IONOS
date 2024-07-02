**IONOS**

## Titanic ETL Pipeline
🔹Overview : This repository made to demonstrate implementation of given assessment. This project implements an Extract-Transform-Load (ETL) pipeline for the Titanic dataset. The pipeline includes data loading, preprocessing, feature engineering, and storing the cleaned data into an SQLite database. The analysis is performed using Jupyter notebooks, and the ETL (Extract, Transform, Load) process is automated through scripts. Additionally, a scheduled job runs this ETL process daily.


🔸Project Structure

![Project Structure](https://github.com/dbda-pooja/IONOS/blob/main/titanic_project/Architecture_diagram/project_structure.png)

🔸Contents
## Data
titanic.csv: This is the raw data file containing information about the passengers on the Titanic.
titanic.db: This SQLite database contains the processed data, making it easy to query and analyze.

### Scripts
* load_data.py: This script is responsible for loading the raw data from the CSV file into a pandas DataFrame.
* preprocess_data.py: This script handles the preprocessing of the data, such as handling missing values, encoding categorical variables, and normalizing numerical features.
* feature_engineering.py: This script performs feature engineering to create new features that can improve the performance of machine learning models.
* save_to_db.py: This script saves the processed data into an SQLite database.
* etl_process.py: This script orchestrates the entire ETL process, calling the other scripts in sequence to load, preprocess, and save the data.

### Analysis
* titanic_data_analysis.ipynb: This Jupyter notebook contains various data analysis tasks, such as exploring the dataset, visualizing data, and building predictive models.

### Scheduling
*schedule_job.py: This script is used to schedule the ETL job. It can be set up with a task scheduler to run the ETL process at regular intervals.

🔸Getting Started
### Prerequisites
To run this project, you'll need the following installed:
* Python 3.x
* pandas
* numpy
* scikit-learn
* Jupyter Notebook
* SQLite3

* You can install the required packages using pip: 
pip install pandas numpy scikit-learn jupyter sqlite3

### Running the ETL Process
1. Navigate to the Scripts directory: 
    cd Scripts
2. Run the etl_process.py script to execute the ETL pipeline:
    python etl_process.py

### Analyzing the Data
1. Open the Jupyter notebook:
    jupyter notebook titanic_data_analysis.ipynb
2. Follow the steps in the notebook to perform data analysis and build predictive models.

### Scheduling the ETL Job
To schedule the ETL job, you can use the schedule_job.py script with a task scheduler. 
1. Navigate to the titanic_project directory: 
    cd ..
2. Run the scheduled_job.py script to execute the ETL pipeline:
    python scheduled_job.py

### ETL Pipeline
The ETL (Extract, Transform, Load) pipeline includes the following steps:

1. Load the Data from CSV

    Script: load_data.py
    Function: load_data(file_path)
    Description: Loads the raw data from the CSV file into a pandas DataFrame.

2.  Preprocess/Clean the Data
    Script: preprocess_data.py
    Function: preprocess_data(df)
    Description: Handles the preprocessing of the data, such as handling missing values, encoding categorical variables, and normalizing numerical features.

3.  Feature Engineering
    Script: feature_engineering.py
    Function: feature_engineering(df)
    Description: Performs feature engineering to create new features that can improve the performance of machine learning models.

4.  Save the Transformed Data to Database
    Script: save_to_db.py
    Function: save_to_db(df, db_path)
    Description: Saves the processed data into an SQLite database.

5.  Main ETL Process
    Script: etl_process.py
    Function: etl_process(file_path, db_path)
    Description: Orchestrates the entire ETL process, calling the other scripts in sequence to load, preprocess, and save the data.


### Data Pipeline Architecture Diagram
Here is a simple data pipeline architecture diagram:
![Data Pipeline Architecture Diagram](https://github.com/dbda-pooja/IONOS/blob/main/titanic_project/Architecture_diagram/data_pipeline_architecture_diagram.png)


### Data Analysis
The Jupyter notebook titanic_data_analysis.ipynb contains various data analysis tasks, such as exploring the dataset, visualizing data, and building predictive models. Here are some key points of the analysis:

Survival Count: Visualize the count of survivors and non-survivors.
Survival Rate by Class: Explore how survival rates vary by passenger class.
Age Distribution: Analyze the age distribution of the passengers.


### SQL Queries
Here are the SQL queries to answer specific questions from the database:

1. Average Age of Women Who Survived
    SELECT AVG(Age) AS avg_age_survived_women
    FROM titanic
    WHERE Survived = 1 AND Sex = 'female';

2. Average and Maximum Fares for Each Class
    SELECT Pclass, AVG(Fare) AS avg_fare, MAX(Fare) AS max_fare
    FROM titanic
    GROUP BY Pclass;




