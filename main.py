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
    print("Cliente conectado. Mostrando pantalla...")

    data = b""
    payload_size = struct.calcsize(">L")

    try:
        while True:
            # Recibir el tamaño de la imagen
            while len(data) < payload_size:
                data += client_socket.recv(4096)

            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack(">L", packed_msg_size)[0]


            # Recibir la imagen
            while len(data) < msg_size:
                data += client_socket.recv(4096)

            frame_data = data[:msg_size]
            data = data[msg_size:]


            # Decodificar la imagen y redimensionarla
            img = cv2.imdecode(np.frombuffer(frame_data, dtype=np.uint8), cv2.IMREAD_COLOR)
            img_resized = cv2.resize(img, (800, 450))  # Ajusta el tamaño (ancho, alto)


            # Mostrar la imagen redimensionada
            cv2.imshow("Pantalla Remota", img_resized)


            if cv2.waitKey(1) == 27:  # Presiona ESC para salir
            

























