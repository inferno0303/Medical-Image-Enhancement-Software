import os
import cv2
import numpy as np
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog

from src.ui.ui_main_widget import Ui_ui_main_widget
from src.widgets.subwidget_histogram import WidgetHistogram
from src.widgets.subwidget_conv import WidgetConv
from src.threads.process_thread import ProcessThread


class Widget01(QWidget):
    """
    主窗口
    """
    def __init__(self):
        super().__init__()

        # 当前控件的status
        self.original_image = None
        self.original_image_rgb = None
        self.original_image_gray = None
        self.width = None
        self.height = None
        self.channels = None
        self.file_path = None
        # 其他控件的实例
        self._subwidget_histogram = None
        self._subwidget_conv = None
        # 线程
        self.thread = ProcessThread()

        self.ui = Ui_ui_main_widget()
        self.ui.setupUi(self)
        self.ui_init()

    def ui_init(self):
        self.ui.pushButton_openImage.clicked.connect(self.slot_open_image)
        self.ui.pushButton_closeImage.clicked.connect(self.slot_close_image)
        self.ui.pushButton_calcHistogram.clicked.connect(self.slot_calc_histogram)
        self.ui.pushButton_conv.clicked.connect(self.slot_conv)
        pass

    """
    pushButton_openImage的槽函数
    """
    def slot_open_image(self):
        # 弹出选择文件对话框
        file_path, file_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '', '图像文件(*.jpg *.bmp *.png)')

        # 判空
        if file_path == "" or file_type == "":
            return 0

        # 用opencv加载图像，并存储到numpy对象中
        self.original_image = cv2.imread(file_path)
        self.file_path = file_path

        # 获得图像的高度、宽度、颜色通道数
        self.height, self.width, self.channels = self.original_image.shape

        # 图像类型
        image_type = None
        if self.channels == 3:
            image_type = "彩色图"
            # 将彩色BGR通道顺序转换为RGB
            self.original_image_rgb = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
        elif self.channels == 1:
            image_type = "灰度图"
            self.original_image_gray = self.original_image
        else:
            return -1

        # 获得图像的色深
        depth = self.original_image.dtype

        # 获得图像的大小
        file_size = int(os.path.getsize(file_path) / 1024)

        # 获得图像的后缀名
        _, file_extension = os.path.splitext(file_path)

        # 将图像详细信息显示到label上
        _str = f"分辨率：{self.width}x{self.height}\n颜色通道：{self.channels}\n色深：{depth}\n类型：{image_type}\n文件大小：{file_size}KB\n扩展名：{file_extension}"
        self.ui.label_image_detail.setText(_str)

        # 将numpy对象转换为QImage对象
        _qimage = None
        if self.channels == 3:
            _qimage = QImage(self.original_image_rgb, self.width, self.height, QImage.Format.Format_RGB888)
        elif self.channels == 1:
            _qimage = QImage(self.original_image_gray, self.width, self.height, QImage.Format.Format_Grayscale8)

        # 保持宽高比不变，最大化显示到label中
        if self.ui.label_original_image.width() > self.ui.label_original_image.height():
            # 如果label宽度比较宽，则按照label的高度缩放图像
            _qimage = _qimage.scaledToHeight(self.ui.label_original_image.height())
        else:
            # 否则按照label的宽度缩放图像
            _qimage = _qimage.scaledToWidth(self.ui.label_original_image.width())
        self.ui.label_original_image.setPixmap(QPixmap.fromImage(_qimage))
        self._update_widget_state()
        return 0

    """
    pushButton_closeImage的槽函数
    """
    def slot_close_image(self):
        self.ui.label_original_image.setText("未打开图像")
        self.original_image = None
        self.original_image_rgb = None
        self.original_image_gray = None
        self.width = None
        self.height = None
        self.channels = None
        self.file_path = None
        self.ui.label_image_detail.setText("未打开图像")
        self._update_widget_state()
        return 0

    """
    更新控件状态，例如enable/disable按钮
    """
    def _update_widget_state(self):
        # 如果已经打开了图像，将按钮设置为可以点击
        if self.original_image is not None:
            self.ui.pushButton_calcHistogram.setEnabled(True)
            self.ui.pushButton_calcDynamicRange.setEnabled(True)
            self.ui.pushButton_calcNoiseLevel.setEnabled(True)
            self.ui.pushButton_conv.setEnabled(True)
        else:
            self.ui.pushButton_calcHistogram.setEnabled(False)
            self.ui.pushButton_calcDynamicRange.setEnabled(False)
            self.ui.pushButton_calcNoiseLevel.setEnabled(False)
            self.ui.pushButton_conv.setEnabled(False)

    """
    pushButton_calcHistogram 的槽函数
    """
    def slot_calc_histogram(self):
        # 打开直方图模块控件
        if self.channels == 3:
            self._subwidget_histogram = WidgetHistogram(self.original_image_rgb)
        elif self.channels == 1:
            self._subwidget_histogram = WidgetHistogram(self.original_image_gray)
        else:
            return -1
        self._subwidget_histogram.show()

    """
    pushButton_conv 的槽函数
    """
    def slot_conv(self):
        # 打开锐化和卷积模块
        if self.channels == 3:
            self._subwidget_conv = WidgetConv(self.original_image_rgb)
        elif self.channels == 1:
            self._subwidget_conv = WidgetConv(self.original_image_gray)
        else:
            return -1
        self._subwidget_conv.show()
