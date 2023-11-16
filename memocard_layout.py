from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

btn_menu = QPushButton('menu')
btn_sleep = QPushButton('sleep')
box_minutes = Q5pinBox()
box_minutes.setValue(30)
slp_text = QLabel('minets')

text_question = QLabel('')
question_group_box =  QGroupBox('варіанти відповідей')

btn_group = QButtonGroup()

rbt1 = QRadioButton()
rbt2 = QRadioButton()
rbt3 = QRadioButton()
rbt4 = QRadioButton()

btn_group.addButton(rbt1)
btn_group.addButton(rbt2)
btn_group.addButton(rbt3)
btn_group.addButton(rbt4)

answer_group = QGroupBox('результати тесту:')
text_res = QLabel()
text_correct = QLabel()

layout_question = QBoxLayout()
layout_question1 = QBoxLayout()
layout_question2 = QBoxLayout()

layout_question1.addWidget(rbt1)
layout_question1.addWidget(rbt2)
layout_question2.addWidget(rbt3)
layout_question2.addWidget(rbt4)
layout_question.addLayout(layout_question1)
layout_question.addLayout(layout_question2)
question_group_box.setLayout(layout_question)

layout_answer = QBoxLayout()
layout_answer.addWidget(text_res, aligment = (Qt.Alitop | Qt.Alignleft))
layout_answer.addWidget(text_correct, aligment = Qt.Aligncentre)
answer_group_box.setLayout(layout_answer)
answer_group_box.hide()

line1 = QHBoxLayout()
line1.addWidget(btn_menu)
line1.addStrech(1)
line1.addWidget(btn_sleep)
line1.addWidget(box_minutes)
line1.addWidget(slp_text)

line2 = QHBoxLayout()
line2.addWidget(text_question)

line3 = QHBoxLayout()
line3.addWidget(question_group_box)
line3.addWidget(answer_group_box)

line4 = QHBoxLayout()
line4.addSpancing(1)
line4.addWidget(btn_answer, strech = 1)
line4.addSpancing(1)

main_line = QHBoxLayout()
main_line.addLayout(line1,strech=1)
main_line.addLayout(line2,strech=2)
main_line.addLayout(line3,strech=3)
main_line.addSpancing(1)
main_line.addLayout(line4,strech=4)
main_line.addSpancing(1)

def show_res():
    def show_question():
    question_group_box.show()
    answer_group_box.hide()
    btn_answer.setText('відповісти')

def show_question():
    question_group_box.show()
    answer_group_box.hide()
    btn_answer.setText('відповісти')
    btn_group.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    btn_group.setExclusive(True)