"""
Karis Kim
CIS 2348
1624226
"""
def userinput():
    user_num1 = int(input("Enter Integer: "))
    user_square = user_num1 * user_num1
    user_cube = user_num1 * user_num1 * user_num1

    print("You entered", user_num1)
    print(user_num1, "squared is", user_square)
    print(user_num1, "cubed is", user_cube, "!!")

    user_num2 = int(input("Enter another integer: "))
    print(user_num1, "+", user_num2, "is", user_num1 + user_num2)
    print(user_num1, "*", user_num2, "is", user_num1 * user_num2)
userinput()
