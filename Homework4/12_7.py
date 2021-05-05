def get_age():  # function to read age from inputs
    age = int(input())
    if age < 18 or age > 75:  # check age validity
        raise ValueError("Invalid age.")  # If age is not valid, raise exception
    return age  # If age is valid, return age


def fat_burning_heart_rate(age):  # function to calculate heart rate

    heart_rate = 220 - age  # calculate 70% of 220 minus age
    heart_rate *= 0.7
    return heart_rate  # return heart rate


if __name__ == "__main__":
    try:  # try block of statements
        age = get_age()
        rate = fat_burning_heart_rate(age)  # call method to calculate heart rate
        print("Fat burning heart rate for a",age,"year-old: ", end="")  # print result
        print(rate, "bpm")
    except ValueError as excpt:  # If exception occurs, handle them with printing message on console
        print(excpt)
        print("Could not calculate heart rate info.\n")