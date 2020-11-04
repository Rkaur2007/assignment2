import socket
import sys
import Data_pb2
import pandas as pd


# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12000)
print(sys.stderr, 'starting up on', server_address)
sock.bind(server_address)
sock.listen(1)

while True:

    print(sys.stderr, 'waiting for a connection to be established')
    connection, client_address = sock.accept()
    try:
        print(sys.stderr, 'connection from', client_address)
        while True:
            data = connection.recv(4096)
            print(sys.stderr, 'received ', data)
            if data:
                r = Data_pb2.Request().FromString(data)
                RFWID = r.RFWID
                BenchType = r.BenchType
                Attributes = r.Attributes
                samples = r.samples
                BatchID = r.BatchID
                BatchSize = r.BatchSize

                dfN = pd.read_csv("https://raw.githubusercontent.com/haniehalipour/Online-Machine-Learning-for-Cloud-Resource-Provisioning-of-Microservice-Backend-Systems/master/Workload%20Data/" + BenchType + ".csv")

                d = Data_pb2.Data()
                d.RFWID = RFWID

                start_from = ((BatchID - 1) * samples)
                show_till = (((BatchID + BatchSize - 1) * BatchSize))
                print(start_from, show_till)
                if show_till >= len(dfN):
                    show_till = len(dfN)
                d.LastBatchID = ((start_from - show_till) // samples) + BatchID - 1
                for i in dfN[Attributes][start_from:show_till].values:
                    d.data.append(i)

                data = d.SerializeToString()
                connection.sendall(data)

            else:
                print(sys.stderr, 'data not available from', client_address)
                break

    finally:
        # closing the connection
        connection.close()