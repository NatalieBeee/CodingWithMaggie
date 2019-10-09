#function determines whether given number is prime

def prime(num):
    
    if num <= 1:
        return False

    elif num == 2:
        return True
    
    elif num % 2 == 0:
        return False
    
    else: 
        for q in range (2, num):
            if num % q == 0:
                return False

        return True

print(prime(2))
print(prime(13))
print(prime(-8))
print(prime(1))
print(prime(0))
print(prime(16))
print(prime(9))
print(prime(3))