from PyQt5.QtWidgets import QApplication
from gui import AutoTypedKeyboardTextGui

def main():
  app = QApplication([])
  window = AutoTypedKeyboardTextGui()
  
  window.show()
  app.exec_()

if __name__ == '__main__':
  main()