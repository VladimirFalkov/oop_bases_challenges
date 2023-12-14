"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f"Product {self.title} with price {self.price}"


class PrintLoggerMixin:
    def log(self, message):
        print(message)


class PremiumProduct(Product, PrintLoggerMixin):
    def increase_price(self):
        self.price *= 1.2
        self.log(f"Price increased to {self.price}")

    def get_info(self):
        base_info = super().get_info()
        self.log(f"{base_info} (Premium)")
        return f"{base_info} (Premium)"


class DiscountedProduct(Product, PrintLoggerMixin):
    def decrease_price(self):
        self.price /= 1.2
        self.log(f"Price decreased to {self.price}")

    def get_info(self):
        base_info = super().get_info()
        self.log(f"{base_info} (Discounted)")
        return f"{base_info} (Discounted)"


if __name__ == "__main__":
    pass

product1 = PremiumProduct("Product 1", 100)
product2 = DiscountedProduct("Product 2", 200)
product1.increase_price()
product1.get_info()
product2.decrease_price()
product2.get_info()
