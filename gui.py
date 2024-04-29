import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Simple App'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Создаем метку
        label = QLabel('Введите ваше имя:', self)
        label.move(20, 20)

        # Создаем строку ввода
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(100, 20)

        # Создаем кнопку
        button = QPushButton('Просмотреть', self)
        button.clicked.connect(self.on_click)
        button.move(200, 20)

        # Добавляем виджеты в контейнер
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(self.lineEdit)
        vbox.addWidget(button)
        self.setLayout(vbox)

        self.show()

    def on_click(self):
        name = self.lineEdit.text()
        label = QLabel(f'Привет, {name}!', self)
        label.move(300, 20)

app = QApplication(sys.argv)
window = SimpleApp()
sys.exit(app.exec_())