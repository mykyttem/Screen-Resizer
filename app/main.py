import sys
from PyQt5.QtWidgets import QApplication
from window import DarkPurpleSoftUIWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DarkPurpleSoftUIWindow()
    window.show()
    sys.exit(app.exec_())