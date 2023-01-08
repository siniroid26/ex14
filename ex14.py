class car:
    def __init__(self, model, year, vmotor, color, price):
        self.model = model
        self.year = year
        self.vmotor = vmotor
        self.color = color
        self.price = price

    def walk(self):
        print(f"Марка: {self.model}\n"
              f"Год выпуска: {self.year}\n"
              f"Объём мотора: {self.vmotor}\n"
              f"Цвет: {self.color}\n"
              f"Цена: {self.price}")

p1 = car("Audi", "2019", "2.0", "black", "31000$")
print(p1.walk())
