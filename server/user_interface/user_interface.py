import random
def user_register_interface():
#     服务器给用户产生一个四位数的验证码
    capatcha=random.randint(1000,9999)
    return capatcha