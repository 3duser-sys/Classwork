"array"
import array as yippee
array_num = yippee.array('i',[1,3,5,3,7,9,3])
print("Original array: " +str(array_num))

print("Number of occurences of number 3 in said array:" +str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))