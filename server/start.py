from server.core import src
from multiprocessing import  Process,JoinableQueue
#100个用户一定是并发查看票数余量，购票当然也是并发执行的
if __name__ == '__main__':
    q=JoinableQueue()
    for i in range(100):
        p=Process(target=src.run(),args=(i,))
        p.start()
        p.join()
    q.join()
