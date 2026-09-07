class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{item.name}: {item.price}" for item in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV("Samsung TV", 50000))
cart.add(TV("LG TV", 45000))
cart.add(Table("Компьютерный стол", 12000))
cart.add(Notebook("Lenovo", 60000))
cart.add(Notebook("ASUS", 70000))
cart.add(Cup("Кружка", 500))

print(cart.get_list())
