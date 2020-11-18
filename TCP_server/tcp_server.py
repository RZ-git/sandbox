import socket


class TCPServer:
    """ TCP通信サーバークラス """

    @staticmethod
    def run_server():
        """ サーバーを起動 """
        # socketを生成
        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # socketをlocalhostのポート8080番に割り当てる
        server_socket.bind(("localhost", 8080))
        server_socket.listen(10)

        # 外部からの接続を待ち、接続があったらコネクションを確立
        (client_socket, address) = server_socket.accept()
        print('接続完了')

        # クライアントから送られてきたデータを取得する
        request = client_socket.recv(4096)

        # クライアントから送られてきたデータをファイルに出力
        with open("server_recv.txt", "wb") as f:
            f.write(request)

        # クライアントへ送信するレスポンスデータをファイルから取得
        with open("server_send.txt", "rb") as f:
            response = f.read()

        # クライアントへレスポンスを送信
        client_socket.send(response)

        # 通信を終了させる
        client_socket.close()


if __name__ == '__main__':
    tcp_server = TCPServer()
    tcp_server.run_server()
