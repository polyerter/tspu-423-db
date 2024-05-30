import sqlite3

connection = sqlite3.connect('employees_db-full-1.0.6.db')
cursor = connection.cursor()


def get_tables():
    cursor.execute(f'''
        SELECT * FROM employees LIMIT 100;
    ''')

    return cursor.fetchall()

print(get_tables())


connection.commit()
connection.close()