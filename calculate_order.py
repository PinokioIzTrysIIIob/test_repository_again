import time

DELIVERY_CAPITALS = 300
DELIVERY_REGION = 500

class Customer:
    """Класс для хранения данных о покупателе"""
    def __init__(self, name: str, age: int, is_student: bool, city: str):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.city = city

    def has_student_discount(self) -> bool:
        """Проверка права на студенческую скидку"""
        return self.age >= 18 and self.is_student


class Order:
    """Класс для управления заказом"""
    def __init__(self, customer: Customer, price: float, quantity: int, discount_percent: float):
        self.customer = customer
        self.price = price
        self.quantity = quantity
        self.discount_percent = discount_percent

    def calculate_base_total(self) -> float:
        """Расчет стоимости товаров с учетом скидки"""
        total = self.price * self.quantity
        if self.customer.has_student_discount() and self.discount_percent > 0:
            total -= total * (self.discount_percent / 100)
        return total

    def get_delivery_cost(self) -> float:
        """Определение стоимости доставки на основе города"""
        if self.customer.city in ["Москва", "Санкт-Петербург"]:
            return DELIVERY_CAPITALS
        return DELIVERY_REGION

    def calculate_full_total(self) -> float:
        """Итоговая стоимость: товары + доставка"""
        return self.calculate_base_total() + self.get_delivery_cost()

    def print_receipt(self):
        """Вывод информации о заказе (разделение логики)"""
        print(f"Заказ покупателя: {self.customer.name}")
        print(f"Возраст: {self.customer.age}")
        print(f"Город: {self.customer.city}")
        print(f"Итоговая стоимость: {self.calculate_full_total()}")


# Данные для теста
price = 1000
quantity = 3
discount = 10
city = "Москва"

start_time = time.perf_counter()  # Точка замера времени

# Создаем объекты (вместо кучи разрозненных параметров)
customer = Customer(name="Иван", age=20, is_student=True, city=city)
order = Order(customer=customer, price=price, quantity=quantity, discount_percent=discount)

# Выполняем операции
order.print_receipt()
final_cost = order.calculate_full_total()

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Заказ обработан. Время выполнения: {execution_time:.6f} секунд")