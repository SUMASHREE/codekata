t1=0
t2=1
n=int(input("Enter no of terms:"))
print(t1)
print(t2)
i=2
while i<n:
        t3=t1+t2
        print(t3)
        t1=t2
        t2=t3
        i=i+1
