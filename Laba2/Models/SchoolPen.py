from Models.Pen import Pen


class SchoolPen(Pen):
    def __init__(self, id, brand, color, material, size, num_pencils, num_pens, num_erasers, pencil_price, pen_price,
                 eraser_price):
        super().__init__(id, brand, color, material, size)
        self.num_pencils = num_pencils
        self.num_pens = num_pens
        self.num_erasers = num_erasers
        self.pencil_price = pencil_price
        self.pen_price = pen_price
        self.eraser_price = eraser_price

    def print_object(self):
        print("Pencilcase:  ", self.id, self.brand, self.color, self.material, self.size, self.num_pencils,
              self.num_pens, self.num_erasers, self.pencil_price, self.pen_price, self.eraser_price)

    def add_pencils(self):
        self.num_pencils += 1

    def add_pen(self):
        self.num_pencils += 1

    def remove_pencils(self):
        self.num_pencils -= 1

    def remove_pen(self):
        self.num_pens -= 1

    def calculate_price(self):
        print("Price: ", self.num_pencils*self.pencil_price+self.num_pens*self.pen_price+self.num_erasers*self.eraser_price)


