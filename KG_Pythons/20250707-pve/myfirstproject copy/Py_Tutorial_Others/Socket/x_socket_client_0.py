'''
[소켓 서버]                         [클라이언트]
1. 소켓 생성                         1. 소켓생성
2. 바인딩: bind()                    2. (바인딩)
3. 접속 대기: listen()               3. 접속 시도: connect()
4. 접속 수락: accept()               4. 
5. 데이터 송/수신: send()/receive()  5. 데이터 송/수신: send()/receive() 
6. 접속 종료: close()                6. 접속종료: close()
'''

import socket

HOST = "172.30.1.68"  # 서버의 IP
PORT = 9970

#1. 소켓 생성
# 주소체계: Address Family INET(IPv4 프로토콜)
# Soc Kind: TCP Stream
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#3. 접속 시도
sock.connect((HOST, PORT))

#5. 데이터 송/수신
sock.sendall(bytes("Hello", "utf-8"))

#6. 접속 종료
sock.close()
