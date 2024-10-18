from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

if __name__ == '__main__':
    print('Запускаем программу "Бухгалтерия"')
    print(calculate_salary())
    print(get_employees())
    print('Текущее время', datetime.datetime.now())