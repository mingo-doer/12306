from socket import *
from client.conf import setting
from client.core import src
import struct
import os

server_address = setting.SERVER_ADDRESS
client = socket(AF_INET, SOCK_STREAM)
client.connect(server_address)


def send_request_dict(request_dict):
    while True:
        if not request_dict:
            continue

        # 1、制作固定长度的报头
        total_size = len(request_dict)
        header = struct.pack('i', total_size)

        # 2、发送报头
        client.send(header)

        # 3、发送真实的数据
        client.send(request_dict.encode('utf-8'))

        # client.close()  # 这里不能关闭

        break


def receive_return_dict():
    while True:
        try:
            # 1、先收固定长度的报头
            header = client.recv(4)

            # 2、解析报头
            total_size = struct.unpack('i', header)[0]

            # 3、根据报头内的信息，收取真实的数据
            receive_size = 0
            return_dict = b''
            while receive_size < total_size:
                receive_data = client.recv(1024)
                return_dict += receive_data
                receive_size += len(receive_data)

            return_dict = return_dict.decode('utf-8')  # Windows系统为gbk
            return_dict = eval(return_dict)

            return return_dict
        except Exception:
            break
    # client.close()


def auth(func):
    def wrapper(*args, **kwargs):
        if not src.user_info['name']:
            src.user_login()
        else:
            return func(*args, **kwargs)

    return wrapper


def request_and_return(request_dict):

    # 1 把dict转化成str
    request_dict = '%s' % request_dict

    # 2 发送请求数据
    send_request_dict(request_dict)

    # 3 接收返回数据
    return_dict = receive_return_dict()

    # 4 解析返回结果
    flag = return_dict['code']
    msg = return_dict['msg']

    return flag, msg


def get_all_dir_obj(path):
    if os.path.exists(path):
        obj_list = os.listdir(path)
        return obj_list
    else:
        return None
