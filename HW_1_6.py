def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        print(a)
        a, b = a + b, a


if __name__ == "__main__":
  fibonacci(100)


