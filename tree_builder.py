from leaf import *
from decision_node import *

class TreeBuilder:
    def __init__(self, gain, partitioner, tree_splitter):
        self.gain = gain
        self.partitioner = partitioner
        self.tree_splitter = tree_splitter

    def build(self, rows):
        info_gain, question = self.tree_splitter.find_split(rows)

        if info_gain == 0:
            return Leaf(rows)

        true_rows, false_rows = self.partitioner.partition(rows, question)

        true_branch = self.build(true_rows)
        false_branch = self.build(false_rows)

        return DecisionNode(question, true_branch, false_branch)

