from sleeper import SleeperTask
from sum_of_squares import SumSquareTask

class Constants():
    SLEEP_UPPER_BOUND = 5
    SUM_SQUARE_UPPER_BOUND = 10000

def main():
    sleep_task = SleeperTask(Constants.SLEEP_UPPER_BOUND)
    sum_square_task = SumSquareTask(Constants.SUM_SQUARE_UPPER_BOUND)

    sleep_sequential_time = sleep_task.exec_sequential()
    sum_square_sequential_time = sum_square_task.exec_sequential()

    sleep_parallel_time = sleep_task.exec_parallel()
    sum_square_parallel_time = sum_square_task.exec_parallel()

    print("\n-------- Results --------")
    print(f"[SleepTask] Sequential: {sleep_sequential_time} s")
    print(f"[SleepTask] Parallel  : {sleep_parallel_time} s")
    print(f"[SumSquareTask] Sequential: {sum_square_sequential_time} s")
    print(f"[SumSquareTask] Parallel  : {sum_square_parallel_time} s\n")

if __name__ == '__main__':
    main()
