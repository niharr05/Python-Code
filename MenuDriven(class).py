while(1):
    print("**********************")
    print("Enter 1 for the odd/even")
    print("Enter 2 for prime or not")
    print("Enter 3 for assert")
    print("Enter 4 for exit")
    ch = int(input("Enter Your Choice "))
    if(ch==1):
        n = int(input("Enter the number "))
        if(n%2==0):
            print("The number is even")
        else:
            print("The number is odd")
    elif(ch==2):
        n = int(input("Enter the number "))
        for i in range(2,n):
            if(n%i==0):
                print("The number is not prime")
                break
            else:
                print("the number is prime")
                break
    elif(ch==3):
        n = int(input("Enter the number "))
        assert n>0
        print("The number is possitive")

    elif(ch==4):
        break
    else:
        print("Invalid Inputs")
