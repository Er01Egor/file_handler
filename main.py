import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>833</width>
    <height>676</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="create_file_button">
   <property name="geometry">
    <rect>
     <x>520</x>
     <y>40</y>
     <width>181</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Создать файл</string>
   </property>
  </widget>
  <widget class="QPushButton" name="open_file_button">
   <property name="geometry">
    <rect>
     <x>520</x>
     <y>110</y>
     <width>181</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Открыть существующий</string>
   </property>
  </widget>
  <widget class="QPushButton" name="read_file_button">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>170</y>
     <width>111</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Прочитать</string>
   </property>
  </widget>
  <widget class="QPushButton" name="correct_file_button">
   <property name="geometry">
    <rect>
     <x>210</x>
     <y>170</y>
     <width>111</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Изменить</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="file_names">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>70</y>
     <width>371</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
  <widget class="QTextEdit" name="file_content">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>270</y>
     <width>801</width>
     <height>371</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="save_button">
   <property name="geometry">
    <rect>
     <x>490</x>
     <y>210</y>
     <width>111</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Сохранить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="delete_button">
   <property name="geometry">
    <rect>
     <x>630</x>
     <y>210</y>
     <width>111</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Удалить </string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class FileHandler(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileHandler()
    window.show()
    sys.exit(app.exec())
