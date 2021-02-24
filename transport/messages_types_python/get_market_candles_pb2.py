# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_market_candles.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_message_info_pb2 as basic__message__info__pb2
import basic_request_info_pb2 as basic__request__info__pb2
import basic_response_info_pb2 as basic__response__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_market_candles.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18get_market_candles.proto\x1a\x18\x62\x61sic_message_info.proto\x1a\x18\x62\x61sic_request_info.proto\x1a\x19\x62\x61sic_response_info.proto\"\xac\x01\n\x10GetMarketCandles\x12-\n\x12\x62\x61sic_message_info\x18\x01 \x01(\x0b\x32\x11.BasicMessageInfo\x12-\n\x12\x62\x61sic_request_info\x18\x02 \x01(\x0b\x32\x11.BasicRequestInfo\x12\x0c\n\x04\x66igi\x18\x03 \x01(\t\x12\r\n\x05\x66rom_\x18\x04 \x01(\t\x12\x0b\n\x03to_\x18\x05 \x01(\t\x12\x10\n\x08interval\x18\x06 \x01(\t\"M\n\x06\x43\x61ndle\x12\t\n\x01o\x18\x01 \x01(\x02\x12\t\n\x01\x63\x18\x02 \x01(\x02\x12\t\n\x01l\x18\x03 \x01(\x02\x12\t\n\x01h\x18\x04 \x01(\x02\x12\x0c\n\x04time\x18\x05 \x01(\t\x12\t\n\x01v\x18\x06 \x01(\x03\"\x94\x01\n\x18GetMarketCandlesResponse\x12-\n\x12\x62\x61sic_message_info\x18\x01 \x01(\x0b\x32\x11.BasicMessageInfo\x12/\n\x13\x62\x61sic_response_info\x18\x02 \x01(\x0b\x32\x12.BasicResponseInfo\x12\x18\n\x07\x63\x61ndles\x18\x03 \x03(\x0b\x32\x07.Candleb\x06proto3'
  ,
  dependencies=[basic__message__info__pb2.DESCRIPTOR,basic__request__info__pb2.DESCRIPTOR,basic__response__info__pb2.DESCRIPTOR,])




_GETMARKETCANDLES = _descriptor.Descriptor(
  name='GetMarketCandles',
  full_name='GetMarketCandles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic_message_info', full_name='GetMarketCandles.basic_message_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='basic_request_info', full_name='GetMarketCandles.basic_request_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='figi', full_name='GetMarketCandles.figi', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_', full_name='GetMarketCandles.from_', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_', full_name='GetMarketCandles.to_', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interval', full_name='GetMarketCandles.interval', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=108,
  serialized_end=280,
)


_CANDLE = _descriptor.Descriptor(
  name='Candle',
  full_name='Candle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='o', full_name='Candle.o', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c', full_name='Candle.c', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='l', full_name='Candle.l', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='h', full_name='Candle.h', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='Candle.time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v', full_name='Candle.v', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=282,
  serialized_end=359,
)


_GETMARKETCANDLESRESPONSE = _descriptor.Descriptor(
  name='GetMarketCandlesResponse',
  full_name='GetMarketCandlesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic_message_info', full_name='GetMarketCandlesResponse.basic_message_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='basic_response_info', full_name='GetMarketCandlesResponse.basic_response_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='candles', full_name='GetMarketCandlesResponse.candles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=362,
  serialized_end=510,
)

_GETMARKETCANDLES.fields_by_name['basic_message_info'].message_type = basic__message__info__pb2._BASICMESSAGEINFO
_GETMARKETCANDLES.fields_by_name['basic_request_info'].message_type = basic__request__info__pb2._BASICREQUESTINFO
_GETMARKETCANDLESRESPONSE.fields_by_name['basic_message_info'].message_type = basic__message__info__pb2._BASICMESSAGEINFO
_GETMARKETCANDLESRESPONSE.fields_by_name['basic_response_info'].message_type = basic__response__info__pb2._BASICRESPONSEINFO
_GETMARKETCANDLESRESPONSE.fields_by_name['candles'].message_type = _CANDLE
DESCRIPTOR.message_types_by_name['GetMarketCandles'] = _GETMARKETCANDLES
DESCRIPTOR.message_types_by_name['Candle'] = _CANDLE
DESCRIPTOR.message_types_by_name['GetMarketCandlesResponse'] = _GETMARKETCANDLESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetMarketCandles = _reflection.GeneratedProtocolMessageType('GetMarketCandles', (_message.Message,), {
  'DESCRIPTOR' : _GETMARKETCANDLES,
  '__module__' : 'get_market_candles_pb2'
  # @@protoc_insertion_point(class_scope:GetMarketCandles)
  })
_sym_db.RegisterMessage(GetMarketCandles)

Candle = _reflection.GeneratedProtocolMessageType('Candle', (_message.Message,), {
  'DESCRIPTOR' : _CANDLE,
  '__module__' : 'get_market_candles_pb2'
  # @@protoc_insertion_point(class_scope:Candle)
  })
_sym_db.RegisterMessage(Candle)

GetMarketCandlesResponse = _reflection.GeneratedProtocolMessageType('GetMarketCandlesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMARKETCANDLESRESPONSE,
  '__module__' : 'get_market_candles_pb2'
  # @@protoc_insertion_point(class_scope:GetMarketCandlesResponse)
  })
_sym_db.RegisterMessage(GetMarketCandlesResponse)


# @@protoc_insertion_point(module_scope)
