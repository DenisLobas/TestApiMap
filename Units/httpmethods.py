import allure
import requests
from Units.logger import Logger


class HttpMethods:
    """Класс для отправки запросов GET, POST, PUT, DELETE"""

    headers = {"Content-Type": "application/json"}
    cookie = ""

    @staticmethod
    def get(url):
        """Метод для отправки запроса GET"""
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            """Метод для отправки запроса POST"""
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            """Метод для отправки запроса PUT"""
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            """Метод для отправки запроса DELETE"""
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result
