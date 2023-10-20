import sqlite3

# Функция для создания соединения с базой данных
def create_connection(database_name):
    try:
        conn = sqlite3.connect(database_name)
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка при создании соединения с базой данных: {e}")
        return None

# Функция для создания таблицы
def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        cursor.close()
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")

# Функция для вставки данных
def insert_data(conn, insert_sql, data_tuple):
    try:
        cursor = conn.cursor()
        cursor.execute(insert_sql, data_tuple)
        conn.commit()
        cursor.close()
    except sqlite3.Error as e:
        print(f"Ошибка при вставке данных: {e}")

# Функция для выборки данных
def select_data(conn, select_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except sqlite3.Error as e:
        print(f"Ошибка при выборке данных: {e}")
        return None

# Функция для обновления данных
def update_data(conn, update_sql, data_tuple):
    try:
        cursor = conn.cursor()
        cursor.execute(update_sql, data_tuple)
        conn.commit()
        cursor.close()
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении данных: {e}")

def main():
    database_name = "Death_Note.db"
    conn = create_connection(database_name)

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS my_table (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    );
    """
    create_table(conn, create_table_sql)

    insert_sql = "INSERT INTO my_table (name, age) VALUES (?, ?)"
    data = ("John", 30)
    insert_data(conn, insert_sql, data)

    select_sql = "SELECT * FROM my_table"
    result = select_data(conn, select_sql)
    print(result)

    update_sql = "UPDATE my_table SET age = ? WHERE name = ?"
    data = (35, "John")
    update_data(conn, update_sql, data)

    conn.close()

if __name__ == "__main__":
    main()
