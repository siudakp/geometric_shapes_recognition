from class_counter import *

class Leaf:
    def __init__(self, rows):
        self.label_counter = LabelCounter()
        self.leaf = self.label_counter.count(rows)





