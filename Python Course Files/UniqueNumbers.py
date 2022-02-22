numbers = [1, 1, 1, 2, 2, 6, 7, 8, 9, 9, 9, 1, 12, 15]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)