try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma: "))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("DEVISION BY ZERO IS A MASSIVE ERROR")
except SyntaxError:
    print("Comma is missing. Enter numbers seperated like this 1,2")
    print("If you didnt input numbers, restart and read the instructions again. Unbelievable.")
except:
    print("Wrong input!!")
    print("If you didnt input numbers, restart and read the instructions again. Unbelievable.")
else:
    print("No execution")

finally:
    print("I AM GONNA GET EXECUTED")