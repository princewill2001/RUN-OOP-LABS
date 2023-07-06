def factorial(q):
        if q == 0:
            return 1
        else:
            return q * factorial(q-1)

print(factorial(15))


