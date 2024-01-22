# Form implementation generated from reading ui file '.\src\ui\ui_main_widget_2.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MyMainWidget(object):
    def setupUi(self, MyMainWidget):
        MyMainWidget.setObjectName("MyMainWidget")
        MyMainWidget.resize(800, 640)
        MyMainWidget.setMinimumSize(QtCore.QSize(800, 640))
        self.verticalLayout = QtWidgets.QVBoxLayout(MyMainWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_title = QtWidgets.QLabel(parent=MyMainWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setKerning(True)
        self.widget_title.setFont(font)
        self.widget_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.widget_title.setObjectName("widget_title")
        self.verticalLayout.addWidget(self.widget_title)
        self.image_label = QtWidgets.QLabel(parent=MyMainWidget)
        self.image_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.image_label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)
        self.frame = QtWidgets.QFrame(parent=MyMainWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.open_image_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.open_image_btn.setObjectName("open_image_btn")
        self.verticalLayout_2.addWidget(self.open_image_btn)
        self.save_image_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.save_image_btn.setEnabled(False)
        self.save_image_btn.setObjectName("save_image_btn")
        self.verticalLayout_2.addWidget(self.save_image_btn)
        self.close_image_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.close_image_btn.setObjectName("close_image_btn")
        self.verticalLayout_2.addWidget(self.close_image_btn)
        self.horizontalLayout.addWidget(self.groupBox)
        self.image_prev_and_next_groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.image_prev_and_next_groupBox.setObjectName("image_prev_and_next_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.image_prev_and_next_groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.prev_image_btn = QtWidgets.QPushButton(parent=self.image_prev_and_next_groupBox)
        self.prev_image_btn.setEnabled(True)
        self.prev_image_btn.setObjectName("prev_image_btn")
        self.verticalLayout_4.addWidget(self.prev_image_btn)
        self.next_image_btn = QtWidgets.QPushButton(parent=self.image_prev_and_next_groupBox)
        self.next_image_btn.setEnabled(True)
        self.next_image_btn.setObjectName("next_image_btn")
        self.verticalLayout_4.addWidget(self.next_image_btn)
        self.horizontalLayout.addWidget(self.image_prev_and_next_groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.file_detail_label = QtWidgets.QLabel(parent=self.groupBox_3)
        self.file_detail_label.setText("")
        self.file_detail_label.setObjectName("file_detail_label")
        self.verticalLayout_3.addWidget(self.file_detail_label)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.function_groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.function_groupBox.setEnabled(True)
        self.function_groupBox.setObjectName("function_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.function_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.denosing_module_btn = QtWidgets.QPushButton(parent=self.function_groupBox)
        self.denosing_module_btn.setEnabled(True)
        self.denosing_module_btn.setObjectName("denosing_module_btn")
        self.gridLayout.addWidget(self.denosing_module_btn, 1, 0, 1, 1)
        self.conv_module_btn = QtWidgets.QPushButton(parent=self.function_groupBox)
        self.conv_module_btn.setEnabled(True)
        self.conv_module_btn.setObjectName("conv_module_btn")
        self.gridLayout.addWidget(self.conv_module_btn, 0, 1, 1, 1)
        self.hist_module_btn = QtWidgets.QPushButton(parent=self.function_groupBox)
        self.hist_module_btn.setEnabled(True)
        self.hist_module_btn.setObjectName("hist_module_btn")
        self.gridLayout.addWidget(self.hist_module_btn, 0, 0, 1, 1)
        self.enhance_module_btn = QtWidgets.QPushButton(parent=self.function_groupBox)
        self.enhance_module_btn.setEnabled(True)
        self.enhance_module_btn.setObjectName("enhance_module_btn")
        self.gridLayout.addWidget(self.enhance_module_btn, 1, 1, 1, 1)
        self.evalueate_module_btn = QtWidgets.QPushButton(parent=self.function_groupBox)
        self.evalueate_module_btn.setEnabled(True)
        self.evalueate_module_btn.setObjectName("evalueate_module_btn")
        self.gridLayout.addWidget(self.evalueate_module_btn, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.function_groupBox)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 3)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(MyMainWidget)
        QtCore.QMetaObject.connectSlotsByName(MyMainWidget)

    def retranslateUi(self, MyMainWidget):
        _translate = QtCore.QCoreApplication.translate
        MyMainWidget.setWindowTitle(_translate("MyMainWidget", "PET医学图像增强系统"))
        self.widget_title.setText(_translate("MyMainWidget", "PET医学图像增强系统 v2.0"))
        self.image_label.setText(_translate("MyMainWidget", "图像预览"))
        self.groupBox.setTitle(_translate("MyMainWidget", "文件操作"))
        self.open_image_btn.setText(_translate("MyMainWidget", "打开文件"))
        self.save_image_btn.setText(_translate("MyMainWidget", "保存图像"))
        self.close_image_btn.setText(_translate("MyMainWidget", "关闭图像"))
        self.image_prev_and_next_groupBox.setTitle(_translate("MyMainWidget", "图像浏览"))
        self.prev_image_btn.setText(_translate("MyMainWidget", "上一张"))
        self.next_image_btn.setText(_translate("MyMainWidget", "下一张"))
        self.groupBox_3.setTitle(_translate("MyMainWidget", "文件信息"))
        self.function_groupBox.setTitle(_translate("MyMainWidget", "功能模块"))
        self.denosing_module_btn.setText(_translate("MyMainWidget", "图像去噪模块"))
        self.conv_module_btn.setText(_translate("MyMainWidget", "卷积与滤波模块"))
        self.hist_module_btn.setText(_translate("MyMainWidget", "直方图模块"))
        self.enhance_module_btn.setText(_translate("MyMainWidget", "自适应增强"))
        self.evalueate_module_btn.setText(_translate("MyMainWidget", "图像评估模块"))
