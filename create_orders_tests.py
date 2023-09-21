# Илья Березин, 8-а когорта — Финальный проект. Инженер по тестированию плюс
import pytest

import sender_stand_request
import configuration
import requests

#@pytest.mark.parametrize('t', [pytest.param(sender_stand_request.get_track_number(), id="Number of track")])
#функция получения заказа по номеру и проверки кода ответа 200
def test_get_order_by_track():
    #возвращаем запрос на получение заказа по треку в параметрах(трек берём из функции сохранения трека)
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                       {"t": sender_stand_request.get_track_number()})
#проверка, что код ответа 200
assert test_get_order_by_track().status_code == 200

#print(test_get_order_by_track().status_code)
#print(test_get_order_by_track().json())