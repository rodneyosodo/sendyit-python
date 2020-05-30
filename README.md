# Unofficial Sendy python API Wrapper
The wrapper provides convenient access to the [Sendy Logistics API](https://www.sendyit.com/) from applications written in server-side python.

![Testing](https://github.com/0x6f736f646f/sendyit-python/workflows/Testing/badge.svg)
![Creating a Release](https://github.com/0x6f736f646f/sendyit-python/workflows/Creating%20a%20Release/badge.svg)
![Upload Python Package to PYPI](https://github.com/0x6f736f646f/sendyit-python/workflows/Upload%20Python%20Package%20to%20PYPI/badge.svg)
[![Build Status](https://travis-ci.com/0x6f736f646f/sendyit-python.svg?branch=master)](https://travis-ci.com/0x6f736f646f/sendyit-python)
[![Coverage Status](https://coveralls.io/repos/github/0x6f736f646f/sendyit-python/badge.svg?branch=master)](https://coveralls.io/github/0x6f736f646f/sendyit-python?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/6c6702b7007a11eb203f/maintainability)](https://codeclimate.com/github/0x6f736f646f/sendyit-python/maintainability)

## Installation
```sh
pip install pysendyit
```

## Usage
In order to run the demo, export the the following values to your environment. They can be found/generated at the API Dashboard.
```bash
export API_USERNAME="{your-api-username}"
export API_KEY="{your-api-key}"
export BASE_URL="{your-base-url}"
```

```python
from pysendyit.pysendyit import Sendy
import os

# Creating an instance of the Sendy Class
sendy = Sendy(api_username=os.getenv('API_USERNAME'), api_key=os.getenv('API_KEY'), base_url=os.getenv('BASE_URL'))

# Printing response
print(sendy.track_or_cancel_delivery(command="track", order_no="AA2395374", request_token_id="request_token_id"))

```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Sendy Logistics 
