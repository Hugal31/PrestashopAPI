#!/usr/bin/env python

import prestapyt
from prestashop import *


SHOP_URL = 'http://shop.lan/api'
PRESTASHOP_TOKEN = ''


def main():
    access = prestapyt.PrestaShopWebServiceDict(SHOP_URL, PRESTASHOP_TOKEN)

    # Retrieve an address
    address = Address.get(access, 42)
    address.firstname = 'Toto'
    address.save()

    # Create an address
    address = Address(access)
    address.alias = 'House'
    address.firstname = 'Foo'
    address.lastname = 'Bar'
    address.id_country = 5
    address.address1 = ''
    address.city = ''
    address.save()

    address.delete()


if __name__ == '__main__':
    main()
