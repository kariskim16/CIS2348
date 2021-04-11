'''
Karis Kim
1624226
CIS 2348
'''
'''
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


    print()
    # Create a list from the inventory information
    inven_l = list(inven_d.values())

    # Sort the list based on manufacturer
    # We need a "getter" for the mfg
    inven_l.sort(key=lambda x: x.get_mfg())
    for obj in inven_l:
        print(obj.get_info())

    # Print/write the list to the file
    with open("FullInventory.csv", "w") as f:
        for obj in inven_l:
            f.write(obj.get_info() + "\n")


    # delete any old files (end with "Inventory.csv")
    import os
    # print(item_types)
    for t in item_types:
        try:
            file_name = t.capitalize() + "Inventory.csv"
            print("Attempting to delete " + file_name)
            os.remove(file_name)
        except Exception:
            print(file_name + " not found.")

    # sort items by item ID
    inven_l.sort(key=lambda x: x._id)
    for obj in inven_l:
        print(obj.get_info())

    # loop through the inventory list
    for obj in inven_l:
        print(obj.get_info())

        # for each inventory item: get the item type and set file_name = [Item_type]Inventory.csv
        file_name = obj._type.capitalize() + "Inventory.csv"

        # create/append to file named [itemType]Inventory.csv
        with open(file_name, 'a') as f:
            # write a line to the file consisting of [item ID, manufacturer name, price, service date, and list if it is damaged]
            f.write(f"{obj._id},{obj._mfg},{obj._price},{obj._service_date},{obj._damaged}\n")


    from datetime import datetime

    # create a date object for today
    today = datetime.today().date()

    # sort from oldest to most recent
    inven_l.sort(key=lambda x: datetime.strptime(x._service_date, "%m/%d/%Y").date())

    print("CREATING PAST DUE SERVICE REPORT")

    # execute the items that are past the service date
    with open("PastServiceDateInventory.csv", 'w') as f:
        for obj in inven_l:
            # only print those that are past due
            # ....
            if today > datetime.strptime(obj._service_date, "%m/%d/%Y").date():
                f.write(obj.get_info() + "\n")
                print(obj.get_info())


    print("CREATING DAMAGED INVENTORY REPORT")
    # sort in the order of most expensive to least expensive
    inven_l.sort(key=lambda x: x._price, reverse=True)

    # execute items that are damaged
    with open("DamagedInventory.csv", 'w') as f:
        for obj in inven_l:
            if obj._damaged:
                # line should contain item ID, manufacturer name, item type, price, and service date.
                f.write(f"{obj._id},{obj._mfg},{obj._type},{obj._price},{obj._service_date}\n")


if __name__ == "__main__":
    main()


