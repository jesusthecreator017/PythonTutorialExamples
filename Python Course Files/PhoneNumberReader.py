phone_num = input("Phone: ")
digits_map = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in phone_num:
    output += digits_map.get(ch, "!") + " "
print(output)