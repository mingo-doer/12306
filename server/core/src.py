from server.lib import  communication

def run():
    print('服务端启动')
    communication.receive_request_dict()