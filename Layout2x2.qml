import QtQuick 2.0

Grid {
    spacing: 4
    columns: 2

    Segment {
        segmentId: "1"
        width: parent.width / 2
        height: parent.height / 2

        // specfies that study 0 and series 0 shall be shown in this segment
        stackSource: "image://dicom_image_provider/0/0"
    }

    Segment {
        segmentId: "2"
        width: parent.width / 2
        height: parent.height / 2

        stackSource: "image://dicom_image_provider/0/1"
    }

    Segment {
        segmentId: "3"
        width: parent.width / 2
        height: parent.height / 2

        stackSource: "image://dicom_image_provider/1/0"
    }

    Segment {
        segmentId: "4"
        width: parent.width / 2
        height: parent.height / 2

        stackSource: "image://dicom_image_provider/1/1"
    }
}
