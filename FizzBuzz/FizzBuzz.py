# Programa FizzBuzz hasta el 1000 en Python

for i in range(1, 1001):  # Desde 1 hasta 1000
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
