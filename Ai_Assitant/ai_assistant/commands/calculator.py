from commands.base import Command


class CalculatorCommand(Command):
    name = "calculate"
    description = "Performs basic math calculations"

    async def execute(self, user_input: str, context: dict) -> str:
        text = user_input.lower()

        for word in ["calculate", "what is", "solve"]:
            text = text.replace(word, "")

        expression = text.strip()

        try:
            result = eval(expression, {"__builtins__": {}})
            return f"Result: {result}"
        except Exception:
            return "Sorry, I could not calculate that."