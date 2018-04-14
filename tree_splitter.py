from question import *

class TreeSplitter:
    """Find the best question by iterating over every
       attribute and calculating the information gain."""

    def __init__(self, gini, partitioner):
        self.gini = gini
        self.partitioner = partitioner

    def find_split(self, dataset):
        best_info_gain = 0
        best_question = None
        entropy = self.gini.entropy(dataset)
        number_of_features = len(dataset[0]) - 1

        for column in range(number_of_features):
            unique_features = set([row[column] for row in dataset])

            for feature in unique_features:
                question = Question(column, feature)
                true_rows, false_rows = self.partitioner.partition(dataset, question)

                # Skip a split when it doesn't divide the dataset.
                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue
                
                # Calculate the information gain from the split.
                info_gain = self.gini.info_gain(true_rows, false_rows, entropy)

                if info_gain >= best_info_gain:
                    best_info_gain, best_question = info_gain, question

        return best_info_gain, best_question