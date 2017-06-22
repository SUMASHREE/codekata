n1=int(input("Enter lower interval:"))
n2=int(input("Enter upper interval:"))
print("Prime numbers:")
for i in range(n1+1,n2):
     for j in range(2,i):
          if i%j==0:
              break
     else:
          print(i)
