from .prestaobject import PrestaObject


class Product(PrestaObject):

    _object_name = 'product'
    _url = 'products'
    _required_fields = [
        'price',
        'link_rewrite',
        'name',
    ]
