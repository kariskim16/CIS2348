'''
Karis Kim
1624226
CIS 2348
'''
'''
A program that manages the inventory of an electronics store.

use of classes, use of dictionaries and input and output of comma delimeted csv files.

Input:

a) ManufacturerList.csv -- contains items listed by row. Each row contains item ID, manufacturer name, item type, and optionally a damaged indicator.

b) PriceList.csv -- contains items listed by row. Each row contains item ID and the item price.

c) ServiceDatesList.csv – contains items listed by row. Each row contains item ID and service date.


create a class: Inventory

Instance/object variables:
    item_id, string
    manu_name, string
    item_type, string
    price, float
    service_date, string
    damaged, boolean

'''


class Inventory:

    # creates/initializes an inventory item from ManufacturerList.csv
    def __init__(self, _id, _mfg, _type, _damaged):
        self._id = _id.strip()
        self._mfg = _mfg.strip()
        self._type = _type.strip()
        if len(_damaged.strip()) > 0:
            self._damaged = True
        else:
            self._damaged = False
        self._price = 0
        self._service_date = ""

    def set_price(self, _price):
        self._price = float(_price.strip())

    def set_service_date(self, service_date):
        self._service_date = service_date.strip()

    def get_mfg(self):
        return self._mfg

    def get_info(self):
        # item ID, manufacturer name, item type, price, service date, and list if it is damaged.
        return f"{self._id},{self._mfg},{self._type},{self._price},{self._service_date},{self._damaged}"


import csv


def main():
    # inven_list = []
    inven_d = {}
    item_types = set()  # used to reset item-type inventory reports

    # read ManufacturerList.csv and create a list of inventory items
    with open("ManufacturerList.csv") as f:
        file = csv.reader(f, delimiter=',')
        for line in file:
            _id, _mfg, _type, _damaged = line
            item_types.add(_type.strip())
            _id = _id.strip()
            inven_d[_id] = Inventory(_id, _mfg, _type, _damaged)

    with open("PriceList.csv") as f:
        file = csv.reader(f, delimiter=',')
        for line in file:
            _id, _price = line
            _id = _id.strip()
            inven_d[_id].set_price(_price)  # update its price to match

    with open("ServiceDatesList.csv") as f:
        file = csv.reader(f, delimiter=',')
        for line in file:
            _id, service_date = line
            _id = _id.strip()
            inven_d[_id].set_service_date(service_date)

    # test print all items
    for _id in inven_d:
        print(inven_d[_id].get_info())

  
