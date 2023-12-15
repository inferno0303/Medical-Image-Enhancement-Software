import numpy as np
import cv2
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget
from src.ui.ui_subwidget_conv import Ui_Form


class WidgetConv(QWidget):
    """
    锐化和卷积模块
    """

    def __init__(self, image):
        # 该类继承于QWidget，实现窗口元素绘制
        super().__init__()

        # 当前组件的state
        self.height, self.width, self.channels = image.shape
        if self.channels == 3:
            self.original_image_rgb = image.copy()
            self.original_image_gray = cv2.cvtColor(self.original_image_rgb, cv2.COLOR_RGB2GRAY)
        elif self.channels == 1:
            self.original_image_gray = image.copy()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui_init()

    def ui_init(self):
        """
        连接信号与槽
        """
        self.ui.comboBox_selector.currentIndexChanged.connect(self.on_combobox_changed)
        self.on_combobox_changed()

        # 显示原图
        if self.channels == 3:
            _q_image = QImage(self.original_image_rgb, self.width, self.height, QImage.Format.Format_RGB888)
        elif self.channels == 1:
            _q_image = QImage(self.original_image_gray, self.width, self.height, QImage.Format.Format_Grayscale8)
        else:
            return -1

        print(self.ui.label_original_image.width(), self.ui.label_original_image.height())

        if self.ui.label_original_image.size().width() > self.ui.label_original_image.size().height():
            _q_image = _q_image.scaledToHeight(400)
        else:
            _q_image = _q_image.scaledToWidth(400)

        self.ui.label_original_image.setPixmap(QPixmap.fromImage(_q_image))

    def on_combobox_changed(self):
        """
        通过当前索引获取当前选中项的文本值和索引
        根据当前选中项的文本值和索引更改 Enable 状态
        """
        if self.ui.comboBox_selector.currentIndex() == 0:
            self.ui.groupBox_sobel_filter.setEnabled(True)
            self.ui.groupBox_laplace_filter.setEnabled(False)
            self.ui.groupBox_custom_filter.setEnabled(False)
        elif self.ui.comboBox_selector.currentIndex() == 1:
            self.ui.groupBox_sobel_filter.setEnabled(False)
            self.ui.groupBox_laplace_filter.setEnabled(True)
            self.ui.groupBox_custom_filter.setEnabled(False)
        elif self.ui.comboBox_selector.currentIndex() == 2:
            self.ui.groupBox_sobel_filter.setEnabled(False)
            self.ui.groupBox_laplace_filter.setEnabled(False)
            self.ui.groupBox_custom_filter.setEnabled(True)
