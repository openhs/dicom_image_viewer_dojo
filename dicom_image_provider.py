# This Python file uses the following encoding: utf-8
from PyQt5.QtQuick import QQuickImageProvider
import pydicom
import PIL.Image
import PIL.ImageQt



class DicomImageProvider(QQuickImageProvider):

    def __init__(self):
        super().__init__(QQuickImageProvider.Image)



    def requestImage(self, id, size):

        # read a frame
        frame = pydicom.dcmread(
            "/tmp/patients/HIREZ_#9_UTMC.pat/HIREZ_#9_UTMC.CT.POST_11_21_2003.3.120.2007.10.12.14.36.23.671875.40010.ima")

        arrayImage = frame.pixel_array

        # convert the array returned from frame to a grayscale image
        pilImage = PIL.Image.fromarray(arrayImage).convert("L")

        # convert the image to a format understood by Qt and return tuple of image and size as required by
        # QQuickImageProvider protocol
        return (PIL.ImageQt.ImageQt(pilImage), size)
