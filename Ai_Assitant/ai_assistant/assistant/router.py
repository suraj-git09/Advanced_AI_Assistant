class Router:
    def __init__(self, classifier, registry, fallback, cache):
        self.classifier = classifier
        self.registry = registry
        self.fallback = fallback
        self.cache = cache

    async def route(self, user_input: str) -> str:
        intent = self.classifier.predict(user_input)
        command = self.registry.get_command(intent)

        if command:
            try:
                response = await command.execute(user_input, context={})

                # If local command cannot answer, try general_qa
                if response is None:
                    general_command = self.registry.get_command("general_qa")
                    if general_command:
                        return await general_command.execute(user_input, context={})

                    return self.fallback.get_response(user_input)

                return response

            except Exception:
                return self.fallback.get_response(user_input)

        # If no intent-specific command found, try general_qa
        general_command = self.registry.get_command("general_qa")
        if general_command:
            return await general_command.execute(user_input, context={})

        return self.fallback.get_response(user_input)