from .prestaobject import PrestaObject


class Address(PrestaObject):

    _object_name = 'address'
    _url = 'addresses'
    _required_fields = [
        'id_country',
        'alias',
        'firstname',
        'lastname',
        'address1',
        'city'
    ]
