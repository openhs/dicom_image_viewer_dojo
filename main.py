# This Python file uses the following encoding: utf-8
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import QUrl

from dicom_image_provider import DicomImageProvider
from patients import Patients
from navigator_items import NavigatorItems



if __name__ == "__main__":
    app = QApplication([])

    view = QQuickView()

    patients = Patients("/tmp/patients")
    dicomImageProvider = DicomImageProvider(patients)
    view.engine().addImageProvider("dicom_image_provider", dicomImageProvider)

    view.rootContext().setContextProperty("navigatorItems", NavigatorItems(patients, app))

    currentDir = os.path.dirname(os.path.abspath(__file__))
    view.setSource(QUrl(os.path.join(currentDir, "main.qml")))
    view.show()

    sys.exit(app.exec_())
