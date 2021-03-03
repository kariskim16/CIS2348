"""
Karis Kim
CIS 2348
1624226
"""
import datetime

c_date = datetime.datetime.now()
print(c_date)


m_list = ["Jan","Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

lines = []
pro_output = []


with open("inputDates.txt", "r") as x:
    lines = x.readlines()

# processing the lines
for line in lines:

    # strip off end whitespace
    _str = line.strip()

    if _str == "-1":
        break

    #find the first space -- its location tells us the end of the month part
    idx1 = _str.find(" ")
    #print(idx1)
    # if idx1 == -1, then no space was found, and this is not properly formatted -- skip to the line
    if idx1 == -1:
        continue

    # find the second space -- it is between the date and the year
    idx2 = _str.find(" ",idx1+1)
    #print(idx2)

    #_month = _str[0:idx1]
    _month = _str[0:3]
    _date = int(_str[idx1+1:idx2-1])
    _year = int(_str[idx2+1:])


    _m_number = m_list.index(_month)+1

    d = datetime.datetime(_year, _m_number, _date)

    # don't accept dates after the current date
    if d > c_date:
        continue

    y = f"{_m_number}/{_date}/{_year}"
    print(y)
    pro_output.append(y)


with open("parsedDates.txt", "w") as x:
    for l in pro_output:
        x.writelines(l + "\n")