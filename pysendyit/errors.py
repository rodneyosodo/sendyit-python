class BaseSendyException(Exception):
    """
    Base exception for all exceptions produced
    """
    def __init__(self, message, http_response):
        self.message = message
        self.status = http_response.status_code
        super(BaseSendyException, self).__init__()

    @property
    def get_message(self):
        """
        Returns this message
        :returns message: str
        """
        return self.message


class UnAuthorisedException(BaseSendyException):
    """
    Exception for requests that are being used without appropriate authorisation
    """


class MalformedRequestException(BaseSendyException):
    """
    Thrown if the request being sent is malformed or missing some paramters
    """


class NotFoundException(BaseSendyException):
    """
    Thrown if the request being sent is not available
    """


class UnAcceptableContentException(BaseSendyException):
    """
    Thrown if the request being sent has a header for a content type which isn't on the server
    """


class InvalidRequestException(BaseSendyException):
    """
    Thrown if the request being sent is parse-able but has invalid content
    """


class RateLimitException(BaseSendyException):
    """
    Thrown if the requests being sent are too many
    """


class ServerException(BaseSendyException):
    """
    Thrown if the there is internal server error
    """


class SendyException(Exception):
    """
    General exception throw
    """
    def __init__(self, message):
        super(SendyException, self).__init__()
        self.message = message

    @property
    def get_message(self):
        """
        Returns this message
        :returns message: str
        """
        return self.message
