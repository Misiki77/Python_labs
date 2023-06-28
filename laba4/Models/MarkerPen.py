from Models.Pen import Pen


class MarkerPen(Pen):
    def __init__(self, id, brand, color, material, size, marker_type, num_markers, marker_price):
        super().__init__(id, brand, color, material, size)
        self.marker_type = marker_type
        self.num_markers = num_markers
        self.marker_price = marker_price

    def calculate_price(self):
        print("Price: ", self.marker_price * self.num_markers)

    def print_object(self):
        print("Pencilcase:  ", self.id, self.brand, self.color, self.material, self.size, self.marker_type,
              self.num_markers, self.marker_price)
