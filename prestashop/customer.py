from .prestaobject import PrestaObject


class Customer(PrestaObject):

    _object_name = 'customer'
    _url = 'customers'
    _required_fields = [
        'passwd',
        'lastname',
        'firstname',
        'email',
    ]
