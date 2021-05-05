def factorial(n: int, acc: int = 1) -> int:
  return acc if n == 0 or n == 1 else factorial(n - 1, acc * n)

def fibonacci(n: int) -> int:
  raise NotImplementedError