import json
import os


class StorageService:
    def __init__(self, notes_file="data/notes.json"):
        self.notes_file = notes_file
        os.makedirs(os.path.dirname(self.notes_file), exist_ok=True)

        if not os.path.exists(self.notes_file):
            with open(self.notes_file, "w", encoding="utf-8") as file:
                json.dump([], file)

    def save_note(self, note: str):
        notes = self.get_notes()
        notes.append(note)

        with open(self.notes_file, "w", encoding="utf-8") as file:
            json.dump(notes, file, indent=4)

    def get_notes(self):
        with open(self.notes_file, "r", encoding="utf-8") as file:
            return json.load(file)