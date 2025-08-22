while(1):
    print("\n**********************")
    print("Press 1 for the area of circle")
    print("Press 2 for the area of rectangle")
    print("Press 3 for the area of square")
    print("Press 4 for the area of triangle")
    print("Press 5 for exit")
    ch = int(input("Enter your choice:- "))

    if(ch==1):
        r = float(input("Enter Radius "))
        area = 3.14*r*r
        print("The area of the circle =",area)
    elif(ch==2):
        l = float(input("Enter the length "))
        b = float(input("Enter the breadth "))
        area = l*b
        print("The area of the rectangle =",area)
    elif(ch==3):
        l = float(input("Enter the length "))
        area = l*l
        print("The area of the square =",area)
    elif(ch==4):
        l = float(input("Enter the length "))
        h = float(input("Enter the height "))
        area = 0.5*l*h
        print("The area of the traingle =",area)
    elif(ch==5):
        break
    else:
        print("Invalid Output")