import QtQuick 2.0
import QtQuick.Controls 2.0

Rectangle {
    width: 800
    height: 600

    Rectangle {
        id: navigator
        color: "#434353"
        width: parent.width * 0.25
        height: parent.height

        ListView {
            anchors.fill: parent

            model: navigatorItems
            delegate: ItemDelegate {
                text: model.studyDescription

                Binding {
                    target: contentItem
                    property: "color"
                    value: "white"
                }
            }
        }
    }

    Layout2x2 {
        anchors.left: navigator.right
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.top: parent.top
    }
}
