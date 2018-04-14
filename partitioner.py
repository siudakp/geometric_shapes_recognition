class Partitioner:
    def partition(self, dataset, question):
        """Partitions a dataset. For each row in the dataset, check if it matches the question.
        If so, add it to true rows, otherwise, add it to false rows."""

        true_rows, false_rows = [], []

        for row in dataset:
            if question.match(row):
                true_rows.append(row)
            else:
                false_rows.append(row)

        return true_rows, false_rows

