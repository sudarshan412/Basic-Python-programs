
# 1 to n series
n = int(input('enter a num: '))
def series(n):
    if n == 0:
        return 0
    
    else:
        series(n-1)
        print(n)
        
series(n)

# N to 1 series
n = int(input('enter a num: '))
def series(n):
    if n == 0:
        return 0
    
    else:
        print(n)
        series(n-1)
        
        
series(n)
