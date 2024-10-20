
# def series(n):
#     sum=0
#     for i in range(1,n):
#         sum+= 1/i
#     return sum
# n=int(input("Enter your number:"))    
# result=series(n)
# print(f"The sum of the series is:{result}")

def series(n):
    N=1
    D=3
    sum=0

    for i in range(1,n):
        sum+=N/D
        N+=2
        D+=2
        
    return sum
n=int(input("Enter your number:"))    
result=series(n)
print(f"The sum of the series is:{result}")


# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         fact = 1
#         for i in range(2, num + 1):
#             fact *= i
#         return fact

# # Function to compute the sum of the series up to n terms
# def compute_series(n):
#     sum = 0  # Starting with 1 as the first term in the series
#     for i in range(1, n+1):
#         sum += 1 / factorial(i)
#     return sum

# # Read the value of n from the user
# n = int(input("Enter the number of terms: "))
# result = compute_series(n)
# print(f"The sum of the series up to {n} terms is: {result}")




