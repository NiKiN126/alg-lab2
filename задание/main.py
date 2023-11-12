import time

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    start_time = time.time()

    n = int(input("Какое число фибоначе вывести: "))

    if n <= 1:
        print(f"F[{n}] = {n}")
    else:
        print(f"Fib [{n}] = {fib(n)}")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time}")
