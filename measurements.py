from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty



class Point(QObject):

    def __init__(self, x, y, parent = None):
        super().__init__(parent)

        self._x = x
        self._y = y



    @pyqtProperty(float)
    def x(self):
        return self._x



    @pyqtProperty(float)
    def y(self):
        return self._y



class Measurement(QObject):

    def __init__(self, point1, point2, parent = None):
        super().__init__(parent)

        self._point1 = point1
        self._point2 = point2



    @pyqtProperty(Point)
    def point1(self):
        return self._point1



    @pyqtProperty(Point)
    def point2(self):
        return self._point2



class Measurements(QObject):

    def __init__(self, parent = None):
        super().__init__(parent)

        # {segment: {frame: [measurement]}}
        self._measurements = {}



    @pyqtSlot(str, int, result = list)
    def get(self, segment, frame):
        return self._measurements[segment][frame] \
               if segment in self._measurements and frame in self._measurements[segment] \
               else []



    @pyqtSlot(str, int, int, int, int, int)
    def add(self, segment, frame, x1, y1, x2, y2):
        if segment not in self._measurements:
            self._measurements[segment] = {}
        if frame not in self._measurements[segment]:
            self._measurements[segment][frame] = []
        self._measurements[segment][frame].append(Measurement(Point(x1, y1, self), Point(x2, y2, self), self))
