# 模拟12306部分功能
1 100个用户一定是并发查看票数余量，购票当然也是并发执行的           2 用户在购票时模拟网络延迟，可能查票的时候有票，但是购票的时候就没有了           3 进程之间的通信使用硬盘来完成           4 不能出现数据错误，比如多个用户买同一张票，购票成功却票数没减           4 不需要写用户的登录注册2. 基于网络通信写一个用户注册的程序，要求如下：           1 用户在客户端注册时，服务器会给用户的客户端发送一个随机验证码，用户使用它校验。           2 多个用户并发执行注册功能时服务端使用消息队列来处理用户请求
