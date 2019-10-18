import os
import pydicom
from itertools import groupby

from patient import Patient



class Patients:

    def __init__(self, path):
        self._patients = self._getPatients(path)



    def __getitem__(self, key):
        return self._patients[key]



    def _getPatients(self, path):
        datasets = self._readDatasets(path)
        sortedDatasets = sorted(datasets, key = lambda ds: str(ds.PatientName))

        # patientsGroups will contain grouped datasets as follows:
        # [(patient_name_1, datasets_for_patient_name_1),
        #  (patient_name_2, datasets_for_patient_name_2)]
        patientsGroups = groupby(sortedDatasets, lambda ds: str(ds.PatientName))

        return [Patient(list(patientDatasets)) for key, patientDatasets in patientsGroups]



    def _readDatasets(self, path):
        datasets = []
        for root, dirs, files in os.walk(path):
            for name in files:
                datasets.append(pydicom.dcmread(os.path.join(root, name)))
        return datasets
