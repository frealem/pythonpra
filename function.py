def functionName(g):
    return g**2
print(functionName(3))


def maxMin(arr):
    return max(arr),min(arr)

print(maxMin([1,2,3,4,6]))

def largest(a,b,c):
    if(a>b and a>c):
        big=a
    elif(b>c):
        big=b
    else:
        big=c  
    return big      


x=int(input("enter first no: ")) 
y=int(input("enter second no: ")) 
z=int(input("enter third no: "))          

print("the largest number is:",largest(x,y,z))  