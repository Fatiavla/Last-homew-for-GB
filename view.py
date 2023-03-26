from datetime import datetime
class View:
    def show_menu(self):
        print('1. Добавить заметку')
        print('2. Редактировать заметку')
        print('3. Удалить заметку')
        print('4. Показать все заметки')
        print('5. Выход')
        return input('Выберите действие: ')

    def get_input(self, message):
        return input(message)

    def show_error(self, message):
        print(message)

    def show_message(self, message):
        print(message)

    def show_note(self, note):
        print(f'ID: {note["id"]}')
        print(f'Заголовок: {note["title"]}')
        print(f'Текст: {note["body"]}')
        print(f'Дата создания: {note["created_at"]}')
        print(f'Дата изменения: {note["updated_at"]}')