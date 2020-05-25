class BaseSendyException(Exception):
    """
    Base exception for all exceptions produced
    """
    def __init__(self, message, http_response):
        self.message = message
        self.status = http_response.status_code

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
    def __init__(self, message, http_response):
        super(UnAuthorisedException, self).__init__(message=message, http_response=http_response)


class MalformedRequestException(BaseSendyException):
    """
    Thrown if the request being sent is malformed or missing some paramters
    """
    def __init__(self, message, http_response):
        super(MalformedRequestException, self).__init__(message=message, http_response=http_response)


class NotFoundException(BaseSendyException):
    """
    Thrown if the request being sent is not available
    """
    def __init__(self, message, http_response):
        super(NotFoundException, self).__init__(message=message, http_response=http_response)


class UnAcceptableContentException(BaseSendyException):
    """
    Thrown if the request being sent has a header for a content type which isn't on the server
    """
    def __init__(self, message, http_response):
        super(UnAcceptableContentException, self).__init__(message=message, http_response=http_response)


class InvalidRequestException(BaseSendyException):
    """
    Thrown if the request being sent is parse-able but has invalid content
    """
    def __init__(self, message, http_response):
        super(InvalidRequestException, self).__init__(message=message, http_response=http_response)


class RateLimitException(BaseSendyException):
    """
    Thrown if the requests being sent are too many
    """
    def __init__(self, message, http_response):
        super(RateLimitException, self).__init__(message=message, http_response=http_response)


class ServerException(BaseSendyException):
    """
    Thrown if the there is internal server error
    """
    def __init__(self, message, http_response):
        super(ServerException, self).__init__(message=message, http_response=http_response)


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
