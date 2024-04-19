num1=int(input("enter fisrt number"))
num2=int(input("enter second number"))
operate=input("enter the operator: ")

if(operate=='+'):
    print("the solution is :",num1+num2)
elif(operate=='-'):
     print("the solution is :",num1-num2)
elif(operate=='*'):
     print("the solution is :",num1*num2)
elif(operate=='/'):
     print("the solution is :",abs(num1/num2))