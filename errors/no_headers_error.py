class NoHeadersException(Exception):
    """When get_headers returns None"""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message