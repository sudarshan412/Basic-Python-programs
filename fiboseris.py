
# using for loop

num = int(input('Enter a number :'))
n1, n2 = 0, 1
sum = 0
if num <= 1:
    print("1")
else:
    for i in range(0,num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum 
        sum = n1+n2

       

#using recursion

n = int(input('Enter a number :'))
def fibo(n):
    if n==1 or n==0:
        return n;
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(0,n):
    print( fibo(i) )

