num=int(input("enter number"))
temp=num
sum=0
while num!=0:
     x=num%10
     sum=sum+x**len(str(temp))
     num=num//10
if temp==sum:
     print("num is armstrong")
else:
     print("num is not armstrong")
     
