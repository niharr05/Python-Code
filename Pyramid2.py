# *
# * *
# * * *
# * * * *
# * * * * *


n = int(input("Enter The last row number = "))

for r in range(1,n+1):
    for c in range(r,n+1):
        print("*",end="")
    print()
