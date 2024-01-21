<h1>
    Приложения для выполнения асинхронных запросов к сайту кинопоиск с получением
    информации о фильмах и актерах
</h1>
<h2>
    Установка и использование:
</h2>
<ol>
    <li>
        git clone
    </li>
    <li>
        pip install -r requirements.txt
    </li>
    <li>
        Получение токена API к сайту кинопоиск: 
        <a href="https://api.kinopoisk.dev/documentation#/">Документация API</a>
    </li>
    <li>
        Создание файла .env и помещение в него ключа: TOKEN_KEY = "***", TOKEN_VALUE = "******".
        Необходимо разделить полученный словарь на ключ и значение
    </li>
    <li>
        run main.py
    </li>
</ol>
<h2>
    Стек технологий: asyncio, aiohttp, python-dotenv
</h2>