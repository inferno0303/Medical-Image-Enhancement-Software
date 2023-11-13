from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化ui
        self.init_ui()

    def init_ui(self):
        # 创建标签并设置文本
        hello_label = QLabel('Hello, World!')

        # 创建垂直布局
        layout = QVBoxLayout()

        # 将标签添加到布局中
        layout.addWidget(hello_label)

        # 将布局设置为窗口的主布局
        self.setLayout(layout)

        # 设置窗口的标题和大小
        self.setWindowTitle('Hello World App')
        self.setGeometry(100, 100, 300, 200)
