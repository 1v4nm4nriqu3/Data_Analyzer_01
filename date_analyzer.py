import datetime


class DateAnalyzer:
    def is_leap_year(self, year):
        """
        Determines if a given year is a leap year.
        """
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def get_current_week(self):
        """
        Returns the current week number of the year.
        """
        today = datetime.date.today()
        week_number = today.isocalendar()[1]
        return week_number


if __name__ == "__main__":
    analyzer = DateAnalyzer()

    # --- Leap Year Verifier Section ---
    print("--- Leap Year verifier ---")

    while True:
        try:
            user_year = int(input("Enter a Year: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

    result = analyzer.is_leap_year(user_year)

    leap_year_info = {
        "consulted_year": user_year,
        "is_leap_year": result,
        "message": f"{user_year} is a leap year" if result else f"{user_year} is not a leap year"
    }

    print(leap_year_info["message"])
    print("-" * 30)

    # --- Current Week Finder Section ---
    print("--- Current Week Finder ---")

    current_week = analyzer.get_current_week()

    print(f"currently we are on the week number: {current_week}")
    print("-" * 30)

    # --- Verifying a List of Years Section ---

"""  print("--- verifying a list of years ---")
    years_to_test = [2000, 2004, 1900, 2023, 2024, 2025]

    for year in years_to_test:
        if analyzer.is_leap_year(year):
            print(f"-> The year {year} is leap.")
        else:
            print(f"-> The year {year} is not leap.")
 """
