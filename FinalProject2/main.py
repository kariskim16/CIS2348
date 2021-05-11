"""
Karis Kim
1624226
CIS 2348
"""
# imports class and functions from previous assignment
import part1code as p1

# loads inventory
inven_l = p1.load_inventory()

'''
You will design a program that manages the inventory of an electronics store. You will need to use a number of concepts that you learned in class including: use of classes, use of dictionaries and input and output of comma delimeted csv files.

Input:
    a) ManufacturerList.csv -- contains items listed by row. Each row contains item ID, manufacturer name,2 item type, and optionally a damaged indicator
    b) PriceList.csv -- contains items listed by row. Each row contains item ID and the item price.
    c) ServiceDatesList.csv – contains items listed by row. Each row contains item ID and service date.

Example ManufacturerList.csv, PriceList.csv and ServiceDatesList.csv are provided for reference. Your code will be expected to work with any group input files of the appropriate format. Manufacturers can and will likely be different as will the items.

You can reuse parts of your code from Part 1.

Required Output:

1) Interactive Inventory Query Capability

a. Query the user of an item by asking for manufacturer and item type with a single query.

'''


# Also, there must be a matching item in inventory (undamaged, and not needing service).
# Ignore items that are beyond service date
# Construct as a list of matching items
def find_match(inven_l, mfg_l, item_type):
    '''
    Return a list of items that match the incoming manufacturer list and item type.
    Returned list may not include items that are damaged or beyond service date.
    '''
    match_list = []
    for item in inven_l:
        if item.get_mfg().lower() in mfg_l and item.get_type().lower() in item_type and item.get_damaged() == False and item.get_needs_service() == False:
            match_list.append(item)

    return match_list


while True:

    print("\nWhat item are you looking for? (Please enter at least a manufacturer name and item type.)")
    user_query = input()

    # remove all starting and trailing spaces from input
    user_query = user_query.strip()

    # convert input to lowercase
    user_query = user_query.lower()

    # if "q" was entered, then leave the loop
    if user_query == "q":
        break

    # print(user_query)
    # make sure there was actually input (length > 0) XXXXX

    # create a list of manufacturers
    # create this as a set, as set automatically eliminate duplicates
    mfl = set()

    # copy the mfg from each inventory item into the mfl set
    for item in inven_l:
        manuf = item.get_mfg().lower()
        mfl.add(manuf)

    # create a list of item_types
    item_types = set()

    for item in inven_l:
        item_type = item.get_type().lower()
        item_types.add(item_type)

    # print(mfl)
    # print(item_types)

    # Parse the user_query

    # find each word in user_query and see if it is a manufacturer or item_type....

    # make holders (lists) for manufacturer and item_type words found in the user_query
    mfgs_found = set()
    types_found = set()

    # split user_query into individual words
    user_words_l = user_query.split()
    # print(user_words_l)

    # look for manufacturer and item type in user_query
    for word in user_words_l:
        if word in mfl:
            mfgs_found.add(word)
        if word in item_types:
            types_found.add(word)

    # print("MFG WORDS FOUND", mfgs_found)
    # print("OBJECT TYPES FOUND", types_found)
    # there must be only one mfg word and only one item_type word in the user_query. Also, there must be a matching item in inventory (undamaged, and not needing service). If so, then show item. Otherwise, show "No such item in inventory."

    # there must be only one mfg word and only one item_type word in the user_query.
    if (len(mfgs_found) != 1 or len(types_found) != 1):
        # query_ok = False
        print("No such item in inventory")
        continue

    match_list = find_match(inven_l, mfgs_found, item_type)

    # if no matches, notify customer and return to top of loop.
    if len(match_list) == 0:
        print("No such item in inventory")
        continue

    # sort the matches price.
    match_list.sort(key=lambda x: x._price)

    # show highest price item (last item in list)
    item = match_list[-1]

    print("Your item is:", item._id, item._mfg, item._type, item._price)

    # LOOK FOR ALTERNATIVES

    # list of all manufacturers less the chosen one.
    new_mfg_set = mfl.difference(mfgs_found)
    # search for a matching item type of any of those manufacturer
    match_list = find_match(inven_l, new_mfg_set, item_type)

    if len(match_list) > 0:
        ref_price = item._price
        # sort matches based on how close they are to the original item's price
        match_list.sort(key=lambda x: abs(ref_price - x._price))
        alternative = match_list[0]
        print("You may also consider:", alternative._id, alternative._mfg, alternative._type, alternative._price)
