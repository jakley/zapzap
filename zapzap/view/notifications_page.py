from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/notifications_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Notifications(object):
    def setupUi(self, Notifications):
        Notifications.setObjectName("Notifications")
        Notifications.resize(400, 300)

        self.retranslateUi(Notifications)
        QtCore.QMetaObject.connectSlotsByName(Notifications)

    def retranslateUi(self, Notifications):
        
        Notifications.setWindowTitle(_("Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Notifications = QtWidgets.QWidget()
    ui = Ui_Notifications()
    ui.setupUi(Notifications)
    Notifications.show()
    sys.exit(app.exec())
