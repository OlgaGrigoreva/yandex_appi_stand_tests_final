import configuration # данные из конфигурации
import requests      # данные ответов
import data          # данные тела из даты

# создать новый заказ
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # полный url
                         json=body,  # тут тело
                         headers=data.headers)  # здесь заголовки

#response = post_new_order(data.order_body);
#print(response.status_code)
#print(response.json())

# получить данные заказа по треку
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH + str(track),  # полный url
                         json={},  # тут тело
                         headers=data.headers)
