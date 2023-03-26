import json
from datetime import datetime
class Model:
    def __init__(self):
        try:
            with open('notes.json', 'r') as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            self.notes = []

    def add(self, note):
        note['id'] = len(self.notes) + 1
        note['created_at'] = str(datetime.now())
        note['updated_at'] = str(datetime.now())
        self.notes.append(note)
        with open('notes.json', 'w') as f:
            json.dump(self.notes, f)

    def edit(self, id_, new_note):
        for note in self.notes:
            if note['id'] == int(id_):
                if new_note['title']:
                    note['title'] = new_note['title']
                if new_note['body']:
                    note['body'] = new_note['body']
                note['updated_at'] = str(datetime.now())
                with open('notes.json', 'w') as f:
                    json.dump(self.notes, f)
                return True
        return False

    def delete(self, id_):
        for i in range(len(self.notes)):
            if self.notes[i]['id'] == int(id_):
                del self.notes[i]
                with open('notes.json', 'w') as f:
                    json.dump(self.notes, f)
                return True
        return False

    def get_all(self):
        return self.notes