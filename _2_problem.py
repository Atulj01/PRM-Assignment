# check valid triangle

def triangle(A,B,C):
   if (A + B <= C ) or (A + C <= B) or (B + C <= A):
        return False
   else: 
        return True 


A = int(input("enter the side of triangle : "))
B = int(input("enter the side of triangle : "))
C = int(input("enter the side of triangle : "))

print("\nvalue for rectangle\n")

def rectangle(A,B,C,D):
    if (A == B and D == C) or (A == C and B == D) or (A == D and B == C):
        return True
    else:
        return False
 
A = int(input("enter the side of rectangle : "))
B = int(input("enter the side of rectangle : "))
C = int(input("enter the side of rectangle : "))
D = int(input("enter the side of rectangle : "))


if triangle(A,B,C):
    print("valid Triangle")
else:
    print("invalid Triangle")


if rectangle(A,B,C,D):
    print("valid Rectangle")
else:
    print("invalid Rectangle")

