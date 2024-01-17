x=input("Enter what do you want to peform: ")
a1=int(input("Enter your 1st number:"))
a2=int(input("Enter your 2nd number:"))

q="+"
w="-"
e="*"
r="/"

def sum(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
if (x==q):
    print(sum(a1,a2))

elif(x==w):
    print(sub(a1,a2))

elif(x==e):
    print(mul(a1,a2))

elif(x==r):
    print(div(a1,a2))

else:
    print("Error 404","Enter Valid option")
#print(sum(5,6))
#x=sub(15,5)
#y=div(6,4)
#z=mul(7,8)
#print(x)
#print(y)
#print(z)

#=sum("Ara","Bihar")
#print(l)