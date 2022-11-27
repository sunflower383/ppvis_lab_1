# Сущности - Погода
class Weather:
    def __init__(self, name, growth_rate):
        self.name = name
        self.growth_rate = growth_rate

    def __str__(self):
        return self.name
    
class Rain(Weather):
    def __init__(self):
        super().__init__("Rain", 0.5)


class Sun(Weather):
    def __init__(self):
        super().__init__("Sun", 1)


class Drought(Weather):
    def __init__(self):
        super().__init__("Drought", 0.1)