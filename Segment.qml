import QtQuick 2.0

Item {
    property string stackSource

    Image {
        property int frame: 50

        anchors.fill: parent
        source: stackSource + "/" + frame

        MouseArea {
            anchors.fill: parent

            onWheel: {
                console.log(wheel.angleDelta.y, parent.frame)
                parent.frame = parent.frame + Math.sign(wheel.angleDelta.y)
            }
        }
    }

    Canvas {
        anchors.fill: parent

        MouseArea {
            property int lineBeginX
            property int lineBeginY

            anchors.fill: parent

            onPressed: {
                lineBeginX = mouseX
                lineBeginY = mouseY
            }

            onPositionChanged: {
                var context = parent.getContext("2d")
                context.clearRect(0, 0, width, height)

                context.strokeStyle = "magenta";
                context.lineWidth = 2;

                context.beginPath()
                context.moveTo(lineBeginX, lineBeginY);
                context.lineTo(mouseX, mouseY);
                context.stroke();
                context.closePath();

                parent.markDirty();
            }
        }
    }
}
