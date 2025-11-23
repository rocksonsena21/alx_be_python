from datetime import datetime, timedelta

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.now()  # save current date & time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # we return this so Part 2 can reuse it

# Part 2: Calculate a future date
def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)  # calculate future date
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

def main():
    # Show the current date & time
    current_date = display_current_datetime()

    # Ask the user for number of days
    days = int(input("Enter the number of days to add to the current date: "))

    # Calculate and show future date
    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
