from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
    def start(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                self.add_note()
            elif choice == '2':
                self.edit_note()
            elif choice == '3':
                self.delete_note()
            elif choice == '4':
                self.show_notes()
            elif choice == '5':
                break
            else:
                self.view.show_error('Неверный выбор')

    def add_note(self):
        title = self.view.get_input('Введите заголовок заметки: ')
        body = self.view.get_input('Введите текст заметки: ')
        note = {'title': title, 'body': body}
        self.model.add(note)
        self.view.show_message('Заметка успешно добавлена')

    def edit_note(self):
        id_ = self.view.get_input('Введите id заметки: ')
        title = self.view.get_input('Введите новый заголовок (оставьте пустым, чтобы оставить прежний): ')
        body = self.view.get_input('Введите новый текст (оставьте пустым, чтобы оставить прежний): ')
        note = {'title': title, 'body': body}
        self.model.edit(id_, note)
        self.view.show_message('Заметка успешно изменена')

    def delete_note(self):
        id_ = self.view.get_input('Введите id заметки: ')
        self.model.delete(id_)
        self.view.show_message('Заметка успешно удалена')

    def show_notes(self):
        notes = self.model.get_all()
        if notes:
            for note in notes:
                self.view.show_note(note)
        else:
            self.view.show_message('Заметок не найдено')