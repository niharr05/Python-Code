import math

while(1):
    print("\n**********************")
    print("Press 1 for convert cm into inch")
    print("Press 2 for celsius to farhenite")
    print("Press 3 for convert seconds into hours and minutes")
    print("Press 4 for exit")
    ch = int(input("Enter your choice:- "))
    if(ch==1):
        num = float(input("Enter the number in cm"))
        inch = num/2.54
        print("The number in inches =",inch)
    elif(ch==2):
        cel = float(input("Enter the temperature into cel"))
        f = (9/5) * (cel-32)
        print("The temperature in f =",f)
    elif(ch==3):
        sec = int(input("Enter the number in seconds"))
        hours = sec/3600
        rem = sec%3600
        minute = rem/60
        seconds = rem%60
        print( math.floor(hours)," Hour",math.floor(minute)," Minutes",math.floor(seconds)," Seconds")
    elif(ch==4):
        break
    else:
        print("Invalid Output")



# Other Logic
# h = s//3600
# m = (s-(h*3600))//60
# s = (s-(h*3600))%60
