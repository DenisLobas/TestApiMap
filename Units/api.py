import allure
from Units.httpmethods import HttpMethods


base_url = "https://rahulshettyacademy.com"  # базовая url
key = "?key=qaclick123"  # ключ для всех запросов


@allure.epic("Test create place")
class GoogleMapsApi:
    """Содержит методы для тестирования Google_maps_api"""

    @staticmethod
    @allure.description("Test create, update, delete new place")
    def create_new_place():
        """Метод для создания новой локации с заданными параметрами для теста"""
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resource = "/maps/api/place/add/json"  # ресурс метода post
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_location)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_place(place_id):
        """Метод для отправки запроса GET с заданными параметрами для теста"""
        ger_resource = "/maps/api/place/get/json"  # ресурс для метода get
        get_url = base_url + ger_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_new_place(place_id):
        """Метод для изменения поля address в локации"""
        put_resource = "/maps/api/place/update/json"  # ресурс для метода put
        put_url = base_url + put_resource + key + "&place_id=" + place_id
        print(put_url)
        json_for_put_new_location = {
            "place_id": place_id,
            "address": "Scotland Yard",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_for_put_new_location)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """Метод для удаления локации"""
        delete_resource = "/maps/api/place/delete/json"  # ресурс для метода delete
        delete_url = base_url + delete_resource + key + "&place_id=" + place_id
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete
