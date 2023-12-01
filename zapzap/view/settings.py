from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/settings.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(750, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMinimumSize(QtCore.QSize(750, 550))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Settings)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settingMargin = QtWidgets.QFrame(parent=Settings)
        self.settingMargin.setObjectName("settingMargin")
        self.verticalLayout_99 = QtWidgets.QVBoxLayout(self.settingMargin)
        self.verticalLayout_99.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName("verticalLayout_99")
        self.setting_frame = QtWidgets.QFrame(parent=self.settingMargin)
        self.setting_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.setting_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.setting_frame.setObjectName("setting_frame")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.setting_frame)
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.leftMenu = QtWidgets.QFrame(parent=self.setting_frame)
        self.leftMenu.setMinimumSize(QtCore.QSize(250, 0))
        self.leftMenu.setMaximumSize(QtCore.QSize(250, 16777215))
        self.leftMenu.setStyleSheet("")
        self.leftMenu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.leftMenu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setContentsMargins(25, 3, 25, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menu = QtWidgets.QFrame(parent=self.leftMenu)
        self.menu.setMinimumSize(QtCore.QSize(0, 0))
        self.menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_58.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.btn_general = QtWidgets.QPushButton(parent=self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.btn_general.sizePolicy().hasHeightForWidth())
        self.btn_general.setSizePolicy(sizePolicy)
        self.btn_general.setMinimumSize(QtCore.QSize(0, 45))
        self.btn_general.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_general.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.btn_general.setObjectName("btn_general")
        self.verticalLayout_58.addWidget(self.btn_general)
        self.btn_account = QtWidgets.QPushButton(parent=self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.btn_account.sizePolicy().hasHeightForWidth())
        self.btn_account.setSizePolicy(sizePolicy)
        self.btn_account.setMinimumSize(QtCore.QSize(0, 45))
        self.btn_account.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_account.setObjectName("btn_account")
        self.verticalLayout_58.addWidget(self.btn_account)
        self.btn_notifications = QtWidgets.QPushButton(parent=self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.btn_notifications.sizePolicy().hasHeightForWidth())
        self.btn_notifications.setSizePolicy(sizePolicy)
        self.btn_notifications.setMinimumSize(QtCore.QSize(0, 45))
        self.btn_notifications.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_notifications.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.btn_notifications.setObjectName("btn_notifications")
        self.verticalLayout_58.addWidget(self.btn_notifications)
        self.btn_personalization = QtWidgets.QPushButton(parent=self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.btn_personalization.sizePolicy().hasHeightForWidth())
        self.btn_personalization.setSizePolicy(sizePolicy)
        self.btn_personalization.setMinimumSize(QtCore.QSize(0, 45))
        self.btn_personalization.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_personalization.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.btn_personalization.setObjectName("btn_personalization")
        self.verticalLayout_58.addWidget(self.btn_personalization)
        self.btn_donations = QtWidgets.QPushButton(parent=self.menu)
        self.btn_donations.setMinimumSize(QtCore.QSize(0, 45))
        self.btn_donations.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_donations.setObjectName("btn_donations")
        self.verticalLayout_58.addWidget(self.btn_donations)
        self.btn_about = QtWidgets.QPushButton(parent=self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy)
        self.btn_about.setMinimumSize(QtCore.QSize(0, 45))
        self.btn_about.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_about.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.btn_about.setObjectName("btn_about")
        self.verticalLayout_58.addWidget(self.btn_about)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_58.addItem(spacerItem)
        self.btn_quit = QtWidgets.QPushButton(parent=self.menu)
        self.btn_quit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_quit.setObjectName("btn_quit")
        self.verticalLayout_58.addWidget(self.btn_quit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_58.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.menu)
        self.horizontalLayout_29.addWidget(self.leftMenu)
        self.line = QtWidgets.QFrame(parent=self.setting_frame)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_29.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(25, 9, 25, 9)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_close = QtWidgets.QPushButton(parent=self.setting_frame)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.settings_stacked = QtWidgets.QStackedWidget(parent=self.setting_frame)
        self.settings_stacked.setObjectName("settings_stacked")
        self.verticalLayout.addWidget(self.settings_stacked)
        self.horizontalLayout_29.addLayout(self.verticalLayout)
        self.verticalLayout_59.addLayout(self.horizontalLayout_29)
        self.verticalLayout_99.addWidget(self.setting_frame)
        self.horizontalLayout.addWidget(self.settingMargin)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        
        Settings.setWindowTitle(_("Form"))
        self.btn_general.setText(_("General"))
        self.btn_account.setText(_("Account"))
        self.btn_notifications.setText(_("Notifications"))
        self.btn_personalization.setText(_("Personalization"))
        self.btn_donations.setText(_("Donations"))
        self.btn_about.setText(_("About"))
        self.btn_quit.setText(_("Quit"))
        self.btn_close.setText(_("x"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QWidget()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec())
