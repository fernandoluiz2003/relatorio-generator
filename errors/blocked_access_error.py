class BlockedAccessException(Exception):
    """An exception for when there are many users logged in with the same certificate"""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message