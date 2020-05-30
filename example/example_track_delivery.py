from pysendyit.pysendyit import Sendy
import os

sendy = Sendy(api_username=os.getenv('API_USERNAME'), api_key=os.getenv('API_KEY'), base_url=os.getenv('BASE_URL'))

print(sendy.track_or_cancel_delivery(command="track", order_no="AA2395374", request_token_id="request_token_id"))
