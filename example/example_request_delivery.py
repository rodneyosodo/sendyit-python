from pysendyit.pysendyit import Sendy
import os

sendy = Sendy(api_username=os.getenv('API_USERNAME'), api_key=os.getenv('API_KEY'), base_url=os.getenv('BASE_URL'))

from_location_data = sendy.prepare_location_details(reference="from", name="test", latitude=-1.300577,
                                                    longitude=36.78183, description="test")
to_location_data = sendy.prepare_location_details(reference="to", name="test", latitude=-1.300577,
                                                  longitude=36.78183, description="test")
sender_person_data = sendy.prepare_person_details(reference="sender", name="test", phone="0712345678",
                                                  email="test@mail.com", notes="test")
recepient_person_data = sendy.prepare_person_details(reference="recepient", name="test", phone="0712345678",
                                                     email="test@mail.com", notes="test")

package_size = sendy.prepare_package_size(weight=2, height=2, width=2, length=2, item_name="test")
payment_data = sendy.prepare_collect_payment(status=False, pay_method=0, amount=200)
delivery_data = sendy.prepare_delivery_details(pick_up_date="2016-04-20 12:12:12", collect_payment=payment_data,
                                               carrier_type=2, return_type=False, note="note",
                                               note_status=True, request_type="delivery",
                                               order_type="ondemand_delivery", ecommerce_order=False,
                                               express=False, skew=1, package_size=package_size)
vendor_type = 1
request_token_id = "request_token_id"

print(sendy.request_delivery(from_location_data, to_location_data, recepient_person_data,
                             sender_person_data, delivery_data, vendor_type, request_token_id))
