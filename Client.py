import random
import socket
import sys
from datetime import datetime
import socket

random.seed(datetime.now())

# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server( local) is listening
server_address = ('localhost', 12000)
print(sys.stderr, 'connecting to port', server_address)
sock.connect(server_address)

import requests
import json
from requests.models import PreparedRequest
import pprint

Workload_Data = {1: "DVD-testing", 2: "DVD-training", 3: "NDBench-testing", 4: "NDBench-training"}
Attributes = {1: "CPUUtilization_Average", 2: "NetworkIn_Average", 3: "NetworkOut_Average", 4: "MemoryUtilization_Average"}
pp = pprint.PrettyPrinter(indent=2)

#get requests from client

RFWID = int(input("Enter your Request ID"))
print("\nSelect the Benchmark from the list: ")
pp.pprint(Workload_Data)
BenchType = Workload_Data[(int(input("Enter your choice: ")))]
print("\nSelect an attribute:")
pp.pprint(Attributes)
Select_Attributes = Attributes[(int(input("Enter your choice: ")))]
samples = int(input("\nEnter Batch Unit (i.e. number of samples in a batch): "))
BatchID = int(input("Enter the batch ID: "))
BatchSize = int(input("Enter Batch Size (i.e. number of batches): "))

import Data_pb2

r = Data_pb2.Request()
dd = Data_pb2.Data()

r.RFWID = RFWID
r.BenchType = BenchType
r.Select_Attributes= Select_Attributes
r.samples = samples
r.BatchID= BatchID
r.BatchSize = BatchSize

t = r.SerializePartialToString()
print(t)

try:
    # Send data
    disp_msg = 'transmitting data.'
    print(sys.stderr, 'sending ')
    sock.sendall(t)

    # Look for the response
    response_received = 0
    response_expected = len(disp_msg)

    while response_received < response_expected:
        data = sock.recv(4096)
        dd.FromString(data)
        print(dd)

        response_received += len(data)
        print(sys.stderr, 'received ', data)

finally:
    print(sys.stderr, 'closing socket')
    sock.close()
    f = open('Proto_DataLog', "wb")
    f.write(data)
    # f.write(dd.FromString(data))
    f.close()
Data = dd.FromString(data)
print('\nReceived Data ..\n', Data)
