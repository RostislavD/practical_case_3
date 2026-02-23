import datetime

class WORKER:
    def __init__(self, surname=None, initials=None, position=None, salary=0, year_joined=None):
        """
        Конструктор: поддерживает как значения по умолчанию,
        так и инициализацию с параметрами.
        """
        self._surname = surname if surname else "Фамилия не указан"
        self._initials = initials if initials else "Инициалы не указаны"
        self._position = position if position else "Стажер"
        self._salary = salary
        self._year_joined = year_joined if year_joined else datetime.date.today().year

    def __del__(self):
        """Деструктор класса"""
        # В Python срабатывает, когда на объект не остается ссылок
        pass

    # Методы изменения полей (Setters)
    def set_surname(self, surname):
        self._surname = surname

    def set_initials(self, initials):
        self._initials = initials

    def set_position(self, pos):
        self._position = pos

    def set_salary(self, amount):
        self._salary = amount

    def set_year(self, year):
        self._year_joined = year

    # Методы отображения (Getters)
    def get_surname(self):
        return self._surname

    def get_initials(self):
        return self._initials

    def get_experience(self):
        current_year = datetime.date.today().year
        return current_year - self._year_joined

    def display_info(self):
        print(f"Фамилия: {self._surname} | Инициалы: {self._initials} | Должность: {self._position} | "
              f"Зарплата: {self._salary} | Год поступления: {self._year_joined}")
