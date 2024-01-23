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
# 图像评估模块
from src.widgets.evaluation_widget import EvaluationWidget


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
        self.conv_widget = ConvWidget()
        self.denoising_widget = DenoisingWidget()
        self.evaluation_widget = EvaluationWidget()

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
        self.ui.hist_module_btn.clicked.connect(self.on_open_hist_widget)
        self.ui.conv_module_btn.clicked.connect(self.on_open_conv_widget)
        self.ui.denosing_module_btn.clicked.connect(self.on_open_denoising_widget)
        self.ui.evalueate_module_btn.clicked.connect(self.on_open_evaluation_widget)
        self.ui.enhance_module_btn.clicked.connect(self.on_one_key_enhance)

        # 连接子组件自定义信号与槽函数，用于从子组件接收处理后的图像
        self.hist_widget.send_after_image.connect(self.receive_after_image)
        self.conv_widget.send_after_image.connect(self.receive_after_image)
        self.denoising_widget.send_after_image.connect(self.receive_after_image)

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

            # 用opencv加载文件，注意：不支持中文路径
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

        # 判断是否已经读取成功图像数组，在这里numpy数组需要用这个方法做判非空
        if np.any(image):

            # 记录当前打开的图片
            self.image = image

            # 显示文件信息到UI
            self._display_file_detail_to_label(image=image, file_path=file_path)

            # 显示图像到UI
            self._display_image_to_label(image=image)

            # 更新UI
            self._update_btn_enable_or_disable()

        # 读取图像出错
        else:
            QMessageBox.warning(self, '读取文件出错', f'请检查文件路径：{file_path}\n不能包含中文字符。', QMessageBox.StandardButton.Ok)
            return -1

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
        if file_path:

            # 获取文件夹路径
            folder_path = os.path.dirname(file_path)

            # 获取文件夹内所有文件
            all_files = os.listdir(folder_path)

            # 用于存储图像数据的数组
            images = []

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
            return []

    def next_image(self):
        if self.file_path:

            # 获取同一个文件夹下的其他图像文件
            images = self._get_other_image_in_folder(self.file_path)
            if images:

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

    def on_open_hist_widget(self):
        """
        打开直方图模块窗口
        """
        if self.image is not None:
            if self.hist_widget.isVisible():
                self.hist_widget.close()
            self.hist_widget.set_image(image=self.image.copy())
            self.hist_widget.show()

    def on_open_conv_widget(self):
        """
        打开卷积与滤波模块窗口
        """
        if self.image is not None:
            if self.conv_widget.isVisible():
                self.conv_widget.close()
            self.conv_widget.set_image(image=self.image.copy())
            self.conv_widget.show()

    def on_open_denoising_widget(self):
        """
        打开图像去噪模块
        """
        if self.image is not None:
            if self.denoising_widget.isVisible():
                self.denoising_widget.close()
            self.denoising_widget.set_image(image=self.image.copy())
            self.denoising_widget.show()

    def on_open_evaluation_widget(self):
        """
        打开图像评估模块
        """
        if self.image is not None:

            # 处理重复点击的清空
            if self.evaluation_widget.isVisible():
                self.evaluation_widget.close()

            # 传递处理后的图像给子组件
            self.evaluation_widget.set_distorted_image(image=self.image.copy())

            # 根据file_path将原图再次打开，并传递给子组件
            if self.file_path is not None:
                file_path = self.file_path
                file_info = QFileInfo(file_path)
                file_suffix = file_info.suffix()
                if file_suffix in ["png", "jpg", "bmp", "tif"]:
                    image = cv2.imread(file_path)
                elif file_suffix in ["dcm"]:
                    dcm = pydicom.dcmread(file_path, force=True)
                    pixel = dcm.pixel_array
                    image = np.array(pixel)
                else:
                    return -1
                self.evaluation_widget.set_original_image(image=image)

                # 显示窗口
                self.evaluation_widget.show()

    def on_one_key_enhance(self):
        """
        一键自适应增强：双边滤波->灰度线性均衡->锐化算子卷积
        """
        if self.image is not None:
            image = self.image.copy()

            # 计算图像信息
            result = self._calc_image_info(image=image)
            channel = result.get("channel")
            depth = result.get("depth")

            # 对非uint8动态范围的图像，归一化到uint8动态范围
            if depth != 'uint8':
                # 线性归一化到8位动态范围
                image = ((image - image.min()) / (image.max() - image.min()) * 255).astype('uint8')

            if channel == 3:

                # 双边滤波
                after_bilateral = cv2.bilateralFilter(src=image, d=25, sigmaColor=10 * 2, sigmaSpace=10 / 2)

                # 灰度线性均衡
                image_yuv = cv2.cvtColor(after_bilateral, cv2.COLOR_BGR2YUV)
                [y, u, v] = cv2.split(image_yuv)
                y = cv2.normalize(y, None, 0, 255, cv2.NORM_MINMAX)
                after_yuv_image = cv2.merge([y, u, v])
                after_normalize = cv2.cvtColor(after_yuv_image, cv2.COLOR_YUV2BGR)

                # 锐化算子卷积
                kernel = np.array([[0.0, -1.0, 0.0], [-1.0, 5.0, -1.0], [0.0, -1.0, 0.0]], np.float32)
                image_yuv = cv2.cvtColor(after_normalize, cv2.COLOR_BGR2YUV)
                [y, u, v] = cv2.split(image_yuv)
                y = cv2.filter2D(src=y, ddepth=-1, kernel=kernel)
                after_yuv_image = cv2.merge([y, u, v])
                after_sharpen = cv2.cvtColor(after_yuv_image, cv2.COLOR_YUV2BGR)

            elif channel == 1:

                # 双边滤波
                after_bilateral = cv2.bilateralFilter(src=image, d=25, sigmaColor=10 * 2, sigmaSpace=10 / 2)

                # 灰度线性均衡
                after_normalize = cv2.normalize(after_bilateral, None, 0, 255, cv2.NORM_MINMAX)

                # 锐化算子卷积
                kernel = np.array([[0.0, -1.0, 0.0], [-1.0, 5.0, -1.0], [0.0, -1.0, 0.0]], np.float32)
                after_sharpen = cv2.filter2D(src=after_normalize, ddepth=-1, kernel=kernel)

            else:
                return -1

            self._display_image_to_label(image=after_sharpen)
            self.image = after_sharpen



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

    @pyqtSlot('QShowEvent')
    def showEvent(self, event):

        # 在窗口显示时执行的逻辑代码
        self._update_btn_enable_or_disable()

        # 需要调用父类的 showEvent
        super().showEvent(event)
