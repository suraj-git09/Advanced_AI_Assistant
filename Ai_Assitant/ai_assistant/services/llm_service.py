import os
import asyncio
from openai import OpenAI


class LLMService:
    def __init__(self, conversation_memory, api_key=None, base_url=None, model=None):
        self.api_key = api_key or os.getenv("sk-9dd3baf18fc99b648c6fbeeb11b14b97a93e4b747233673bb80b36d7355db4ba")
        self.base_url = base_url or os.getenv("https://portal.torouter.ai/api/v1")
        self.model = model or os.getenv("OPENAI_MODEL", "openai/gpt-4o-mini")
        self.conversation_memory = conversation_memory

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def _call_model(self, user_input: str) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ] + self.conversation_memory.get_messages() + [
            {"role": "user", "content": user_input}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )

        return response.choices[0].message.content.strip()

    async def answer_question(self, user_input: str) -> str:
        return await asyncio.to_thread(self._call_model, user_input)