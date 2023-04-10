import os
import sys

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_PATH)

from module import app
from module import api

import multiprocessing

if __name__ == "__main__":
    num_processes = 2
    processes = []
    p1 = multiprocessing.Process(target=app.run)
    p2 = multiprocessing.Process(target=api.run)
    process_list = [p1, p2]
    for p in process_list:
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

