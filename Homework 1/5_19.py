"""
Karis Kim
CIS 2348
1624226
"""
def caroptions():
    # options
    print("Davy's auto shop services")
    print("Oil change -- $35")
    print("Tire rotation -- $19")
    print("Car wash -- $7")
    print("Car wax -- $12")


# setting the prices
oil_change = 35;
tire_rotation = 19;
car_wash = 7;
car_wax = 12;
total = 0;
first_service = 0;
sec_service = 0;

caroptions()

# userinput
option_one = input("Select first service:")

if ("oil" in option_one.lower()):
    total = total + oil_change;
    first_service = oil_change;

elif ("tire" in option_one.lower()):
    total = total + tire_rotation;
    first_service = tire_rotation;

elif ("wash" in option_one.lower()):
    total = total + car_wash;
    first_service = car_wash;

elif ("wax" in option_one.lower()):
    total = total + car_wax;
    first_service = car_wax;

elif (option_one == "-"):
    option_one = "No service";
    total = total + 0;

# userinput for 2nd service
option_two = input("Select second service:")

if ("oil" in option_two.lower()):
    total = total + oil_change;
    sec_service = oil_change;

elif ("tire" in option_two.lower()):
    total = total + tire_rotation;
    sec_service = tire_rotation;

elif ("wash" in option_two.lower()):
    total = total + car_wash;
    sec_service = car_wash;

elif ("wax" in option_two.lower()):
    total = total + car_wax;
    sec_service = car_wax;

elif (option_two == "-"):
    option_two = "No service";
    sec_service = 0;
    total = total + 0;

print()
print("Davy's auto shop invoice")
print()
# noservice part of the code
if (option_one == "No service") and (option_two == "No service"):
    print("Service 1:" + first_service)
    print("Service 2:" + sec_service)
    print()

elif (sec_service == "No service"):
    print("Service 1:" + option_one + ",$" + option_one)
    print("Service 2:" + option_two)
    print()

elif (option_one == "No service"):
    print("Service 1:" + option_one)
    print("Service 2:" + option_one + ",$" + option_two)
    print()

else:
    print("Service 1:" + option_one + ",$" + first_service)
    print("Service 2:" + option_two + ",$" + sec_service)
    print()
# give output total
print("Total: $" + total)