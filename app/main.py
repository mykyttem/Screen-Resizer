import sys
from PyQt5.QtWidgets import QApplication
from window import WindowUI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowUI()
    window.show()
    sys.exit(app.exec_())