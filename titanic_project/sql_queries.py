import sqlite3

def run_queries(db_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # 1. What’s the average age of women that survived the sinking of the Titanic?
    query1 = """
    SELECT AVG(Age) 
    FROM titanic 
    WHERE Survived = 1 AND Sex = 'female'
    """
    cursor.execute(query1)
    avg_age_women_survived = cursor.fetchone()[0]
    print(f"* Average age of women that survived: {avg_age_women_survived}")

    # 2. What are the average and maximum fares for each class?
    query2 = """
    SELECT Pclass, AVG(Fare) AS Average_Fare, MAX(Fare) AS Maximum_Fare 
    FROM titanic 
    GROUP BY Pclass
    """
    cursor.execute(query2)
    fare_stats = cursor.fetchall()
    print("* Average and Maximum fares for each class:")
    for row in fare_stats:
        print(f"Class {row[0]} - Average Fare: {row[1]}, Maximum Fare: {row[2]}")

    # Close the connection
    conn.close()

# Example usage
db_name = r'.\data\titanic.db'
run_queries(db_name)