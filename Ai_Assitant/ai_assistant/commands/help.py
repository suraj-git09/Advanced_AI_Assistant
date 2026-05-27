from commands.base import Command


class HelpCommand(Command):
    name = "help"
    description = "Shows available commands"

    async def execute(self, user_input: str, context: dict) -> str:
        return (
            "I can help you with:\n"
            "- Calculations\n"
            "- Saving notes\n"
            "- Showing saved notes\n"
            "- System information\n"
            "- Current time\n"
            "\nTry commands like:\n"
            "- calculate 5 + 3\n"
            "- save note buy milk\n"
            "- show notes\n"
            "- system info\n"
            "- what is the time"
        )