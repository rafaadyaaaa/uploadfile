from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

app = QApplication([])
window =  QWidget()
window.setWindowTitle('My First app')
window.resize(400, 300)
title = QLabel('Hello world')
v_layout = QVBoxLayout()
v_layout.addwidget(title, alignment=Qt.AlignCenter)
window.setLayout(v_layout)
window.show()
app.exec_()