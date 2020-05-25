from pysendyit.api import Api
from pysendyit.errors import SendyException
from pysendyit.check import (check_api_details, check_location_details,
                             check_person_details, check_url, check_package_size,
                             check_collect_payment, check_delivery_details)


class Sendy(Api):

    def __init__(self, api_key: str, api_username: str, base_url: str):
        """
        :param api_key: api_key of the request eg: 'mysendykey'.
        :param api_username: api_username of the request eg: 'mysendyusername'.
        :param base_url:
        """
        self.api_key = check_api_details(api_details=api_key)
        self.api_username = check_api_details(api_details=api_username)
        self.base_url = check_url(base_url)
        super(Sendy, self).__init__(api_key, api_username, base_url)

    @staticmethod
    def prepare_location_details(reference: str, name: str, latitude: float,
                                 longitude: float, description: str) -> dict:
        """
        Prepares data for pickup location and destination of goods
        :param reference: Either 'from' or 'to'
        :param name: name of the pick up location or destination
        :param latitude: latitude of the pick up location or destination
        :param longitude: longitude of the pick up location or destination
        :param description: description of the pick up location or destination
        """
        if reference == "from" or reference == "to":
            return check_location_details({
                "{}_name".format(reference): name,
                "{}_lat".format(reference): latitude,
                "{}_long".format(reference): longitude,
                "{}_description".format(reference): description
            })
        else:
            raise SendyException("Invalid location reference")

    @staticmethod
    def prepare_person_details(reference: str, name: str, phone: str, email: str, notes: str) -> dict:
        """
        Prepares data of recepient or sender
        :param reference: Either 'sender' or 'recepient'
        :param name: name of the recepient or sender
        :param phone: phone of the recepient or sender
        :param email: email of the recepient or sender
        :param notes: notes of the recepient or sender
        """
        if reference == "recepient" or reference == "sender":
            return check_person_details({
                "{}_name".format("recepient"): name,
                "{}_phone".format("recepient"): phone,
                "{}_email".format("recepient"): email,
                "{}_notes".format("recepient"): notes
            })
        else:
            raise SendyException("Invalid reference for person. Give 'sender' or 'recepient'")

    @staticmethod
    def prepare_package_size(weight: float, height: float, width: float, length: float, item_name: str) -> dict:
        """
        Prepares data package size
        :param weight: weight of the package
        :param height: height of the package
        :param width: width of the package
        :param length: length of the package
        :param item_name: item_name of the package
        """
        return check_package_size(dict(weight=weight, height=height, width=width, length=length, item_name=item_name))

    @staticmethod
    def prepare_collect_payment(status: float, pay_method: float, amount: float) -> dict:
        """
        Prepares data package size
        :param status: weight of the package
        :param pay_method: height of the package
        :param amount: width of the package
        """
        return check_collect_payment(dict(status=status, pay_method=pay_method, amount=amount))

    @staticmethod
    def prepare_delivery_details(pick_up_date, collect_payment, carrier_type, return_type,
                                 note, note_status, request_type, order_type, ecommerce_order,
                                 express, skew, package_size) -> dict:
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

    def request_multi_pickup_delivery(self, rider_phone, from_details_one, from_details_two,
                                      to_details, recepient,
                                      sender, delivery_details, vendor_type=1):
        """
        This call is used to create new multi pickup delivery request,
        obtaining rates , estimated time of arrival and
        estimated time of delivery between a set of locations.
        The main difference with the normal delivery is the 
        number of pickup locations passed , on the from key.
        In this request pass an array with multiple destination.
        Multi-Pickup orders cannot be placed alongside multi-delivery orders.
        """
        command = "request"
        endpoint = "##requestmultipickup"
        values = {
            "command": command,
            "data": {
                "api_key": self.api_key,
                "api_username": self.api_username,
                "vendor_type": vendor_type,
                "rider_phone": rider_phone,
                "from": [check_location_details(from_details_one),
                         check_location_details(from_details_two)],
                "to": [check_location_details(to_details)],
                "recepient": check_person_details(recepient),
                "sender": check_person_details(sender),
                "delivery_details": check_delivery_details(delivery_details)
            }
        }
        return self.make_request(url_parameter=endpoint, body=values)

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

    def track_or_cancel_delivery(self, command="track", order_no="AA2395374", request_token_id="request_token_id"):
        """
        This call provides you with the ability to cancel current deliveries or track current deliveries.
        :param command: Cancel or track the delivery
        :param order_no: status if money is being collected on your behalf
        :param request_token_id: request_token_id of the request
        :type order_no: str
        :type request_token_id: str
        """
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
