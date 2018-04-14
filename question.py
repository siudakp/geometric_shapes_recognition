class Question:
    header = ["vertices", "thinness", "extent", "label"]

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def is_numeric(self, value):
        return isinstance(value, int) or isinstance(value, float)

    def match(self, attribute):
        value = attribute[self.column]

        if self.is_numeric(value):
            return value >= self.value
        else:
            return value == self.value

    def __repr__(self):
        condition = "=="

        if self.is_numeric(self.value):
            condition = ">="

        return "Is {} {} {}?".format(self.header[self.column], condition, self.value)




