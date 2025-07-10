'''age=int(input("enter you age:"))'''

"""
syntax
if ccondition:
     stetement
else:
    stetement
"""

'''age=int(input("enter you age:"))
if age>=18:
 print("eligibil for votung")
 print("please get your voting id")
else:
    print("not eligibil for voting")'''

'''age=int(input("enter your age:"))
if age>=18:
    print("eligibil for voting:")
    print("enter your voter id")
else:print("not eligibil")'''


"""number=int(input("enter your number:"))
if number %2==0:
    print("number,is even")
else:
    print("number,is odd")"""

"""year=int(input("enter your year : "))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not leap year")"""

payment_status=False
mark=int(input("enter your mark:"))
if payment_status:
    if mark>=60:
        print("eligibile for exam")
    else:
        print("please enter your modeal exam mark")
else:
    print("please compleat your payment")
