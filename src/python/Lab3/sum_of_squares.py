import time
import threading

class SumSquareTask:
    def __init__(self, n):
        self.upper_bound = n

    def sum_of_square(self, n):
        sum_square = 0
        for i in range(1, n):
            sum_square += i * i
        print(f"[SumSquareTask]:\t Sum of square of first {n} numbers is = {sum_square}")

    def exec_sequential(self):
        start = time.perf_counter()
        for i in range (1, self.upper_bound):
            self.sum_of_square(i)
        end = time.perf_counter()
        return end - start

    def exec_parallel(self):
        start = time.perf_counter()
        current_threads=[]
        for i in range (1, self.upper_bound):
            t = threading.Thread(target = self.sum_of_square, args=[i])
            t.start()
            current_threads.append(t)
        for thread in current_threads:
            thread.join()

        end = time.perf_counter()
        return end - start
