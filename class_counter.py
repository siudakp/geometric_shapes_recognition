class LabelCounter:
    def count(self, rows):
        """Counts the number of each type in a dataset."""
        counts = {}

        for row in rows:
            label = row[-1]

            if label not in counts:
                counts[label] = 0

            counts[label] += 1

        return counts