# BMI Calculator
# A simple Python BMI calculator program built to practice user input, calculations, and conditional logic.

unit = input("Do you want to use kg/m or lb/in? ")

if unit == "kg/m":
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

elif unit == "lb/in":
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))

    weight = weight * 0.453592
    height = height * 0.0254

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")