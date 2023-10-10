# Ольга Григорьева_08-а_Earth_Финальный_проект_Инженер_по_тестированию+
import sender_stand_request   # данные из файла с заготовками
import data                   # данные тела

#получить данные о созданном заказе и параметре track
def get_new_order_track():
    # Создать новый заказ
    order_body = data.order_body
    # получить ответ по созданному заказу
    response_order = sender_stand_request.post_new_order(order_body)
    # Запомнить трек заказа
    return response_order.json()["track"]

# получить данные заказа по треку
def get_order_info():
    # сохраним трек закза
    track = get_new_order_track()
    # запрос на данные по номеру трека
    response_order = sender_stand_request.get_order(track)
    # вернуть ответ сервера
    return response_order

# проверить статус ответа
def test_order_info():
    assert get_order_info().status_code == 200
