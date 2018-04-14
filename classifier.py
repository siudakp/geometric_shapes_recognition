from leaf import *

class Classifier:
    def classify(self, row, node):
        if isinstance(node, Leaf):
            return node.leaf

        if node.question.match(row):
            return self.classify(row, node.true_branch)
        else:
            return self.classify(row, node.false_branch)