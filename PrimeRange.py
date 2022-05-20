a=int(input())
b=int(input())

for i in range(a,b+1): # 2 and 10 = 2,3,5,7 so 2 to 11
    count=0
    for j in range(1,i+1):# 1 to 2 or 3  or 5 or 7
        if i%j!=0:
            continue
        else:
            count+=1
    if count==2:
        print(i)  