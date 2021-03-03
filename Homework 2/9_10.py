"""
Karis Kim
CIS 2348
1624226
"""
import csv

# user input for the file
file_name = input()

words = {}

# reading the file
with open(file_name, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:

        for letter in row:

            if letter not in words.keys():
                words[letter] = 1

            else:
                words[letter] += 1

# result
for key in words.keys():
    print(key + " " + str(words[key]))