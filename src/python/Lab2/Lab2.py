import threading
import time

# Constants
num_square = 1000
sleep_time = 10

class Test():
    def sum_of_square(self, n):
        sum = 0
        for i in range(1, n + 1):
            sum += i * i
        print(f"[test]:\t Sum of square of first {n} numbers is = {sum}")

    def sleep_function(self, seconds):
        print(f"[test]:\t Waiting for {seconds} seconds...")
        time.sleep(seconds)
        print(f"[test]:\t Done waiting")

    def run_sequentially(self):
        sequential_start = time.perf_counter()

        self.sum_of_square(self, num_square)
        self.sleep_function(self ,sleep_time)

        sequential_end = time.perf_counter()

        return sequential_end - sequential_start

    def run_multithreaded(self):
        sum_of_square_thread = threading.Thread(target=self.sum_of_square, args=[self, num_square])
        sleep_thread = threading.Thread(target=self.sleep_function, args=[self, sleep_time])

        multithread_start = time.perf_counter()

        sum_of_square_thread.start()
        sleep_thread.start()

        sum_of_square_thread.join()
        sleep_thread.join()

        multithread_end = time.perf_counter()

        return multithread_end - multithread_start

print(f"[core]:\t num_square = {num_square} \t sleep_time = {sleep_time} seconds")

sequential_runtime = Test.run_sequentially(Test)
multithreaded_runtime = Test.run_multithreaded(Test)

print("\n\n------ Results ------")
print(f"Sequential runtime = {sequential_runtime} seconds.")
print(f"Multi-Threaded runtime = {multithreaded_runtime} seconds.")
