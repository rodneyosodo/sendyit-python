import unittest
from pysendyit.check import (check_api_details, check_collect_payment,
                             check_delivery_details, check_location_details,
                             check_package_size, check_person_details,
                             check_url)
from pysendyit.errors import SendyException


class CheckTest(unittest.TestCase):
    def setUp(self):
        self.location_data = {"name": "test", "latitude": -1.300577,
                              "longitude": 36.78183, "description": "test"}
        self.person_data = {"name": "test", "phone": "0712345678",
                            "email": "test@mail.com", "notes": "test"}
        self.package_size = {"weight": "2", "height": "2", "width": "2",
                             "length": "2", "item_name": "test"}
        self.payment_data = {"status": "test", "pay_method": "test",
                             "amount": "200"}
        self.delivery_data = {
            "pick_up_date": "pick_up_date",
            "collect_payment": self.payment_data,
            "carrier_type": "carrier_type",
            "return": "return_type",
            "note": "note",
            "note_status": "note_status",
            "request_type": "request_type",
            "order_type": "order_type",
            "ecommerce_order": "ecommerce_order",
            "express": "express",
            "skew": "skew",
            "package_size": [self.package_size, self.package_size]
        }

    def test_check_url_1(self):
        self.assertEqual("https://apitest.sendyit.com/v1/",
                         check_url("https://apitest.sendyit.com/v1"))

    def test_check_url_2(self):
        self.assertRaises(SendyException, check_url, "")

    def test_check_url_3(self):
        self.assertRaises(SendyException, check_url, None)

    def test_check_url_4(self):
        self.assertEqual("https://apitest.sendyit.com/v1/",
                         check_url("https://apitest.sendyit.com/v1/"))

    def test_check_url_5(self):
        self.assertEqual("https://api.sendyit.com/v1/",
                         check_url("https://api.sendyit.com/v1/"))

    def test_check_url_6(self):
        self.assertEqual(
            "https://private-faab6-sendypublicapi.apiary-mock.com/v1/",
            check_url(
                "https://private-faab6-sendypublicapi.apiary-mock.com/v1/"
            )
        )

    def test_check_url_7(self):
        self.assertRaises(SendyException, check_url,
                          "https://private-faab6-sendypublicapi.apiary.com/v1")

    def test_check_api_details_1(self):
        self.assertRaises(SendyException, check_api_details, "")

    def test_check_api_details_2(self):
        self.assertRaises(SendyException, check_api_details, None)

    def test_check_api_details_3(self):
        self.assertEqual("name", check_api_details("name"))

    def test_check_location_details_empty_name_1(self):
        self.location_data['name'] = ""
        self.assertRaises(SendyException, check_location_details,
                          self.location_data)

    def test_check_location_details_empty_name_2(self):
        self.location_data['name'] = None
        self.assertRaises(SendyException, check_location_details,
                          self.location_data)

    def test_check_location_details_empty_latitude_1(self):
        self.location_data["latitude"] = ""
        self.assertRaises(SendyException, check_location_details,
                          self.location_data)

    def test_check_location_details_empty_latitude_2(self):
        self.location_data['latitude'] = None
        self.assertRaises(SendyException, check_location_details,
                          self.location_data)

    def test_check_location_details_empty_longitude_1(self):
        self.location_data['longitude'] = ""
        self.assertRaises(SendyException, check_location_details,
                          self.location_data)

    def test_check_location_details_empty_longitude_2(self):
        self.location_data['longitude'] = None
        self.assertRaises(SendyException, check_location_details,
                          self.location_data)

    def test_check_location_details_empty_description_1(self):
        self.location_data['description'] = ""
        self.assertRaises(SendyException, check_location_details,
                          self.location_data)

    def test_check_location_details_empty_description_2(self):
        self.location_data['description'] = None
        self.assertRaises(SendyException, check_location_details,
                          self.location_data)

    def test_check_location_details_1(self):
        data = self.location_data
        self.assertDictEqual(data, check_location_details(data))

    def test_check_location_details_2(self):
        data = self.location_data
        self.assertIsNotNone(check_location_details(data))

    def test_check_person_details_empty_name_1(self):
        self.person_data['name'] = ""
        self.assertRaises(SendyException, check_person_details,
                          self.person_data)

    def test_check_person_details_empty_name_2(self):
        self.person_data['name'] = None
        self.assertRaises(SendyException, check_person_details,
                          self.person_data)

    def test_check_person_details_empty_phone_1(self):
        self.person_data["phone"] = ""
        self.assertRaises(SendyException, check_person_details,
                          self.person_data)

    def test_check_person_details_empty_phone_2(self):
        self.person_data['phone'] = None
        self.assertRaises(SendyException, check_person_details,
                          self.person_data)

    def test_check_person_details_empty_email_1(self):
        self.person_data['email'] = ""
        self.assertRaises(SendyException, check_person_details,
                          self.person_data)

    def test_check_person_details_empty_email_2(self):
        self.person_data['email'] = None
        self.assertRaises(SendyException, check_person_details,
                          self.person_data)

    def test_check_person_details_empty_notes_1(self):
        self.person_data['notes'] = ""
        self.assertRaises(SendyException, check_person_details,
                          self.person_data)

    def test_check_person_details_empty_notes_2(self):
        self.person_data['notes'] = None
        self.assertRaises(SendyException, check_person_details,
                          self.person_data)

    def test_check_person_details_1(self):
        data = self.person_data
        self.assertDictEqual(data, check_person_details(data))

    def test_check_person_details_2(self):
        data = self.person_data
        self.assertIsNotNone(check_person_details(data))

    def test_check_package_size_empty_weight_1(self):
        self.package_size['weight'] = ""
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_empty_weight_2(self):
        self.package_size['weight'] = None
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_empty_height_1(self):
        self.package_size["height"] = ""
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_empty_height_2(self):
        self.package_size['height'] = None
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_empty_width_1(self):
        self.package_size['width'] = ""
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_empty_width_2(self):
        self.package_size['width'] = None
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_empty_length_1(self):
        self.package_size['length'] = ""
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_empty_length_2(self):
        self.package_size['length'] = None
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_empty_item_name_1(self):
        self.package_size['item_name'] = ""
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_empty_item_name_2(self):
        self.package_size['item_name'] = None
        self.assertRaises(SendyException, check_package_size,
                          self.package_size)

    def test_check_package_size_1(self):
        data = self.package_size
        self.assertDictEqual(data, check_package_size(data))

    def test_check_package_size_2(self):
        data = self.package_size
        self.assertIsNotNone(check_package_size(data))

    def test_check_collect_payment_empty_status_1(self):
        self.payment_data['status'] = ""
        self.assertRaises(SendyException, check_collect_payment,
                          self.payment_data)

    def test_check_collect_payment_empty_status_2(self):
        self.payment_data['status'] = None
        self.assertRaises(SendyException, check_collect_payment,
                          self.payment_data)

    def test_check_collect_payment_empty_pay_method_1(self):
        self.payment_data["pay_method"] = ""
        self.assertRaises(SendyException, check_collect_payment,
                          self.payment_data)

    def test_check_collect_payment_empty_pay_method_2(self):
        self.payment_data['pay_method'] = None
        self.assertRaises(SendyException, check_collect_payment,
                          self.payment_data)

    def test_check_collect_payment_empty_amount_1(self):
        self.payment_data['amount'] = ""
        self.assertRaises(SendyException, check_collect_payment,
                          self.payment_data)

    def test_check_collect_payment_empty_amount_2(self):
        self.payment_data['amount'] = None
        self.assertRaises(SendyException, check_collect_payment,
                          self.payment_data)

    def test_check_collect_payment_1(self):
        data = self.payment_data
        self.assertDictEqual(data, check_collect_payment(data))

    def test_check_collect_payment_2(self):
        data = self.payment_data
        self.assertIsNotNone(check_collect_payment(data))

    def test_check_delivery_details_empty_pick_up_date_1(self):
        self.delivery_data['pick_up_date'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_pick_up_date_2(self):
        self.delivery_data['pick_up_date'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_carrier_type_1(self):
        self.delivery_data["carrier_type"] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_carrier_type_2(self):
        self.delivery_data['carrier_type'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_return_1(self):
        self.delivery_data['return'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_return_2(self):
        self.delivery_data['return'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_note_1(self):
        self.delivery_data['note'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_note_2(self):
        self.delivery_data['note'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_note_status_1(self):
        self.delivery_data['note_status'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_note_status_2(self):
        self.delivery_data['note_status'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_request_type_1(self):
        self.delivery_data['request_type'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_request_type_2(self):
        self.delivery_data['request_type'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_order_type_1(self):
        self.delivery_data['order_type'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_order_type_2(self):
        self.delivery_data['order_type'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_ecommerce_order_1(self):
        self.delivery_data['ecommerce_order'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_ecommerce_order_2(self):
        self.delivery_data['ecommerce_order'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_express_1(self):
        self.delivery_data['express'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_express_2(self):
        self.delivery_data['express'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_skew_1(self):
        self.delivery_data['skew'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_skew_2(self):
        self.delivery_data['skew'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_collect_payment_1(self):
        self.delivery_data['collect_payment'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_collect_payment_2(self):
        self.delivery_data['collect_payment'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_package_size_1(self):
        self.delivery_data['package_size'] = ""
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_empty_package_size_2(self):
        self.delivery_data['package_size'] = None
        self.assertRaises(SendyException, check_delivery_details,
                          self.delivery_data)

    def test_check_delivery_details_collect_payment_1(self):
        self.assertEqual(self.delivery_data['collect_payment'],
                         check_delivery_details(
                             self.delivery_data)['collect_payment']
                         )

    def test_check_delivery_details_package_size_1(self):
        self.assertEqual(self.delivery_data['package_size'],
                         check_delivery_details(
                             self.delivery_data)['package_size']
                         )

    def test_check_delivery_details_package_size_2(self):
        self.delivery_data['package_size'] = [
            self.delivery_data['package_size'][0]
        ]
        self.assertEqual(self.delivery_data['package_size'],
                         check_delivery_details(
                             self.delivery_data)['package_size']
                         )

    def test_check_delivery_details_1(self):
        data = self.delivery_data
        self.assertDictEqual(data, check_delivery_details(data))

    def test_check_delivery_details_2(self):
        data = self.delivery_data
        self.assertIsNotNone(check_delivery_details(data))


if __name__ == '__main__':
    unittest.main()
