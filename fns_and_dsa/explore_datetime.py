from datetime import datetime, timedelta
import time

# dt = datetime.datetime.fromtimestamp(time.time())

datetime.now()


# def display_current_datetime():
#     current_date = datetime.fromtimestamp(time.time())
#     print(f'Current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}')

def display_current_datetime():
    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f'{formatted_date}')

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date.date() - timedelta(number_of_days)
    print(future_date)

calculate_future_date()

