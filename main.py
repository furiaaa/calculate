from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Calculate")
window.setStyleSheet('background-color: grey; color:white; font-size: 40px')



line_edit = QLineEdit()
button_0 = QPushButton('0')
button_1 = QPushButton('1')
button_1.setStyleSheet('background-color:#b3cccc')
button_2 = QPushButton('2')
button_2.setStyleSheet('background-color:#b3cccc')
button_3 = QPushButton('3')
button_3.setStyleSheet('background-color:#b3cccc')
button_4 = QPushButton('4')
button_4.setStyleSheet('background-color:#b3cccc')
button_5 = QPushButton('5')
button_5.setStyleSheet('background-color:#b3cccc')
button_6 = QPushButton('6')
button_6.setStyleSheet('background-color:#b3cccc')
button_7 = QPushButton('7')
button_7.setStyleSheet('background-color:#b3cccc')
button_8 = QPushButton('8')
button_8.setStyleSheet('background-color:#b3cccc')
button_9 = QPushButton('9')
button_9.setStyleSheet('background-color:#b3cccc')
button_plus = QPushButton('+')
button_plus.setStyleSheet('background-color:#669999')
button_minus = QPushButton('-')
button_minus.setStyleSheet('background-color:#669999')
button_multiply = QPushButton('*')
button_multiply.setStyleSheet('background-color:#669999')
button_divide = QPushButton('/')
button_divide.setStyleSheet('background-color:#669999')
button_dot = QPushButton('.')
button_delete = QPushButton('CE')
button_equals = QPushButton('=')

h1 = QHBoxLayout()
h1.addWidget(button_7)
h1.addWidget(button_8)
h1.addWidget(button_9)
h1.addWidget(button_plus)

h2 = QHBoxLayout()
h2.addWidget(button_4)
h2.addWidget(button_5)
h2.addWidget(button_6)
h2.addWidget(button_minus)


h3 = QHBoxLayout()
h3.addWidget(button_1)
h3.addWidget(button_2)
h3.addWidget(button_3)
h3.addWidget(button_multiply)

h4 = QHBoxLayout()
h4.addWidget(button_0)
h4.addWidget(button_dot)
h4.addWidget(button_divide)


h5 = QHBoxLayout()
h5.addWidget(button_delete)
h5.addWidget(button_equals)

main_layout = QVBoxLayout()
main_layout.addWidget(line_edit)
main_layout.addLayout(h1)
main_layout.addLayout(h2)
main_layout.addLayout(h3)
main_layout.addLayout(h4)
main_layout.addLayout(h5)

window.setLayout(main_layout)
window.show()
app.exec_()




