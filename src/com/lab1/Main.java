// Name       : Yash Pandey (https://github.com/EmperorYP7)
// Roll Number: 2019UGCS039R
// Subject    : Parallel and Distributed Computing
// Lab 1      : Construct an algorithm to show total number of threads and their thread IDs.

package com.lab1;

import java.util.Scanner;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;

public class Main {

    public static void main(String[] args) {
        int num_threads;

        if(args.length < 2) {
            num_threads = 2;
            System.out.println("Enter the number of threads (tasks) desired: ");
            Scanner in = new Scanner(System.in);
            num_threads =  Math.max(in.nextInt(), num_threads);
        }
        else
            num_threads = Math.max(Integer.parseInt(args[1]), 2);

        CreateThreads(num_threads);
    }

    public static void CreateThreads(int num_threads) {
        System.out.println("Initiating " + num_threads + " tasks in parallel");

        ForkJoinPool pool = new ForkJoinPool();
        Integer result = pool.invoke(new Lab1(num_threads));

        Thread thread = Thread.currentThread();

        System.out.println("Shutting down pool in main thread.\tThread ID: " + thread.getId());
        pool.shutdown();
    }
};

class Lab1 extends RecursiveTask<Integer> {
    final int m_num_threads;

    Lab1(int m_num_threads) {
        this.m_num_threads = m_num_threads;
    }

    @Override
    protected Integer compute() {
        Thread thread = Thread.currentThread();
        System.out.println("[task #" + m_num_threads + "]\tThread ID: " + thread.getId());

        if(m_num_threads > 1) {
            Lab1 fork_task = new Lab1(m_num_threads - 1);

            fork_task.fork();

            return fork_task.join();
        }
        return null;
    }
};
