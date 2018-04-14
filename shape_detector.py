import cv2

class ShapeDetector:
    def __init__(self, classifier, tree):
        self.classifier = classifier
        self.tree = tree

    def thinness(self, contour):
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        return perimeter ** 2 / float(area)

    def extent(self, contour):
        area = cv2.contourArea(contour)
        rect = cv2.minAreaRect(contour)

        ((x, y), (w, h), r) = rect
        rect_area = w * h

        return area / float(rect_area)

    def shapeName(self, counts):
        total = sum(counts.values()) * 1.0
        probs = {}

        for label in counts.keys():
            probs[label] = str(int(counts[label] / total * 100))

        return probs

    def drawContours(self, img, contours):
        cv2.drawContours(img, contours, -1, (255, 0, 0), 1)

    def putText(self, img, contour, text):
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv2.putText(img, str(text), (cX - 20, cY - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 0), 2)

    def detect(self, img):
        img = cv2.imread(img)

        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)

        image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour_list = []

        for contour in contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.01 * peri, True)
            contour_list.append(contour)

            vertices = len(approx)
            extent = self.extent(contour)
            thinness = self.thinness(contour)

            #print(vertices)
            #print(extent)
            #print(thinness)

            row = [vertices, thinness, extent, 'Label']
            prediction = self.classifier.classify(row, self.tree)
            shape = list(prediction.keys())[0]

            self.drawContours(img, contour_list)
            self.putText(img, contour, shape)

        cv2.imshow('Geometric Shapes Detector', img)
        cv2.waitKey(0)