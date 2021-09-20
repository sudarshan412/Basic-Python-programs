#using for loop
'''n = int(input("input number :"))
sum = 0
for i in range(0,n+1):
    sum = sum+i
print(sum)'''


# using recursion
n = int(input("input number :"))
def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)
        
print(sum(n))