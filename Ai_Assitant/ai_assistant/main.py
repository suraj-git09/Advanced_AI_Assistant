import asyncio
from dotenv import load_dotenv

from assistant.core import AssistantCore
from assistant.router import Router
from assistant.fallback import OfflineFallback

from commands.registry import CommandRegistry
from commands.calculator import CalculatorCommand
from commands.notes import NotesCommand
from commands.system_info import SystemInfoCommand
from commands.help import HelpCommand
from commands.weather import WeatherCommand
from commands.general_qa import GeneralQACommand

from nlp.intent_classifier import IntentClassifier

from services.cache import CacheService
from services.storage import StorageService
from services.scheduler import BackgroundWorker
from services.llm_service import LLMService
from services.knowledge_base import KnowledgeBaseService
from services.conversation_memory import ConversationMemory


async def main():
    load_dotenv()

    print("Starting AI Assistant...")

    # Initialize services
    cache_service = CacheService(db_path="data/cache.db")
    storage_service = StorageService(notes_file="data/notes.json")
    fallback_service = OfflineFallback(cache_service)
    knowledge_base_service = KnowledgeBaseService()
    conversation_memory = ConversationMemory()
    llm_service = LLMService(conversation_memory=conversation_memory)

    # Initialize NLP
    intent_classifier = IntentClassifier()

    # Initialize command registry
    registry = CommandRegistry()
    registry.register(CalculatorCommand())
    registry.register(NotesCommand(storage_service))
    registry.register(SystemInfoCommand())
    registry.register(HelpCommand())
    registry.register(WeatherCommand())
    registry.register(
        GeneralQACommand(
            cache_service=cache_service,
            knowledge_base_service=knowledge_base_service,
            llm_service=llm_service,
            conversation_memory=conversation_memory
        )
    )

    # Initialize router and assistant core
    router = Router(
        classifier=intent_classifier,
        registry=registry,
        fallback=fallback_service,
        cache=cache_service
    )

    assistant = AssistantCore(router)

    # Start background worker
    worker = BackgroundWorker()
    worker.start()

    print("Assistant is ready.")
    print("Type 'exit' to quit.\n")

    try:
        while True:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("Shutting down assistant...")
                break

            response = await assistant.handle_input(user_input)
            print(f"Assistant: {response}\n")

    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")

    finally:
        worker.stop()


if __name__ == "__main__":
    asyncio.run(main())

# import asyncio
# from dotenv import load_dotenv
# from services.conversation_memory import ConversationMemory

# from assistant.core import AssistantCore
# from assistant.router import Router
# from assistant.fallback import OfflineFallback

# from commands.registry import CommandRegistry
# from commands.calculator import CalculatorCommand
# from commands.notes import NotesCommand
# from commands.system_info import SystemInfoCommand
# from commands.help import HelpCommand
# from commands.weather import WeatherCommand
# from commands.general_qa import GeneralQACommand

# from nlp.intent_classifier import IntentClassifier

# from services.cache import CacheService
# from services.storage import StorageService
# from services.scheduler import BackgroundWorker
# from services.llm_service import LLMService
# from services.knowledge_base import KnowledgeBaseService


# async def main():
#     load_dotenv()

#     print("Starting AI Assistant...")

#     # Initialize services
#     cache_service = CacheService(db_path="data/cache.db")
#     storage_service = StorageService(notes_file="data/notes.json")
#     fallback_service = OfflineFallback(cache_service)
#     llm_service = LLMService()
#     conversation_memory = ConversationMemory()
#     llm_service = LLMService(conversation_memory=conversation_memory)
#     knowledge_base_service = KnowledgeBaseService()

#     # Initialize NLP
#     intent_classifier = IntentClassifier()

#     # Initialize command registry
#     registry = CommandRegistry()
#     registry.register(CalculatorCommand())
#     registry.register(NotesCommand(storage_service))
#     registry.register(SystemInfoCommand())
#     registry.register(HelpCommand())
#     registry.register(WeatherCommand())
#     registry.register(GeneralQACommand(cache_service, knowledge_base_service, llm_service))

#     # Initialize router and core
#     router = Router(
#         classifier=intent_classifier,
#         registry=registry,
#         fallback=fallback_service,
#         cache=cache_service
#     )

#     assistant = AssistantCore(router)

#     # Start background worker
#     worker = BackgroundWorker()
#     worker.start()

#     print("Assistant is ready.")
#     print("Type 'exit' to quit.\n")

#     try:
#         while True:
#             user_input = input("You: ").strip()

#             if not user_input:
#                 continue

#             if user_input.lower() in ["exit", "quit"]:
#                 print("Shutting down assistant...")
#                 break

#             response = await assistant.handle_input(user_input)
#             print(f"Assistant: {response}\n")

#     except KeyboardInterrupt:
#         print("\nInterrupted by user. Exiting...")

#     finally:
#         worker.stop()


# if __name__ == "__main__":
#     asyncio.run(main())