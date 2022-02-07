import time
import threading

class SleeperTask:
    def __init__(self, time):
        self.upper_bound_time = time

    def sleep_function(self, seconds):
        print(f"[SleeperTask]:\t Waiting for {seconds} seconds...")
        time.sleep(seconds)
        print(f"[SleeperTask]:\t Done waiting")

    def exec_sequential(self):
        start = time.perf_counter()

        for i in range (1, self.upper_bound_time):
            self.sleep_function(i)

        end = time.perf_counter()
        return end - start

    def exec_parallel(self):
        start = time.perf_counter()

        current_threads=[]
        for i in range (1, self.upper_bound_time):
            t = threading.Thread(target = self.sleep_function, args=[i])
            t.start()
            current_threads.append(t)

        for thread in current_threads:
            thread.join()

        end = time.perf_counter()
        return end - start
