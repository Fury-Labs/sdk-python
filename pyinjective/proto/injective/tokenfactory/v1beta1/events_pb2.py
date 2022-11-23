# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from injective.tokenfactory.v1beta1 import authorityMetadata_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/tokenfactory/v1beta1/events.proto',
  package='injective.tokenfactory.v1beta1',
  syntax='proto3',
  serialized_options=b'ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+injective/tokenfactory/v1beta1/events.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x36injective/tokenfactory/v1beta1/authorityMetadata.proto\"4\n\x12\x45ventCreateTFDenom\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\"^\n\x10\x45ventMintTFDenom\x12\x19\n\x11recipient_address\x18\x01 \x01(\t\x12/\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"[\n\x10\x45ventBurnTFDenom\x12\x16\n\x0e\x62urner_address\x18\x01 \x01(\t\x12/\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\">\n\x12\x45ventChangeTFAdmin\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x19\n\x11new_admin_address\x18\x02 \x01(\t\"_\n\x17\x45ventSetTFDenomMetadata\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x35\n\x08metadata\x18\x02 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00\x42TZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos_dot_bank_dot_v1beta1_dot_bank__pb2.DESCRIPTOR,injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2.DESCRIPTOR,])




_EVENTCREATETFDENOM = _descriptor.Descriptor(
  name='EventCreateTFDenom',
  full_name='injective.tokenfactory.v1beta1.EventCreateTFDenom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='injective.tokenfactory.v1beta1.EventCreateTFDenom.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='denom', full_name='injective.tokenfactory.v1beta1.EventCreateTFDenom.denom', index=1,
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
  serialized_start=221,
  serialized_end=273,
)


_EVENTMINTTFDENOM = _descriptor.Descriptor(
  name='EventMintTFDenom',
  full_name='injective.tokenfactory.v1beta1.EventMintTFDenom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipient_address', full_name='injective.tokenfactory.v1beta1.EventMintTFDenom.recipient_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='injective.tokenfactory.v1beta1.EventMintTFDenom.amount', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=275,
  serialized_end=369,
)


_EVENTBURNTFDENOM = _descriptor.Descriptor(
  name='EventBurnTFDenom',
  full_name='injective.tokenfactory.v1beta1.EventBurnTFDenom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='burner_address', full_name='injective.tokenfactory.v1beta1.EventBurnTFDenom.burner_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='injective.tokenfactory.v1beta1.EventBurnTFDenom.amount', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=371,
  serialized_end=462,
)


_EVENTCHANGETFADMIN = _descriptor.Descriptor(
  name='EventChangeTFAdmin',
  full_name='injective.tokenfactory.v1beta1.EventChangeTFAdmin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='injective.tokenfactory.v1beta1.EventChangeTFAdmin.denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_admin_address', full_name='injective.tokenfactory.v1beta1.EventChangeTFAdmin.new_admin_address', index=1,
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
  serialized_start=464,
  serialized_end=526,
)


_EVENTSETTFDENOMMETADATA = _descriptor.Descriptor(
  name='EventSetTFDenomMetadata',
  full_name='injective.tokenfactory.v1beta1.EventSetTFDenomMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='injective.tokenfactory.v1beta1.EventSetTFDenomMetadata.denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='injective.tokenfactory.v1beta1.EventSetTFDenomMetadata.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=528,
  serialized_end=623,
)

_EVENTMINTTFDENOM.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_EVENTBURNTFDENOM.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_EVENTSETTFDENOMMETADATA.fields_by_name['metadata'].message_type = cosmos_dot_bank_dot_v1beta1_dot_bank__pb2._METADATA
DESCRIPTOR.message_types_by_name['EventCreateTFDenom'] = _EVENTCREATETFDENOM
DESCRIPTOR.message_types_by_name['EventMintTFDenom'] = _EVENTMINTTFDENOM
DESCRIPTOR.message_types_by_name['EventBurnTFDenom'] = _EVENTBURNTFDENOM
DESCRIPTOR.message_types_by_name['EventChangeTFAdmin'] = _EVENTCHANGETFADMIN
DESCRIPTOR.message_types_by_name['EventSetTFDenomMetadata'] = _EVENTSETTFDENOMMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventCreateTFDenom = _reflection.GeneratedProtocolMessageType('EventCreateTFDenom', (_message.Message,), {
  'DESCRIPTOR' : _EVENTCREATETFDENOM,
  '__module__' : 'injective.tokenfactory.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.EventCreateTFDenom)
  })
_sym_db.RegisterMessage(EventCreateTFDenom)

EventMintTFDenom = _reflection.GeneratedProtocolMessageType('EventMintTFDenom', (_message.Message,), {
  'DESCRIPTOR' : _EVENTMINTTFDENOM,
  '__module__' : 'injective.tokenfactory.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.EventMintTFDenom)
  })
_sym_db.RegisterMessage(EventMintTFDenom)

EventBurnTFDenom = _reflection.GeneratedProtocolMessageType('EventBurnTFDenom', (_message.Message,), {
  'DESCRIPTOR' : _EVENTBURNTFDENOM,
  '__module__' : 'injective.tokenfactory.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.EventBurnTFDenom)
  })
_sym_db.RegisterMessage(EventBurnTFDenom)

EventChangeTFAdmin = _reflection.GeneratedProtocolMessageType('EventChangeTFAdmin', (_message.Message,), {
  'DESCRIPTOR' : _EVENTCHANGETFADMIN,
  '__module__' : 'injective.tokenfactory.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.EventChangeTFAdmin)
  })
_sym_db.RegisterMessage(EventChangeTFAdmin)

EventSetTFDenomMetadata = _reflection.GeneratedProtocolMessageType('EventSetTFDenomMetadata', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSETTFDENOMMETADATA,
  '__module__' : 'injective.tokenfactory.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.EventSetTFDenomMetadata)
  })
_sym_db.RegisterMessage(EventSetTFDenomMetadata)


DESCRIPTOR._options = None
_EVENTMINTTFDENOM.fields_by_name['amount']._options = None
_EVENTBURNTFDENOM.fields_by_name['amount']._options = None
_EVENTSETTFDENOMMETADATA.fields_by_name['metadata']._options = None
# @@protoc_insertion_point(module_scope)