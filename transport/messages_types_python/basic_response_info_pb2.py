# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basic_response_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='basic_response_info.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x62\x61sic_response_info.proto\"2\n\x11\x42\x61sicResponseInfo\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\tb\x06proto3'
)




_BASICRESPONSEINFO = _descriptor.Descriptor(
  name='BasicResponseInfo',
  full_name='BasicResponseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='BasicResponseInfo.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='BasicResponseInfo.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['BasicResponseInfo'] = _BASICRESPONSEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BasicResponseInfo = _reflection.GeneratedProtocolMessageType('BasicResponseInfo', (_message.Message,), {
  'DESCRIPTOR' : _BASICRESPONSEINFO,
  '__module__' : 'basic_response_info_pb2'
  # @@protoc_insertion_point(class_scope:BasicResponseInfo)
  })
_sym_db.RegisterMessage(BasicResponseInfo)


# @@protoc_insertion_point(module_scope)