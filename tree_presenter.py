from leaf import *

class TreePresenter:
    def display(self, node, spacing = ""):
        if isinstance(node, Leaf):
            leaf = list(node.leaf.keys())[0]
            print(spacing + "Leaf: " + leaf)
            return

        print(spacing + str(node.question))
        print(spacing + '-> True')
        self.display(node.true_branch, spacing + "  ")
        print(spacing + '-> False')
        self.display(node.false_branch, spacing + "  ")



