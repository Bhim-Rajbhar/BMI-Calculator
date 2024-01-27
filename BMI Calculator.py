
################ BMI Calculator ######################

'''
BMI full form is Body Mass Index.
Formula for calculating BMI :

BMI = Weight / Height ** 2 
or
BMI = kg/m2
'''


print("Welcome to Bhim's BMI Calculator\n")

# Getting user input for weight and height
Weight = float(input("Enter your Weight in KG : ")) # Using Input Fuction
Height = float(input("Enter your Height in M : ")) # Using Input Fuction

# Calculating BMI using the formula
BMI = Weight / Height ** 2 

# Rounding the BMI to two decimal places
BMI = round(BMI, 2) 

# Printing the calculated BMI
print(BMI)
