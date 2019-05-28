import  time,random
from multiprocessing import  process,Lock
from server.db import  db_handler
mutex=Lock()

def check_ticket():
    # 查票是可以完全并发的
    db_handler.select()


def buy_ticket(lock):
    # 因为购票需要有先后顺序  需要用到acquire
    lock.acquire()
    check_ticket()
    choice=int(input('输入要购买的车票'))
    db_handler.save(choice)
    lock.release()


func_dict = {
    '1': check_ticket,
    '2': buy_ticket,

}

def run():
    while True:
        print("""
            1 查询余票
            2 买票 
            3 注册 
            """)
        choice = input('请选择功能>>:').strip()
        if choice not in func_dict:
            continue
        if choice=='2':
            buy_ticket(mutex)
        else:
            func_dict[choice]()