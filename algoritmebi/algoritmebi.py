#1

def f(arr, n):

    for i in arr:
        for x in arr:
            if i != x and i + x == n:
                return True
    return False
            
print(f([1,2,4,3,5,6], 8))
        

    



#6
def f(N):
    n = 0
    while N != 0:
        if N % 2 == 1:
            n += 1
        N = N // 2
    return n
        
print(f(20))