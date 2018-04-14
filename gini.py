import numpy as np

class Gini:
    def __init__(self, label_counter):
        self.label_counter = label_counter

    def entropy(self, rows):
        labels = self.label_counter.count(rows)
        number_of_rows = len(rows)
        entropy = 0

        for label in labels:
            prop_of_label = labels[label] / float(number_of_rows)
            entropy = prop_of_label * np.log2(prop_of_label)

        return -entropy

    def info_gain(self, left, right, entropy):
        """Information Gain. The uncertainty of the starting node, minus the weighted impurity of two child nodes."""
        p = float(len(left)) / (len(left) + len(right))

        return entropy - p * self.entropy(left) - (1 - p) * self.entropy(right)