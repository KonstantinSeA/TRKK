import io
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1030</width>
    <height>835</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPlainTextEdit" name="text1_2">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>80</y>
      <width>501</width>
      <height>661</height>
     </rect>
    </property>
   </widget>
   <widget class="QDoubleSpinBox" name="alert_value">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>10</y>
      <width>851</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="text1">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>501</width>
      <height>661</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="checkBtn">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>750</y>
      <width>1011</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Сравнить</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_t1">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>50</y>
      <width>481</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Текст 1</string>
    </property>
    <property name="textFormat">
     <enum>Qt::AutoText</enum>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_t2">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>50</y>
      <width>481</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Текст 2</string>
    </property>
    <property name="textFormat">
     <enum>Qt::AutoText</enum>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>151</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Порог срабатывания (%)</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1030</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.checkBtn.clicked.connect(self.run_check)

    def run_check(self):
        ft = self.text1.toPlainText()
        print(ft)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())
