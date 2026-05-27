from commands.base import Command


class GeneralQACommand(Command):
    name = "general_qa"
    description = "Handles general questions using offline-first logic"

    def __init__(self, cache_service, knowledge_base_service, llm_service=None, conversation_memory=None):
        self.cache_service = cache_service
        self.knowledge_base_service = knowledge_base_service
        self.llm_service = llm_service
        self.conversation_memory = conversation_memory

    def _is_valid_cached_response(self, response: str) -> bool:
        if not response:
            return False

        bad_phrases = [
            "i do not have an offline answer",
            "online ai service is unavailable",
            "sorry",
            "could not",
            "service is unavailable",
            "error",
            "failed"
        ]

        response_lower = response.lower()
        return not any(phrase in response_lower for phrase in bad_phrases)

    async def execute(self, user_input: str, context: dict) -> str:
        cached = self.cache_service.lookup(user_input)
        if cached and self._is_valid_cached_response(cached):
            return f"(cached) {cached}"

        offline_answer = self.knowledge_base_service.answer(user_input)
        if offline_answer:
            self.cache_service.save(user_input, offline_answer)
            return offline_answer

        if self.llm_service is not None:
            try:
                llm_answer = await self.llm_service.answer_question(user_input)

                if self.conversation_memory:
                    self.conversation_memory.add_user_message(user_input)
                    self.conversation_memory.add_assistant_message(llm_answer)

                if llm_answer and self._is_valid_cached_response(llm_answer):
                    self.cache_service.save(user_input, llm_answer)

                return llm_answer
            except Exception as e:
                print("LLM ERROR:", e)

        return "I do not have an offline answer for that, and the online AI service is unavailable."