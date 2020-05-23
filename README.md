# sendit-python
Python wrapper for Sendy's API. https://www.sendyit.com/


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
