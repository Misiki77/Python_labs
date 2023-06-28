from Models.Pen import Pen
import logging

class PenNotFoundError(Exception):
    """Raised when a pen is not found in the pencil case."""

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



    def calculate_price(self):
        print("Price: ", self.num_pencils*self.pencil_price+self.num_pens*self.pen_price+self.num_erasers*self.eraser_price)


    def logged(exception, mode="console"):
        def decorator(func):
            if mode == "console":
                logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
            elif mode == "file":
                logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    logging.error(str(e))
                    raise e

            return wrapper

        return decorator

    @logged(PenNotFoundError, mode = "console")
    def remove_pen(self):
        if self.num_pens == 0:
            raise PenNotFoundError(f"There is no pens to remove from pencilcase.")
        self.num_pens -= 1


school_pen = SchoolPen("grown-l2g", "Camel", "yellow", "cloth", 12, 3, 0, 2, 17, 13, 23)

try:
    school_pen.remove_pen()
except PenNotFoundError as e:
    print(str(e))
