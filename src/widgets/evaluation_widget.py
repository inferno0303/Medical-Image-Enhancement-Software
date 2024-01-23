import math

import numpy as np
import cv2
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal, pyqtSlot

from src.ui.ui_evaluation_widget import Ui_EvaluationWidget


class EvaluationWidget(QWidget):
    """
    图像评估模块逻辑
    """

    def __init__(self):
        super().__init__()

        # 初始化UI
        self.ui = Ui_EvaluationWidget()
        self.ui.setupUi(self)

        # 连接信号与槽
        self.ui.buttonGroup.buttonToggled.connect(self.on_select_mode)

        # 当前组件状态
        self.original_image = None
        self.original_image_qimage = None
        self.distorted_image = None
        self.distorted_image_qimage = None

    def set_original_image(self, image):
        """
        设置原图到类成员变量中
        """
        # 计算图像信息
        result = self._calc_image_info(image=image)
        depth = result.get("depth")

        # 对非uint8动态范围的图像，归一化到uint8动态范围
        if depth != 'uint8':
            # 线性归一化到8位动态范围
            image = ((image - image.min()) / (image.max() - image.min()) * 255).astype('uint8')
        self.original_image = image

    def set_distorted_image(self, image):
        """
        设置处理后的图像到类成员变量中
        """
        # 计算图像信息
        result = self._calc_image_info(image=image)
        depth = result.get("depth")

        # 对非uint8动态范围的图像，归一化到uint8动态范围
        if depth != 'uint8':
            # 线性归一化到8位动态范围
            image = ((image - image.min()) / (image.max() - image.min()) * 255).astype('uint8')
        self.distorted_image = image

    def on_select_mode(self, button, checked):
        """
        选择评估算法
        """
        if self.original_image is not None and self.distorted_image is not None:
            # MSE
            if button == self.ui.MSE_radio and checked is True:
                self.on_MSE(original_image=self.original_image, distorted_image=self.distorted_image)

            # PSNR
            elif button == self.ui.PSNR_radio and checked is True:
                self.on_PSNR(original_image=self.original_image, distorted_image=self.distorted_image)

    def on_MSE(self, original_image, distorted_image):
        """
        计算两幅图像之间的均方误差（MSE）
        """
        # 将图像转换为浮点数
        original_image = original_image.astype(np.float32)
        distorted_image = distorted_image.astype(np.float32)

        # 计算均方误差 (MSE)
        mse = np.mean((original_image - distorted_image) ** 2)
        mse = format(mse, ".2f")
        self.ui.evaluation_result_label.setText(f"均方误差（MSE）：{mse}")

    def on_PSNR(self, original_image, distorted_image):
        """
        计算两幅图像之间的峰值信噪比（PSNR）
        """
        # 将图像转换为浮点数
        original_image = original_image.astype(np.float32)
        distorted_image = distorted_image.astype(np.float32)

        # 计算 PSNR
        psnr_value = cv2.PSNR(original_image, distorted_image)
        psnr_value = format(psnr_value, ".2f")
        self.ui.evaluation_result_label.setText(f"峰值信噪比（PSNR）：{psnr_value} dB")

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

        if self.original_image_qimage:
            # 将图像按label的短边拉伸，以填满label
            label_width = self.ui.original_image_label.width()
            label_height = self.ui.original_image_label.height()
            if label_width < label_height:
                self.ui.original_image_label.setPixmap(QPixmap.fromImage(
                    self.original_image_qimage.scaledToWidth(label_width)))
            else:
                self.ui.original_image_label.setPixmap(QPixmap.fromImage(
                    self.original_image_qimage.scaledToHeight(label_height)))

        if self.distorted_image_qimage:
            # 将图像按label的短边拉伸，以填满label
            label_width = self.ui.after_process_image_label.width()
            label_height = self.ui.after_process_image_label.height()
            if label_width < label_height:
                self.ui.after_process_image_label.setPixmap(QPixmap.fromImage(
                    self.distorted_image_qimage.scaledToWidth(label_width)))
            else:
                self.ui.after_process_image_label.setPixmap(QPixmap.fromImage(
                    self.distorted_image_qimage.scaledToHeight(label_height)))

    @pyqtSlot('QShowEvent')
    def showEvent(self, event):

        # 在窗口显示时执行的逻辑代码
        if self.original_image is not None and self.distorted_image is not None:
            # 显示原图
            self.original_image_qimage = self._display_image_to_label(image=self.original_image,
                                                                      label=self.ui.original_image_label)
            # 显示处理后的图像
            self.distorted_image_qimage = self._display_image_to_label(image=self.distorted_image,
                                                                       label=self.ui.after_process_image_label)
            # 计算PSNR
            self.on_PSNR(original_image=self.original_image, distorted_image=self.distorted_image)

        # 需要调用父类的 showEvent
        super().showEvent(event)

    def closeEvent(self, event):
        # 关闭前清理组件状态
        self.original_image = None
        self.original_image_qimage = None
        self.distorted_image = None
        self.distorted_image_qimage = None
        self.ui.original_image_label.setText("原图")
        self.ui.after_process_image_label.setText("处理后")
        self.ui.evaluation_result_label.setText("评估结果")
