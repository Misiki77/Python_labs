from abc import ABC, abstractmethod


class Pen(ABC):
    def __init__(self, id, brand, color, material, size):
        """
        Конструктор, що інііалізує кожний об'єкт класу SchoolPen
        """

        self.id = id
        self.brand = brand
        self.color = color
        self.material = material
        self.size = size

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def print_object(self):
        pass

    def dict_comprehension(self, value_type):
        attributes = {key: value for key, value in vars(self).items() if isinstance(value, value_type)}
        return attributes