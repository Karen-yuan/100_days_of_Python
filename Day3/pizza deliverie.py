print("Welcome to python pizza deliveries!")
size=input("What size pizza do you want? S,M or L")
bill=0
if size=="S":
  bill+=15
elif size=="M":
  bill+=20
else:
  bill+=25
add_pepperoni=input("Do you want to add pepperoni? Y or N")
if add_pepperoni=="Y":
  if size=="S":
    bill+=2
  elif size=="M"or"L":
    bill+=3
else:
  bill+=0
extra_cheese=input("Do you want extra cheese? Y or N")
if extra_cheese=="Y":
  bill+=1
print(f"your final bill is ${bill}")
