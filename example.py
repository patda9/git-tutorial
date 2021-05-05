def factorial(n: int, acc: int = 1) -> int:
  return acc if n == 0 or n == 1 else factorial(n - 1, acc * n)

def fibonacci(n: int, fn1: int = 0, fn2: int = 1) -> int:
  return fn1 if n == 0 else (fn2 if n == 1 else fibonacci(n - 1, fn2 , fn2 + fn1))