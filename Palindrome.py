n = int(input('number:'))
temp = n
res = 0

while (temp!=0) :
    x = temp % 10
    res = res*10+x
    temp = temp // 10

print(res)
if res == n:
    print('palindrome')
else:
    print('not a palindrome')