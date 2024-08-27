from telethon import TelegramClient
import requests
from dotenv import load_dotenv
import os
import schedule
import time
import asyncio

# Загрузка переменных окружения из файла .env
load_dotenv()

# Конфигурация
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone = os.getenv('TELEGRAM_PHONE')
openweather_api_key = os.getenv('OPENWEATHER_API_KEY')
youtube_music_link = os.getenv('YOUTUBE_MUSIC_LINK')
recipient_username = os.getenv('RECIPIENT_USERNAME')


# Получение текущей погоды
def get_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Tallinn&appid={openweather_api_key}&units=metric&lang=ru'
    response = requests.get(url)

    if response.status_code != 200:
        return "Не удалось получить погоду. Попробуйте позже."

    data = response.json()

    if 'weather' not in data or 'main' not in data:
        return "Не удалось получить погоду. Попробуйте позже."

    description = data['weather'][0]['description']
    temp = data['main']['temp']

    weather_message = f"Погода в Таллине: {description}, температура: {temp}°C."
    return weather_message


# Получение случайной шутки на русском языке
def get_russian_joke():
    url = "http://rzhunemogu.ru/RandJSON.aspx?CType=1"
    response = requests.get(url)
    if response.status_code != 200:
        return "Шутка не загрузилась. Но не переживайте, улыбайтесь чаще!"

    # Ответ приходит в некорректном формате JSON, поэтому его нужно обработать
    joke_text = response.content.decode('windows-1251')  # Декодируем контент напрямую из windows-1251 в UTF-8
    joke_text = joke_text.replace('{"content":"', '').replace('"}', '')  # Убираем лишние части

    return joke_text


# Функция для отправки сообщения через Telegram
async def send_message(client):
    # Составляем сообщение
    weather_message = get_weather()
    joke = get_russian_joke()
    message = f"Доброе утро!\n{weather_message}\n\nВот ссылка на песню, чтобы начать день с хорошего настроения: {youtube_music_link}\n\nИ напоследок шутка дня:\n{joke}"

    # Отправляем сообщение
    await client.send_message(recipient_username, message)


# Основная функция
async def main():
    # Подключаемся к Telegram один раз и остаемся подключенными
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone)

    # Планирование задачи на 8 утра каждый день
    schedule.every().day.at("08 :00").do(lambda: asyncio.create_task(send_message(client)))

    # Основной цикл, который следит за временем и запускает задачи
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

    # Отключаемся от клиента в случае завершения работы (если это когда-то случится)
    await client.disconnect()


# Запуск программы
asyncio.run(main())
