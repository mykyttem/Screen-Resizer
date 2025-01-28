import PyInstaller.__main__

PyInstaller.__main__.run([
    'app/main.py',
    '--onefile',
    '--noconsole',
    '--icon=icon/icon.ico',
    '--name=Window resizer',
    '--add-data=styles/styles.qss;styles',
    '--add-data=icon/icon.ico;icon',
])