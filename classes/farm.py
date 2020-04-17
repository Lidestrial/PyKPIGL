class Farm:
    square_price = 350
    sheep_price = 20
    cow_price = 30
    chicken_price = 2

    def __init__(self, name: str, square: int, sheeps: int, cows: int, chicks: int):
        self.name = name
        self.cows = cows
        self.sheeps = sheeps
        self.chicks = chicks
        self.square = square

    def price_sheep(self):
        return self.sheeps * Farm.sheep_price

    def price_cow(self):
        return self.cows * Farm.cow_price

    def price_chicken(self):
        return self.chicks * Farm.chicken_price

    def price_square(self):
        return self.square * Farm.square_price

    def get_value(self):
        return self.price_square()+self.price_chicken()+self.price_cow()+self.price_sheep()

    def __eq__(self, other):
        if not isinstance(other, Farm):
            return False
        return self.get_value() == other.get_value()

    def __gt__(self, other):
        return self.get_value() > other.get_value()
