import Data_pb2

d = Data_pb2.Data()
f = open('Proto_DataLog', "rb")
show_msg = d.FromString(f.read())
f.close()
print(show_msg)
