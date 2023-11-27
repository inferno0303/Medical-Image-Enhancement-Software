import numpy as np
import cv2
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget
from src.ui.ui_subwidget_histogram import Ui_ui_subwidget_histogram


class WidgetHistogram(QWidget):
    """
    直方图模块
    """
    def __init__(self, image):

        # 该类继承于QWidget，实现窗口元素绘制
        super().__init__()

        # 当前组件的state
        self.width = None
        self.height = None
        self.channels = None
        self.original_image_rgb = None
        self.original_image_gray = None
        self.histogram_y_channel = None
        self.histogram_r_channel = None
        self.histogram_g_channel = None
        self.histogram_b_channel = None
        self.histogram_y_image = None
        self.histogram_r_image = None
        self.histogram_g_image = None
        self.histogram_b_image = None

        self.ui = Ui_ui_subwidget_histogram()
        self.ui.setupUi(self)

        self.ui_init(image)

    def ui_init(self, image):

        self.height, self.width, self.channels = image.shape
        if self.channels == 3:
            self.original_image_rgb = image.copy()
            self.original_image_gray = cv2.cvtColor(self.original_image_rgb, cv2.COLOR_RGB2GRAY)
        elif self.channels == 1:
            self.original_image_gray = image.copy()
        else:
            return -1

        """
        显示原图
        """
        if self.channels == 3:
            _qimage = QImage(self.original_image_rgb, self.width, self.height, QImage.Format.Format_RGB888)
        elif self.channels == 1:
            _qimage = QImage(self.original_image_gray, self.width, self.height, QImage.Format.Format_Grayscale8)
        else:
            return -1
        if self.ui.label_original_image.width() > self.ui.label_original_image.height():
            _qimage = _qimage.scaledToHeight(self.ui.label_original_image.height())
        else:
            _qimage = _qimage.scaledToWidth(self.ui.label_original_image.width())
        self.ui.label_original_image.setPixmap(QPixmap.fromImage(_qimage))

        """
        计算直方图
        """
        # Y通道直方图
        self.histogram_y_channel = cv2.calcHist([self.original_image_gray], [0], None, [256], [0, 256])
        cv2.normalize(self.histogram_y_channel, self.histogram_y_channel, 0, 1024, cv2.NORM_MINMAX)
        self.histogram_y_image = np.zeros((1024, 1024, 3), dtype=np.uint8)
        for i, value in enumerate(self.histogram_y_channel):
            cv2.line(self.histogram_y_image, (i * 4, 1024), (i * 4, 1024 - int(value)), (255, 255, 255), 4)
        _qimage = QImage(self.histogram_y_image, 1024, 1024, QImage.Format.Format_RGB888).scaledToWidth(200)
        self.ui.label_y_channel_hist.setPixmap(QPixmap.fromImage(_qimage))

        # 彩色图还要绘制RGB通道的直方图
        if self.channels == 3:
            # R通道直方图
            self.histogram_r_channel = cv2.calcHist([self.original_image_rgb], [0], None, [256], [0, 256])
            cv2.normalize(self.histogram_r_channel, self.histogram_r_channel, 0, 1024, cv2.NORM_MINMAX)
            self.histogram_r_image = np.zeros((1024, 1024, 3), dtype=np.uint8)
            for i, value in enumerate(self.histogram_r_channel):
                cv2.line(self.histogram_r_image, (i * 4, 1024), (i * 4, 1024 - int(value)), (100, 100, 255), 4)
            _qimage = QImage(self.histogram_r_image, 1024, 1024, QImage.Format.Format_RGB888).scaledToWidth(200)
            self.ui.label_r_channel_hist.setPixmap(QPixmap.fromImage(_qimage))

            # G通道直方图
            self.histogram_g_channel = cv2.calcHist([self.original_image_rgb], [1], None, [256], [0, 256])
            cv2.normalize(self.histogram_g_channel, self.histogram_g_channel, 0, 1024, cv2.NORM_MINMAX)
            self.histogram_g_image = np.zeros((1024, 1024, 3), dtype=np.uint8)
            for i, value in enumerate(self.histogram_g_channel):
                cv2.line(self.histogram_g_image, (i * 4, 1024), (i * 4, 1024 - int(value)), (100, 255, 100), 4)
            _qimage = QImage(self.histogram_g_image, 1024, 1024, QImage.Format.Format_RGB888).scaledToWidth(200)
            self.ui.label_g_channel_hist.setPixmap(QPixmap.fromImage(_qimage))

            # B通道直方图
            self.histogram_b_channel = cv2.calcHist([self.original_image_rgb], [2], None, [256], [0, 256])
            cv2.normalize(self.histogram_b_channel, self.histogram_b_channel, 0, 1024, cv2.NORM_MINMAX)
            self.histogram_b_image = np.zeros((1024, 1024, 3), dtype=np.uint8)
            for i, value in enumerate(self.histogram_b_channel):
                cv2.line(self.histogram_b_image, (i * 4, 1024), (i * 4, 1024 - int(value)), (255, 100, 100), 4)
            _qimage = QImage(self.histogram_b_image, 1024, 1024, QImage.Format.Format_RGB888).scaledToWidth(200)
            self.ui.label_b_channel_hist.setPixmap(QPixmap.fromImage(_qimage))

