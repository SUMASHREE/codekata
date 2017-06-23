    n=int(input("Enter number for which seed is to be found:"))
    num=n
    sum=1
    while n>0:
        rem=n%10
        sum=sum*rem
        n=n//10
    print("Seed of "+str(num)+" is "+str(num*sum))
