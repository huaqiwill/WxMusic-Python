import QtQuick 2.0
import QtQuick.Window 2.2

Window {
    visible : true //此属性必须要定义，否则窗口不显示
    width: 320; height: 240
    // visible: true
    color: "lightblue"

    Text {
        id: txt
        text: "Clicked me"
        font.pixelSize: 20
        anchors.centerIn: parent
    }
}
