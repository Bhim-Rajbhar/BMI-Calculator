
################ BMI Calculator ######################

"""
BMI full form is Body Mass Index.
Formula for calculating BMI :

BMI = Weight / Height ** 2 
or
BMI = kg/m2
"""
###########################################################################
print("Welcome to Bhim's BMI Calculator\n")

# Getting user input for weight and height
Weight = float(input("Enter your Weight in KG : ")) # Using Input Fuction
Height = float(input("Enter your Height in M : ")) # Using Input Fuction

# Calculating BMI using the formula
BMI = Weight / ( Height * Height )
BMI_Round = round(BMI, 2)

if BMI < 18.5:
  print(f"Your BMI is {BMI_Round}, you are underweight. ")
elif BMI < 25:
  print(f"Your BMI is {BMI_Round}, you have a normal weight.")
elif BMI < 30:
  print(f"Your BMI is {BMI_Round}, you are slightly overweight.")
elif BMI < 35:
  print(f"Your BMI is {BMI_Round}, you are obese.")
else:
  print(f"Your BMI is {BMI_Round}, you are clinically obese.")

