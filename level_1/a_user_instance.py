"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"Информация о пользователе: {self.name}, {self.username}, {self.age}, {self.phone}"


if __name__ == "__main__":
    user1 = User("Зинаида", "zinatut", 23, "+12023456789")


print(user1)
