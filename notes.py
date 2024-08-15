import json
import os

class NoteApp:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.notes, file, indent=4)

    def create_note(self, title, content):
        note = {'title': title, 'content': content}
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        return self.notes

    def edit_note(self, index, title, content):
        if 0 <= index < len(self.notes):
            self.notes[index] = {'title': title, 'content': content}
            self.save_notes()
        else:
            print("Заметка не найдена.")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
            self.save_notes()
        else:
            print("Заметка не найдена.")

    def display_notes(self):
        for idx, note in enumerate(self.notes):
            print(f"{idx}. {note['title']}: {note['content']}")

def main():
    app = NoteApp()

    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")
            app.create_note(title, content)
            print("Заметка создана.")
        
        elif choice == '2':
            print("Список заметок:")
            app.display_notes()
        
        elif choice == '3':
            index = int(input("Введите номер заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            content = input("Введите новое содержание заметки: ")
            app.edit_note(index, title, content)
            print("Заметка отредактирована.")
        
        elif choice == '4':
            index = int(input("Введите номер заметки для удаления: "))
            app.delete_note(index)
            print("Заметка удалена.")
        
        elif choice == '5':
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
