import sys
from partitioner import *
from gini import *
from tree_splitter import *
from tree_builder import *
from tree_presenter import *
from classifier import *
from shape_detector import *

training_set_1 = [[3, 22, 0.5, 'Triangle'],
                [4, 16, 1, 'Square'],
                [4, 17.58, 1, 'Rectangle'],
                [5, 15.9, 0.69, 'Pentagon'],
                [14, 14, 0.79, 'Circle'],
                [8, 32.24, 0.79, 'Ellipse']]

training_set_2 = [[3, 22, 0.5, 'Triangle'],
                [3, 31.64, 0.51, 'Triangle'],
                [4, 16, 1, 'Square'],
                [4, 18.11, 1, 'Rectangle'],
                [4, 16.17, 1, 'Rectangle'],
                [5, 15.9, 0.69, 'Pentagon'],
                [5, 16.2, 0.69, 'Pentagon'],
                [14, 14, 0.79, 'Circle'],
                [16, 13.97, 0.79, 'Circle'],
                [12, 22.46, 0.79, 'Ellipse'],
                [15, 14.99, 0.76, 'Ellipse']]

training_set_3 = [[3, 22, 0.5, 'Triangle'],
                [3, 31.64, 0.51, 'Triangle'],
                [4, 16, 1, 'Square'],
                [4, 17.58, 1, 'Rectangle'],
                [4, 18.11, 1, 'Rectangle'],
                [4, 16.17, 1, 'Rectangle'],
                [5, 15.9, 0.69, 'Pentagon'],
                [5, 16.2, 0.69, 'Pentagon'],
                [14, 14, 0.79, 'Circle'],
                [16, 13.97, 0.79, 'Circle'],
                [8, 26.46, 0.79, 'Ellipse'],
                [8, 32.24, 0.79, 'Ellipse'],
                [12, 22.46, 0.79, 'Ellipse'],
                [12, 14.27, 0.78, 'Ellipse'],
                [12, 18.49, 0.78, 'Ellipse'],
                [12, 16.92, 0.78, 'Ellipse'],
                [15, 14.99, 0.76, 'Ellipse']]

partitioner = Partitioner()
label_counter = LabelCounter()
gini_test = Gini(label_counter)
tree_splitter = TreeSplitter(gini_test, partitioner)
tree_builder = TreeBuilder(gini_test, partitioner, tree_splitter)
tree_presenter = TreePresenter()
classifier = Classifier()

my_tree = tree_builder.build(training_set_3)
print("***** Decision Tree *****")
tree_presenter.display(my_tree)
shapeDetector = ShapeDetector(classifier, my_tree)

try:
    sys.argv[1]
except IndexError:
    img = 'images/shapes1.jpg'
else:
    img = 'images/' + sys.argv[1]

shapeDetector.detect(img)
