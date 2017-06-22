n1=int(input("Enter lower interval:"))
n2=int(input("Enter upper interval"))
flag=0
print("Armstrong numbers:")
for n in range(n1+1,n2):
  t=n
  sum=0
  while n>0:
      rem=n%10
      sum=sum+(rem*rem*rem)
      n=n//10
  if(t==sum):
      print(t)
      flag=1
if flag==0:
  print("No Armstrong numbers between the given intervals")
