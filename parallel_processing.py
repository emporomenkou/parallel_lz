import multiprocessing as mp
import time
import random as rd
import math

def monte_carlo(n : int):
    inside = 0
    rd.seed()
    for _ in range(n):
        x = rd.random()
        y = rd.random()
        if x*x + y*y <= 1.0:
            inside += 1
    return inside

def multiprocess(process_num, point_num : int):
    point_per_process = math.ceil(point_num / process_num)
    tasks = [point_per_process] * process_num
    with mp.Pool(processes=process_num) as pool:
        results = pool.map(monte_carlo, tasks)
    return sum(results)

def main():
    print("Многопроцессорность: ")
    points = 100_000_000    
    start = time.time()
    processes = 10
    total_inside = multiprocess(processes, points)
    pi1 = (4 * total_inside / points)
    print(f"Результаты асинхронного выпонения: {time.time() - start}, {pi1}")
    start = time.time()
    total_inside = monte_carlo(points)
    pi2 = (4 * total_inside / points)
    print(f"Результаты синхронного выпонения: {time.time() - start}, {pi2}")

if __name__ == "__multiprocessing_main__":
    main() 
