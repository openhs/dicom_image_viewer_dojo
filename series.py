#- # This Python file uses the following encoding: utf-8
#- from PyQt5 import QtWidgets

from itertools import islice
from pydicom.dataset import Dataset



class Series:

    def __init__(self, datasets = []):
        self._datasets = datasets



    def getFrame(self, number):
        return next(islice(self._datasets, number, None), Dataset())
