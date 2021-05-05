def factorial(n: int) -> int:
  return 1 if n == 0 or n == 1 else n * factorial(n - 1) 

def fibonacci(n: int) -> int:
  raise NotImplementedError