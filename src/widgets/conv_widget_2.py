import numpy as np
import cv2
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal, pyqtSlot

from src.ui.ui_conv_widget_2 import Ui_ConvWidget


class ConvWidget(QWidget):
    """
    卷积与滤波模块逻辑
    """

    # 自定义信号，保存图像
    send_after_image = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # 初始化UI
        self.ui = Ui_ConvWidget()
        self.ui.setupUi(self)

        # 连接信号与槽
        self.ui.buttonGroup.buttonToggled.connect(self.on_select_mode)
        self.ui.darker_btn.clicked.connect(self.on_custom_conv_default_set)
        self.ui.lighter_btn.clicked.connect(self.on_custom_conv_default_set)
        self.ui.sharpen_btn.clicked.connect(self.on_custom_conv_default_set)
        self.ui.sobel_conv_btn.clicked.connect(lambda: self.sobel_conv(image=self.image))
        self.ui.laplace_conv_btn.clicked.connect(lambda: self.laplace_conv(image=self.image))
        self.ui.custom_conv_btn.clicked.connect(lambda: self.custom_conv(image=self.image))
        self.ui.ok_btn.clicked.connect(self.ok)

        # 当前组件状态
        self.image = None
        self.qimage = None
        self.after_image = None
        self.after_image_qimage = None

    def set_image(self, image):
        """
        设置图像到类成员变量中
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
        if button == self.ui.custom_conv_radio and checked is True:
            self.ui.custom_conv_groupBox.setEnabled(True)
            self.ui.sobel_conv_groupBox.setEnabled(False)
            self.ui.laplace_conv_groupBox.setEnabled(False)
        elif button == self.ui.sobel_conv_radio and checked is True:
            self.ui.custom_conv_groupBox.setEnabled(False)
            self.ui.sobel_conv_groupBox.setEnabled(True)
            self.ui.laplace_conv_groupBox.setEnabled(False)
        elif button == self.ui.laplace_conv_radio and checked is True:
            self.ui.custom_conv_groupBox.setEnabled(False)
            self.ui.sobel_conv_groupBox.setEnabled(False)
            self.ui.laplace_conv_groupBox.setEnabled(True)

    def on_custom_conv_default_set(self):
        """
        点击自定义卷积预设按钮后，设置卷积核
        """
        # 获取发送信号的按钮
        sender_button = self.sender()
        if sender_button == self.ui.lighter_btn:
            self.ui.costom_conv_1_param.setValue(0.1)
            self.ui.costom_conv_2_param.setValue(0.1)
            self.ui.costom_conv_3_param.setValue(0.1)
            self.ui.costom_conv_4_param.setValue(0.1)
            self.ui.costom_conv_5_param.setValue(0.6)
            self.ui.costom_conv_6_param.setValue(0.1)
            self.ui.costom_conv_7_param.setValue(0.1)
            self.ui.costom_conv_8_param.setValue(0.1)
            self.ui.costom_conv_9_param.setValue(0.1)
        elif sender_button == self.ui.darker_btn:
            self.ui.costom_conv_1_param.setValue(-0.1)
            self.ui.costom_conv_2_param.setValue(-0.1)
            self.ui.costom_conv_3_param.setValue(-0.1)
            self.ui.costom_conv_4_param.setValue(-0.1)
            self.ui.costom_conv_5_param.setValue(1.5)
            self.ui.costom_conv_6_param.setValue(-0.1)
            self.ui.costom_conv_7_param.setValue(-0.1)
            self.ui.costom_conv_8_param.setValue(-0.1)
            self.ui.costom_conv_9_param.setValue(-0.1)
        elif sender_button == self.ui.sharpen_btn:
            self.ui.costom_conv_1_param.setValue(0.0)
            self.ui.costom_conv_2_param.setValue(-1.0)
            self.ui.costom_conv_3_param.setValue(0.0)
            self.ui.costom_conv_4_param.setValue(-1.0)
            self.ui.costom_conv_5_param.setValue(5.0)
            self.ui.costom_conv_6_param.setValue(-1.0)
            self.ui.costom_conv_7_param.setValue(0.0)
            self.ui.costom_conv_8_param.setValue(-1.0)
            self.ui.costom_conv_9_param.setValue(0.0)
        self.custom_conv(image=self.image)

    def custom_conv(self, image):
        """
        自定义卷积计算
        """
        # 从UI获取卷积核
        kernel = np.array(
            [[self.ui.costom_conv_1_param.value(),
              self.ui.costom_conv_2_param.value(),
              self.ui.costom_conv_3_param.value()],
             [self.ui.costom_conv_4_param.value(),
              self.ui.costom_conv_5_param.value(),
              self.ui.costom_conv_6_param.value()],
             [self.ui.costom_conv_7_param.value(),
              self.ui.costom_conv_8_param.value(),
              self.ui.costom_conv_9_param.value()]],
            np.float32)

        # 计算图像信息
        result = self._calc_image_info(image=image)
        channel = result.get("channel")

        if channel == 3:

            # 将 BGR 转换为 YUV 通道
            image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

            # 分离 YUV 通道
            [y, u, v] = cv2.split(image_yuv)

            # 对Y通道进行卷积
            y = cv2.filter2D(src=y, ddepth=-1, kernel=kernel)

            # 合并 YUV 通道
            after_yuv_image = cv2.merge([y, u, v])

            # 转换回 BGR 通道
            after_image = cv2.cvtColor(after_yuv_image, cv2.COLOR_YUV2BGR)

        elif channel == 1:
            after_image = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
        else:
            return -1

        # 保存处理后的图像，以实现将处理后的图像发送回主窗口
        self.after_image = after_image

        # 显示到UI，并将QImage缓存，以实现随视口大小变化而缩放
        self.after_image_qimage = self._display_image_to_label(image=after_image,
                                                               label=self.ui.after_process_image_label)

    def sobel_conv(self, image):
        """
        Sobel卷积计算
        """
        if self.ui.sobel_dx_radio.isChecked():
            after_image = cv2.Sobel(image, ddepth=-1, scale=1, dx=1, dy=0)
        elif self.ui.sobel_dy_radio.isChecked():
            after_image = cv2.Sobel(image, ddepth=-1, scale=1, dx=0, dy=1)
        elif self.ui.sobel_dx_dy_radio.isChecked():
            after_image = cv2.Sobel(image, ddepth=-1, scale=1, dx=1, dy=1)
        else:
            return -1

        # 保存处理后的图像，以实现将处理后的图像发送回主窗口
        self.after_image = after_image

        # 显示到UI，并将QImage缓存，以实现随视口大小变化而缩放
        self.after_image_qimage = self._display_image_to_label(image=after_image,
                                                               label=self.ui.after_process_image_label)

    def laplace_conv(self, image):
        """
        Laplace卷积计算
        """
        kernel_size = 3
        if self.ui.laplace_conv_3_radio.isChecked():
            kernel_size = 3
        elif self.ui.laplace_conv_5_radio.isChecked():
            kernel_size = 5
        elif self.ui.laplace_conv_7_radio.isChecked():
            kernel_size = 7
        after_image = cv2.Laplacian(image, ddepth=-1, scale=3, ksize=kernel_size)

        # 保存处理后的图像，以实现将处理后的图像发送回主窗口
        self.after_image = after_image

        # 显示到UI，并将QImage缓存，以实现随视口大小变化而缩放
        self.after_image_qimage = self._display_image_to_label(image=after_image,
                                                               label=self.ui.after_process_image_label)

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
            # 显示处理前的图像，并把QImage放到类成员变量，以实现实时缩放
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
