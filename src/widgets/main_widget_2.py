import os
import time
import cv2
import numpy as np
import pydicom
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt6.QtCore import QFileInfo, pyqtSlot, pyqtSignal

# 主窗口UI
from src.ui.ui_main_widget_2 import Ui_MyMainWidget
# 直方图模块逻辑
from src.widgets.hist_widget_2 import HistWidget
# 卷积和锐化模块逻辑
from src.widgets.conv_widget_2 import ConvWidget
# 图像去噪模块
from src.widgets.denoising_widget import DenoisingWidget


class MyMainWidget(QWidget):
    """
    主窗口逻辑
    """

    def __init__(self):
        super().__init__()

        # 初始化ui
        self.ui = Ui_MyMainWidget()
        self.ui.setupUi(self)

        # 初始化子组件
        self.hist_widget = HistWidget()
        self.hist_widget.send_after_image.connect(self.receive_after_image)
        self.conv_widget = ConvWidget()
        self.conv_widget.send_after_image.connect(self.receive_after_image)
        self.denoising_widget = DenoisingWidget()
        self.denoising_widget.send_after_image.connect(self.receive_after_image)

        # 当前组件的状态
        self.file_path = None
        self.image = None
        self.qimage = None

        # 连接信号与槽
        self.ui.open_image_btn.clicked.connect(self.open_file_dialog)
        self.ui.save_image_btn.clicked.connect(self.save_image)
        self.ui.close_image_btn.clicked.connect(self.close_image)
        self.ui.next_image_btn.clicked.connect(self.next_image)
        self.ui.prev_image_btn.clicked.connect(self.prev_image)
        self.ui.hist_module_btn.clicked.connect(self.open_hist_widget)
        self.ui.conv_module_btn.clicked.connect(self.open_conv_widget)
        self.ui.denosing_module_btn.clicked.connect(self.open_denoising_widget)

    def open_file_dialog(self):
        """
        弹出选择文件对话框
        """

        # 弹出选择文件对话框
        file_path, _ = QFileDialog.getOpenFileName(QFileDialog(), '选择文件', '',
                                                   'dcm文件或图像文件(*png *.jpg *.bmp *tif *.dcm)')

        if file_path:
            self.open_image(file_path)

    def open_image(self, file_path):
        """
        读取文件
        """

        # 记录当前打开的文件路径
        self.file_path = file_path

        # 计算文件类型
        file_info = QFileInfo(file_path)
        file_suffix = file_info.suffix()

        # 区分文件类型，如果是图像文件，就用opencv打开，如果是dcm文件，就用pydicom打开
        if file_suffix in ["png", "jpg", "bmp", "tif"]:

            # 用opencv加载文件
            image = cv2.imread(file_path)

        elif file_suffix in ["dcm"]:

            # 用pydicom加载dcm文件
            dcm = pydicom.dcmread(file_path, force=True)

            # 提取dcm文件的图像序列
            pixel = dcm.pixel_array

            # 转换为numpy类型
            image = np.array(pixel)

        else:
            return -1

        # 记录当前打开的图片
        self.image = image

        # 显示文件信息到UI
        self._display_file_detail_to_label(image=image, file_path=file_path)

        # 显示图像到UI
        self._display_image_to_label(image=image)

        # 更新UI
        self._update_btn_enable_or_disable()

    def _update_btn_enable_or_disable(self):
        """
        根据是否打开了图像，修改按钮样式为 enable/disable
        """
        if self.file_path:
            self.ui.save_image_btn.setEnabled(True)
            self.ui.image_prev_and_next_groupBox.setEnabled(True)
            self.ui.function_groupBox.setEnabled(True)
        else:
            self.ui.save_image_btn.setEnabled(False)
            self.ui.image_prev_and_next_groupBox.setEnabled(False)
            self.ui.function_groupBox.setEnabled(False)

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

    def _display_file_detail_to_label(self, image, file_path):
        """
        显示文件信息到UI
        """
        # 计算文件后缀名和大小
        file_info = QFileInfo(file_path)
        file_name = file_info.fileName()
        file_size = file_info.size()  # 以字节为单位

        # 计算图像的信息
        result = self._calc_image_info(image)
        height = result.get("height")
        width = result.get("width")
        channel = result.get("channel")
        depth = result.get("depth")

        # 计算图像类型（灰度图 或 彩色图）
        color_type = None
        if channel == 1:
            color_type = "灰度图"
        elif channel == 3:
            color_type = "彩色图"

        # 显示文件信息到UI
        _str = (f"图像分辨率：{width}x{height}\n颜色通道：{channel}\n动态范围：{depth}\n"
                f"色彩类型：{color_type}\n文件大小：{format(file_size / 1024, '.2f')}KB\n"
                f"文件名：{file_name}")
        self.ui.file_detail_label.setText(_str)

    def _display_image_to_label(self, image):
        """
        显示图像到UI
        """
        # 计算图像信息
        height = image.shape[0]
        width = image.shape[1]
        channel = None
        if image.ndim == 2:
            channel = 1
        elif image.ndim == 3:
            channel = 3
        depth = image.dtype

        # 转换为QImage类型
        _qimage = None
        if channel == 3 and depth == 'uint8':
            _qimage = QImage(image, width, height, QImage.Format.Format_BGR888)
        elif channel == 1:
            if depth == 'uint8':
                _qimage = QImage(image, width, height, QImage.Format.Format_Grayscale8)
            elif depth == 'uint16':
                # QImage无法处理uint16类型
                _qimage = QImage(image.astype('uint8'), width, height, QImage.Format.Format_Grayscale8)
            elif depth == 'int16':
                _qimage = QImage(image.astype('uint16'), width, height, QImage.Format.Format_Grayscale16)

        if _qimage:
            # 将图像按label的短边拉伸，以填满label
            label_width = self.ui.image_label.width()
            label_height = self.ui.image_label.height()
            if label_width < label_height:
                self.ui.image_label.setPixmap(QPixmap.fromImage(_qimage.scaledToWidth(label_width)))
            else:
                self.ui.image_label.setPixmap(QPixmap.fromImage(_qimage.scaledToHeight(label_height)))

            # 将QImage对象放到类成员变量，以实现伸缩窗口时能重新缩放到label
            self.qimage = _qimage

    def save_image(self):
        """
        保存图像文件
        """
        if self.image is not None:

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
                cv2.imwrite(selected_file, self.image)

        # 提示框
        QMessageBox.information(self, '提示', '保存成功。', QMessageBox.StandardButton.Ok)

    def close_image(self):
        """
        关闭文件，清理
        """

        self.ui.file_detail_label.setText("")
        self.ui.image_label.setText("未打开图像")

        self.qimage = None
        self.file_path = None

        # 更新UI
        self._update_btn_enable_or_disable()

    @staticmethod
    def _get_other_image_in_folder(file_path):
        """
        获取同一个文件夹下的其他图像文件
        """

        # 用于存储图像数据的数组
        images = []

        if file_path:
            # 获取文件夹路径
            folder_path = os.path.dirname(file_path)

            # 获取文件夹内所有文件
            all_files = os.listdir(folder_path)

            # 遍历文件夹内所有文件
            for file_name in all_files:
                # 拼接文件的完整路径
                file_full_path = folder_path + '/' + file_name

                # 检查文件是否为图像文件（你可能需要根据实际情况添加其他判断条件）
                if file_name.lower().endswith(('.png', '.jpg', '.bmp', '.tif', '.dcm')):
                    # 将图像数据添加到数组中
                    images.append(file_full_path)

            return images

        else:
            return images

    def next_image(self):
        if self.file_path:

            # 获取同一个文件夹下的其他图像文件
            images = self._get_other_image_in_folder(self.file_path)

            # 定位到当前打开的文件的下标
            current_index = images.index(self.file_path)

            # 计算下一个文件的路径
            if current_index + 1 > len(images) - 1:
                next_index = 0
            else:
                next_index = current_index + 1
            next_file_path = images[next_index]

            # 打开下一个文件
            self.open_image(file_path=next_file_path)

    def prev_image(self):
        if self.file_path:
            # 获取同一个文件夹下的其他图像文件
            images = self._get_other_image_in_folder(self.file_path)

            # 定位到当前打开的文件的下标
            current_index = images.index(self.file_path)

            # 计算上一个文件的路径
            if current_index == 0:
                prev_index = len(images) - 1
            else:
                prev_index = current_index - 1
            prev_file_path = images[prev_index]

            # 打开上一个文件
            self.open_image(file_path=prev_file_path)

    def open_hist_widget(self):
        """
        打开直方图模块窗口
        """
        if self.image is not None:
            if self.hist_widget.isVisible():
                self.hist_widget.close()
            self.hist_widget.set_image(image=self.image.copy())
            self.hist_widget.show()

    def open_conv_widget(self):
        """
        打开卷积与滤波模块窗口
        """
        if self.image is not None:
            if self.conv_widget.isVisible():
                self.conv_widget.close()
            self.conv_widget.set_image(image=self.image.copy())
            self.conv_widget.show()

    def open_denoising_widget(self):
        """
        打开图像去噪模块
        """
        if self.image is not None:
            if self.denoising_widget.isVisible():
                self.denoising_widget.close()
            self.denoising_widget.set_image(image=self.image.copy())
            self.denoising_widget.show()

    def receive_after_image(self, after_image):
        """
        接收处理后的图像：自定义信号save_signal的槽函数
        """
        self._display_image_to_label(image=after_image)
        self.image = after_image

    @pyqtSlot('QWheelEvent*')
    def wheelEvent(self, event):
        """
        重载wheelEvent槽函数，监听鼠标滚轮事件，实现上一张、下一张图像预览
        """
        if self.file_path:

            # 获取滚轮滚动的角度，正值表示向上滚动，负值表示向下滚动
            angle = event.angleDelta().y()

            # 向上滚动
            if angle > 0:
                self.prev_image()
            # 向下滚动
            else:
                self.next_image()

    @pyqtSlot('QResizeEvent')
    def resizeEvent(self, event):
        """
        重载resizeEvent槽函数，监听窗口size变化事件，实现伸缩窗口时能重新缩放到label
        """
        if self.qimage:
            _qimage = self.qimage
            # 将图像按label的短边拉伸，以填满label
            label_width = self.ui.image_label.width()
            label_height = self.ui.image_label.height()
            if label_width < label_height:
                self.ui.image_label.setPixmap(QPixmap.fromImage(_qimage.scaledToWidth(label_width)))
            else:
                self.ui.image_label.setPixmap(QPixmap.fromImage(_qimage.scaledToHeight(label_height)))
