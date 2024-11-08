import socket
import numpy as np
import cv2
import struct


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(1)

    print("Esperando conexión del cliente...")
    client_socket, _ = server_socket.accept()
