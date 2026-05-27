class IntentClassifier:
    def predict(self, user_input: str) -> str:
        text = user_input.lower().strip()

        if any(word in text for word in ["help", "what can you do", "what all can you do", "commands"]):
            return "help"

        if any(word in text for word in ["save note", "show notes", "note", "remember this"]):
            return "notes"

        if any(word in text for word in ["system info", "cpu", "memory", "battery", "os", "time"]):
            return "system_info"

        if any(word in text for word in ["weather", "temperature", "forecast", "rain"]):
            return "weather"

        math_symbols = ["+", "-", "*", "/"]
        math_words = ["calculate", "solve"]

        if any(symbol in text for symbol in math_symbols):
            return "calculate"

        if any(word in text for word in math_words):
            return "calculate"

        return "general_qa"