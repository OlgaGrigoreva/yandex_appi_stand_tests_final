# ДЛЯ СОЗДАНИЯ ЗАКАЗА
# берем заголовок из api

headers = {
    "Content-Type": "application/json"
}

# берем тело json
order_body = {
    "firstName": "Максим",
    "lastName": "Бочкин",
    "address": "Таганская, 25",
    "metroStation": 129,
    "phone": "+7 800 355 35 35",
    "rentTime": 1,
    "deliveryDate": "2023-10-12",
    "comment": "хочу кататься и не платить",
    "color": []
}

track_body = {

}