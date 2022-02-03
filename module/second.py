def is_palindrome(st):
    if st==st[::-1]:
        return True
    else:return False
    
    
def find_frequency(st,word):
    return st.count(word)


def factorial(n):
    fact=1
    for num in range(n,0,-1):
        fact*=num
    return fact