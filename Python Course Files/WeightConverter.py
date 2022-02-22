weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * .45
print(weight_kg)

# My version / Updated Verison
'''
lbs_or_kg = input("What conversion do you want to make? (lbs or kg): ")
weight = int(input("What is your weight?: "))
if (lbs_or_kg == "kg"):
    print(f"Your weight in kg is: {weight * .45}")
elif(lbs_or_kg == "lbs"):
    print(f"Your weight in lbs is {weight / .45}")
'''