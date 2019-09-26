import QtQuick 2.0

Grid {
    spacing: 4
    columns: 2

    Image {
        width: parent.width / 2
        height: parent.height / 2

        // specfies that study 0 and series 0 shall be shown in this segment
        source: "image://dicom_image_provider/0/0"
    }

    Image {
        width: parent.width / 2
        height: parent.height / 2

        source: "image://dicom_image_provider/0/1"
    }

    Image {
        width: parent.width / 2
        height: parent.height / 2

        source: "image://dicom_image_provider/1/0"
    }

    Image {
        width: parent.width / 2
        height: parent.height / 2

        source: "image://dicom_image_provider/1/1"
    }
}
