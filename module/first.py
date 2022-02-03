def is_even(n):
    if n%2==0:
        return True
    else:
        return False
    
    
def is_prime(n):
    count=0
    for num in range(1,n+1):
        if n%num==0:
            count+=1
    if count==2:
        return True
    else:return False
    
    
#is_prime(n)
def is_perfect(n):
    s=0
    for num in range(1,n//2+1):
        if n%num==0:
            s+=num
    if s==num:
        return True
    else:return False