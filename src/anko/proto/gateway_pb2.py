# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z(github.com/anglo-korean/anko-go-sdk;anko',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rgateway.proto\"*\n\x08Metadata\x12\n\n\x02ua\x18\x01 \x01(\t\x12\x12\n\x04tags\x18\x02 \x03(\x0b\x32\x04.Tag\"!\n\x03Tag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"b\n\x08\x46orecast\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03ric\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x01\x12\x17\n\x06symbol\x18\x04 \x01(\x0b\x32\x07.Symbol\x12\x15\n\x05label\x18\x05 \x01(\x0e\x32\x06.Label\"H\n\x06Symbol\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x01\x12\r\n\x05ratio\x18\x03 \x01(\x01\x12\x10\n\x08\x65xchange\x18\x04 \x01(\t*f\n\x05Label\x12\x0b\n\x07unknown\x10\x00\x12\x08\n\x04\x64own\x10\x01\x12\t\n\x05up1_5\x10\x02\x12\x07\n\x03up2\x10\x03\x12\t\n\x05up2_5\x10\x04\x12\x07\n\x03up3\x10\x05\x12\t\n\x05up3_5\x10\x06\x12\x07\n\x03up4\x10\x07\x12\n\n\x06higher\x10\x08\x32/\n\tForecasts\x12\"\n\x06Stream\x12\t.Metadata\x1a\t.Forecast\"\x00\x30\x01\x42*Z(github.com/anglo-korean/anko-go-sdk;ankob\x06proto3'
)

_LABEL = _descriptor.EnumDescriptor(
  name='Label',
  full_name='Label',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknown', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='down', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='up1_5', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='up2', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='up2_5', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='up3', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='up3_5', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='up4', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='higher', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=270,
  serialized_end=372,
)
_sym_db.RegisterEnumDescriptor(_LABEL)

Label = enum_type_wrapper.EnumTypeWrapper(_LABEL)
unknown = 0
down = 1
up1_5 = 2
up2 = 3
up2_5 = 4
up3 = 5
up3_5 = 6
up4 = 7
higher = 8



_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ua', full_name='Metadata.ua', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='Metadata.tags', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=17,
  serialized_end=59,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Tag.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Tag.value', index=1,
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
  serialized_start=61,
  serialized_end=94,
)


_FORECAST = _descriptor.Descriptor(
  name='Forecast',
  full_name='Forecast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Forecast.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ric', full_name='Forecast.ric', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='Forecast.score', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='Forecast.symbol', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='Forecast.label', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=96,
  serialized_end=194,
)


_SYMBOL = _descriptor.Descriptor(
  name='Symbol',
  full_name='Symbol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='Symbol.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='Symbol.score', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ratio', full_name='Symbol.ratio', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='Symbol.exchange', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=196,
  serialized_end=268,
)

_METADATA.fields_by_name['tags'].message_type = _TAG
_FORECAST.fields_by_name['symbol'].message_type = _SYMBOL
_FORECAST.fields_by_name['label'].enum_type = _LABEL
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['Forecast'] = _FORECAST
DESCRIPTOR.message_types_by_name['Symbol'] = _SYMBOL
DESCRIPTOR.enum_types_by_name['Label'] = _LABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:Metadata)
  })
_sym_db.RegisterMessage(Metadata)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:Tag)
  })
_sym_db.RegisterMessage(Tag)

Forecast = _reflection.GeneratedProtocolMessageType('Forecast', (_message.Message,), {
  'DESCRIPTOR' : _FORECAST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:Forecast)
  })
_sym_db.RegisterMessage(Forecast)

Symbol = _reflection.GeneratedProtocolMessageType('Symbol', (_message.Message,), {
  'DESCRIPTOR' : _SYMBOL,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:Symbol)
  })
_sym_db.RegisterMessage(Symbol)


DESCRIPTOR._options = None

_FORECASTS = _descriptor.ServiceDescriptor(
  name='Forecasts',
  full_name='Forecasts',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=374,
  serialized_end=421,
  methods=[
  _descriptor.MethodDescriptor(
    name='Stream',
    full_name='Forecasts.Stream',
    index=0,
    containing_service=None,
    input_type=_METADATA,
    output_type=_FORECAST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FORECASTS)

DESCRIPTOR.services_by_name['Forecasts'] = _FORECASTS

# @@protoc_insertion_point(module_scope)
