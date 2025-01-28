from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsDropShadowEffect, QComboBox, QHBoxLayout, QSystemTrayIcon, QMenu, QAction, QMainWindow
from PyQt5.QtGui import QColor, QFont, QIcon
from PyQt5.QtCore import Qt

import pywintypes
import win32api
import win32con

from settings import ICON_TRAY, WINDOW_STYLES, FONTS_SET
from items import LIST_RESIZES


class DarkPurpleSoftUIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dark Purple Soft UI Design")
        self.setGeometry(200, 200, 500, 400)
        self.setFixedSize(500, 400)
        self.load_styles()

        # Central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Main layout
        self.layout = QVBoxLayout(self.central_widget)

        # Styled title
        self.label = QLabel("Dark Purple Soft UI Design")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont(FONTS_SET, 20, QFont.Bold))
        self.add_shadow(self.label, QColor(50, 50, 50))
        self.layout.addWidget(self.label)

        # Container for resolution dropdowns
        self.resolution_layout = QVBoxLayout()
        self.layout.addLayout(self.resolution_layout)

        # Add/Remove buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Resolution")
        self.add_button.setFont(QFont(FONTS_SET, 12))
        self.add_button.clicked.connect(self.add_resolution_dropdown)
        button_layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Resolution")
        self.remove_button.setFont(QFont(FONTS_SET, 12))
        self.remove_button.clicked.connect(self.remove_resolution_dropdown)
        button_layout.addWidget(self.remove_button)

        self.layout.addLayout(button_layout)

        # Button for minimizing to tray
        self.minimize_button = QPushButton("Minimize to Tray")
        self.minimize_button.setFont(QFont(FONTS_SET, 12))
        self.minimize_button.clicked.connect(self.minimize_to_tray)
        self.layout.addWidget(self.minimize_button)

        # Add system tray functionality
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(ICON_TRAY))
        self.tray_icon.setVisible(True)

        tray_menu = QMenu(self)
        minimize_action = QAction("Minimize to Tray", self)
        minimize_action.triggered.connect(self.minimize_to_tray)
        tray_menu.addAction(minimize_action)

        restore_action = QAction("Restore", self)
        restore_action.triggered.connect(self.restore_window)
        tray_menu.addAction(restore_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(tray_menu)

        # List of resolution widgets
        self.resolution_widgets = []
        self.add_resolution_dropdown()

    def load_styles(self):
        """Load the styles from the external .qss file."""
        try:
            with open(WINDOW_STYLES, "r") as f:
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
        combo.setFont(QFont(FONTS_SET, 12))
        combo.addItems(LIST_RESIZES)
        
        apply_button = QPushButton("Apply")
        apply_button.setFont(QFont(FONTS_SET, 12))
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
        width, height = map(int, selected_resolution.split("x"))
        self.change_screen_resolution(width, height)

    def change_screen_resolution(self, width, height):
        """Changes the screen resolution (Windows only)."""
        devmode = pywintypes.DEVMODEType()
        devmode.PelsWidth = width
        devmode.PelsHeight = height
        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

        win32api.ChangeDisplaySettings(devmode, win32con.CDS_FULLSCREEN)

    def minimize_to_tray(self):
        """Minimizes the window to the system tray."""
        self.hide()

    def restore_window(self):
        """Restores the window from the tray."""
        self.showNormal()