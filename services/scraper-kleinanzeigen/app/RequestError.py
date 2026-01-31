class RequestError(Exception):
    def __init__(self, message: str, original_error: Exception = None):
        self.message = message
        self.original_error = original_error
        super().__init__(message)

    def __str__(self):
        if self.original_error:
            return f"{self.message} {self.original_error}"
        return self.message
