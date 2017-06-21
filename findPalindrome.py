n=int(input("Enter a number:"))
num=n
rev=str(num)[::-1]
if int(rev)==n:
   print("Palindrome")
else:
   print("Not palindrome")
