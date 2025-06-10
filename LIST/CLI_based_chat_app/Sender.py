import socket
try:
    # creating socket// connecting to server
    s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #dgram -datagram---n/w ke trough data transfer karne ke liye
    print("Socket successfully created")
    ip_address = "192.168.65.38"
    port_number =      5050                          #0-65536
    target_add =(ip_address,port_number)
    message= input("enter the message:---->")
    encripted_message =message.encode("ascii")
    s.sendto(encripted_message,target_add)

except Exception as msg:
    print(msg)    