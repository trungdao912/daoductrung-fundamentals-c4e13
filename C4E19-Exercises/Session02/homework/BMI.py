height_cm = float(input("Enter your height:"))

weight = float(input("Enter your weight:"))

height_m = height_cm / 100

BMI = weight / (height_m**2)

if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5: 
    print("Under weight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Over weight")
else:
    print("Obese")