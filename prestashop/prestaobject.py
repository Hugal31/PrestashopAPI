from prestapyt import PrestaShopWebServiceError


class PrestaObject(dict):

    _object_name = ''
    _url = ''
    _required_fields = []

    def __init__(self, access, obj=None):
        self._access = access
        if obj is not None:
            super(PrestaObject, self).__init__(obj)
        else:
            super(PrestaObject, self).__init__()

    def __repr__(self):
        return self.__class__.__name__ + ':\n' + '\n'.join(['\t%s=%s' % (k, v) for k, v in self.iteritems()])

    def __getattr__(self, item):
        return self.__dict__[item] if item[0] == '_' else self[item]

    def __setattr__(self, key, value):
        if key[0] == '_':
            self.__dict__[key] = value
        else:
            self[key] = value

    def add(self):
        for field in self._required_fields:
            if field not in self:
                raise PrestaShopWebServiceError('Missing value \'%s\' for %s object' % (field, self.__class__.__name__))
        result = self._access.add(self._url, {self._object_name: self})
        self.update(result['prestashop'][self._object_name])

    def edit(self):
        self._access.edit(self._url, {self._object_name: self})

    def save(self):
        if 'id' in self:
            self.edit()
        else:
            self.add()

    def delete(self):
        self._access.delete(self._url, resource_ids=self['id'])

    @classmethod
    def get(cls, access, id):
        return cls(access, access.get(cls._url, resource_id=id)[cls._object_name])
