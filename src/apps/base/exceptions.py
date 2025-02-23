class MessageException(Exception):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message)
        if message is not None:
            self.message = message


class BusinessRuleValidationError(MessageException):
    pass
