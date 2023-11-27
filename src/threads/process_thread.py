import cv2
from PyQt6.QtCore import QThread, pyqtSignal


class ProcessThread(QThread):
    """
    多线程
    """
    def __init__(self):
        super().__init__()

        # 信号
        s1 = pyqtSignal(object)

    def run(self):
        pass
