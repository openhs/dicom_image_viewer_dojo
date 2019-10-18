#- # This Python file uses the following encoding: utf-8
#- from PyQt5 import QtWidgets
from itertools import groupby, islice

from series import Series



class Study:

    def __init__(self, datasets = []):
        self._datasets = datasets



    @property
    def studyDescription(self):
        return self._datasets[0].StudyDescription if self._datasets else ""



    def getSeries(self, number):
        return next(islice(self._getSerieses(), number, None), Series())



    def _getSerieses(self):

        # sort by instance and series number to get frames in order
        sortedDatasets = sorted(self._datasets, key = lambda ds: ds.InstanceNumber)
        sortedDatasets = sorted(sortedDatasets, key = lambda ds: ds.SeriesNumber)

        sortedDatasets = sorted(sortedDatasets, key = lambda ds: str(ds.SeriesDescription))
        seriesGroups = groupby(sortedDatasets, lambda ds: str(ds.SeriesDescription))
        return (Series(list(seriesDatasets)) for key, seriesDatasets in seriesGroups)
