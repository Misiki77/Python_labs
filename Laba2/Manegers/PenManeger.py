from Models.MarkerPen import MarkerPen
from Models.SchoolPen import SchoolPen


class PenManeger:
    def __init__(self):
        self.pen_list = []

    def add_pen(self, pen):
        self.pen_list.append(pen)



maneger = PenManeger()

pencilcase1 = SchoolPen("rfs-54", "Kite", "blue", "cloth", 11, 4, 3, 2, 17, 13, 23)
pencilcase2 = SchoolPen("tpy-12", "Bic", "black", "cloth", 13, 3, 4, 1, 17, 13, 23)
pencilcase3 = MarkerPen("gpt4", "Bic", "orange", "cloth", 8, "for drawing", 6, 24)
pencilcase4 = MarkerPen("fgr1-2", "Camel", "yellow", "cloth", 9, "for drawing", 6, 24)

maneger.add_pen(pencilcase1)
maneger.add_pen(pencilcase2)
maneger.add_pen(pencilcase3)
maneger.add_pen(pencilcase4)

for pen in maneger:
    pen.print_object()
    pen.calculate_price()
