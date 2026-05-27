from commands.base import Command


class NotesCommand(Command):
    name = "notes"
    description = "Saves and retrieves notes"

    def __init__(self, storage_service):
        self.storage_service = storage_service

    async def execute(self, user_input: str, context: dict) -> str:
        text = user_input.strip()
        lower_text = text.lower()

        if lower_text.startswith("save note"):
            note = text[len("save note"):].strip()

            if not note:
                return "Please provide a note to save."

            self.storage_service.save_note(note)
            return f"Note saved: {note}"

        elif lower_text == "show notes":
            notes = self.storage_service.get_notes()

            if not notes:
                return "No notes found."

            return "Your notes:\n" + "\n".join(f"- {note}" for note in notes)

        return "Try 'save note <your note>' or 'show notes'."