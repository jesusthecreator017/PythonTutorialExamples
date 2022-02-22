from numpy import number


numbers = [3, 5, 7, 9, 12, 25, 1]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)