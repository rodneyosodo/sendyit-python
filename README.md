# sendit-python
Python wrapper for Sendy's API. https://www.sendyit.com/

![Testing](https://github.com/0x6f736f646f/sendyit-python/workflows/Testing/badge.svg)
![Creating a Release](https://github.com/0x6f736f646f/sendyit-python/workflows/Creating%20a%20Release/badge.svg)
![Upload Python Package](https://github.com/0x6f736f646f/sendyit-python/workflows/Upload%20Python%20Package/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/0x6f736f646f/sendyit-python/badge.svg?branch=master)](https://coveralls.io/github/0x6f736f646f/sendyit-python?branch=master)
[![Build Status](https://travis-ci.com/0x6f736f646f/sendyit-python.svg?branch=master)](https://travis-ci.com/0x6f736f646f/sendyit-python)
[![Maintainability](https://api.codeclimate.com/v1/badges/6c6702b7007a11eb203f/maintainability)](https://codeclimate.com/github/0x6f736f646f/sendyit-python/maintainability)
# Installation
```sh
pip install pysendyit
```

Usage
-----
```python
from pysendyit import Sendy
s = Sendy(base_url='http://your_sendy_url')

# subscription
s.subscribe(name='John Doe', email='email@to.subscribe', list_id='the_list_id', 
    custom_field1='custom_value1', custom_value2='custom_value2')

# unsubscription
s.unsubscribe(email='email@to.unsubscribe', list_id='the_list_id')
```
