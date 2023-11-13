import sys
from PyQt6.QtWidgets import QApplication
# Widget实例
from widgets.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化Widget
    _main_window = MainWindow()
    # 显示Widget
    _main_window.show()
    # UI线程循环
    sys.exit(app.exec())
