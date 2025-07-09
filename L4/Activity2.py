Amount =int(input("Please Enter Amount for Withdraw :"))

note = Amount//1000
note_1 = (Amount%1000)//100
note_2 = ((Amount%1000)%100)//50
note_3 = (((Amount%1000)%50)%100)//10

print("notes of 1000 dollars", note)
print( "notes of 100 dollars" , note_1)
print("notes of 50 dollars", note_2)
print("notes of 10 dollars" , note_3)