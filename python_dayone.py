print("welcome to the band game generator")
a=input("what is name of the city you grew up in?\n")
b=input("what is your pet's name?\n")
print("your band name could be "+ a +" "+ b)
num_char=len(input("what is you name"))
new_num_char=str(num_char)
print("your name has"+""+ new_num_char+" "+"characters.")
two_digit_number=input("enter a number")
first_digit=two_digit_number[0]
sec_digit=two_digit_number[1]
result=int(first_digit)+int(sec_digit)
print(result)
print(int(3*3+3/3-3))
height=input("enter your height in m:")
weight=input("enter your weight in kg:")
BMI=int(weight)/(float(height)*float(height))
print(BMI)
print(round(8/3,2))
score=0
height=1.83
final_result=True
result=(f"your score is {score}, and your height is {height},so your final result is {final_result}")
print(result)
age=input("what is your current age")
new_age=int(age)
days=32850-new_age*365
weeks=4680-new_age*52
months=1080-new_age*12
print(f"your have{days}days,{weeks}weeks,{months}months left")



