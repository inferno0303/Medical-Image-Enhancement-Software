import numpy as np
import cv2
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal, pyqtSlot

from src.ui.ui_hist_widget_2 import Ui_HistWidget


class HistWidget(QWidget):
    """
    直方图模块逻辑
    """

    # 自定义信号，保存图像
    send_after_image = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # 初始化UI
        self.ui = Ui_HistWidget()
        self.ui.setupUi(self)

        # 连接信号与槽
        self.ui.start_process_btn.clicked.connect(lambda: self.hist_equ(image=self.image))
        self.ui.lighter_btn.clicked.connect(self.on_default_set_lower_and_upper_value)
        self.ui.darker_btn.clicked.connect(self.on_default_set_lower_and_upper_value)
        self.ui.high_contrast_btn.clicked.connect(self.on_default_set_lower_and_upper_value)
        self.ui.low_contrast_btn.clicked.connect(self.on_default_set_lower_and_upper_value)
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

    def on_default_set_lower_and_upper_value(self):
        """
        点击预设按钮后，设置上限亮度和下限亮度值的槽函数
        """
        # 获取发送信号的按钮
        sender_button = self.sender()
        if sender_button == self.ui.lighter_btn:
            self.ui.brightness_lower_limit.setValue(70)
            self.ui.brightness_upper_limit.setValue(255)
        elif sender_button == self.ui.darker_btn:
            self.ui.brightness_lower_limit.setValue(0)
            self.ui.brightness_upper_limit.setValue(180)
        elif sender_button == self.ui.high_contrast_btn:
            self.ui.brightness_lower_limit.setValue(0)
            self.ui.brightness_upper_limit.setValue(255)
        elif sender_button == self.ui.low_contrast_btn:
            self.ui.brightness_lower_limit.setValue(70)
            self.ui.brightness_upper_limit.setValue(180)
        self.hist_equ(image=self.image)

    def calc_hist(self, image):
        """
        计算直方图：只计算Y通道的直方图（灰度直方图），返回一个QImage
        """
        # 计算图像信息
        result = self._calc_image_info(image=image)
        channel = result.get("channel")

        if channel == 3:
            # 将BGR转换为灰度图
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        elif channel == 1:
            gray_image = image.copy()

        else:
            return -1

        # 计算直方统计图
        hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

        # 将直方统计图归一化到0~255
        cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)

        # 绘制灰度直方图
        hist_image = np.zeros((256, 256, 3), dtype=np.uint8)
        index = 0
        for value in hist:
            cv2.line(hist_image, (index, 256), (index, 256 - int(value)), (255, 255, 0), 1)
            index += 1

        return QImage(hist_image, 256, 256, QImage.Format.Format_RGB888)

    def hist_equ(self, image):
        """
        直方图均衡化处理
        """
        # 计算图像信息
        result = self._calc_image_info(image=image)
        channel = result.get("channel")

        if channel == 3:

            # 将 BGR 转换为 YUV 通道
            image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

            # 分离 YUV 通道
            [y, u, v] = cv2.split(image_yuv)

            # 对Y通道进行线性均衡
            lower = self.ui.brightness_lower_limit.value()
            upper = self.ui.brightness_upper_limit.value()
            y = cv2.normalize(y, None, lower, upper, cv2.NORM_MINMAX)

            # 合并 YUV 通道
            after_yuv_image = cv2.merge([y, u, v])

            # 转换回 BGR 通道
            after_image = cv2.cvtColor(after_yuv_image, cv2.COLOR_YUV2BGR)

        elif channel == 1:

            # 对灰度图进行线性均衡
            lower = self.ui.brightness_lower_limit.value()
            upper = self.ui.brightness_upper_limit.value()
            after_image = cv2.normalize(image, None, lower, upper, cv2.NORM_MINMAX)

        else:
            return -1

        # 保存处理后的图像到类成员对象
        self.after_image = after_image

        # 显示处理后的图像到UI，并把QImage放到类成员对象，以实现实时缩放
        self.after_image_qimage = self._display_image_to_label(image=after_image, label=self.ui.after_process_image_label)

        # 计算处理后的图像的直方图
        after_hist_qimage = self.calc_hist(image=after_image)

        # 显示处理后的灰度直方图到UI
        self.ui.after_process_hist_label.setPixmap(QPixmap.fromImage(after_hist_qimage))

    def ok(self):
        if self.after_image is not None:
            self.send_after_image.emit(self.after_image)
            self.close()
        else:
            QMessageBox.warning(self, '警告', '您未进行直方图均衡化处理。', QMessageBox.StandardButton.Ok)

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
                self.ui.after_process_image_label.setPixmap(QPixmap.fromImage(self.after_image_qimage.scaledToWidth(label_width)))
            else:
                self.ui.after_process_image_label.setPixmap(QPixmap.fromImage(self.after_image_qimage.scaledToHeight(label_height)))

    @pyqtSlot('QShowEvent')
    def showEvent(self, event):

        # 在窗口显示时执行的逻辑代码
        if self.image is not None:

            # 显示处理前的图像，并把QImage放到类成员对象，以实现实时缩放
            self.qimage = self._display_image_to_label(image=self.image, label=self.ui.original_image_label)

            # 计算直方图统计
            _qimage = self.calc_hist(image=self.image)

            # 将灰度直方图显示到UI
            self.ui.hist_label.setPixmap(QPixmap.fromImage(_qimage))

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
        self.ui.hist_label.setText("直方图统计")
        self.ui.after_process_hist_label.setText("处理后直方图统计")
