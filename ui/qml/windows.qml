import QtQuick 2.14
import QtQuick.Window 2.0

Window{
    visible:true
    width:360
    height:260
    
    MouseArea{
        anchors.fill: parent
        onClicked: {
            Qt.Quit();
        }
    }

    Text{
        text: qsTr("Window")
        anchors.centerIn:parent
    }
}   