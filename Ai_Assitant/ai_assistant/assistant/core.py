class AssistantCore:
    def __init__(self, router):
        self.router = router

    async def handle_input(self, user_input: str) -> str:
        response = await self.router.route(user_input)
        return response