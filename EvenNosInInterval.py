n1=int(input("Enter lower interval:"))
n2=int(input("Enter upper interval:"))
print("Even numbers between "+str(n1)+" and " +str(n2))
for i in range(n1+1,n2):
    if i%2==0:
       print(i)
