from PyQt5.QtWidgets import QMainWindow, QApplication, QToolTip, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QTimer
import keyboard
import time
import os
import sys

import const

class AutoTypedKeyboardTextGui(QMainWindow):
  def __init__(self, parent=None):
    super().__init__()

    self.UI_FILE = const.UI_FILE_PATH
    # loadUi(self.getUIFilePath(), self)
    loadUi(self.UI_FILE, self)

    self.initUI()
  def initUI(self):
    # Add Tooltip
    self.pushButton_ChooseFile.setToolTip("Choose file from your PC")
    self.pushButton_Start.setToolTip("Start 'AUTO TYPE' in 5 seconds")

    # Add External Styling
    self.pushButton_ChooseFile.setStyleSheet(const.STYLE.BUTTON)
    self.pushButton_Start.setStyleSheet(const.STYLE.BUTTON)

    QToolTip.setFont(QFont('SansSerif',10))
    self.setStyleSheet(const.STYLE.TOOLTIP)

    #Set Icon
    self.setWindowIcon(QIcon(const.ICON_FILE_PATH))

    #Set Title
    self.setWindowTitle(f"{const.APP_NAME} v{const.APP_VERSION}")

    #Add Functionality
    self.pushButton_ChooseFile.clicked.connect(self.chooseFile)
    self.pushButton_Start.clicked.connect(self.start)

    #Set Timer
    self.timer = QTimer()
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.countDown)
    self.count_timer_in_seconds = 5
    self.label_CountDownNumber.setText("")
    self.label_CountDownString.setText("")

    #Set Label Initial
    self.label_CountDownNumber.setText("")
    self.label_CountDownString.setText("")
    self.label_Info.setText("")

  def chooseFile(self):self.showFileDialog()
  
  def showFileDialog(self):
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All File (*.*);;Text Files (*.txt)', options=options)

    if file_path:
      print(file_path)
      self.readFileContent(file_path)
      self.label_Info.setText("")
    else:
      self.label_Info.setText('No file selected')
  
  def readFileContent(self, file_path):
    try:
      with open(file_path, 'r') as file:
        content = file.read()
        self.textInputField.setText(content)
        self.label_Info.setText("")
    except Exception as e:
      self.label_Info.setText(f"Error reading file : {e}")

  def start(self):
    txt = self.textInputField.toPlainText()
    self.seperated = list(map(str.strip, txt.split(",")))

    # count 5 seconds to start
    self.startCountDownTimer()

    # for second in range(5,0,-1):
    #   self.label_CountDownNumber.setText(str(second))
    #   print(str(second))
    self.label_CountDownString.setText("GET READY")
    self.label_CountDownNumber.setText("")
    self.label_Info.setText("")

  def startCountDownTimer(self):self.timer.start()

  def countDown(self):
    self.label_CountDownNumber.setText(str(self.count_timer_in_seconds))
    if self.count_timer_in_seconds == 0:
      self.label_CountDownString.setText("")
      self.label_CountDownNumber.setText("START")

    if self.count_timer_in_seconds < 0:
      self.label_CountDownString.setText("")
      self.label_CountDownNumber.setText("")
      self.count_timer_in_seconds=5
      self.timer.stop()
      self.typeWords(self.seperated)
      self.label_Info.setText("Finished")
    self.count_timer_in_seconds-=1

  @staticmethod
  def typeWords(words):
    print(words)
    for word in words:
      for letter in word:
        if letter.isupper():
          keyboard.press_and_release('shift+' + letter.lower())
        else:
          keyboard.press_and_release(letter)
        time.sleep(0.1)
      keyboard.press_and_release('enter')
      time.sleep(0.1)
    

if __name__ == "__main__":
  app = QApplication([])
  window = AutoTypedKeyboardTextGui()
  window.show()
  app.exec_()