import psycopg2

# Параметри підключення до бази даних PostgreSQL
dbname = 'lesson_37'
user = 'postgres'
password = '123'
host = 'localhost'

# Підключення до бази даних PostgreSQL
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cursor = conn.cursor()

# Отримання інформації про структуру таблиць
cursor.execute("""
    SELECT table_name, column_name, data_type
    FROM information_schema.columns
    WHERE table_schema = 'public'; -- Можливо, вам слід вказати вашу схему, якщо вона відрізняється
""")
table_info = cursor.fetchall()

# Виведення інформації про структуру таблиць
for table_name, column_name, data_type in table_info:
    print(f"Таблиця: {table_name}, Стовпець: {column_name}, Тип даних: {data_type}")

# Закриття з'єднання
cursor.close()
conn.close()
