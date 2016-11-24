from .prestaobject import PrestaObject


class Category(PrestaObject):

    _object_name = 'category'
    _url = 'categories'
    _required_fields = [
        'active',
        'name',
        'link_rewrite',
    ]
