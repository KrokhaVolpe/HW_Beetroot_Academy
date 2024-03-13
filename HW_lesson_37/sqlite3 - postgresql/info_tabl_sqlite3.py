import sqlite3

# Підключення до бази даних SQLite
sqlite_conn = sqlite3.connect('data_base.db')
sqlite_cursor = sqlite_conn.cursor()

# Список таблиць для перевірки типів даних
tables_to_check = ['prod_backup', 'orders', 'tb1']

# Перевірка типів даних у кожній таблиці
for table_name in tables_to_check:
    # Отримання структури таблиці
    sqlite_cursor.execute(f"PRAGMA table_info('{table_name}')")
    columns_info = sqlite_cursor.fetchall()

    # Виведення інформації про типи даних у стовпцях таблиці
    print(f"Типи даних для таблиці {table_name}:")
    for column_info in columns_info:
        column_name, data_type = column_info[1], column_info[2]
        print(f"{column_name}: {data_type}")

