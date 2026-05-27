class OfflineFallback:
    def __init__(self, cache_service):
        self.cache_service = cache_service

    def get_response(self, user_input: str) -> str:
        cached = self.cache_service.lookup(user_input)
        if cached:
            return f"(cached) {cached}"
        return "Sorry, I could not understand that or the service is unavailable."