"""
Karis Kim
1624226
CIS 2348
"""
class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total))

    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))


class ShoppingCart:

    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        # self.cart_items = cart_items
        self.cart_items = []

    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, itemName):

        tremove_item = False

        for item in self.cart_items:
            if item.item_name == itemName:
                self.cart_items.remove(item)
                tremove_item = True
                break
        if not tremove_item:
            print('Item not found in the cart. Nothing removed')

    def modify_item(self, itemToPurchase):

        tmodify_item = False

        for i in range(len(self.cart_items)):

            if self.cart_items[i].item_name == itemToPurchase.item_name:
                tmodify_item = True

                # check for default values
                if (
                        itemToPurchase.item_price == 0 and itemToPurchase.item_quantity == 0 and itemToPurchase.item_description == 'none'):
                    break
                else:
                    if (itemToPurchase.item_price != 0):
                        self.cart_items[i].item_price = itemToPurchase.item_price
                    if (itemToPurchase.item_quantity != 0):
                        self.cart_items[i].item_quantity = itemToPurchase.item_quantity
                    if (itemToPurchase.item_description != 'none'):
                        self.cart_items[i].item_description = itemToPurchase.item_description

                    break
        if not tmodify_item:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        return total_cost

    def print_total(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items: %d\n' % self.get_num_items_in_cart())
        if (self.get_num_items_in_cart() == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print('\nTotal: $%d' % self.get_cost_of_cart())

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()


def print_menu(newCart):
    customer_Cart = newCart
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            "i - Output items' descriptions\n"
            'o - Output shopping cart\n'
            'q - Quit\n')

    command = ''
    while (command != 'q'):
        print(menu)
        while True:
            command = input('Choose an option:\n')
            if command in "aoiqrc":
                break
        if (command == 'a'):
            print("ADD ITEM TO CART")
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            itemtoPurchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            customer_Cart.add_item(itemtoPurchase)

        elif (command == 'o'):
            print('OUTPUT SHOPPING CART')
            customer_Cart.print_total()
        elif (command == 'i'):
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            customer_Cart.print_descriptions()
        elif (command == 'r'):
            print('REMOVE ITEM FROM CART')
            itemName = input('Enter name of item to remove :\n')
            customer_Cart.remove_item(itemName)
        elif (command == 'c'):
            print('CHANGE ITEM QUANTITY')
            itemName = input('Enter the item name :\n')
            qty = int(input('Enter the new quantity :\n'))
            itemToPurchase = ItemToPurchase(itemName, 0, qty)
            customer_Cart.modify_item(itemToPurchase)


if __name__ == "__main__":
    print("Enter customer's name:")
    customer_name = input()
    #customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name: %s" % customer_name)
    print("Today's date: %s" % current_date)
    newCart = ShoppingCart(customer_name, current_date)
    print_menu(newCart)
