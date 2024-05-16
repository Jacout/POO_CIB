#!/usr/bin/python3
# Obtiene servidor banner

import socket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obtiene banner de servidor")
    # Main argumentos
    parser.add_argument("-target" , dest="target", help="target IP / domain", required=True)
    parser.add_argument("-port", dest="port", help="Port" , type=int, required=True)
    parser_args = parser.parse_args()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((parser_args.target, parser.port))
    sock.settimeout(2)
    
    targetBytes = parser_args.target.encode()
    http_get = b"GET /index.html HTTP/1.1\r\nHost:" + targetBytes + b"\r\nAccept: */*\r\n\r\n"
    
    try:
        sock.sendall(http_get)
        data = sock.recvfrom(1024)
        print (data[0].decode())
    except socket.error:
        print("Socket error", socket.error)
    finally:
        print("Closing connection")
        sock.close()