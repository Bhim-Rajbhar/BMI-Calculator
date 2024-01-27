
################ BMI Calculator ######################

'''

BMI full form is Body Mass Index.
Formula for calculating BMI :

BMI = Weight / Height ** 2

'''

print("Welcome to Bhim's BMI Calculator\n")

Weight = float(input("Enter your Weight in KG : ")) # Using Input Fuction

Height = float(input("Enter your Height in M : ")) # Using Input Fuction

BMI = Weight / Height ** 2 # formula for calculating BMI

BMI = round(BMI, 2) # Using round function

print(BMI)