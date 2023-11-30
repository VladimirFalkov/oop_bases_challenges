"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username):
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            return "Такого пользователя не существует."


class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        self.usernames.clear()


if __name__ == "__main__":
    print("#" * 20 + "__UserManager__" + "#" * 20)
    manager1 = UserManager()
    manager1.add_user("nickname")
    manager1.add_user("nickname1")
    manager1.add_user("nickname2")
    c = manager1.get_users()
    print(c)
    print("#" * 20 + "__AdminManager__" + "#" * 20)
    manager2 = AdminManager()
    manager2.add_user("nickname")
    manager2.add_user("nickname1")
    manager2.add_user("nickname2")
    print(manager2.get_users())
    manager2.ban_username("nickname1")
    print(manager2.get_users())
    print(manager2.ban_username("nickname3"))
    print(manager2.get_users())

    print("#" * 20 + "__SuperAdminManager__" + "#" * 20)
    manager3 = SuperAdminManager()
    manager3.add_user("nickname")
    manager3.add_user("nickname1")
    manager3.add_user("nickname2")
    print(manager3.get_users())
    manager3.ban_username("nickname1")
    print(manager3.get_users())
    print(manager3.ban_username("nickname3"))
    print(manager3.get_users())
    manager3.add_user("nickname1")
    print(manager3.get_users())
    manager3.ban_all_users()
    print(manager3.get_users())
