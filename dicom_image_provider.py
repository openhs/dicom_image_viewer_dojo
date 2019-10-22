from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage
from PyQt5.QtQuick import QQuickImageProvider
import pydicom
import PIL.Image
import PIL.ImageQt



class DicomImageProvider(QQuickImageProvider):

    def __init__(self, patients):
        super().__init__(QQuickImageProvider.Image)
        self._patients = patients

        self._emptyImage = QImage(512, 512, QImage.Format_RGB32)
        self._emptyImage.fill(Qt.darkRed)



    def requestImage(self, id, size):
        """Returns DICOM image.

        id: <study_number>/<series_number>/<frame_number>"""

        studyNumber, seriesNumber, frameNumber = self._parseUri(id)

        patient = self._patients[0]
        study = patient.getStudy(studyNumber)
        series = study.getSeries(seriesNumber)
        frame = series.getFrame(frameNumber)

        if "PixelData" not in frame:
            return (self._emptyImage, size)

        arrayImage = frame.pixel_array

        # convert the array returned from frame to a grayscale image
        pilImage = PIL.Image.fromarray(arrayImage).convert("L")

        # convert the image to a format understood by Qt and return tuple of image and size as required by
        # QQuickImageProvider protocol
        return (PIL.ImageQt.ImageQt(pilImage), size)



    def _parseUri(self, uri):
        uriSplit = uri.split("/")
        studyNumber = int(uriSplit[0])
        seriesNumber = int(uriSplit[1])
        frameNumber = int(uriSplit[2])

        return (studyNumber, seriesNumber, frameNumber)
