"""Методы для проверки ответов наших запросов"""
import json


class Checking:
    """Класс хранящий методы дял проверки тестов"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, "Ошибка, статус-код не совпадает"
        print(f"Успешно, статус код = {result.status_code}")

    @staticmethod
    def check_json_token(result, expected_value):
        """Метод для проверки наличия полей в ответе запроса"""
        token = json.loads(result.text)
        assert list(token) == expected_value, "Ошибка, некоторые поля отсутствуют"
        print("Все поля пресутствуют!")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """Метод для проверки значения полей в ответе запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Не верное значение полей: {field_name}"
        print(f"Значение полей верно: {field_name}")
