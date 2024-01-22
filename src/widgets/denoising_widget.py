import numpy as np
import cv2
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal, pyqtSlot

from src.ui.ui_denoising_widget import Ui_DenoisingWidget


class DenoisingWidget(QWidget):
    """
    图像去噪模块逻辑
    """

    # 自定义信号，保存图像
    send_after_image = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # 初始化UI
        self.ui = Ui_DenoisingWidget()
        self.ui.setupUi(self)

        # 连接信号与槽
        self.ui.buttonGroup.buttonToggled.connect(self.on_select_mode)
        # self.ui.darker_btn.clicked.connect(self.on_custom_conv_default_set)
        # self.ui.lighter_btn.clicked.connect(self.on_custom_conv_default_set)
        # self.ui.sharpen_btn.clicked.connect(self.on_custom_conv_default_set)
        # self.ui.sobel_conv_btn.clicked.connect(lambda: self.sobel_conv(image=self.image))
        # self.ui.laplace_conv_btn.clicked.connect(lambda: self.laplace_conv(image=self.image))
        # self.ui.custom_conv_btn.clicked.connect(lambda: self.custom_conv(image=self.image))
        self.ui.ok_btn.clicked.connect(self.ok)

        # 当前组件状态
        self.image = None
        self.qimage = None
        self.after_image = None
        self.after_image_qimage = None

    def set_image(self, image):
        """
        设置图像到类成员对象中
        """
        # 计算图像信息
        result = self._calc_image_info(image=image)
        depth = result.get("depth")

        # 对非uint8动态范围的图像，归一化到uint8动态范围
        if depth != 'uint8':
            # 线性归一化到8位动态范围
            image = ((image - image.min()) / (image.max() - image.min()) * 255).astype('uint8')
        self.image = image

    def on_select_mode(self, button, checked):
        if button == self.ui.mean_filter_radio and checked is True:
            self.ui.mean_filter_groupBox.setEnabled(True)
            self.ui.gaussian_filter_groupBox.setEnabled(False)
            self.ui.median_filter_groupBox.setEnabled(False)
            self.ui.bilateral_filter_groupBox.setEnabled(False)
        elif button == self.ui.gaussian_filter_radio and checked is True:
            self.ui.mean_filter_groupBox.setEnabled(False)
            self.ui.gaussian_filter_groupBox.setEnabled(True)
            self.ui.median_filter_groupBox.setEnabled(False)
            self.ui.bilateral_filter_groupBox.setEnabled(False)
        elif button == self.ui.median_filter_radio and checked is True:
            self.ui.mean_filter_groupBox.setEnabled(False)
            self.ui.gaussian_filter_groupBox.setEnabled(False)
            self.ui.median_filter_groupBox.setEnabled(True)
            self.ui.bilateral_filter_groupBox.setEnabled(False)
        elif button == self.ui.bilateral_filter_radio and checked is True:
            self.ui.mean_filter_groupBox.setEnabled(False)
            self.ui.gaussian_filter_groupBox.setEnabled(False)
            self.ui.median_filter_groupBox.setEnabled(False)
            self.ui.bilateral_filter_groupBox.setEnabled(True)

    def ok(self):
        if self.after_image is not None:
            self.send_after_image.emit(self.after_image)
            self.close()
        else:
            QMessageBox.warning(self, '警告', '您未对图像进行处理。', QMessageBox.StandardButton.Ok)

    @staticmethod
    def _calc_image_info(image):
        """
        计算图像信息
        """
        height = image.shape[0]
        width = image.shape[1]
        channel = None
        if image.ndim == 2:
            channel = 1
        elif image.ndim == 3:
            channel = 3
        depth = image.dtype
        return {"height": height, "width": width, "channel": channel, "depth": depth}

    def _display_image_to_label(self, image, label):
        """
        显示图像到UI
        """
        # 计算图像信息
        result = self._calc_image_info(image=image)
        height = result.get("height")
        width = result.get("width")
        channel = result.get("channel")

        # 转换为QImage类型
        _qimage = None
        if channel == 3:
            _qimage = QImage(image, width, height, QImage.Format.Format_BGR888)
        elif channel == 1:
            _qimage = QImage(image, width, height, QImage.Format.Format_Grayscale8)

        if _qimage:
            # 将图像按label的短边拉伸，以填满label
            if label.width() < label.height():
                label.setPixmap(QPixmap.fromImage(_qimage.scaledToWidth(label.width())))
            else:
                label.setPixmap(QPixmap.fromImage(_qimage.scaledToHeight(label.height())))

            return _qimage

    @pyqtSlot('QResizeEvent')
    def resizeEvent(self, event):
        """
        重载resizeEvent槽函数，监听窗口size变化事件，实现伸缩窗口时能重新缩放到label
        """

        if self.qimage:
            # 将图像按label的短边拉伸，以填满label
            label_width = self.ui.original_image_label.width()
            label_height = self.ui.original_image_label.height()
            if label_width < label_height:
                self.ui.original_image_label.setPixmap(QPixmap.fromImage(self.qimage.scaledToWidth(label_width)))
            else:
                self.ui.original_image_label.setPixmap(QPixmap.fromImage(self.qimage.scaledToHeight(label_height)))

        if self.after_image_qimage:
            # 将图像按label的短边拉伸，以填满label
            label_width = self.ui.after_process_image_label.width()
            label_height = self.ui.after_process_image_label.height()
            if label_width < label_height:
                self.ui.after_process_image_label.setPixmap(
                    QPixmap.fromImage(self.after_image_qimage.scaledToWidth(label_width)))
            else:
                self.ui.after_process_image_label.setPixmap(
                    QPixmap.fromImage(self.after_image_qimage.scaledToHeight(label_height)))

    @pyqtSlot('QShowEvent')
    def showEvent(self, event):

        # 在窗口显示时执行的逻辑代码
        if self.image is not None:
            # 显示处理前的图像，并把QImage放到类成员对象，以实现实时缩放
            self.qimage = self._display_image_to_label(image=self.image, label=self.ui.original_image_label)

        # 需要调用父类的 showEvent
        super().showEvent(event)

    def closeEvent(self, event):
        # 关闭前清理组件状态
        self.image = None
        self.qimage = None
        self.after_image = None
        self.after_image_qimage = None
        self.ui.original_image_label.setText("原图")
        self.ui.after_process_image_label.setText("处理后")
