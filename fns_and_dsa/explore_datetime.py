from datetime import datetime, timedelta
import time

# dt = datetime.datetime.fromtimestamp(time.time())


def display_current_datetime():
    current_date = datetime.fromtimestamp(time.time())
    print(f'Current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}')

display_current_datetime()

number_of_days = int(input("Enter a number of days: "))

def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date.date() - timedelta(number_of_days)
    print(future_date)

calculate_future_date()

