import sqlite3
from datetime import datetime

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS tasks (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     task TEXT NOT NULL,
#     created_at TEXT NOT NULL,
#     is_done INTEGER DEFAULT 0
# )
# ''')
# conn.commit()



def new_tusk():
    tusk = input('Введите задачу:')
    time_ = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO tasks (task, created_at) VALUES (?, ?)', (tusk, time_))
    conn.commit()
    print('Задача добавлена!')


def show_tusk():
    cursor.execute('SELECT id, task, created_at, is_done FROM tasks')
    tusks = cursor.fetchall()

    if not tusks:
        print('Список задач пуст!')
        return

    print('Список задач:')

    for tusk in tusks:
        id_, text, created_at, is_done = tusk
        res = '✔' if is_done else 'x'
        print(f"{id_}. [{res}] {text} (добавлено: {created_at})")


def delete_tusk():
    show_tusk()
    tusk_id = input("Введите ID задачи для удаления: ")

    try:
        cursor.execute('DELETE FROM tasks WHERE id = ?', (tusk_id,))
        conn.commit()
        print("Задача удалена!")
    except:
        print("Ошибка: такой задачи нет!")


def mark_():
    show_tusk()
    tusk_id = input("Введите ID выполненной задачи: ")

    try:
        cursor.execute('UPDATE tasks SET is_done = 1 WHERE id=?', (tusk_id,))
        conn.commit()
        print('Задача отмечена как выполненная!')
    except:
        print('Ошибка: такой задачи нет!')

def main():
    while True:
        print("\n To-Do List Меню:")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Отметить как выполненную")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            new_tusk()
        elif choice == '2':
            show_tusk()
        elif choice == '3':
            mark_()
        elif choice == '4':
            delete_tusk()
        elif choice == '5':
            print('Вы вышли!')
            break
        else:
            print('Ошибка: не верный выбор попробуйте сного!')

if __name__ == '__main__':
    main()
    conn.close()
