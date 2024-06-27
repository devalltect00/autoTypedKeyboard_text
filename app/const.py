import os
import sys

if getattr(sys, 'frozen', False):
  BASE_DIR = os.path.dirname(sys.executable)
else:
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# def getUIFilePath(self):
#   if getattr(sys, 'frozen', False):
#     base_path = sys._MEIPASS #PyInstaller temporary directory
#   else:
#     base_path = os.path.abspath(os.path.dirname(__file__))
#   return os.path.join(base_path, 'ui', 'autoTypedKeyboard_text.ui')

# def getUIFilePath(self):
#   if getattr(sys, 'frozen', False):
#     base_path = sys._MEIPASS #PyInstaller temporary directory
#   else:
#     base_path = os.path.abspath(os.path.dirname(__file__))
#   return base_path

# Application Constants
APP_NAME = "Devalltect00 - Auto Type"
APP_VERSION = "1.0.0"

# Colors
BACKGROUND_COLOR = "#ffffff"
PRIMARY_COLOR = "#55AA00"
SECONDARY_COLOR = "#55AA00"

# File Path Constants
# UI_FILE_PATH = os.path.join(BASE_DIR, 'app', 'ui', 'autoTypedKeyboard_text.ui')
UI_FILE_PATH = os.path.join(BASE_DIR, 'ui', 'autoTypedKeyboard_text.ui')
# ICON_FILE_PATH = os.path.join(BASE_DIR, 'app', 'resources', 'images', 'logo-devalltect00.png')
ICON_FILE_PATH = os.path.join(BASE_DIR, 'resources', 'images', 'logo-devalltect00.png')
# ICON_FILE_PATH = "app/resources/images/logo-devalltect00.png"

# Style Constants
class STYLE:
  BUTTON = """
    QPushButton {
      color: rgb(85, 170, 0);
      background-color: rgb(255, 255, 255);
      border-radius:10px;
      padding:10px;
    }
    QPushButton:hover {
      color: rgb(85, 170, 0, 192);
      background-color: rgb(255, 255, 255);
      border-radius:10px;
      padding:10px;
    }
  """
  TOOLTIP = """
    QToolTip {
      color: #FFFFFF;
    }
  """
