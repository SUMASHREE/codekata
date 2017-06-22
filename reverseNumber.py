n=int(input("Enter a number:"))
num=n
sum=0
while(n>0):
     rem=n%10
     sum=(sum*10)+rem
     n=n//10
print("The reverse of "+str(num)+" is "+str(sum))
