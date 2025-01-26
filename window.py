from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsDropShadowEffect, QComboBox, QHBoxLayout
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt


class DarkPurpleSoftUIWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dark Purple Soft UI Design")
        self.setGeometry(200, 200, 500, 400)
        self.load_styles()

        # Main layout
        self.layout = QVBoxLayout()

        # Styled title
        self.label = QLabel("Dark Purple Soft UI Design")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 20, QFont.Bold))
        self.add_shadow(self.label, QColor(50, 50, 50))
        self.layout.addWidget(self.label)

        # Container for resolution dropdowns
        self.resolution_layout = QVBoxLayout()
        self.layout.addLayout(self.resolution_layout)

        # Add/Remove buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Resolution")
        self.add_button.setFont(QFont("Arial", 12))
        self.add_button.clicked.connect(self.add_resolution_dropdown)
        button_layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Resolution")
        self.remove_button.setFont(QFont("Arial", 12))
        self.remove_button.clicked.connect(self.remove_resolution_dropdown)
        button_layout.addWidget(self.remove_button)

        self.layout.addLayout(button_layout)

        # Styled apply button
        self.apply_button = QPushButton("Apply Resolution")
        self.apply_button.setFont(QFont("Arial", 14))
        self.add_shadow(self.apply_button, QColor(50, 50, 50))
        self.apply_button.clicked.connect(self.apply_resolution)
        self.layout.addWidget(self.apply_button)

        self.setLayout(self.layout)

        # List of dropdowns
        self.resolution_combos = []
        self.add_resolution_dropdown()

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

    def add_resolution_dropdown(self):
        """Adds a new resolution dropdown."""
        combo = QComboBox()
        combo.setFont(QFont("Arial", 12))
        combo.addItems([
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
        self.resolution_combos.append(combo)
        self.resolution_layout.addWidget(combo)

    def remove_resolution_dropdown(self):
        """Removes the last added resolution dropdown if at least one remains."""
        if self.resolution_combos:
            combo = self.resolution_combos.pop()
            self.resolution_layout.removeWidget(combo)
            combo.deleteLater()

    def apply_resolution(self):
        """Handle resolution change action."""
        selected_resolutions = [combo.currentText() for combo in self.resolution_combos]
        print(f"Selected resolutions: {', '.join(selected_resolutions)}")