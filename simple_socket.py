from socket import socket, AF_INET, SOCK_RAW, IPPROTO_RAW, IPPROTO_IP, IP_HDRINCL

def open_sockets():
    client_socket = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)
    client_socket.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)