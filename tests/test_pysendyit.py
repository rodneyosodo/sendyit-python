import unittest
import requests
import os
from pysendyit.pysendyit import Sendy
from pysendyit.errors import SendyException

api_username = os.getenv('API_USERNAME')
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')


class SendyTest(unittest.TestCase):
    def setUp(self):
        self.sendy = Sendy(api_key=api_key, api_username=api_username, base_url=base_url)
        self.url_parameter = "track"
        self.request_data = {"command":"track", "order_no":"AA2395374", "request_token_id":"request_token_id"}
        self.location_data = {"name":"test", "latitude":-1.300577, "longitude": 36.78183, "description": "test"}
        self.person_data = {"name":"test", "phone":"0712345678", "email": "test@mail.com", "notes": "test"}
        self.package_size = {"weight":"2", "height":"2", "width": "2", "length":"2", "item_name":"test"}
        self.payment_data = {"status":"test", "pay_method":"test", "amount": "200"}
        self.delivery_data = {
            "pick_up_date": "pick_up_date", "collect_payment": self.payment_data,
            "carrier_type": "carrier_type", "return": "return_type", "note": "note",
            "note_status": "note_status", "request_type": "request_type",
            "order_type": "order_type", "ecommerce_order": "ecommerce_order",
            "express": "express", "skew": "skew",
            "package_size": [self.package_size, self.package_size]
        }

    def test_prepare_location_details_1(self):
        self.assertNotEqual(self.location_data.values(), self.sendy.prepare_location_details("from", self.location_data['name'], self.location_data['latitude'], self.location_data['longitude'], self.location_data['description']).values())

    def test_prepare_location_details_2(self):
        self.assertNotEqual(self.location_data.values(), self.sendy.prepare_location_details("to", self.location_data['name'], self.location_data['latitude'], self.location_data['longitude'], self.location_data['description']).values())

    def test_prepare_location_details_3(self):
        self.assertIsNotNone(self.sendy.prepare_location_details("to", self.location_data['name'], self.location_data['latitude'], self.location_data['longitude'], self.location_data['description']))

    def test_prepare_location_details_4(self):
        self.assertRaises(SendyException, self.sendy.prepare_location_details, "test", self.location_data['name'], self.location_data['latitude'], self.location_data['longitude'], self.location_data['description'])

    def test_prepare_person_details_1(self):
        self.assertNotEqual(self.person_data.values(), self.sendy.prepare_person_details("recepient", self.person_data['name'], self.person_data['phone'], self.person_data['email'], self.person_data['notes']).values())

    def test_prepare_person_details_2(self):
        self.assertNotEqual(self.person_data.values(), self.sendy.prepare_person_details("sender", self.person_data['name'], self.person_data['phone'], self.person_data['email'], self.person_data['notes']).values())

    def test_prepare_person_details_3(self):
        self.assertIsNotNone(self.sendy.prepare_person_details("sender", self.person_data['name'], self.person_data['phone'], self.person_data['email'], self.person_data['notes']))

    def test_prepare_person_details_4(self):
        self.assertRaises(SendyException, self.sendy.prepare_person_details, "test", self.person_data['name'], self.person_data['phone'], self.person_data['email'], self.person_data['notes'])

    def test_prepare_package_size_1(self):
        self.assertDictEqual(self.package_size, self.sendy.prepare_package_size(self.package_size['weight'], self.package_size['height'], self.package_size['width'], self.package_size['length'], self.package_size['item_name']))

    def test_prepare_package_size_2(self):
        self.assertIsNotNone(self.sendy.prepare_package_size(self.package_size['weight'], self.package_size['height'], self.package_size['width'], self.package_size['length'], self.package_size['item_name']))

    def test_prepare_collect_payment_1(self):
        self.assertDictEqual(self.payment_data, self.sendy.prepare_collect_payment(self.payment_data['status'], self.payment_data['pay_method'], self.payment_data['amount']))

    def test_prepare_collect_payment_2(self):
        self.assertIsNotNone(self.sendy.prepare_collect_payment(self.payment_data['status'], self.payment_data['pay_method'], self.payment_data['amount']))

    def test_prepare_delivery_details_1(self):
        self.delivery_data['package_size'] = [self.delivery_data['package_size'][0]]
        self.assertEqual(self.delivery_data, self.sendy.prepare_delivery_details(self.delivery_data['pick_up_date'], self.delivery_data['collect_payment'], self.delivery_data['carrier_type'], self.delivery_data['return'], self.delivery_data['note'], self.delivery_data['note_status'], self.delivery_data['request_type'], self.delivery_data['order_type'], self.delivery_data['ecommerce_order'], self.delivery_data['express'], self.delivery_data['skew'], self.delivery_data['package_size'][0]))

    def test_prepare_delivery_details_2(self):
        self.assertIsNotNone(self.sendy.prepare_delivery_details(self.delivery_data['pick_up_date'], self.delivery_data['collect_payment'], self.delivery_data['carrier_type'], self.delivery_data['return'], self.delivery_data['note'], self.delivery_data['note_status'], self.delivery_data['request_type'], self.delivery_data['order_type'], self.delivery_data['ecommerce_order'], self.delivery_data['express'], self.delivery_data['skew'], self.delivery_data['package_size'][0]))

    def test_request_delivery(self):
        self.assertIsNotNone(self.sendy.request_delivery(self.location_data, self.location_data, self.person_data, self.person_data, self.delivery_data))

    def test_request_multi_destination_delivery(self):
        self.assertIsNotNone(self.sendy.request_multi_destination_delivery(self.location_data, self.location_data, self.location_data, self.person_data, self.person_data, self.delivery_data))

    def test_request_multi_pickup_delivery(self):
        self.assertIsNotNone(self.sendy.request_multi_pickup_delivery("0712345678", self.location_data, self.location_data, self.location_data, self.person_data, self.person_data, self.delivery_data))

    def test_complete_delivery(self):
        self.assertIsNotNone(self.sendy.complete_delivery(self.delivery_data))

    def test_track_or_cancel_delivery(self):
        self.assertIsNotNone(self.sendy.track_or_cancel_delivery(command="track", order_no="AA2395374", request_token_id="request_token_id"))


if __name__ == '__main__':
    unittest.main()
