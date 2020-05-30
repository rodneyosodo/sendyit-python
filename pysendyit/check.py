from pysendyit.errors import SendyException


def check_url(path: str) -> str:
    """
    Checks the url
    Adds a "/" at the end if it does not exist.
    It also checks the path is the same as the ones available
    :param path: The url endpoint
    :return: path
    """
    if path == "" or path is None:
        raise SendyException("Base url given is empty")
    else:
        if path[-1] != "/":
            path = path + "/"
        if (path == "https://apitest.sendyit.com/v1/") or (
                path == "https://api.sendyit.com/v1/") or (
                path.__contains__("mock")):
            return path
        else:
            raise SendyException("The Base url is unavailable or invalid")


def check_api_details(api_details: str) -> str:
    """
    Checks the API_KEY and API_USERNAME if they are empty
    :param api_details: api_key or api_username or the request
    :return: api_key or api_username
    """
    if api_details == "" or api_details is None:
        raise SendyException("API detail provided is empty")
    else:
        return api_details


def check_location_details(data: dict) -> dict:
    """
    Checks the from location details if they are empty
    data['name'] name of the pick up location
    data['latitude'] latitude of the pick up location or destination
    data['longitude'] longitude of the pick up location or destination
    data['description']description of the pick up location or destination
    :param data:
    :return:
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


def check_person_details(data: dict) -> dict:
    """
    Checks person's data if it is empty
    data["name"] name of the recepient or sender
    data["phone"] phone number of the recepient or sender
    data["email"] email of the recepient or sender
    data["notes"] notes of the recepient or sender
    :param data:
    :return: data
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


def check_package_size(data: dict) -> dict:
    """
    Checks the package data if it is empty
    data["weight"] weight of the package
    data["height"] height of the package
    data["width"] width of the package
    data["length"] notes of the package
    data["item_name"] item_name of the package
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


def check_collect_payment(data: dict) -> dict:
    """
    checks the collect payment data if it has an empty field
    data["status"] status of the payment data
    data["pay_method"] pay_method of the payment data
    data["amount"] amount of the payment data
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


def check_delivery_details(data: dict) -> dict:
    """
    Prepares Delivery details
    :param data:
    :return:
    """
    if data["pick_up_date"] == "" or data["pick_up_date"] is None:
        raise SendyException("pick_up_date given is empty")
    if data["collect_payment"] == "" or data["collect_payment"] is None:
        raise SendyException("collect_payment given is empty")
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
    if data["package_size"] == "" or data["package_size"] is None:
        raise SendyException("package_size given is empty")
    if len(data['package_size']) > 1:
        for i in range(len(data["package_size"])):
            data['package_size'][i] = check_package_size(
                data=data['package_size'][i]
            )
    elif len(data['package_size']) == 1:
        data["package_size"][0] = check_package_size(data["package_size"][0])
    return data
