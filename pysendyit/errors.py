class UnAuthorisedException(Exception):
    """
    Exception for requests that are being used without appropriate authorisation
    """
    def __init__(self, message, http_response):
        super(UnAuthorisedException, self).__init__()
        self.message = message
        self.status = http_response.status

    @property
    def get_message(self):
        """
        Returns the message of the Un authorised error
        :returns message: str
        """
        return self.message


class MalformedRequestException(Exception):
    """
    Thrown if the request being sent is malformed or missing some paramters
    """
    def __init__(self, message, http_response):
        super(MalformedRequestException, self).__init__()
        self.message = message
        self.status = http_response.status

    @property
    def get_message(self):
        """
        Returns the message of the Un authorised error
        :returns message: str
        """
        return self.message


class NotFoundException(Exception):
    """
    Thrown if the request being sent is not available
    """
    def __init__(self, message, http_response):
        super(NotFoundException, self).__init__()
        self.message = message
        self.status = http_response.status

    @property
    def get_message(self):
        """
        Returns the message of the Un authorised error
        :returns message: str
        """
        return self.message


class UnAcceptableContentException(Exception):
    """
    Thrown if the request being sent has a header for a content type which isn't on the server
    """
    def __init__(self, message, http_response):
        super(UnAcceptableContentException, self).__init__()
        self.message = message
        self.status = http_response.status

    @property
    def get_message(self):
        """
        Returns the message of the Un authorised error
        :returns message: str
        """
        return self.message


class InvalidRequestException(Exception):
    """
    Thrown if the request being sent is parse-able but has invalid content
    """
    def __init__(self, message, http_response):
        super(InvalidRequestException, self).__init__()
        self.message = message
        self.status = http_response.status

    @property
    def get_message(self):
        """
        Returns the message of the Un authorised error
        :returns message: str
        """
        return self.message


class RateLimitException(Exception):
    """
    Thrown if the requests being sent are too many
    """
    def __init__(self, message, http_response):
        super(RateLimitException, self).__init__()
        self.message = message
        self.status = http_response.status

    @property
    def get_message(self):
        """
        Returns the message of the Un authorised error
        :returns message: str
        """
        return self.message


class ServerException(Exception):
    """
    Thrown if the there is internal server error
    """
    def __init__(self, message, http_response):
        super(ServerException, self).__init__()
        self.message = message
        self.status = http_response.status

    @property
    def get_message(self):
        """
        Returns the message of the Un authorised error
        :returns message: str
        """
        return self.message


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
        Returns the message of the Un authorised error
        :returns message: str
        """
        return self.message
