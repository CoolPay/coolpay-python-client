# coolpay-python-client

[![Build Status](https://travis-ci.org/CoolPay/coolpay-python-client.svg)](https://travis-ci.org/CoolPay/coolpay-python-client)

`coolpay-python-client` is a official python client for [CoolPay API](http://tech.coolpay.net/api). Coolpay API enables you to accept payments in a secure and reliable manner. This library currently supports CoolPay `v10` api.

Installation
===============

Add to your `requirements.txt`

    coolpay-api-client

or install via [pip](https://github.com/pypa/pip):

    $ pip install coolpay-api-client

It is currently tested with Python >= `2.7.9` and Python >= `3.4`.

Usage
=====

Before doing anything you should register yourself with CoolPay and get access credentials. If you haven't please [click](http://coolpay.net) here to apply.


Create a CoolPay client
------------------------

First you should create a client instance that is anonymous or authorized with api_key or login credentials provided by CoolPay.

To initialise an anonymous client:

```
from coolpay_api_client import CPClient
client = CPClient()
```

To initialise a client with CoolPay Api Key:

```
from coolpay_api_client import CPClient
secret = ":{0}".format(os.environ['COOLPAY_API_KEY'])
client = CPClient(secret)
```

Or you can provide login credentials like:

```
from coolpay_api_client import CPClient
secret= "{0}:{1}".format(os.environ['COOLPAY_LOGIN'], os.environ['COOLPAY_PASSWORD'])
client = CPClient(secret)
```

API Calls
---------

You can afterwards call any method described in CoolPay api with corresponding http method and endpoint. These methods are supported currently: `get`, `post`, `put`, `patch` and `delete`.

```
for activity in client.get('/activities'):
    print activity['id']
```

If you want raw http response, headers Please add `raw=True` parameter:

```
status, body, headers = client.get("/activities", raw=True)

if status == 200:
    for activity in json.loads(body):  ## note: import json
      print activity['id']
else:
    print "Error", body
```

Handling API exceptions
----------------------

By default (get|post|patch|put|delete) will return JSON parsed body on success (i.e. 2xx response code) otherwise it will raise `ApiError`. Your code should handle the errors appropriately.

You can listen for any api error like:

```
from coolpay_api_client.exceptions import ApiError
try:
    client.post('/payments', currency='DKK', order_id='1212')
    ...
except ApiError as e:
    print e.body
    print e.status_code
```

You can read more about api responses at [http://www.coolpay.com/docs/](http://www.coolpay.com/docs/).
