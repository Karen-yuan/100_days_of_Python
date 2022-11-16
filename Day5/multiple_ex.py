# student_scores=input("input a list of student scores").split()
# for n in range(0,len(student_scores)):
#     student_scores[n]= int(student_scores[n])
# maxi_score=student_scores[0]
# for i in student_scores:
#     if i> maxi_score:
#         maxi_score=i
# print("the highest score in the class is:", maxi_score)
# total=0
# for number in range(1,101):
#     total+= number
# print(total)
# total=0
# for number in range(2,101,2):
#     total+= number
# print(total)

# for number in range(1,101):
#     if number%15==0:
#         print("FizzBuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     else:
#         print(number)
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("welcome to the pypassword generator!")
nr_letters=int(input("how many letters would you like in your password?\n"))
nr_numbers=int(input("how many symbols would you like?\n"))
nr_symbols=int(input("how many numbers would you like?\n"))
password=""
for char in range(1,nr_letters+1):
    random_char= random.choice(letters)
    password=password +random_char

for char in range(1,nr_numbers+1):
    random_char= random.choice(numbers)
    password=password +random_char
    
for char in range(1,nr_symbols+1):
    random_char= random.choice(symbols)
    password=password +random_char
print(password)

    


    