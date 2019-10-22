import QtQuick 2.0

Image {
    property string stackSource
    property int frame: 50

    source: stackSource + "/" + frame

    MouseArea {
        anchors.fill: parent

        onWheel: {
            console.log(wheel.angleDelta.y, parent.frame)
            parent.frame = parent.frame + Math.sign(wheel.angleDelta.y)
        }
    }
}
