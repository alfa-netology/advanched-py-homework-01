from datetime import datetime as dt
from application import salary
from application.db import people

def main():
    print(f"today: {dt.date(dt.now())}")
    salary.calculate_salary()
    people.get_employees()


if __name__ == '__main__':
    main()
