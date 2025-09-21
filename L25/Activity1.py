"Adding two lists using map and lambda"
"lambda?"

numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))

#using map

nums = [1,2,3,4,5]
def square2(n):
    return n*n
square = list(map(square2, nums))
print("Square of numbers in list")
print(square)