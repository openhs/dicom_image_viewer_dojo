from PyQt5.QtCore import QAbstractListModel, QModelIndex



class NavigatorItems(QAbstractListModel):

    def __init__(self, patients, parent = None):
        super().__init__(parent)

        self._studyDescs = []
        self._populate(patients)



    def roleNames(self):
        return {0: b"studyDescription"}



    def data(self, index, role):
        return self._studyDescs[index.row()]



    def rowCount(self, parent = QModelIndex()):
        return len(self._studyDescs)



    def _populate(self, patients):
        self.beginResetModel()
        self._studyDescs.clear()

        for patient in patients:
            for study in patient.studies:
                self._studyDescs.append(study.studyDescription)

        self.endResetModel()
