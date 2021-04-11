'''
Karis Kim
1624226
CIS 2348
'''

    '''

    Required Output:
    Processed Inventory Reports:

    a. FullInventory.csv -- 
    all the items listed by row with all their information . The items should be sorted alphabetically by manufacturer. Each row should contain item ID, manufacturer name, item type, price, service date, and list if it is damaged. The item attributes must appear in this order.
    '''
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

    '''
    b. Item type Inventory list, i.e LaptopInventory.csv -- there should be a file for each item type and the item type needs to be in the file name. Each row of the file should contain item ID, manufacturer name, price, service date, and list if it is damaged. The items should be sorted by their item ID.
    '''

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

    '''
    c. PastServiceDateInventory.csv – all the items that are past the service date on the day the program is actually executed. Each row should contain: item ID, manufacturer name, item type, price, service date, and list if it is damaged. The items must appear in the order of service date from oldest to most recent.
    '''
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

    '''
    d. DamagedInventory.csv –all items that are damaged. Each row should contain : item ID, manufacturer name, item type, price, and service date. The items must appear in the order of most expensive to least expensive. 
    '''
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


