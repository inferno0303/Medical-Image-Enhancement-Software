# Form implementation generated from reading ui file '.\src\ui\ui_subwidget_conv.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        Form.setMinimumSize(QtCore.QSize(1024, 600))
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_original_image = QtWidgets.QLabel(parent=self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_original_image.sizePolicy().hasHeightForWidth())
        self.label_original_image.setSizePolicy(sizePolicy)
        self.label_original_image.setMinimumSize(QtCore.QSize(0, 0))
        self.label_original_image.setText("")
        self.label_original_image.setObjectName("label_original_image")
        self.verticalLayout_5.addWidget(self.label_original_image)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_after_image = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_after_image.setObjectName("groupBox_after_image")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_after_image)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_after_image = QtWidgets.QLabel(parent=self.groupBox_after_image)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_after_image.sizePolicy().hasHeightForWidth())
        self.label_after_image.setSizePolicy(sizePolicy)
        self.label_after_image.setText("")
        self.label_after_image.setObjectName("label_after_image")
        self.verticalLayout_6.addWidget(self.label_after_image)
        self.horizontalLayout_4.addWidget(self.groupBox_after_image)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.groupBox_99 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_99.setObjectName("groupBox_99")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_99)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(parent=self.groupBox_99)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_selector = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_selector.setObjectName("comboBox_selector")
        self.comboBox_selector.addItem("")
        self.comboBox_selector.addItem("")
        self.comboBox_selector.addItem("")
        self.verticalLayout.addWidget(self.comboBox_selector)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.groupBox_sobel_filter = QtWidgets.QGroupBox(parent=self.groupBox_99)
        self.groupBox_sobel_filter.setEnabled(False)
        self.groupBox_sobel_filter.setObjectName("groupBox_sobel_filter")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_sobel_filter)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_sobel_dx = QtWidgets.QRadioButton(parent=self.groupBox_sobel_filter)
        self.radioButton_sobel_dx.setChecked(True)
        self.radioButton_sobel_dx.setObjectName("radioButton_sobel_dx")
        self.verticalLayout_4.addWidget(self.radioButton_sobel_dx)
        self.radioButton_sobel_dy = QtWidgets.QRadioButton(parent=self.groupBox_sobel_filter)
        self.radioButton_sobel_dy.setObjectName("radioButton_sobel_dy")
        self.verticalLayout_4.addWidget(self.radioButton_sobel_dy)
        self.radioButton_sobel_dx_dy = QtWidgets.QRadioButton(parent=self.groupBox_sobel_filter)
        self.radioButton_sobel_dx_dy.setObjectName("radioButton_sobel_dx_dy")
        self.verticalLayout_4.addWidget(self.radioButton_sobel_dx_dy)
        self.pushButton_sobel_filter = QtWidgets.QPushButton(parent=self.groupBox_sobel_filter)
        self.pushButton_sobel_filter.setObjectName("pushButton_sobel_filter")
        self.verticalLayout_4.addWidget(self.pushButton_sobel_filter)
        self.horizontalLayout_5.addWidget(self.groupBox_sobel_filter)
        self.groupBox_laplace_filter = QtWidgets.QGroupBox(parent=self.groupBox_99)
        self.groupBox_laplace_filter.setEnabled(False)
        self.groupBox_laplace_filter.setObjectName("groupBox_laplace_filter")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_laplace_filter)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_title_9 = QtWidgets.QLabel(parent=self.groupBox_laplace_filter)
        self.label_title_9.setObjectName("label_title_9")
        self.verticalLayout_3.addWidget(self.label_title_9)
        self.spinBox_laplace_ksize = QtWidgets.QSpinBox(parent=self.groupBox_laplace_filter)
        self.spinBox_laplace_ksize.setMinimum(1)
        self.spinBox_laplace_ksize.setMaximum(19)
        self.spinBox_laplace_ksize.setSingleStep(2)
        self.spinBox_laplace_ksize.setProperty("value", 3)
        self.spinBox_laplace_ksize.setObjectName("spinBox_laplace_ksize")
        self.verticalLayout_3.addWidget(self.spinBox_laplace_ksize)
        self.pushButton_laplace_filter = QtWidgets.QPushButton(parent=self.groupBox_laplace_filter)
        self.pushButton_laplace_filter.setObjectName("pushButton_laplace_filter")
        self.verticalLayout_3.addWidget(self.pushButton_laplace_filter)
        self.horizontalLayout_5.addWidget(self.groupBox_laplace_filter)
        self.groupBox_custom_filter = QtWidgets.QGroupBox(parent=self.groupBox_99)
        self.groupBox_custom_filter.setEnabled(False)
        self.groupBox_custom_filter.setObjectName("groupBox_custom_filter")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_custom_filter)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_custom_filter_6 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_6.setDecimals(1)
        self.doubleSpinBox_custom_filter_6.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_6.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_6.setProperty("value", -1.0)
        self.doubleSpinBox_custom_filter_6.setObjectName("doubleSpinBox_custom_filter_6")
        self.gridLayout.addWidget(self.doubleSpinBox_custom_filter_6, 1, 2, 1, 1)
        self.doubleSpinBox_custom_filter_3 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_3.setDecimals(1)
        self.doubleSpinBox_custom_filter_3.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_3.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_3.setObjectName("doubleSpinBox_custom_filter_3")
        self.gridLayout.addWidget(self.doubleSpinBox_custom_filter_3, 0, 2, 1, 1)
        self.doubleSpinBox_custom_filter_7 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_7.setDecimals(1)
        self.doubleSpinBox_custom_filter_7.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_7.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_7.setObjectName("doubleSpinBox_custom_filter_7")
        self.gridLayout.addWidget(self.doubleSpinBox_custom_filter_7, 2, 0, 1, 1)
        self.doubleSpinBox_custom_filter_2 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_2.setDecimals(1)
        self.doubleSpinBox_custom_filter_2.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_2.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_2.setProperty("value", -1.0)
        self.doubleSpinBox_custom_filter_2.setObjectName("doubleSpinBox_custom_filter_2")
        self.gridLayout.addWidget(self.doubleSpinBox_custom_filter_2, 0, 1, 1, 1)
        self.doubleSpinBox_custom_filter_8 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_8.setDecimals(1)
        self.doubleSpinBox_custom_filter_8.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_8.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_8.setProperty("value", -1.0)
        self.doubleSpinBox_custom_filter_8.setObjectName("doubleSpinBox_custom_filter_8")
        self.gridLayout.addWidget(self.doubleSpinBox_custom_filter_8, 2, 1, 1, 1)
        self.doubleSpinBox_custom_filter_9 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_9.setDecimals(1)
        self.doubleSpinBox_custom_filter_9.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_9.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_9.setObjectName("doubleSpinBox_custom_filter_9")
        self.gridLayout.addWidget(self.doubleSpinBox_custom_filter_9, 2, 2, 1, 1)
        self.doubleSpinBox_custom_filter_1 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_1.setDecimals(1)
        self.doubleSpinBox_custom_filter_1.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_1.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_1.setObjectName("doubleSpinBox_custom_filter_1")
        self.gridLayout.addWidget(self.doubleSpinBox_custom_filter_1, 0, 0, 1, 1)
        self.doubleSpinBox_custom_filter_5 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_5.setDecimals(1)
        self.doubleSpinBox_custom_filter_5.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_5.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_5.setProperty("value", 5.0)
        self.doubleSpinBox_custom_filter_5.setObjectName("doubleSpinBox_custom_filter_5")
        self.gridLayout.addWidget(self.doubleSpinBox_custom_filter_5, 1, 1, 1, 1)
        self.doubleSpinBox_custom_filter_4 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_4.setDecimals(1)
        self.doubleSpinBox_custom_filter_4.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_4.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_4.setProperty("value", -1.0)
        self.doubleSpinBox_custom_filter_4.setObjectName("doubleSpinBox_custom_filter_4")
        self.gridLayout.addWidget(self.doubleSpinBox_custom_filter_4, 1, 0, 1, 1)
        self.pushButton_custom_filter = QtWidgets.QPushButton(parent=self.groupBox_custom_filter)
        self.pushButton_custom_filter.setObjectName("pushButton_custom_filter")
        self.gridLayout.addWidget(self.pushButton_custom_filter, 3, 0, 1, 3)
        self.horizontalLayout_5.addWidget(self.groupBox_custom_filter)
        self.groupBox_ok_cancel = QtWidgets.QGroupBox(parent=self.groupBox_99)
        self.groupBox_ok_cancel.setObjectName("groupBox_ok_cancel")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_ok_cancel)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_ok = QtWidgets.QPushButton(parent=self.groupBox_ok_cancel)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(parent=self.groupBox_ok_cancel)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.horizontalLayout_5.addWidget(self.groupBox_ok_cancel)
        self.verticalLayout_7.addWidget(self.groupBox_99)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "锐化和卷积处理模块"))
        self.groupBox_4.setTitle(_translate("Form", "原图"))
        self.groupBox_after_image.setTitle(_translate("Form", "处理后"))
        self.groupBox_99.setTitle(_translate("Form", "功能控制区"))
        self.groupBox.setTitle(_translate("Form", "选择锐化类型"))
        self.comboBox_selector.setItemText(0, _translate("Form", "Sobel算子锐化"))
        self.comboBox_selector.setItemText(1, _translate("Form", "Laplace算子锐化"))
        self.comboBox_selector.setItemText(2, _translate("Form", "自定义卷积核"))
        self.groupBox_sobel_filter.setTitle(_translate("Form", "Sobel算子锐化"))
        self.radioButton_sobel_dx.setText(_translate("Form", "X方向梯度"))
        self.radioButton_sobel_dy.setText(_translate("Form", "Y方向梯度"))
        self.radioButton_sobel_dx_dy.setText(_translate("Form", "X和Y方向梯度"))
        self.pushButton_sobel_filter.setText(_translate("Form", "确定"))
        self.groupBox_laplace_filter.setTitle(_translate("Form", "Laplace算子锐化"))
        self.label_title_9.setText(_translate("Form", "核大小："))
        self.pushButton_laplace_filter.setText(_translate("Form", "确定"))
        self.groupBox_custom_filter.setTitle(_translate("Form", "自定义3*3卷积核"))
        self.pushButton_custom_filter.setText(_translate("Form", "确定"))
        self.groupBox_ok_cancel.setTitle(_translate("Form", "确定更改"))
        self.pushButton_ok.setText(_translate("Form", "确定"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
