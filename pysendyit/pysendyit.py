from pysendyit.api import Api
from pysendyit.errors import SendyException
from pysendyit.check import *


class Sendy(Api):

    def __init__(self, api_key, api_username, base_url):
        """
        `api_key` String api_key of the request eg: 'mysendykey'.
        `api_username` String api_username of the request eg: 'mysendyusername'.
        :param api_key:
        :param api_username:
        :param base_url:
        """
        self.api_key = check_api_key(api_key)
        self.api_username = check_api_username(api_username)
        self.base_url = check_url(base_url)
        super(Sendy, self).__init__(api_key, api_username, base_url)

    @staticmethod
    def prepare_from_details(name, latitude, longitude, description):
        """
        Prepares data where you want the goods are, from location
        :type name: str
        :type latitude: float
        :type longitude: float
        :type description: str
        :param name: from_name of the pick up location
        :param latitude: from_latitude of the pick up location
        :param longitude: from_longitude of the pick up location
        :param description: from_description of the pick up location
        :return from: dict
        """
        return check_location_details({
            "from_name": name,
            "from_lat": latitude,
            "from_long": longitude,
            "from_description": description
        })

    @staticmethod
    def prepare_to_details(name, latitude, longitude, description):
        """
        Prepares data where you want the goods are, from location
        :type name: str
        :type latitude: float
        :type longitude: float
        :type description: str
        :param name: name of the destination
        :param latitude: latitude of the destination
        :param longitude: longitude of the destination
        :param description: description of the destination
        :return:
        """
        return check_location_details({
            "to_name": name,
            "to_lat": latitude,
            "to_long": longitude,
            "to_description": description
        })

    @staticmethod
    def prepare_recipient_details(name, phone, email, notes):
        """
        Prepares data of recepient
        :type name: str
        :type phone: str
        :type email: str
        :type notes: str
        :param name: recepient_name of the recepient
        :param phone: recepient_phone of the recepient
        :param email: recepient_email of the recepient
        :param notes: recepient_notes of the recepient
        :return:
        """
        return check_person_details({
            "recepient_name": name,
            "recepient_phone": phone,
            "recepient_email": email,
            "recepient_notes": notes
        })

    @staticmethod
    def prepare_sender_details(name, phone, email, notes):
        """
        Prepares data of sender
        :type name: str
        :type phone: str
        :type email: str
        :type notes: str
        :param name: recepient_name of the recepient
        :param phone: recepient_phone of the recepient
        :param email: recepient_email of the recepient
        :param notes: recepient_notes of the recepient
        :return:
        """
        return check_person_details({
            "sender_name": name,
            "sender_phone": phone,
            "sender_email": email,
            "sender_notes": notes
        })

    @staticmethod
    def prepare_package_size(weight, height, width, length, item_name):
        """
        Prepares data package size
        :type weight: float
        :type height: float
        :type width: float
        :type length: float
        :type item_name: str
        :param weight: weight of the package
        :param height: height of the package
        :param width: width of the package
        :param length: length of the package
        :param item_name: item_name of the package
        :return:
        """
        return check_package_size({
            "weight": weight,
            "height": height,
            "width": width,
            "length": length,
            "item_name": item_name
        })

    @staticmethod
    def prepare_collect_payment(status, pay_method, amount):
        """
        Prepares data package size
        :type status: float
        :type pay_method: float
        :type amount: float
        :param status: weight of the package
        :param pay_method: height of the package
        :param amount: width of the package
        :return:
        """
        return check_collect_payment({
            "status": status,
            "pay_method": pay_method,
            "amount": amount,
        })

    @staticmethod
    def prepare_delivery_details(pick_up_date, collect_payment, carrier_type, return_type,
                                 note, note_status, request_type, order_type, ecommerce_order,
                                 express, skew, package_size):
        return check_delivery_details({
            "pick_up_date": pick_up_date,
            "collect_payment": collect_payment,
            "carrier_type": carrier_type,
            "return": return_type,
            "note": note,
            "note_status": note_status,
            "request_type": request_type,
            "order_type": order_type,
            "ecommerce_order": ecommerce_order,
            "express": express,
            "skew": skew,
            "package_size": [package_size]
        })

    def request_delivery(self, from_details, to_details, recepient,
                         sender, delivery_details, vendor_type=1,
                         request_token_id="request_token_id"):
        """
        This call is used to create new delivery request,
        obtaining rates, estimated time of arrival and
        estimated time of delivery between a set of locations.
        """
        command = "request"
        endpoint = "#request"
        values = {
            "command": command,
            "data": {
                "api_key": self.api_key,
                "api_username": self.api_username,
                "vendor_type": vendor_type,
                "rider_phone": "0728561783",
                "from": check_location_details(from_details),
                "to": check_location_details(to_details),
                "recepient": check_person_details(recepient),
                "sender": check_person_details(sender),
                "delivery_details": check_delivery_details(delivery_details)
            },
            "request_token_id": request_token_id
        }
        return self.make_request(url_parameter=endpoint, body=values)

    def request_multi_destination_delivery(self, from_details, to_details_first,
                                           to_details_second, recepient, sender, delivery_details):
        """
        This call is used to create new multi destination delivery request,
        obtaining rates , estimated time of arrival and
        estimated time of delivery between a set of locations.
        The main difference with the normal delivery is the
        number of destinations passed, on the to key.
        In this request pass an array with multiple destination.
        """
        endpoint = "#requestmultidestination"
        values = {
            "command": "request",
            "data": {
                "api_key": self.api_key,
                "api_username": self.api_username,
                "vendor_type": 1,
                "rider_phone": "0728561783",
                "from": check_location_details(from_details),
                "to": [
                    check_location_details(to_details_first),
                    check_location_details(to_details_second)
                ],
                "recepient": check_person_details(recepient),
                "sender": check_person_details(sender),
                "delivery_details": check_delivery_details(delivery_details)
            },
            "request_token_id": "request_token_id"
        }
        return self.make_request(url_parameter=endpoint, body=values)

    def request_multi_pickup_delivery(self):
        """
        This call is used to create new multi pickup delivery request,
        obtaining rates , estimated time of arrival and
        estimated time of delivery between a set of locations.
        The main difference with the normal delivery is the 
        number of pickup locations passed , on the from key.
        In this request pass an array with multiple destination.
        Multi-Pickup orders cannot be placed alongside multi-delivery orders.
        """
        pass

    def complete_delivery(self, delivery_details, order_no="AA23MS878", request_token_id="request_token_id"):
        """
        If you had earlier requested an order using request_type
        as 'quote' you can use this call to complete your delivery.
        """
        command = "complete"
        endpoint = command
        values = {
            "command": command,
            "data": {
                "api_key": self.api_key,
                "api_username": self.api_username,
                "order_no": order_no,
                "rider_phone": "0728561783",
                "delivery_details": check_delivery_details(delivery_details)
            },
            "request_token_id": request_token_id
        }
        return self.make_request(url_parameter=endpoint, body=values)

    def track_delivery(self, order_no="AA34BE331", request_token_id="request_token_id"):
        """
        This call provides you with the ability to track current deliveries.
        :param order_no: status if money is being collected on your behalf
        :param request_token_id: request_token_id of the request
        :type order_no: str
        :type request_token_id: str
        """
        command = "track"
        endpoint = command
        values = {
            "command": command,
            "data": {
                "api_key": self.api_key,
                "api_username": self.api_username,
                "order_no": order_no
            },
            "request_token_id": request_token_id
        }
        return self.make_request(url_parameter=endpoint, body=values)

    def cancel_delivery(self, order_no="AA2395374", request_token_id="request_token_id"):
        """
        This call provides you with the ability to cancel current deliveries.
        :param order_no: status if money is being collected on your behalf
        :param request_token_id: request_token_id of the request
        :type order_no: str
        :type request_token_id: str
        """
        command = "cancel"
        endpoint = command
        values = {
            "command": command,
            "data": {
                "api_key": self.api_key,
                "api_username": self.api_username,
                "order_no": order_no
            },
            "request_token_id": request_token_id
        }
        return self.make_request(url_parameter=endpoint, body=values)

    def rider_availability(self, latitude=-1.28869, longitude=36.823363, request_token_id="request_token_id"):
        """
        Provides locations of available riders, vans and trucks
        based on the pick up location or any point of reference.
        :param latitude: to_lat of the pick up location
        :param longitude: from_long of the pick up location
        :param request_token_id: request_token_id of the request
        :type latitude: float
        :type longitude: float
        :type request_token_id: str
        """
        command = "rider_location"
        endpoint = "#rider"
        values = {
            "command": command,
            "data": {
                "api_key": self.api_key,
                "api_username": self.api_username,
                "lat": latitude,
                "long": longitude
            },
            "request_token_id": request_token_id
        }
        return self.make_request(url_parameter=endpoint, body=values)
