import time
from utils import (
    fibonacci,
    fibonacci_pow,
    fibonacci_pow_bottomup
)

print("Fibonacci:")
start = time.time()
for i in range(1, 10):
    print(fibonacci(i))
end = time.time()
print("Duration: ", end - start)

print("\nFibonacci Pow:")
start = time.time()
for i in range(1, 10):
    print(fibonacci_pow(1, 1, i))
end = time.time()
print("Duration: ", end - start)


print("\nBottom-Up Fibonacci Pow:")
start = time.time()
for i in range(1, 10):
    print(fibonacci_pow_bottomup(1, 1, i))
end = time.time()
print("Duration: ", end - start)