import json
import os

from worker_module import WORKER

DB_FILE = "workers.json"


def load_data():
    """Загрузка списка сотрудников из JSON файла"""
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            data_list = json.load(f)
            return [WORKER.from_dict(item) for item in data_list]
    except (json.JSONDecodeError, KeyError):
        return []


def save_data(workers):
    """Сохранение списка сотрудников в JSON файл"""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump([w.to_dict() for w in workers], f, ensure_ascii=False, indent=4)


def main():
    # 1. Загрузка данных из прошлых сессий
    workers_list = load_data()
    while True:
        print("\n--- СИСТЕМА УПРАВЛЕНИЯ ПЕРСОНАЛОМ ---")
        print("1. Ввести новых сотрудников")
        print("2. Вывести список сотрудников по стажу")
        print("3. Показать всех сотрудников")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        if choice == '1':
            try:
                count = int(input("Сколько сотрудников добавить? "))
                for i in range(count):
                    print(f"\nСотрудник №{len(workers_list) + 1}:")
                    surname = input("Введите фамилию: ")
                    initials = input("Введите инициалы: ")
                    pos = input("Введите название должности: ")
                    sal = float(input("Зарплата: "))
                    year = int(input("Год поступления: "))

                    workers_list.append(WORKER(surname, initials, pos, sal, year))

                # Сохраняем сразу после ввода
                save_data(workers_list)
                print("\nДанные успешно сохранены!")
            except ValueError:
                print("Ошибка: некорректный формат данных.")

        elif choice == '2':
            if not workers_list:
                print("Список пуст. Сначала добавьте данные.")
                continue

            try:
                target_exp = int(input("Введите минимальный стаж: "))
                print(f"\nСотрудники со стажем более {target_exp} лет:")
                found = False
                for w in workers_list:
                    if w.get_experience() > target_exp:
                        print(f"- {w.get_surname()} (Стаж: {w.get_experience()} лет)")
                        found = True
                if not found:
                    print("Таких работников нет.")
            except ValueError:
                print("Ошибка: стаж должен быть числом.")

        elif choice == '3':
            print("\nВесь список сотрудников:")
            for w in workers_list:
                w.display_info()

        elif choice == '0':
            print("Завершение работы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
