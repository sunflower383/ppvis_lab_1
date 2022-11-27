# Сущности - вредителей
class Pests:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f'Pests {self.name} has damage {self.damage}'

    def __repr__(self):
        return f'Pests {self.name} has damage {self.damage}'