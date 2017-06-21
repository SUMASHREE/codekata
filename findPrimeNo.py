a=int(input("Enter a no:"))
for i in range(2,a):
    if a%i==0:
        print("It is not a prime number")
        break
else:
    print("It is a prime number")
