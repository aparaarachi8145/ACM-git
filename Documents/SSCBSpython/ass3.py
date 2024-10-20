# for i in range(1,5):
#     j=0
#     while j<i:
#         print(j,end=" ")
#         j+=1

i=0
while i<5:
    for j in range(i,1,-1):
        print(j,end=" ")
    print('****')
    i+=1