import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data = mysock.recv(512)         #recv 一次接收多少字节
messege = data.decode()         #data.decode() 转码
head_end_pos = messege.find('\r\n\r\n')+4       #由于要求不显示空行 所以+4 跳过空行\r\n\r\n

print(data.decode()[head_end_pos:])      #切片

while True:                         #构筑循环接收内容 接收完毕后关闭                            
    data = mysock.recv(512)      
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()