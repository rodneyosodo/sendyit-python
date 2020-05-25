import json
import requests
from pysendyit.errors import (MalformedRequestException, ServerException,
                              UnAuthorisedException, NotFoundException,
                              UnAcceptableContentException,
                              RateLimitException, InvalidRequestException)
from pysendyit.check import check_url, check_api_details


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
        self.api_key = check_api_details(api_details=api_key)
        self.api_username = check_api_details(api_details=api_username)
        self.base_url = check_url(path=base_url)

    @staticmethod
    def check_status(content, response):
        """
        Checks the response that is returned for known exceptions and errors
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

    def _build_url(self, path):
        """
        Build the url to send to the server
        :param path:
        :type path: str
        :return:
        """
        url = check_url(path=self.base_url)
        self.base_url = url + "#" + path

    def make_request(self, url_parameter=None, body=None):
        self._build_url(path=url_parameter)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(self.base_url, data=body, headers=headers)
        self.check_status(response=response, content=response.content)
        return json.loads(response.content.decode('utf-8'))
