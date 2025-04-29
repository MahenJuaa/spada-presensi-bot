import schedule
import time
from bot import login_and_check_presence

def job():
    login_and_check_presence()

schedule.every().monday.at("08:00").do(job)
schedule.every().tuesday.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
