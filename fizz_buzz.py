def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return ""

i = 1
while i <= 20:
    result = fb(i)
    if result:
        print(i, result)
    else:
        print(i)
    i = i + 1
