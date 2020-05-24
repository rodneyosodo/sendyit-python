import json
import requests
from pysendyit.errors import *


class Api:
    """
    Base class to handle making requests and receiving responses
    """

    def __init__(self, api_key, api_username, base_url):
        """
        Creates and instance of a new Api object
        :param api_key: api key for the application provided by Sendy
        :param api_username: api username for the application provided by Sendy
        :param base_url: base url for the api application
        """
        self.api_key = api_key
        self.api_username = api_username
        self.base_url = base_url
        if self.api_key == "" or self.api_key is None:
            raise SendyException("API KEY is required")
        if self.api_username == "" or self.api_username is None:
            raise SendyException("API Username is required")
        if self.base_url == "" or self.base_url is None:
            raise SendyException("Base url is required")

    @staticmethod
    def check_status(content, response):
        """
        Checks the reponse that is returned for known exceptions and errors
        :param content:
        :param response:
        :return: str
        """
        if response.status_code == 400:
            raise MalformedRequestException(content, response)

        if response.status_code == 401:
            raise UnAuthorisedException(content, response)

        if response.status_code == 404:
            raise NotFoundException(content, response)

        if response.status_code == 406:
            raise UnAcceptableContentException(content, response)

        if response.status_code == 422:
            raise InvalidRequestException(content, response)

        if response.status_code == 429:
            raise RateLimitException(content, response)

        if response.status_code >= 500:
            raise ServerException(content, response)

    @staticmethod
    def _format_url(path):
        """
        Adds a "/" at the end if it does not exist.
        It also checks the path is the same as the ones available
        :param path:
        :type path: str
        :return: str
        """
        if path[-1] != "/":
            path = path + "/"
        if path == "https://apitest.sendyit.com/v1/" or path == "https://api.sendyit.com/v1/":
            return path
        else:
            raise SendyException("The Base url is not availble")

    def _build_url(self, path):
        """
        Build the url to send to the server
        :param path:
        :type path: str
        :return:
        """
        url = self._format_url(path=self.base_url)
        self.base_url = url + "#" + path

    def make_request(self, url_parameter=None, body=None):
        self._build_url(path=url_parameter)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(self.base_url, data=body, headers=headers)
        self.check_status(response=response, content=response.content)
        return json.loads(response.content.decode('utf-8'))
