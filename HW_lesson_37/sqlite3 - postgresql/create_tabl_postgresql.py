import psycopg2

# Підключаємося до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname='lesson_37',
    user='postgres',
    password='123',
    host='localhost'
)
cursor = conn.cursor()

# SQL-запити для створення таблиць
sql_queries = """
CREATE TABLE countries (
    country_id VARCHAR(2) PRIMARY KEY NOT NULL,
    country_name VARCHAR(40) NOT NULL,
    region_id INTEGER NOT NULL
);

CREATE TABLE regions (
    region_id INTEGER PRIMARY KEY NOT NULL,
    region_name VARCHAR(25) NOT NULL
);

CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY NOT NULL,
    street_address VARCHAR(25) NOT NULL,
    postal_code VARCHAR(12),
    city VARCHAR(30) NOT NULL,
    state_province VARCHAR(12),
    country_id VARCHAR(2)
);

CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY NOT NULL,
    depart_name VARCHAR(20) NOT NULL,
    manager_id INTEGER NOT NULL,
    location_id INTEGER
);

CREATE TABLE jobs (
    job_id VARCHAR(10) PRIMARY KEY NOT NULL,
    job_title VARCHAR(25) NOT NULL,
    min_salary DECIMAL,
    max_salary DECIMAL
);

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY NOT NULL,
    first_name VARCHAR(20),
    last_name VARCHAR(25),
    email VARCHAR(25),
    phone_number VARCHAR(20),
    hire_date DATE,
    job_id VARCHAR(10) NOT NULL,
    salary DECIMAL,
    commission_pct NUMERIC,
    manager_id INTEGER,
    department_id INTEGER,
    avg_salary NUMERIC
);

CREATE TABLE department (
    department_id TEXT,
    department_name TEXT,
    manager_id TEXT,
    location_id TEXT
);

CREATE TABLE job_history (
    employee_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    job_id VARCHAR(10) NOT NULL,
    department_id INTEGER NOT NULL
);

CREATE TABLE prod_mast (
    prod_id INTEGER PRIMARY KEY,
    prod_name TEXT,
    prod_rate INTEGER,
    prod_qc TEXT DEFAULT 'OK'
);

CREATE TABLE prod_backup (
    prod_id INTEGER PRIMARY KEY,
    prod_name TEXT,
    prod_rate INTEGER,
    prod_qc TEXT DEFAULT 'OK'
);

CREATE TABLE orders (
    ord_no INTEGER PRIMARY KEY,
    item_id INTEGER,
    item_name TEXT,
    ord_qty INTEGER,
    cost INTEGER
);

CREATE TABLE tb1 (
    c1 INT,
    c2 CHAR(5),
    c3 FLOAT
);

CREATE TABLE ESERCICIO1 (
    C TEXT,
    D TEXT
);

CREATE TABLE users (
    name VARCHAR(128),
    email VARCHAR(128)
);

CREATE TABLE tags (
    title TEXT,
    description TEXT,
    created TEXT
);

CREATE TABLE s (
    A INT,
    D INT,
    E INT
);

CREATE TABLE r (
    A INT,
    B INT
);

CREATE TABLE Emor (
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT
);

CREATE TABLE MIN_SALARY (
    job_id TEXT,
    min_salary DECIMAL
);

CREATE TABLE employee_data (
    employee_name TEXT,
    item TEXT,
    rate REAL,
    quantity INTEGER,
    date TEXT,
    id INTEGER PRIMARY KEY
);

CREATE TABLE STUDENT (
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    FEES REAL
);

CREATE TABLE EMPLOYEE_INCOME (
    EMPID INTEGER,
    NAME VARCHAR(20),
    SALARY INTEGER
);

CREATE TABLE details (
    id INTEGER,
    name VARCHAR(50),
    weight INTEGER,
    turn INTEGER
);

CREATE TABLE "user_table" (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

CREATE TABLE "my_user_table" (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    phone TEXT
);

"""

# Розділяємо SQL-запити на окремі команди
queries = sql_queries.split(';')

# Виконуємо кожну окрему команду SQL
for query in queries:
    if query.strip():
        cursor.execute(query)

# Підтверджуємо транзакцію
conn.commit()

# Закриваємо з'єднання
cursor.close()
conn.close()
