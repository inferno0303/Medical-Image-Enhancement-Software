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
        self.ui.pushButton_sobel_filter.clicked.connect(self.sobel_sharpen_filter)
        self.ui.pushButton_laplace_filter.clicked.connect(self.laplacian_sharpen_filter)
        self.ui.pushButton_custom_filter.clicked.connect(self.custom_filter)

        # 显示原图
        if self.channels == 3:
            _q_image = QImage(self.original_image_rgb, self.width, self.height, QImage.Format.Format_RGB888)
        elif self.channels == 1:
            _q_image = QImage(self.original_image_gray, self.width, self.height, QImage.Format.Format_Grayscale8)
        else:
            return -1

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

    # Sobel算子：是对图像进行梯度计算，在灰度图中计算
    def sobel_sharpen_filter(self):
        if self.ui.radioButton_sobel_dx.isChecked():
            after_image = cv2.Sobel(self.original_image_gray, ddepth=-1, scale=3, dx=1, dy=0)
        elif self.ui.radioButton_sobel_dy.isChecked():
            after_image = cv2.Sobel(self.original_image_gray, ddepth=-1, scale=3, dx=0, dy=1)
        elif self.ui.radioButton_sobel_dx_dy.isChecked():
            after_image = cv2.Sobel(self.original_image_gray, ddepth=-1, scale=3, dx=1, dy=1)
        else:
            return -1
        _q_image = QImage(after_image, self.width, self.height, QImage.Format.Format_Grayscale8)
        _q_image = _q_image.scaledToHeight(400)
        self.ui.label_after_image.setPixmap(QPixmap.fromImage(_q_image))
        self.ui.groupBox_after_image.setTitle("处理后：Sobel算子锐化预览")

    # Laplacian算子：对图像进行拉普拉斯算子卷积计算，在灰度图中进行
    def laplacian_sharpen_filter(self):
        after_image = cv2.Laplacian(self.original_image_gray, ddepth=-1, scale=3,
                                    ksize=int(self.ui.spinBox_laplace_ksize.value()))
        _q_image = QImage(after_image, self.width, self.height, QImage.Format.Format_Grayscale8)
        _q_image = _q_image.scaledToHeight(400)
        self.ui.label_after_image.setPixmap(QPixmap.fromImage(_q_image))
        self.ui.groupBox_after_image.setTitle("处理后：Laplacian算子锐化预览")

    def custom_filter(self):
        kernel = np.array(
            [[self.ui.doubleSpinBox_custom_filter_1.value(), self.ui.doubleSpinBox_custom_filter_2.value(),
              self.ui.doubleSpinBox_custom_filter_3.value()],
             [self.ui.doubleSpinBox_custom_filter_4.value(), self.ui.doubleSpinBox_custom_filter_5.value(),
              self.ui.doubleSpinBox_custom_filter_6.value()],
             [self.ui.doubleSpinBox_custom_filter_7.value(), self.ui.doubleSpinBox_custom_filter_8.value(),
              self.ui.doubleSpinBox_custom_filter_9.value()]], np.float32)
        if self.channels == 3:
            after_image = cv2.filter2D(src=self.original_image_rgb, ddepth=-1, kernel=kernel)
            _q_image = QImage(after_image, self.width, self.height, QImage.Format.Format_RGB888)
        else:
            after_image = cv2.filter2D(src=self.original_image_gray, ddepth=-1, kernel=kernel)
            _q_image = QImage(after_image, self.width, self.height, QImage.Format.Format_Grayscale8)
        _q_image = _q_image.scaledToHeight(400)
        self.ui.label_after_image.setPixmap(QPixmap.fromImage(_q_image))
        self.ui.groupBox_after_image.setTitle("处理后：自定义卷积效果预览")
