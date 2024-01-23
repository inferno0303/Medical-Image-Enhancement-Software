# Form implementation generated from reading ui file '.\src\ui\ui_evaluation_widget.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EvaluationWidget(object):
    def setupUi(self, EvaluationWidget):
        EvaluationWidget.setObjectName("EvaluationWidget")
        EvaluationWidget.resize(800, 600)
        EvaluationWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EvaluationWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_title = QtWidgets.QLabel(parent=EvaluationWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.widget_title.setFont(font)
        self.widget_title.setObjectName("widget_title")
        self.verticalLayout_2.addWidget(self.widget_title)
        self.frame = QtWidgets.QFrame(parent=EvaluationWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.original_image_label = QtWidgets.QLabel(parent=self.frame)
        self.original_image_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.original_image_label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.original_image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.original_image_label.setObjectName("original_image_label")
        self.horizontalLayout_2.addWidget(self.original_image_label)
        self.after_process_image_label = QtWidgets.QLabel(parent=self.frame)
        self.after_process_image_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.after_process_image_label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.after_process_image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.after_process_image_label.setObjectName("after_process_image_label")
        self.horizontalLayout_2.addWidget(self.after_process_image_label)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=EvaluationWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MSE_radio = QtWidgets.QRadioButton(parent=self.groupBox)
        self.MSE_radio.setChecked(False)
        self.MSE_radio.setObjectName("MSE_radio")
        self.buttonGroup = QtWidgets.QButtonGroup(EvaluationWidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.MSE_radio)
        self.verticalLayout.addWidget(self.MSE_radio)
        self.PSNR_radio = QtWidgets.QRadioButton(parent=self.groupBox)
        self.PSNR_radio.setChecked(True)
        self.PSNR_radio.setObjectName("PSNR_radio")
        self.buttonGroup.addButton(self.PSNR_radio)
        self.verticalLayout.addWidget(self.PSNR_radio)
        self.horizontalLayout.addWidget(self.groupBox)
        self.evaluation_result_label = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        self.evaluation_result_label.setFont(font)
        self.evaluation_result_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.evaluation_result_label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.evaluation_result_label.setLineWidth(1)
        self.evaluation_result_label.setMidLineWidth(0)
        self.evaluation_result_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.evaluation_result_label.setObjectName("evaluation_result_label")
        self.horizontalLayout.addWidget(self.evaluation_result_label)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(EvaluationWidget)
        QtCore.QMetaObject.connectSlotsByName(EvaluationWidget)

    def retranslateUi(self, EvaluationWidget):
        _translate = QtCore.QCoreApplication.translate
        EvaluationWidget.setWindowTitle(_translate("EvaluationWidget", "图像评估模块"))
        self.widget_title.setText(_translate("EvaluationWidget", "图像评估模块"))
        self.original_image_label.setText(_translate("EvaluationWidget", "原图"))
        self.after_process_image_label.setText(_translate("EvaluationWidget", "处理后"))
        self.groupBox.setTitle(_translate("EvaluationWidget", "选择评估方式"))
        self.MSE_radio.setText(_translate("EvaluationWidget", "均方根（MSE）"))
        self.PSNR_radio.setText(_translate("EvaluationWidget", "峰值信噪比（PSNR）"))
        self.evaluation_result_label.setText(_translate("EvaluationWidget", "评估结果"))
