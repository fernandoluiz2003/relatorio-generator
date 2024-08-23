class CaptchaException(Exception):
    """An exception for when the captcha appers in the begging of the run"""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message