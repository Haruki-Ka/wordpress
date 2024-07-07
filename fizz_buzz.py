def fb(n):
    return (n % 3 == 0) * "Fizz" + (n % 5 == 0) * "Buzz" or str(n)

for i in range(1, 200):
    print(i, fb(i))
