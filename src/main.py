import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

# Widget实例
from widgets.main_widget import Widget01

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 显示widget_01
    _widget_01 = Widget01()
    _widget_01.show()

    # UI线程循环
    sys.exit(app.exec())
