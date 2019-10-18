from PyQt5.QtQuick import QQuickImageProvider
import pydicom
import PIL.Image
import PIL.ImageQt



class DicomImageProvider(QQuickImageProvider):

    def __init__(self, patients):
        super().__init__(QQuickImageProvider.Image)
        self._patients = patients



    def requestImage(self, id, size):
        """Returns DICOM image.

        id: <study_number>/<series_number>"""

        studyNumber, seriesNumber = self._parseUri(id)

        patient = self._patients[0]
        study = patient.getStudy(studyNumber)
        series = study.getSeries(seriesNumber)
        frame = series.getFrame(50)

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

        return (studyNumber, seriesNumber)
