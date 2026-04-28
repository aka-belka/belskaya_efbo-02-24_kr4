# Контрольная работа №4: Технологии разработки серверных приложений

## Установка

```bash
# Клонирование репозитория
git clone https://github.com/aka-belka/belskaya_efbo-02-24_kr4.git
cd tdsa_kr4

# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt
```

## Запуск и тестирование каждого задания 

### Задание 9.1
```bash
#Создание базы данных в PostgreSQL:
CREATE DATABASE tdsa;

cd ex9_1

# Создание файла .env из примера
copy .env.example .env
# Отредактируйте .env

alembic upgrade head
```

### Задание 10.1
```bash
uvicorn ex10_1:app --reload 

# Тестирование в другом терминале
curl http://localhost:8000/resource/0     
curl http://localhost:8000/resource/999    
curl http://localhost:8000/items/-1      
curl http://localhost:8000/items/42  
```

### Задание 10.2
```bash
uvicorn ex10_2:app --reload 

# Тестирование в другом терминале
curl -X POST http://localhost:8000/users/ -H "Content-Type: application/json" -d "{\"username\":\"Valera\",\"age\":19,\"email\":\"serg@gmail.com\",\"password\":\"qwerty123\"}"
curl -X POST http://localhost:8000/users/ -H "Content-Type: application/json" -d "{\"username\":\"a\",\"age\":17,\"email\":\"bad\",\"password\":\"123\"}"
```

### Задание 11.1
```bash
cd ex11_1
pytest
```

### Задание 11.2
```bash
cd ex11_2
pytest
```