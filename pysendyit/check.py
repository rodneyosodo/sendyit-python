from pysendyit.errors import SendyException


def check_url(path):
    """
    Checks the url
    Adds a "/" at the end if it does not exist.
    It also checks the path is the same as the ones available
    :param path:
    :return:
    """
    if path[-1] != "/":
        path = path + "/"
    if path == "" or path is None:
        raise SendyException("Base url given is empty")
    else:
        if path == "https://apitest.sendyit.com/v1/" or path == "https://api.sendyit.com/v1/":
            return path
        else:
            raise SendyException("The Base url is unavailable or invalid")


def check_api_details(api_details):
    if api_details == "" or api_details is None:
        raise SendyException("API detail provided is empty")
    else:
        return api_details


def check_location_details(data):
    """
    Checks the from location details
    """
    if data["name"] == "" or data["name"] is None:
        raise SendyException("Name given is empty")
    if data["latitude"] == "" or data["latitude"] is None:
        raise SendyException("Latitude given is empty")
    if data["longitude"] == "" or data["longitude"] is None:
        raise SendyException("longitude given is empty")
    if data["description"] == "" or data["description"] is None:
        raise SendyException("description given is empty")
    return data


def check_person_details(data):
    """
    Prepares person's data
    :param data:
    :return:
    """
    if data["name"] == "" or data["name"] is None:
        raise SendyException("Name given is empty")
    if data["phone"] == "" or data["phone"] is None:
        raise SendyException("Phone given is empty")
    if data["email"] == "" or data["email"] is None:
        raise SendyException("Email given is empty")
    if data["notes"] == "" or data["notes"] is None:
        raise SendyException("Note given is empty")
    return data


def check_package_size(data):
    """
    Prepares data package
    :param data:
    :return:
    """
    if data["weight"] == "" or data["weight"] is None:
        raise SendyException("Weight given is empty")
    if data["height"] == "" or data["height"] is None:
        raise SendyException("Height given is empty")
    if data["width"] == "" or data["width"] is None:
        raise SendyException("Width given is empty")
    if data["length"] == "" or data["length"] is None:
        raise SendyException("Length given is empty")
    if data["item_name"] == "" or data["item_name"] is None:
        raise SendyException("Item name given is empty")
    return data


def check_collect_payment(data):
    """
    Prepares collect payment
    :param data:
    :return:
    """
    if data["status"] == "" or data["status"] is None:
        raise SendyException("status given is empty")
    if data["pay_method"] == "" or data["pay_method"] is None:
        raise SendyException("pay_method given is empty")
    if data["amount"] == "" or data["amount"] is None:
        raise SendyException("amount given is empty")
    return data


def check_delivery_details(data):
    """
    Prepares Delivery details
    :param data:
    :return:
    """
    if data["pick_up_date"] == "" or data["pick_up_date"] is None:
        raise SendyException("pick_up_date given is empty")
    data["collect_payment"] = check_collect_payment(data["collect_payment"])
    if data["carrier_type"] == "" or data["carrier_type"] is None:
        raise SendyException("carrier_type given is empty")
    if data["return"] == "" or data["return"] is None:
        raise SendyException("return given is empty")
    if data["note"] == "" or data["note"] is None:
        raise SendyException("Note given is empty")
    if data["note_status"] == "" or data["note_status"] is None:
        raise SendyException("note_status given is empty")
    if data["request_type"] == "" or data["request_type"] is None:
        raise SendyException("request_type given is empty")
    if data["order_type"] == "" or data["order_type"] is None:
        raise SendyException("order_type given is empty")
    if data["ecommerce_order"] == "" or data["ecommerce_order"] is None:
        raise SendyException("ecommerce_order given is empty")
    if data["express"] == "" or data["express"] is None:
        raise SendyException("express given is empty")
    if data["skew"] == "" or data["skew"] is None:
        raise SendyException("skew given is empty")
    if len(data['package_size']) > 1:
        for i in range(len(data["package_size"])):
            data['package_size'][i] = check_package_size(data=data['package_size'][i])
    else:
        data["package_size"] = check_package_size(data["package_size"][0])
    return data
