from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt


class DarkPurpleSoftUIWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dark Purple Soft UI Design")
        self.setGeometry(200, 200, 500, 300)
        self.load_styles()

        # Main layout
        layout = QVBoxLayout()

        # Styled title
        self.label = QLabel("Dark Purple Soft UI Design")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 20, QFont.Bold))
        self.add_shadow(self.label, QColor(50, 50, 50))  # Soft dark gray shadow

        layout.addWidget(self.label)

        # Styled button
        self.button = QPushButton("Click Me")
        self.button.setFont(QFont("Arial", 14))
        self.add_shadow(self.button, QColor(50, 50, 50))  # Soft dark gray shadow

        layout.addWidget(self.button)

        self.setLayout(layout)

    def load_styles(self):
        """Load the styles from the external .qss file."""
        with open("styles.qss", "r") as f:
            self.setStyleSheet(f.read())

    def add_shadow(self, widget, color):
        """Adds a soft shadow effect to the widget."""
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(color)
        shadow.setOffset(3, 3)
        widget.setGraphicsEffect(shadow)