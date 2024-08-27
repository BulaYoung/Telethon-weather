# Telegram Weather and Joke Bot

Этот скрипт на Python автоматически отправляет сообщение с пожеланием доброго утра, текущей погодой в выбранном городе, случайной шуткой на русском языке и ссылкой на песню в Telegram. Сообщение отправляется каждый день в назначенное время с использованием библиотеки `telethon` для взаимодействия с Telegram.

## Функциональность

- Получает текущую погоду для указанного города через API OpenWeatherMap.
- Получает случайную шутку на русском языке с помощью API rzhunemogu.ru.
- Формирует сообщение с добрым утром, информацией о погоде, шуткой и ссылкой на песню.
- Отправляет это сообщение в указанный Telegram-чат или пользователю.

## Настройка

### 1. Клонируйте репозиторий и перейдите в директорию проекта

```bash
git clone https://github.com/your_username/telegram-weather-joke-bot.git
cd telegram-weather-joke-bot
```
## 2. Установите необходимые зависимости

Убедитесь, что у вас установлен Python 3. Затем установите необходимые библиотеки:

```bash
pip install -r requirements.txt
```
## 3. Создайте файл .env

Создайте файл .env в корневой директории проекта и вставьте в него следующие строки, заменив примерные данные на ваши реальные значения:

```plaintext

TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
TELEGRAM_PHONE=your_phone_number
OPENWEATHER_API_KEY=your_openweather_api_key
YOUTUBE_MUSIC_LINK=https://music.youtube.com/watch?v=your_youtube_music_link
RECIPIENT_USERNAME=telegram_recipient_username_or_chat_id
```
Пояснения к параметрам .env файла:
```plaintext
TELEGRAM_API_ID и TELEGRAM_API_HASH: Ваши идентификаторы API Telegram, которые можно получить на my.telegram.org.
TELEGRAM_PHONE: Номер телефона, связанный с вашим аккаунтом Telegram (в международном формате, например, +1234567890).
OPENWEATHER_API_KEY: Ваш API-ключ для OpenWeatherMap, который можно получить на openweathermap.org.
YOUTUBE_MUSIC_LINK: Ссылка на YouTube Music, которую вы хотите отправить вместе с сообщением.
RECIPIENT_USERNAME: Имя пользователя или ID чата в Telegram, куда будет отправляться сообщение.
```
## 4. Настройка города

По умолчанию скрипт использует город Таллин для получения данных о погоде. Если вы хотите изменить город, замените Tallinn в коде на название другого города:

```python
url = f'http://api.openweathermap.org/data/2.5/weather?q=Tallinn&appid={openweather_api_key}&units=metric&lang=ru'
```
Например, если вы хотите получать погоду для Москвы, измените Tallinn на Moscow:

```python
url = f'http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid={openweather_api_key}&units=metric&lang=ru'
```
## 5. Запуск скрипта

Чтобы запустить скрипт, просто выполните:

```bash
python3 main.py
```
Скрипт будет подключаться к Telegram, получать данные о погоде и шутку, а затем отправлять сообщение в назначенное время каждый день.