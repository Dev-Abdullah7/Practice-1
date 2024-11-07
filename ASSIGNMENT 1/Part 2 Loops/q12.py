# Print all prime numbers between 1 and 50

print("Prime numbers between 1 and 50:")
for num in range(1, 51):
    if num < 2:
        continue 
    is_prime = True  
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  
            break  
    if is_prime:
        print(num)
