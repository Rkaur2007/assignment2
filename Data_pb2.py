
import sys

_b = sys.version_info[0] <3 and (lambda x: x) or (lambda x: x.encode('latin1'))

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Data.proto',
  package='CServer',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\nData.proto\x12\x07\x43Server\"u\n\x07Request\x12\r\n\x05RFWID\x18\x01 \x02(\x05\x12\x11\n\tBenchType\x18\x02 \x02(\t\x12\x0e\n\x06\x43olumn\x18\x03 \x02(\t\x12\x10\n\x08\x64inbatch\x18\x04 \x02(\x05\x12\x14\n\x0c\x42\x61tchesStart\x18\x05 \x02(\x05\x12\x10\n\x08\x42\x61tchNum\x18\x06 \x02(\x05\"7\n\x04\x44\x61ta\x12\r\n\x05RFWID\x18\x02 \x02(\x05\x12\x12\n\nLastBatchN\x18\x03 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"$\n\x06ReqLog\x12\x1a\n\x03\x64\x61t\x18\x01 \x03(\x0b\x32\r.CServer.Data')
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='CServer.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RFWID', full_name='CServer.Request.RFWID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BenchType', full_name='CServer.Request.BenchType', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Select_Attributes', full_name='CServer.Request.Select_Attributes', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='samples', full_name='CServer.Request.samples', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BatchID', full_name='CServer.Request.BatchID', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BatchSize', full_name='CServer.Request.BatchSize', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=140,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='CServer.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RFWID', full_name='CServer.Data.RFWID', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LastBatchID', full_name='CServer.Data.LastBatchID', index=1,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='CServer.Data.data', index=2,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=197,
)


_REQLOG = _descriptor.Descriptor(
  name='ReqLog',
  full_name='CServer.ReqLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dat', full_name='CServer.ReqLog.dat', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=235,
)

_REQLOG.fields_by_name['dat'].message_type = _DATA
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['ReqLog'] = _REQLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR': _REQUEST,
  '__module__': 'Data_pb2'
  # @@protoc_insertion_point(class_scope:CServer.Request)
  })
_sym_db.RegisterMessage(Request)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR': _DATA,
  '__module__': 'Data_pb2'
  # @@protoc_insertion_point(class_scope:CServer.Data)
  })
_sym_db.RegisterMessage(Data)

ReqLog = _reflection.GeneratedProtocolMessageType('ReqLog', (_message.Message,), {
  'DESCRIPTOR': _REQLOG,
  '__module__': 'Data_pb2'
  # @@protoc_insertion_point(class_scope:CServer.ReqLog)
  })
_sym_db.RegisterMessage(ReqLog)


# @@protoc_insertion_point(module_scope)
