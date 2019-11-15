import QtQuick 2.0


Item {
    property string segmentId
    property string stackSource

    Image {
        id: image

        property int frame: 50

        anchors.fill: parent
        source: stackSource + "/" + frame

        onFrameChanged: graphicsCanvas.drawMeasurements()

        MouseArea {
            anchors.fill: parent

            onWheel: {
                console.log(wheel.angleDelta.y, parent.frame)
                parent.frame = parent.frame + Math.sign(wheel.angleDelta.y)
            }
        }
    }

    Canvas {
        id: graphicsCanvas

        anchors.fill: parent

        function drawMeasurements() {
            var context = getContext("2d");
            context.clearRect(0, 0, width, height);
            context.strokeStyle = "magenta";
            context.lineWidth = 2;

            context.beginPath();
            for (var measurement of measurements.get(parent.segmentId, image.frame)) {
                context.moveTo(measurement.point1.x, measurement.point1.y);
                context.lineTo(measurement.point2.x, measurement.point2.y);
            }
            context.stroke();
            context.closePath();

            markDirty();
        }

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

                parent.drawMeasurements()

                context.strokeStyle = "magenta";
                context.lineWidth = 2;

                context.beginPath()
                context.moveTo(lineBeginX, lineBeginY);
                context.lineTo(mouseX, mouseY);
                context.stroke();
                context.closePath();

                parent.markDirty();
            }

            onReleased: measurements.add(parent.parent.segmentId, image.frame, lineBeginX, lineBeginY, mouseX, mouseY)
        }
    }
}
