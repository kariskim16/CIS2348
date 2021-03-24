"""
Karis Kim
1624226
CIS 2348
"""
soccer_details = {}


# (1) Prompting user to input 5 pair of number
def addplayers(self):
    for i in range(1, 6):
        jersey = int(input("Enter player {}'s jersey number:".format(i)))
        rating = int(input("Enter player {}'s ratings:".format(i)))
        self.soccer_details[jersey] = rating


# (2) Implementing a menu option
def menu(self):
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    option = input("\nChoose an option:  ")
    return option


# (3)Implementing "Output roaster" menu option
def Output_Roster(self):
    sorted_jersey = sorted(self.soccer_details.keys())
    print("ROSTER")
    for jersey in sorted_jersey:
        print("Jersey number: {}, Rating: {}".format(jersey, self.soccer_details[jersey]))


# (4)Implementing "Add player" menu option:
def Add_Player(self):
    jersey = int(input("Enter a new player's jersey number: "))
    rating = int(input("Enter the player's rating: "))
    self.soccer_details[jersey] = rating


# (5)Implementing "delete player" menu option
def Remove_Player(self):
    jersey = int(input("Enter a jersey number: "))
    del self.soccer_details[jersey]


# (6) Implementing "update player raing" menu option
def Update_Player_Rating(self):
    jersey = int(input("Enter a jersey number: "))
    new_rating = int(input("Enter a new rating for player: "))
    self.soccer_details[jersey] = new_rating


# (7)Implementing "Output player above a rating" menu option
def Above_Rating(self):
    rating = int(input("Enter a rating"))
    sorted_jersey = sorted(self.soccer_details.keys())
    print("ABOVE {}".format(rating))
    for jersey in sorted_jersey:
        if (self.soccer_details[jersey] > rating):
            print("Jersey number: {}, Rating: {}".format(jersey, self.soccer_details[jersey]))


if __name__ == "__main__":
    # creating object for the class
    obj = Soccer()

    # Prompting user to input 5 pair of number
    obj.addplayers()

    # menu actions
    while (True):
        option = obj.menu()
        if (option == 'a'):
            obj.Add_Player()
        elif (option == 'd'):
            obj.Remove_Player()
        elif (option == 'u'):
            obj.Update_Player_Rating()
        elif (option == 'r'):
            obj.Above_Rating()
        elif (option == 'o'):
            obj.Output_Roster()
        elif (option == 'q'):
            exit()
        else:
            print("Invalid option")
