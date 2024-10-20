# count=0
# while count<10:
#      print(count)

# count=0
# while count < 100:
#     print(count)
#     count -= 1

# count=0
# while count<10:
#     print(count)
#     count +=1

sum=0
while(sum<1001):
    sum+=1
    print(sum)



n = int(input("Enter the number of elements: "))
num=[]
count=0
for i in range(n):
    num=int(input("Enter the numner"))
    
    if num%3==0:
        count+=1
print("the number is divisible by 3:",count)       



# n=int(input("Enter your number of elements:")) 
# num=[]
# smallest=float('inf')
# count=0
# for i in range(n):
#     num=int(input("Enter your number:"))
#     if(num<smallest):
#         smallest=num
#         count+=1
# print("The smallest number is",smallest)




