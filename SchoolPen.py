class SchoolPen:
    pass
    id = "isn-101"
    brand = None
    color = None
    material = None
    size = None
    num_pencils = None
    num_pens = None
    num_erasers = None

    def __init__(self, id, brand, color, material, size, num_pencils, num_pens, num_erasers):
        """
        Конструктор, що інііалізує кожний об'єкт класу SchoolPen
        """

        self.id = id
        self.brand = brand
        self.color = color
        self.material = material
        self.size = size
        self.num_pencils = num_pencils
        self.num_pens = num_pens
        self.num_erasers = num_erasers

    def print_object(self):
        print("Pencilcase:  ", self.id, self.brand, self.color, self.material, self.size, self.num_pencils,
              self.num_pens, self.num_erasers)

    def add_pencils(self):
        self.num_pencils += 1

    def add_pen(self):
        self.num_pencils += 1

    def remove_pencils(self):
        self.num_pencils -= 1

    def remove_pen(self):
        self.num_pens -= 1


def main():
    pencilcase = SchoolPen("rfs-54", "Kite", "blue", "cloth", 11, 4, 3, 2)
    pencilcase.print_object()

    pencilcase.add_pencils()
    pencilcase.add_pen()
    pencilcase.remove_pencils()
    pencilcase.remove_pen()
    pencilcase.print_object()

    if __name__ == "__main__":
        main()
