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

        self.setLayout(self.layout)

        # List of resolution widgets
        self.resolution_widgets = []
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
        """Adds a new resolution dropdown with an apply button."""
        resolution_box = QHBoxLayout()
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
        
        apply_button = QPushButton("Прийняти")
        apply_button.setFont(QFont("Arial", 12))
        apply_button.clicked.connect(lambda: self.apply_resolution(combo))
        
        resolution_box.addWidget(combo)
        resolution_box.addWidget(apply_button)
        
        self.resolution_widgets.append((combo, apply_button))
        self.resolution_layout.addLayout(resolution_box)

    def remove_resolution_dropdown(self):
        """Removes the last added resolution dropdown if at least one remains."""
        if self.resolution_widgets:
            combo, button = self.resolution_widgets.pop()
            combo.setParent(None)
            button.setParent(None)

    def apply_resolution(self, combo):
        """Handles applying a selected resolution."""
        selected_resolution = combo.currentText()
        print(f"Selected resolution: {selected_resolution}")