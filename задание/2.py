import time

def fibonacci(n):
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
        print(f"F[{i + 1}] = {arr[i]}")
    return arr

if __name__ == "__main__":
    start_time = time.time()

    n = int(input("Размерность массива и сколько чисел фибоначи вывести: "))
    result_array = fibonacci(n)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time}")