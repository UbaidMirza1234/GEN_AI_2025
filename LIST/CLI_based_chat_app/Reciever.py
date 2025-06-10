import socket
s=socket.socket(socket.AF_INEcdT,socket.SOCK_DGRAM)
#sender ke anadaer hamesha reciever ka ip addd dena hai
#reciever me khud ka
ip_add = "192.168.65.38"
port_number = 9999
complete_add = (ip_add, port_number)
s.bind(complete_add)
while True:
    message =s.recvfrom(1024)
    print(message)
    data =message[0]
    data ="\n"
    print(data.encode("ascii"))