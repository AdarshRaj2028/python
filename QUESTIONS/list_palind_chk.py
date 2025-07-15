# Method 1(For checking the palindrome in the list)
l = [1,2,3,3,2,1]
l1 = l.copy()
l.reverse()

if(l1 == l):
    print("yea")
else:
    print("no")

# Method 2(For checking the palindrome in the list)

l = [1, 2, 3, 3, 1]
n = len(l)

for i in range(n // 2):
    if l[i] != l[n - 1 - i]:
        break
else:
    print("yea") 
    exit()

print("no")

 # Check for prime numbers:

x=int(input("enter the number: "))
if(x==2):
    print("yes")
elif(x==1):
    print("no")
else:
    for i in range(2,x):
        if(x%i==0):
            break;
    else:
        print("yes")
        exit()
    print("no")