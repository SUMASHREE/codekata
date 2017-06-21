n1=int(input("Enter no1:"))
n2=int(input("Enter no2:"))
n3=int(input("Enter no3:"))
if n1>n2 and n1>n3:
  print("Greatest no is:"+str(n1))
elif n2>n3 and n2>n1:
  print("Greatest no is:"+str(n2))
else:
  print("Greatest no is:"+str(n3))
