import schedule
import time
from scripts.etl_process import etl_process

def daily_job(csv_file, db_name):
    print("Starting daily ETL job...")
    etl_process(csv_file, db_name)
    print("Daily ETL job completed.")

if __name__ == "__main__":
    csv_file = r'.\data\titanic.csv'
    db_name = r'.\data\titanic.db'

    # Schedule the daily job
    schedule.every(1).minute.do(daily_job, csv_file, db_name)
    # schedule.every().day.at("02:00").do(daily_job, csv_file, db_name)

    print("Scheduled daily ETL job. Waiting for the scheduled time...")

    # Keep the script running to allow the scheduler to run the job
    while True:
        schedule.run_pending()
        time.sleep(1)