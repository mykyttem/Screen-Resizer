import os
import sys


ICON = "icon/tray.png"
FONTS_SET = "Arial"


def resource_path(relative_path):
    """Gets the path to resources in PyInstaller or when running from source code"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

WINDOW_STYLES = resource_path("styles/styles.qss")