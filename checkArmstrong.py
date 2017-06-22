n=int(input("Enter a number:"))
t=n
sum=0
while n>0:
    rem=n%10
    sum=sum+(rem*rem*rem)
    n=n//10
if(t==sum):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
