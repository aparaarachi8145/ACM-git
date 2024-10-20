# a="APARA"
# b=2
# c=None
# d=True
# print("The type of a is",type(a))
# print("The type of b is",type(b))
# print("The type of c is",type(c))
# print("The type of d is",type(d))

# for a in range(1,6):
    # b=a+1
    # print(f"{a}\t{b}\t{a**b}")

# import math
# x1,y1=map(float,input("Enter the values x1 and y1:\n").split())
# x2,y2=map(float,input("Enter the values x2 and y2:\n").split())
# x3,y3=map(float,input("Enter the values x3 and y3:\n").split())

# side1=math.sqrt((x2-x1)**2 + (y2-y1)**2)
# side2=math.sqrt((x3-x2)**2 + (y3-y2)**2)
# side3=math.sqrt((x3-x1)**2 + (y3-y1)**2)
# s=(side1 + side2 + side3)/2
# area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
# print("The area of triangle is",area)


sum_of_squares = 0


for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))  # Prompt the user for input
    sum_of_squares += number ** 2  # Compute the square and add it to the sum

# Display the result
print(f"The sum of the squares of the entered numbers is: {sum_of_squares}")
