while True:
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    print("Please enter your choice :\n 1.Addition \n 2.Substarction\n3.Multiplication\n4.Division")
    choice=int(input("Enter your choice 1,2,3,4 : "))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a/b)
    else:
        print("Please enter a valid input from choices given")
    c=input("Do you wish to continue (yes/no) ?")
    if c.lower()!="yes":
        break
