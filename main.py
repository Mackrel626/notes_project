from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QTextEdit, QLineEdit, QListWidget

import json

app = QApplication([])
window = QWidget()

notes = {
    "ласкаво" : {
        "текст" : "додаток для заміток",
        "теги" : ["ласкаво","замітки"]
    }
}
with open("notes_data.json", "w", encoding="utf-8") as file:
    json.dump(notes, file)


text_note = QTextEdit()
h_main = QHBoxLayout()
h_main.addWidget(text_note, stretch=2)

v1 = QVBoxLayout()
lbl_notelist = QLabel("Список заміток")
v1.addWidget(lbl_notelist)
list_note = QListWidget()
v1.addWidget(list_note)

btn_create = QPushButton('Створити замітку')
btn_delete = QPushButton('Видалити замітку')
btn_save = QPushButton('Зберегти замітку')
h2 = QHBoxLayout()
h2.addWidget(btn_create)
h2.addWidget(btn_delete)
v1.addLayout(h2)
v1.addWidget(btn_save)

lbl_taglist = QLabel("Список тегів")
list_tag = QListWidget()
line_tag = QLineEdit()
line_tag.setPlaceholderText("Введіть тег...")

btn_append = QPushButton('Додати до замітку')
btn_clear = QPushButton('Відкріпити від замітку')
btn_search = QPushButton('Шукати замітки за тегами')
h3 = QHBoxLayout()
h3.addWidget(btn_append)
h3.addWidget(btn_clear)

v1.addWidget(lbl_taglist)
v1.addWidget(list_tag)
v1.addWidget(line_tag)
v1.addLayout(h3)
v1.addWidget(btn_search)










h_main.addLayout(v1, stretch=1)
window.setLayout(h_main)
window.show()

def show_note():
    key = list_note.selectedItems()[0].text()
    print(key)
    text_note.setText(notes[key]["текст"])
    list_tag.clear()
    list_tag.addItems(notes[key]["теги"])

list_note.itemClicked.connect(show_note)

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_note.addItems(notes)

app.exec_()