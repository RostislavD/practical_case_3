from worker_module import WORKER


def main():
    workers_list = []

    print("--- Учет персонала Университета 'Синергия' ---")

    try:
        count = int(input("Введите количество сотрудников для добавления: "))
    except ValueError:
        print("Ошибка: введите число.")
        return

    # Ввод данных
    for i in range(count):
        print(f"\nЗаполнение данных сотрудника №{i + 1}:")
        surname = input("Введите фамилию: ")
        initials = input("Введите инициалы: ")
        pos = input("Введите название должности: ")
        try:
            sal = float(input("Введите зарплату: "))
            year = int(input("Введите год поступления на работу: "))

            # Создание объекта и добавление в список
            new_worker = WORKER(surname, initials, pos, sal, year)
            workers_list.append(new_worker)
        except ValueError:
            print("Ошибка ввода числовых данных. Сотрудник не добавлен.")

    # Вывод по стажу
    try:
        target_exp = int(input("\nВведите минимальный стаж работы для поиска: "))
        print(f"\nФамилии сотрудников со стажем более {target_exp} лет:")

        found = False
        for worker in workers_list:
            if worker.get_experience() > target_exp:
                print(worker.get_surname())
                found = True

        if not found:
            print("Таких работников нет.")

    except ValueError:
        print("Ошибка: стаж должен быть целым числом.")


if __name__ == "__main__":
    main()
