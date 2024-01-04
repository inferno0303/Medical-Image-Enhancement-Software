import os
import time
import cv2
import numpy as np
import pydicom
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt6.QtCore import QFileInfo, QObject, pyqtSignal

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

        # 当前组件的state
        self.original_image = None
        self.original_image_rgb = None
        self.original_image_gray = None
        self.width = None
        self.height = None
        self.channels = None
        self.file_path = None
        self.after_image = None

        # 其他widget实例
        self._subwidget_histogram = None
        self._subwidget_conv = None

        # 线程实例
        self.thread = ProcessThread()

        self.ui = Ui_ui_main_widget()
        self.ui.setupUi(self)
        self.ui_init()

    def ui_init(self):

        # 连接信号与槽
        self.ui.pushButton_openImage.clicked.connect(self.slot_open_image)
        self.ui.pushButton_closeImage.clicked.connect(self.slot_close_image)
        self.ui.pushButton_calcHistogram.clicked.connect(self.slot_calc_histogram)
        self.ui.pushButton_conv.clicked.connect(self.slot_conv)
        self.ui.pushButton_saveImage.clicked.connect(self.slot_save_image)
        pass

    def slot_open_image(self):
        """
        打开文件：pushButton_openImage的槽函数
        """

        # 弹出选择文件对话框
        file_path, _ = QFileDialog.getOpenFileName(QFileDialog(), '选择文件', '',
                                                   '图像或dcm档案(*png *.jpg *.bmp *tif *.dcm)')

        # 未选择文件
        if file_path == '':
            return 0

        # 获取文件的后缀名
        file_info = QFileInfo(file_path)
        file_suffix = file_info.suffix()
        self.file_path = file_path

        if file_suffix in ["png", "jpg", "bmp", "tif"]:

            # 用opencv加载图像，并存储到numpy对象中
            self.original_image = cv2.imread(file_path)

            # 获得图像的高度、宽度、颜色通道数
            self.height, self.width, self.channels = self.original_image.shape

            # 将彩色BGR通道顺序转换为RGB
            if self.channels == 3:
                self.original_image_rgb = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            elif self.channels == 1:
                self.original_image_gray = self.original_image
            else:
                return -1

        elif file_suffix in ["dcm"]:

            # 用PyDICOM加载dcm文件
            print(file_suffix, file_path)
            dcm_file = pydicom.dcmread(file_path, force=True)
            pixel_array = np.array(dcm_file.pixel_array)
            self.original_image = pixel_array.astype(np.uint8)

            # 获得图像的高度、宽度、颜色通道数
            self.height, self.width = self.original_image.shape
            if self.original_image.ndim == 2:
                self.channels = 1
                self.original_image_gray = self.original_image
            elif self.original_image.ndim == 3:
                self.channels = 3
                self.original_image_rgb = self.original_image

        else:
            return -1

        # 获得图像类型
        if self.channels == 3:
            image_type = "彩色图"
        elif self.channels == 1:
            image_type = "灰度图"
        else:
            return -1

        # 获得图像的色深
        depth = self.original_image.dtype

        # 获得图像的大小
        file_size = int(os.path.getsize(file_path) / 1024)

        # 将图像详细信息显示到label上
        _str = f"分辨率：{self.width}x{self.height}\n颜色通道：{self.channels}\n色深：{depth}\n类型：{image_type}\n文件大小：{file_size}KB\n扩展名：{file_suffix}"
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

    def slot_close_image(self):
        """
        关闭图像：pushButton_closeImage的槽函数
        """
        self.ui.label_original_image.setText("未打开图像")
        self.original_image = None
        self.original_image_rgb = None
        self.original_image_gray = None
        self.width = None
        self.height = None
        self.channels = None
        self.file_path = None
        self.after_image = None
        self.ui.label_image_detail.setText("未打开图像")
        self.ui.label_after_image.setText("未打开图像")
        self._update_widget_state()
        return 0

    def _update_widget_state(self):
        """
        更新控件状态，enable/disable按钮
        """
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

    def slot_calc_histogram(self):
        """
        打开直方图模块：pushButton_calcHistogram的槽函数
        """
        # 打开直方图模块控件
        if self.channels == 3:
            self._subwidget_histogram = WidgetHistogram(self.original_image_rgb)
            self._subwidget_histogram.save_signal.connect(self.slot_receive_after_image)
        elif self.channels == 1:
            self._subwidget_histogram = WidgetHistogram(self.original_image_gray)
            self._subwidget_histogram.save_signal.connect(self.slot_receive_after_image)
        else:
            return -1
        self._subwidget_histogram.show()

    def slot_conv(self):
        """
        打开卷积模块：pushButton_conv的槽函数
        """
        # 打开锐化和卷积模块
        if self.channels == 3:
            self._subwidget_conv = WidgetConv(self.original_image_rgb)
            self._subwidget_conv.save_signal.connect(self.slot_receive_after_image)
        elif self.channels == 1:
            self._subwidget_conv = WidgetConv(self.original_image_gray)
            self._subwidget_conv.save_signal.connect(self.slot_receive_after_image)
        else:
            return -1
        self._subwidget_conv.show()

    def slot_receive_after_image(self, after_image):
        """
        接收处理后的图像：自定义信号save_signal的槽函数
        """
        self.after_image = after_image

        # 显示处理后的图像
        _qimage = None
        if self.channels == 3:
            _qimage = QImage(self.after_image, self.width, self.height, QImage.Format.Format_RGB888)
        elif self.channels == 1:
            _qimage = QImage(self.after_image, self.width, self.height, QImage.Format.Format_Grayscale8)

        # 保持宽高比不变，最大化显示到label中
        if self.ui.label_after_image.width() > self.ui.label_after_image.height():
            # 如果label宽度比较宽，则按照label的高度缩放图像
            _qimage = _qimage.scaledToHeight(self.ui.label_after_image.height())
        else:
            # 否则按照label的宽度缩放图像
            _qimage = _qimage.scaledToWidth(self.ui.label_after_image.width())
        self.ui.label_after_image.setPixmap(QPixmap.fromImage(_qimage))

        # 关闭子窗口
        # if self._subwidget_conv is not None:
        #     self._subwidget_conv.close()
        #     self._subwidget_conv = None
        # if self._subwidget_histogram is not None:
        #     self._subwidget_histogram.close()
        #     self._subwidget_conv = None

        return 0

    def slot_save_image(self):
        """
        保存图像文件：pushButton_saveImage的槽函数
        """
        if self.after_image is None:
            print("hello")

            # 提示框
            dialog = QMessageBox(self)
            dialog.setWindowTitle("没有需要保存的图像")
            dialog.setText("没有需要保存的图像，请在功能模块处理图像后再保存图像。")
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.exec()

        else:
            # 弹出文件保存对话框

            file_dialog = QFileDialog()
            default_file_name = "output_image_" + str(time.time())
            file_dialog.selectFile(default_file_name)
            file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
            file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
            file_dialog.setNameFilter("PNG files (*.png)")

            if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
                # 获取用户选择的文件路径
                selected_file = file_dialog.selectedFiles()[0]

                # 保存图像到用户选择的路径
                cv2.imwrite(selected_file, cv2.cvtColor(self.after_image, cv2.COLOR_RGB2BGR))

        # 提示框
        dialog = QMessageBox(self)
        dialog.setWindowTitle("保存成功")
        dialog.setText("保存成功")
        dialog.setIcon(QMessageBox.Icon.Warning)
        dialog.exec()
