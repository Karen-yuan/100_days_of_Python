print("welcome to the tip calculator")
pure_bill=float(input("what is the total bill?$"))
tip=int(input("what percentage tip would you like to give? 10, 12 or 15"))
num_ppl=int(input("how many ppl to split the bill?"))
total_bill_per_person=(tip/100*pure_bill+pure_bill)/num_ppl
final_bill=round(total_bill_per_person,2)
final_bill="{:.2f}".format(final_bill)
print("each person should pay:"+str(final_bill))