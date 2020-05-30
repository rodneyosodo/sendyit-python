import unittest
import requests
import os
from pysendyit.api import Api
from pysendyit.errors import (MalformedRequestException, ServerException,
                              UnAuthorisedException, NotFoundException,
                              UnAcceptableContentException,
                              RateLimitException, InvalidRequestException)

api_username = os.getenv('API_USERNAME')
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.api = Api(api_key=api_key,
                       api_username=api_username,
                       base_url=base_url)
        self.url_parameter = "track"
        self.request_data = {"command": "track", "order_no": "AA2395374",
                             "request_token_id": "request_token_id"}
        self.response = requests.Response

    def test_check_status_MalformedRequestException(self):
        self.response.status_code = 400
        self.assertRaises(MalformedRequestException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_UnAuthorisedException(self):
        self.response.status_code = 401
        self.assertRaises(UnAuthorisedException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_NotFoundException(self):
        self.response.status_code = 404
        self.assertRaises(NotFoundException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_UnAcceptableContentException(self):
        self.response.status_code = 406
        self.assertRaises(UnAcceptableContentException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_InvalidRequestException(self):
        self.response.status_code = 422
        self.assertRaises(InvalidRequestException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_RateLimitException(self):
        self.response.status_code = 429
        self.assertRaises(RateLimitException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_ServerException_1(self):
        self.response.status_code = 500
        self.assertRaises(ServerException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_ServerException_2(self):
        self.response.status_code = 501
        self.assertRaises(ServerException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_ServerException_3(self):
        self.response.status_code = 502
        self.assertRaises(ServerException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_ServerException_4(self):
        self.response.status_code = 503
        self.assertRaises(ServerException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_ServerException_5(self):
        self.response.status_code = 504
        self.assertRaises(ServerException, self.api.check_status,
                          self.response.content, self.response)

    def test_check_status_ServerException_6(self):
        self.response.status_code = 505
        self.assertRaises(ServerException, self.api.check_status,
                          self.response.content, self.response)

    def test_build_url_1(self):
        self.api._build_url(path=self.url_parameter)
        self.assertIsNotNone(self.api.base_url)

    def test_build_url_2(self):
        self.api._build_url(path=self.url_parameter)
        self.assertIn("#", self.api.base_url)

    def test_build_url_3(self):
        self.api._build_url(path=self.url_parameter)
        url = base_url + "#" + self.url_parameter
        self.assertEqual(self.api.base_url, url)

    def test_make_request_1(self):
        response = self.api.make_request(url_parameter=self.url_parameter,
                                         body=self.request_data)
        self.assertIsNotNone(response)

    def test_make_request_2(self):
        response = self.api.make_request(url_parameter=self.url_parameter,
                                         body=self.request_data)
        self.assertEqual(response['status'], True)

    def test_make_request_3(self):
        response = self.api.make_request(url_parameter=self.url_parameter,
                                         body=self.request_data)
        self.assertTrue(type(response) == dict)


if __name__ == '__main__':
    unittest.main()
