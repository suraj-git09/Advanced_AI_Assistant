import platform
from datetime import datetime

from commands.base import Command


class SystemInfoCommand(Command):
    name = "system_info"
    description = "Shows basic system information"

    async def execute(self, user_input: str, context: dict) -> str:
        text = user_input.lower().strip()

        if "time" in text:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return f"Current time: {current_time}"

        system = platform.system()
        release = platform.release()
        version = platform.version()
        machine = platform.machine()
        processor = platform.processor()

        return (
            f"System: {system}\n"
            f"Release: {release}\n"
            f"Version: {version}\n"
            f"Machine: {machine}\n"
            f"Processor: {processor}"
        )