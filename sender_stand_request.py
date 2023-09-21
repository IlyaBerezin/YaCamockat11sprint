import configuration
import requests
import data

#функция создания заказа
def post_order(order_body):
    #возвращаем запрос POST создания заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         headers=data.headers, json=order_body)

response = post_order(data.order_body);
print(response.status_code)
print(response.json())

#функция сохранения номера заказа
def get_track_number():
    order_body = data.order_body
    # ответу присваиваем значение функции создания заказа
    response = post_order(order_body)
    # возвращается номер track из созданного заказа
    return response.json()["track"]

print(response.status_code)
print(response.json())



