import threading as th
import queue as q
import time
import random as rd
import os

file_lock = th.Lock()
dat_queue = q.Queue()

def generating():
    numbers = [str(rd.randint(1, 1000)) for _ in range(2000)]
    s1 = ", ".join(numbers) + ", "
    time.sleep(0.1)    
    with file_lock:
        with open("input.txt", "a", encoding="utf-8") as file:
            file.write(s1)


def reading(j1 : int):
    i = 100
    time.sleep(0.1)    
    with file_lock:
        with open("input.txt", "r", encoding="utf-8") as file:
            file.seek(j1 * i)
            s1 = file.read(i)
    dat_queue.put(s1)
    j1 += 1


def writing():
    while True:
        s1 = dat_queue.get()
        if s1 == "-1":
            dat_queue.task_done()   
            break         
        with open("output.txt", "a", encoding="utf-8") as file:
            file.write(s1)
        dat_queue.task_done()
def thread_queue(f):
    threads = []
    if f == reading:
        for j in range(5):
            t = th.Thread(target=f, args=(j,))
            t.start()
            threads.append(t)
    else:
        for _ in range(5):
            t = th.Thread(target=f)
            t.start()
            threads.append(t)
    for t in threads:
        t.join()

def multithreading():
    j = 0    
    thread_queue(generating)
    thread_queue(reading)
    writter = th.Thread(target=writing)
    writter.start()
    dat_queue.put('-1')
    writter.join()
    os.remove("input.txt")
    os.remove("output.txt")     

def sync():
    for _ in range(5):
        numbers = [str(rd.randint(1, 1000)) for _ in range(2000)]
        s1 = ", ".join(numbers) + ", "
        time.sleep(0.1)
        with open("input.txt", "a", encoding="utf-8") as file:
            file.write(s1)
    i = 100
    for j in range(5):
        time.sleep(0.1)
        with open("input.txt", "r", encoding="utf-8") as file:
            file.seek(j * i)
            s1 = file.read(i)
        with open("output.txt", "a", encoding="utf-8") as file:
            file.write(s1)
    os.remove("input.txt")
    os.remove("output.txt")    

def main():
    print("Многопоточность:")
    start = time.time()
    sync()
    print(f"Время синхронного выполнения: {time.time() - start}")
    start = time.time()
    multithreading()
    print(f"Время aсинхронного выполнения: {time.time() - start}")    

if __name__ == "__main__":
    main()
    

