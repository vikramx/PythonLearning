#python program to check BMI
h=float(input("Enter height in centimetres here:"))
w=float(input("Enter weight in kilograms here:"))
num=h/100
num2=num**2
bmi=w/num2
print(bmi)
if(bmi<18.5):
    print("You are underweight.")
elif(bmi>=18.5 and bmi<=24.9):
    print("You are normal.")
elif(bmi>=25 and bmi<=29.9):
    print("You are overweight.")
else:
    print("You are obese.")
