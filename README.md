## Binance WebSocket 

Данный пример позволяет: 
  1) Подключаться к binance.com через __websocket__ (https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md)
  2) Получать минутные (легко изменяемо) свечи  для пар: BTC/USDT, ETH/USDT, BNB/BTC
  3) По полученным свечам считать скользящее среднее (SMA) для каждой пары отдельно 
  4) Выводить результат в лог

Для __запуска программы__ необходимо выполнить следующие команды (в директории проекта):
  1) docker build -t server:1.0
  2) docker images - чтобы узнать IMAGE ID запущенного контейнера
  3) docker run <IMAGE ID>
  
 Для __запуска unit тестов__ необходимо:
  1) в папке tests создать файл \_\_init__.py
  2) выполнить следующую команду: pytest tests/test_work.py

  
  
__WebSocket Programming guide__: https://autobahn.readthedocs.io/en/latest/websocket/programming.html
