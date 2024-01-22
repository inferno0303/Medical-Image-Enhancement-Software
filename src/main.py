import sys

from PyQt6.QtWidgets import QApplication

# 主界面逻辑
from widgets.main_widget_2 import MyMainWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 显示MainWidget
    mw = MyMainWidget()
    mw.show()

    # UI线程循环
    sys.exit(app.exec())
