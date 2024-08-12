from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
import names

def show_current_datetime():
    print(f"Текущая дата и время: {datetime.now()}")

def generate_random_name():
    name = names.get_full_name()
    print(f"Выбранное имя: {name}")

if __name__ == '__main__':
    show_current_datetime()
    calculate_salary()
    get_employees()
    generate_random_name()
