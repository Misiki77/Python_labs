from Models import Pen
from Models.MarkerPen import MarkerPen
from Models.SchoolPen import SchoolPen


class PenManeger:
    def __init__(self):
        self.pen_list = []

    def add_pen(self, pen, list):
        list.append(pen)

    def __len__(self):
        return len(self.id)

    def __getitem__(self, index):
        return self.id[index]

    def __iter__(self):
        return iter(self.color)


pen_list = []
maneger = PenManeger()

pencilcase1 = SchoolPen("rfs-54", "Kite", "blue", "cloth", 11, 4, 3, 2, 17, 13, 23)
pencilcase2 = SchoolPen("tpy-12", "Bic", "black", "cloth", 13, 3, 4, 1, 17, 13, 23)
pencilcase3 = MarkerPen("gpt4", "Bic", "orange", "cloth", 8, "for drawing", 6, 24)
pencilcase4 = MarkerPen("fgr1-2", "Camel", "yellow", "cloth", 9, "for drawing", 6, 24)

maneger.add_pen(pencilcase1, pen_list)
maneger.add_pen(pencilcase2, pen_list)
maneger.add_pen(pencilcase3, pen_list)
maneger.add_pen(pencilcase4, pen_list)


for pen in pen_list:
    print(pen)


    def list_comprehension(abstract_class, method_name):
        result_list = []

        for subclass in abstract_class.__subclasses__():

            if hasattr(subclass, method_name) and callable(getattr(subclass, method_name)):
                obj = subclass()
                result_list.append(getattr(obj, method_name)())

        return result_list

    def enumerate_list(lst):

        return [(item, index) for index, item in enumerate(lst)]

    def zip_combine(objects, results):
        return list(zip(objects, results))

    def check_objects(objects, condition):
        all_objects_satisfy_condition = all(condition(obj) for obj in objects)
        any_object_satisfies_condition = any(condition(obj) for obj in objects)
        return {'all': all_objects_satisfy_condition, 'any': any_object_satisfies_condition}


prices = list_comprehension(Pen, "calculate_price")
print(prices)

number = enumerate_list(pen_list)
print(number)

combined = zip_combine(pen_list, prices)
print(combined)

result = maneger.dict_comprehension(int)
print(result)

looking_for_yellow_object = check_objects(pen_list, lambda obj: obj.color == 'yellow')
print(looking_for_yellow_object)

