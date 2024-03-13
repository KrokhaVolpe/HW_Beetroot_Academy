import sqlite3
import psycopg2

# З'єднання з базою даних SQLite
sqlite_conn = sqlite3.connect('data_base.db')
sqlite_cursor = sqlite_conn.cursor()

# З'єднання з базою даних PostgreSQL
postgresql_conn = psycopg2.connect(
    dbname="lesson_37", 
    user="postgres",
    password="123",
    host="localhost"
)
postgresql_cursor = postgresql_conn.cursor()

# Створення словника для відповідності типів даних між SQLite та PostgreSQL
type_map = {
    'INTEGER': 'INTEGER',
    'REAL': 'REAL',
    'NUMERIC': 'NUMERIC',
    'TEXT': 'TEXT',
    'DOUBLE PRECISION': 'DOUBLE PRECISION',
    'CHARACTER VARYING': 'VARCHAR',
    'CHARACTER': 'CHAR',
    'text(20)': 'VARCHAR(20)',  
    'text(10)': 'VARCHAR(10)',
    'CHAR': 'CHAR',
    'INT': 'INTEGER',
    'CHAR(5)': 'CHAR(5)',
    'FLOAT': 'FLOAT', 
}


# Список таблиць, які потрібно перенести
tables_to_transfer = ['prod_backup', 'orders', 'tb1', 's', 'r', 'emor', 'min_salary', 'employee_data', 'student', 'employee_income', 'details', 'countries', 'regions', 'locations', 'departments', 'jobs', 'employees', 'department', 'job_history', 'prod_mast', 'user_table', 'my_user_table', 'tags']

for table_name in tables_to_transfer:
    # Отримання структури таблиці з SQLite
    sqlite_cursor.execute(f"PRAGMA table_info('{table_name}')")
    columns = sqlite_cursor.fetchall()

    # Виведення типів даних стовпців
    print(f"Типи даних для таблиці {table_name}:")
    for column in columns:
        print(column[2])

    # Створення SQL-запиту для створення таблиці в PostgreSQL
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for column in columns:
        column_name = column[1]
        if column[2]:  # Перевіряємо, чи стовпець має тип даних
            data_type = type_map.get(column[2])  # Використовуємо .get() для уникнення KeyError
            if data_type:  # Перевіряємо, чи визначено відповідність для типу даних
                create_table_query += f"{column_name} {data_type}, "
            else:
                print(f"Тип даних '{column[2]}' для стовпця '{column[1]}' не визначено у словнику type_map.")
        else:
            print(f"Стовпець '{column[1]}' не має визначеного типу даних.")
    create_table_query = create_table_query[:-2] + ")"  # Виправлена позиція дужки


    # Виконання SQL-запиту для створення таблиці в PostgreSQL
    postgresql_cursor.execute(create_table_query)
    postgresql_conn.commit()

    # Вибірка даних з SQLite
    sqlite_cursor.execute(f"SELECT * FROM {table_name}")
    rows = sqlite_cursor.fetchall()

# Вставка даних у таблицю PostgreSQL
for row in rows:
    # Перевірка, чи існує вже рядок з таким самим prod_id
    postgresql_cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE prod_id = %s", (row[0],))
    if postgresql_cursor.fetchone()[0] == 0:
        placeholders = ','.join(['%s'] * len(row))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        postgresql_cursor.execute(insert_query, row)
postgresql_conn.commit()

# Закриття з'єднань
sqlite_conn.close()
postgresql_conn.close()

print("Перенесення даних завершено.")

