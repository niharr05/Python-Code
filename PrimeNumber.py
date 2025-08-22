# Here we use else with for loop
n=int(input("Enter number "))

for i in range(2,n):
    if(n%i==0):
        print("The number is not prime")
        break
else:
    print("The number is prime")