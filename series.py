from itertools import islice
from pydicom.dataset import Dataset



class Series:

    def __init__(self, datasets = []):
        self._datasets = datasets



    def getFrame(self, number):
        return next(islice(self._datasets, number, None), Dataset()) if number > 0 else Dataset()
