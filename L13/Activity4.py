N = int( input("enter number of rows: "))
M = int( input("enter number of columns: "))

for i in range(1, N, 2): 
    print((i*".|.").center(M,"-"))

print("WELCOME".center(M, "-"))
for i in range(N-2, -1, -2):
    print((i*".|.").center(M, "-"))