import requests
from datetime import datetime
from package.application.db.people import get_employees
from package.application.salary import calculate_salary

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None


if __name__ == '__main__':
    print("Текущая дата и время:", current_date)
    calculate_salary()
    get_employees()

    url = "https://jsonplaceholder.typicode.com/todos/1"
    print(fetch_data(url))
