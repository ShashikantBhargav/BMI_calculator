height = float(input("enter height in float:"))
height_in_meter = height = height*12/39.37
weight = int(input("enter weight in kg:"))
bmi = weight/pow(height_in_meter,2)
print("BMI ::- ",bmi)
if bmi>=26:
    print("unfit :- overweight")
elif bmi<=17:
    print("unfit :- underweight")
else:
    print("fit")
    
