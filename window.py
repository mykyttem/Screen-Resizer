from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsDropShadowEffect, QComboBox
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt


class DarkPurpleSoftUIWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dark Purple Soft UI Design")
        self.setGeometry(200, 200, 500, 400)
        self.load_styles()

        # Main layout
        layout = QVBoxLayout()

        # Styled title
        self.label = QLabel("Dark Purple Soft UI Design")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 20, QFont.Bold))
        self.add_shadow(self.label, QColor(50, 50, 50))
        layout.addWidget(self.label)

        # Dropdown for screen resolution 1
        self.resolution_combo1 = QComboBox()
        self.resolution_combo1.setFont(QFont("Arial", 12))
        self.resolution_combo1.addItems([
            "800x600",
            "1024x768",
            "1280x720",
            "1366x768",
            "1440x900",
            "1600x900",
            "1920x1080",
            "2560x1440",
            "3840x2160"
        ])
        layout.addWidget(self.resolution_combo1)

        # Dropdown for screen resolution 2
        self.resolution_combo2 = QComboBox()
        self.resolution_combo2.setFont(QFont("Arial", 12))
        self.resolution_combo2.addItems([
            "800x600",
            "1024x768",
            "1280x720",
            "1366x768",
            "1440x900",
            "1600x900",
            "1920x1080",
            "2560x1440",
            "3840x2160"
        ])
        layout.addWidget(self.resolution_combo2)

        # Styled button
        self.button = QPushButton("Apply Resolution")
        self.button.setFont(QFont("Arial", 14))
        self.add_shadow(self.button, QColor(50, 50, 50))
        self.button.clicked.connect(self.apply_resolution)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def load_styles(self):
        """Load the styles from the external .qss file."""
        try:
            with open("styles.qss", "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("styles.qss not found. Using default styles.")

    def add_shadow(self, widget, color):
        """Adds a soft shadow effect to the widget."""
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(color)
        shadow.setOffset(3, 3)
        widget.setGraphicsEffect(shadow)

    def apply_resolution(self):
        """Handle resolution change action."""
        selected_resolution1 = self.resolution_combo1.currentText()
        selected_resolution2 = self.resolution_combo2.currentText()
        print(f"Selected resolutions: {selected_resolution1}, {selected_resolution2}")