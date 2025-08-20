def total_calc(bill_amount,tip_perc):
        total = bill_amount*(1+0.01*tip_perc)
        total = round(total,2)
        print("Please pay $", total)



input1 = int(input("Please put in your bill amount."))

input2 = int(input("Please put in your tip percentage."))
total_calc(input1,input2)