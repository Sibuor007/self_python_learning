weight = float(input("Enter your weight in kg "))
height = float(input("Enter your height in meters "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and your are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} and your have normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi} and your are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi} and your are Obese")
else:
    print(f"Your BMI is {bmi} and your are clinically obese")
