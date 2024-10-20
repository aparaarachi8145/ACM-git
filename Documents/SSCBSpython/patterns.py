# a) 
# def pattern(n):
#     for i in range(1,n):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
# pattern(6)    

#b)
def pattern(n):
    for i in range(1,n):
        for j in range(1,1+i):
            print(j,end=" ")
        print() 
        for i in range(n,0,-1):
          for j in range(1,1+i):
            print(j,end=" ")
        print()
pattern(5)                  