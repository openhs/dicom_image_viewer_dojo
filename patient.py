#- # This Python file uses the following encoding: utf-8
#- from PyQt5 import QtWidgets
from itertools import groupby, islice

from study import Study



class Patient:

    def __init__(self, datasets = []):
        self._studies = self._getStudies(datasets)



    @property
    def studies(self):
        return self._studies



    def getStudy(self, number):
        return self.studies[number]



    def _getStudies(self, datasets):
        sortedDatasets = sorted(datasets, key = lambda ds: str(ds.StudyDescription))
        studyGroups = groupby(sortedDatasets, lambda ds: str(ds.StudyDescription))
        return [Study(list(studyDatasets)) for key, studyDatasets in studyGroups]
