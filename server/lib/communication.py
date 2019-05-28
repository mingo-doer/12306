from socket import socket
from server.conf import settings
from server.user_interface import user_interface
import struct
server_address = settings.SERVER_ADDRESS
server = socket()
server.bind(server_address)
server.listen(5)
conn, client_address = server.accept()

def send_return_dict(result):
    while True:
        try:
            code = result[0]
            msg = result[1]
            data = '%s' % {'code': code, 'msg': msg, }

            # 1、制作固定长度的报头
            total_size = len(data)
            header = struct.pack('i', total_size)

            # 2、发送报头
            conn.send(header)

            # 3、发送真实的数据
            conn.send(data.encode('utf-8'))
            break
        except Exception:
            break
        # conn.close()
    # server.close()

def receive_request_dict():
    print('客户端 ', client_address)
    while True:
        # try:

        # 1、先接收固定长度的报头
        header = conn.recv(4)

        # 2、解析报头
        total_size = struct.unpack('i', header)[0]

        # 3、根据报头内的信息，收取真实的数据
        receive_size = 0
        request_dict = b''
        while receive_size < total_size:
            receive_data = conn.recv(1024)
            request_dict += receive_data
            receive_size += len(receive_data)

        # 4 分发任务
        result = distribute(request_dict)

        # 5 发送执行结果
        send_return_dict(result)
        # break

        # return request_dict
    # except Exception:
    #     break
    # conn.close()
    # server.close()


func_dict = {
    'register': user_interface.user_register_interface,
}
# 分发任务
def distribute(request_dict):
    operation = eval(request_dict)['operation']
    result = func_dict[operation](request_dict)
    return result
