# *Проверка получения данных заказа по его трекеру :sun_with_face:Яндекс.Самокат:sun_with_face:*  
___   
## Проверка статус-кода=200 в ответе 

Проверка данных заказа, созданного пользователем, по треку заказа, с помощью API Яндекс.Самокат

:point_up: Важно:
- Автотест написан на языке Python
- Для запуска автотестов должны быть установлены пакеты:    
:white_check_mark: pytest    
:white_check_mark: request    
- Запустить тест можно командой `pytest`   

Основные функции проекта:    
:star: Создание заказа     
def post_new_order(body):     
:star: Получение трека заказа     
def get_new_order_track():     
:star: Получение заказа по треку     
def get_order_info():     
:star: Проверка статус-кода =200      
def test_order_info():      


:yellow_heart: Результат - тест пройден :yellow_heart: