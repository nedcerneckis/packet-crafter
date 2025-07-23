from socket import socket, AF_INET, SOCK_RAW, IPPROTO_RAW, IPPROTO_IP, IPPROTO_TCP, IP_HDRINCL

def open_sockets():
  try:
    client_socket = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)
    client_socket.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
    print("Client socket is opened.")
  except Exception as e:
    print(f"Failed to open client socket: {e}")
    return None, None

  address = ("10.0.0.2", 12345) 
  try:
    server_socket = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)
    server_socket.bind(address)
    print(f"Server socket open for {address[0]}:{address[1]}")
  except Exception as e:
    print(f"Failed to open server socket : {e}")
    return client_socket, None
  
  return client_socket, server_socket

def build_ip_header():
  # Build raw bytes for IPv4 header
  VERSION_IHL = (4 << 4) + 5 # 0x45 which means upper 4 bits represent int 4, lower 4 bits present int 5
  TYPE_OF_SERVICE = 0x00 # Not used, set to 0


if __name__ == "__main__":
  client_sock, server_sock = open_sockets()