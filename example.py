import unittest

def factorial(n: int, acc: int = 1) -> int:
  return acc if n == 0 or n == 1 else factorial(n - 1, acc * n)

def fibonacci(n: int, fn1: int = 0, fn2: int = 1) -> int:
  return fn1 if n == 0 else (fn2 if n == 1 else fibonacci(n - 1, fn2 , fn2 + fn1))

class ExampleTest(unittest.TestCase):
  def test_factorial(self):
    self.assertEqual(factorial(10), 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)

  def test_fibonacci(self):
    self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55][-1])

if __name__ == "__main__":
  unittest.main()
