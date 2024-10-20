# def pyramid(n):
#     i=0
#     for i in range(1,n):
#         print(" "*(n-i), end=" ")
#         print("* "*i)

# def reverse_pyramid(n):
#     for i in range(n,0,-1):
#         print(" "*(n-i), end=" ")
#         print("* "*i)

# pyramid(6) 
# reverse_pyramid(6) 

# import math
# def roots(a,b,c):
#     discriminant=b**2-4*a*c 

#     if discriminant>0:
#         root1= (-b+math.sqrt(discriminant))/(a*2)   
#         root2= (-b-math.sqrt(discriminant))/(a*2)  
#         print(f"The roots are real and different:{root1} and {root2}")
#     elif discriminant==0:
#         root1=-b/(a*2)
#         print(f"The roots are real and same:{root1}")
#     else:
#         real= -b/(a*2)    
#         imaginary= (math.sqrt(discriminant))/(a*2) 
#         print(f"The roots are complex:{real} + {imaginary}i and {real} - {imaginary}i")
# roots(1,6,-7)        

def a(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i ==0:
            return False
        else:
            return True
def b(n):
    prime=[]
    
    for i in range(2,n):
        if a(i):
            prime.append(i)
    return prime

def c(n):
    prime=[]        
    num=2
    while len(prime)<n:
        if a(num):
            prime.append(num)
        num+=1    
    return prime        

def main():

    n=int(input("Enter your number:\n"))
    
    if a(n):
        print(n,"is a prime number.")
    else:
        print(n,"is not a prime number.")  

    b(n)
    print("Prime numbers till", n,"are",b(n))

    c(n)
    print("The first", n,"prime number are:",c(n))
main()
print(main())    
          


        

