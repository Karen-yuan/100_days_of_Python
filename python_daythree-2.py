height=float(input("enter your height in m:"))
weight=float(input("enter your weight in kg:"))
BMI=round(weight/(height*height))
if BMI<18.5:
    print(f"your BMI is:{BMI},you are underweight")
elif BMI<25:
    print(f"your BMI is:{BMI},you have a normal weight")
elif BMI<30:
    print(f"your BMI is:{BMI},you are overweight")
elif BMI<35:
    print(f"your BMI is:{BMI},you are obese")
else:
    print(f"your BMI is:{BMI},you are clinically obese")
from operator import irshift


year=int(input("Which year do you want to check?"))
if year%4==0:
    if year%100==0:
        if year%400==0:
          print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year")     
else:
    print("it is not leap year")






