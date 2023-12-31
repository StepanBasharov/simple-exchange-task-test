# Микросервис для конвертации валют 

<h2>Стек технологий</h2>
<ul>
<li>Python 3.10</li>
<li>FastAPI</li>
<li>SQLAlchemy</li>
<li>Alembic</li>
<li>Postgresql</li>
<li>Docker-compose</li>
<li>Celery</li>
<li>Httpx</li>
</ul>

<h2>Деплой</h2>
<li>Создайте файл .env и скопируйте в него содержимое example.env</li>
<br>
<code>
HOST="0.0.0.0"
PORT=8000
DB_URL="postgresql+asyncpg://postgres:postgres@db/exchange_db"
DB_URL_ALEMBIC="postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/exchange_db"
DB_URL_ALEMBIC="postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/exchange_db"
BROKER_URL="redis://redis"
RESULT_BACKEND="redis://redis"
API_KEY="API_KEY"
PRICES_URL="http://api.exchangeratesapi.io/v1/latest?access_key="
NAMES_URL="https://openexchangerates.org/api/currencies.json"
DB_SYNC_URL="postgresql://postgres:postgres@db/exchange_db"
</code>
<br>
<li>Запустите команду <code>docker-compose up --build -d</code></li>


<h4>Сервис полностью готов к работе :)</h4>


<h2>Тестирование</h2>

Для запуска unit тестов в корневой папке запустить <code>pytest</code> 