# Form implementation generated from reading ui file '.\src\ui\ui_subwidget_histogram.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ui_subwidget_histogram(object):
    def setupUi(self, ui_subwidget_histogram):
        ui_subwidget_histogram.setObjectName("ui_subwidget_histogram")
        ui_subwidget_histogram.setEnabled(True)
        ui_subwidget_histogram.resize(840, 588)
        self.verticalLayout = QtWidgets.QVBoxLayout(ui_subwidget_histogram)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=ui_subwidget_histogram)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 280))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_y_channel_hist = QtWidgets.QLabel(parent=self.groupBox)
        self.label_y_channel_hist.setMinimumSize(QtCore.QSize(200, 200))
        self.label_y_channel_hist.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_y_channel_hist.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_y_channel_hist.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_y_channel_hist.setObjectName("label_y_channel_hist")
        self.horizontalLayout_2.addWidget(self.label_y_channel_hist)
        self.label_r_channel_hist = QtWidgets.QLabel(parent=self.groupBox)
        self.label_r_channel_hist.setMinimumSize(QtCore.QSize(200, 200))
        self.label_r_channel_hist.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_r_channel_hist.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_r_channel_hist.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_r_channel_hist.setObjectName("label_r_channel_hist")
        self.horizontalLayout_2.addWidget(self.label_r_channel_hist)
        self.label_g_channel_hist = QtWidgets.QLabel(parent=self.groupBox)
        self.label_g_channel_hist.setMinimumSize(QtCore.QSize(200, 200))
        self.label_g_channel_hist.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_g_channel_hist.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_g_channel_hist.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_g_channel_hist.setObjectName("label_g_channel_hist")
        self.horizontalLayout_2.addWidget(self.label_g_channel_hist)
        self.label_b_channel_hist = QtWidgets.QLabel(parent=self.groupBox)
        self.label_b_channel_hist.setMinimumSize(QtCore.QSize(200, 200))
        self.label_b_channel_hist.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_b_channel_hist.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_b_channel_hist.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_b_channel_hist.setObjectName("label_b_channel_hist")
        self.horizontalLayout_2.addWidget(self.label_b_channel_hist)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=ui_subwidget_histogram)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_original_image = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_original_image.setMinimumSize(QtCore.QSize(300, 250))
        self.label_original_image.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_original_image.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_original_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_original_image.setObjectName("label_original_image")
        self.horizontalLayout_5.addWidget(self.label_original_image)
        self.label_processed_image = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_processed_image.setMinimumSize(QtCore.QSize(300, 250))
        self.label_processed_image.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_processed_image.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_processed_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_processed_image.setObjectName("label_processed_image")
        self.horizontalLayout_5.addWidget(self.label_processed_image)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.setStretch(0, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_histogramEqualize = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_histogramEqualize.setObjectName("pushButton_histogramEqualize")
        self.verticalLayout_4.addWidget(self.pushButton_histogramEqualize)
        self.pushButton_ok = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.verticalLayout_4.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.verticalLayout_4.addWidget(self.pushButton_cancel)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(ui_subwidget_histogram)
        QtCore.QMetaObject.connectSlotsByName(ui_subwidget_histogram)

    def retranslateUi(self, ui_subwidget_histogram):
        _translate = QtCore.QCoreApplication.translate
        ui_subwidget_histogram.setWindowTitle(_translate("ui_subwidget_histogram", "直方图处理模块"))
        self.groupBox.setTitle(_translate("ui_subwidget_histogram", "计算直方图"))
        self.label_y_channel_hist.setText(_translate("ui_subwidget_histogram", "Y通道直方图"))
        self.label_r_channel_hist.setText(_translate("ui_subwidget_histogram", "R通道直方图"))
        self.label_g_channel_hist.setText(_translate("ui_subwidget_histogram", "G通道直方图"))
        self.label_b_channel_hist.setText(_translate("ui_subwidget_histogram", "B通道直方图"))
        self.label_7.setText(_translate("ui_subwidget_histogram", "Y通道直方图"))
        self.label_9.setText(_translate("ui_subwidget_histogram", "R通道直方图"))
        self.label_8.setText(_translate("ui_subwidget_histogram", "G通道直方图"))
        self.label_6.setText(_translate("ui_subwidget_histogram", "B通道直方图"))
        self.groupBox_2.setTitle(_translate("ui_subwidget_histogram", "基于直方图的图像增强"))
        self.label_original_image.setText(_translate("ui_subwidget_histogram", "没有预览"))
        self.label_processed_image.setText(_translate("ui_subwidget_histogram", "没有预览"))
        self.label_10.setText(_translate("ui_subwidget_histogram", "原图"))
        self.label.setText(_translate("ui_subwidget_histogram", "处理后"))
        self.groupBox_3.setTitle(_translate("ui_subwidget_histogram", "处理模块"))
        self.pushButton_histogramEqualize.setText(_translate("ui_subwidget_histogram", "直方图均衡化"))
        self.pushButton_ok.setText(_translate("ui_subwidget_histogram", "确定更改"))
        self.pushButton_cancel.setText(_translate("ui_subwidget_histogram", "取消"))
