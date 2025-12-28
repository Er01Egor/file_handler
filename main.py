import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog

UI_FILE_NAME = 'style_ui.ui'


class FileHandler(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_FILE_NAME, self)

        self.name_f = ''

        self.create_file_button.clicked.connect(self.create_file)
        self.open_file_button.clicked.connect(self.choose_file)
        self.read_file_button.clicked.connect(self.file_open)
        # self.delete_button.clicked.connect(self.delete_text)
        self.save_button.clicked.connect(self.create_file)
        # self.correct_file_button.clicked.connect(self.correct_text)

    def file_open(self):

        try:
            file_name = self.name_f
            with open(file_name, 'r', encoding='utf-8') as file:
                content_file = file.read()

                self.file_content.setReadOnly(True)
                self.file_content.setText(content_file)

        except FileNotFoundError:
            print(f'Файл с именем: "{file_name}" отсутствовал')

        except Exception as err:
            print(f'Произошла ошибка: {err}')

    def create_file(self):
        try:
            file_name = self.file_names.text()

            full_content = self.file_content.toPlainText()

            with open(file_name, 'w', encoding='utf-8') as file:

                lines = full_content.splitlines()

                for line in lines:
                    cleaned_line = line.strip()

                    file.write(cleaned_line + '\n')
        except Exception as err:
            print(f'Произошла ошибка: {err}')

    def choose_file(self):
        self.file_names.clear()
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл')[0]
        self.name_f += self.fname
        self.file_names.setText(self.name_f)

    def delete_text(self):
        self.file_content.clear()

    def save_file_text(self):
        pass

    def correct_text(self):
        try:
            file_name = self.file_names.text()
            self.file_content.setReadOnly(False)

            full_content = self.file_content.toPlainText()

            with open(file_name, 'a', encoding='utf-8') as file:

                lines = full_content.splitlines()

                for line in lines:
                    cleaned_line = line.strip()

                    file.write(cleaned_line + '\n')
        except Exception as err:
            print(f'Произошла ошибка: {err}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileHandler()
    window.show()
    sys.exit(app.exec())
