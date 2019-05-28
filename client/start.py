from client.core import  src
from multiprocessing import Process
import time,random
if __name__ == '__main__':
    start_time=time.time()
    p_list=[]
    for i in range(100):
        p=Process(target=src.run(),args=(i,))
        p_list.append(p)
        p.start()
        time.sleep(random.randint(1,3))
    for p in p_list:
        p.join()
