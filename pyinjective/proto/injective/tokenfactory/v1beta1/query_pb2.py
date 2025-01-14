# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from injective.tokenfactory.v1beta1 import authorityMetadata_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2
from injective.tokenfactory.v1beta1 import params_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_params__pb2
from injective.tokenfactory.v1beta1 import genesis_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_genesis__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/tokenfactory/v1beta1/query.proto',
  package='injective.tokenfactory.v1beta1',
  syntax='proto3',
  serialized_options=b'ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*injective/tokenfactory/v1beta1/query.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x36injective/tokenfactory/v1beta1/authorityMetadata.proto\x1a+injective/tokenfactory/v1beta1/params.proto\x1a,injective/tokenfactory/v1beta1/genesis.proto\"\x14\n\x12QueryParamsRequest\"S\n\x13QueryParamsResponse\x12<\n\x06params\x18\x01 \x01(\x0b\x32&.injective.tokenfactory.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\"p\n\"QueryDenomAuthorityMetadataRequest\x12!\n\x07\x63reator\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"denom\"\x12\'\n\tsub_denom\x18\x02 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"sub_denom\"\"\x9c\x01\n#QueryDenomAuthorityMetadataResponse\x12u\n\x12\x61uthority_metadata\x18\x01 \x01(\x0b\x32\x36.injective.tokenfactory.v1beta1.DenomAuthorityMetadataB!\xf2\xde\x1f\x19yaml:\"authority_metadata\"\xc8\xde\x1f\x00\"D\n\x1dQueryDenomsFromCreatorRequest\x12#\n\x07\x63reator\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"creator\"\"C\n\x1eQueryDenomsFromCreatorResponse\x12!\n\x06\x64\x65noms\x18\x01 \x03(\tB\x11\xf2\xde\x1f\ryaml:\"denoms\"\"\x19\n\x17QueryModuleStateRequest\"W\n\x18QueryModuleStateResponse\x12;\n\x05state\x18\x01 \x01(\x0b\x32,.injective.tokenfactory.v1beta1.GenesisState2\xc9\x06\n\x05Query\x12\xa1\x01\n\x06Params\x12\x32.injective.tokenfactory.v1beta1.QueryParamsRequest\x1a\x33.injective.tokenfactory.v1beta1.QueryParamsResponse\".\x82\xd3\xe4\x93\x02(\x12&/injective/tokenfactory/v1beta1/params\x12\xfa\x01\n\x16\x44\x65nomAuthorityMetadata\x12\x42.injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataRequest\x1a\x43.injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataResponse\"W\x82\xd3\xe4\x93\x02Q\x12O/injective/tokenfactory/v1beta1/denoms/{creator}/{sub_denom}/authority_metadata\x12\xd9\x01\n\x11\x44\x65nomsFromCreator\x12=.injective.tokenfactory.v1beta1.QueryDenomsFromCreatorRequest\x1a>.injective.tokenfactory.v1beta1.QueryDenomsFromCreatorResponse\"E\x82\xd3\xe4\x93\x02?\x12=/injective/tokenfactory/v1beta1/denoms_from_creator/{creator}\x12\xc2\x01\n\x17TokenfactoryModuleState\x12\x37.injective.tokenfactory.v1beta1.QueryModuleStateRequest\x1a\x38.injective.tokenfactory.v1beta1.QueryModuleStateResponse\"4\x82\xd3\xe4\x93\x02.\x12,/injective/tokenfactory/v1beta1/module_stateBTZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2.DESCRIPTOR,injective_dot_tokenfactory_dot_v1beta1_dot_params__pb2.DESCRIPTOR,injective_dot_tokenfactory_dot_v1beta1_dot_genesis__pb2.DESCRIPTOR,])




_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='injective.tokenfactory.v1beta1.QueryParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=321,
  serialized_end=341,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='injective.tokenfactory.v1beta1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='injective.tokenfactory.v1beta1.QueryParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=343,
  serialized_end=426,
)


_QUERYDENOMAUTHORITYMETADATAREQUEST = _descriptor.Descriptor(
  name='QueryDenomAuthorityMetadataRequest',
  full_name='injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataRequest.creator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\014yaml:\"denom\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_denom', full_name='injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataRequest.sub_denom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"sub_denom\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=428,
  serialized_end=540,
)


_QUERYDENOMAUTHORITYMETADATARESPONSE = _descriptor.Descriptor(
  name='QueryDenomAuthorityMetadataResponse',
  full_name='injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority_metadata', full_name='injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataResponse.authority_metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\031yaml:\"authority_metadata\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=543,
  serialized_end=699,
)


_QUERYDENOMSFROMCREATORREQUEST = _descriptor.Descriptor(
  name='QueryDenomsFromCreatorRequest',
  full_name='injective.tokenfactory.v1beta1.QueryDenomsFromCreatorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='injective.tokenfactory.v1beta1.QueryDenomsFromCreatorRequest.creator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\016yaml:\"creator\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=701,
  serialized_end=769,
)


_QUERYDENOMSFROMCREATORRESPONSE = _descriptor.Descriptor(
  name='QueryDenomsFromCreatorResponse',
  full_name='injective.tokenfactory.v1beta1.QueryDenomsFromCreatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denoms', full_name='injective.tokenfactory.v1beta1.QueryDenomsFromCreatorResponse.denoms', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\ryaml:\"denoms\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=771,
  serialized_end=838,
)


_QUERYMODULESTATEREQUEST = _descriptor.Descriptor(
  name='QueryModuleStateRequest',
  full_name='injective.tokenfactory.v1beta1.QueryModuleStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=840,
  serialized_end=865,
)


_QUERYMODULESTATERESPONSE = _descriptor.Descriptor(
  name='QueryModuleStateResponse',
  full_name='injective.tokenfactory.v1beta1.QueryModuleStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='injective.tokenfactory.v1beta1.QueryModuleStateResponse.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=867,
  serialized_end=954,
)

_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = injective_dot_tokenfactory_dot_v1beta1_dot_params__pb2._PARAMS
_QUERYDENOMAUTHORITYMETADATARESPONSE.fields_by_name['authority_metadata'].message_type = injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2._DENOMAUTHORITYMETADATA
_QUERYMODULESTATERESPONSE.fields_by_name['state'].message_type = injective_dot_tokenfactory_dot_v1beta1_dot_genesis__pb2._GENESISSTATE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
DESCRIPTOR.message_types_by_name['QueryDenomAuthorityMetadataRequest'] = _QUERYDENOMAUTHORITYMETADATAREQUEST
DESCRIPTOR.message_types_by_name['QueryDenomAuthorityMetadataResponse'] = _QUERYDENOMAUTHORITYMETADATARESPONSE
DESCRIPTOR.message_types_by_name['QueryDenomsFromCreatorRequest'] = _QUERYDENOMSFROMCREATORREQUEST
DESCRIPTOR.message_types_by_name['QueryDenomsFromCreatorResponse'] = _QUERYDENOMSFROMCREATORRESPONSE
DESCRIPTOR.message_types_by_name['QueryModuleStateRequest'] = _QUERYMODULESTATEREQUEST
DESCRIPTOR.message_types_by_name['QueryModuleStateResponse'] = _QUERYMODULESTATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'injective.tokenfactory.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'injective.tokenfactory.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryDenomAuthorityMetadataRequest = _reflection.GeneratedProtocolMessageType('QueryDenomAuthorityMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMAUTHORITYMETADATAREQUEST,
  '__module__' : 'injective.tokenfactory.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataRequest)
  })
_sym_db.RegisterMessage(QueryDenomAuthorityMetadataRequest)

QueryDenomAuthorityMetadataResponse = _reflection.GeneratedProtocolMessageType('QueryDenomAuthorityMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMAUTHORITYMETADATARESPONSE,
  '__module__' : 'injective.tokenfactory.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataResponse)
  })
_sym_db.RegisterMessage(QueryDenomAuthorityMetadataResponse)

QueryDenomsFromCreatorRequest = _reflection.GeneratedProtocolMessageType('QueryDenomsFromCreatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMSFROMCREATORREQUEST,
  '__module__' : 'injective.tokenfactory.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.QueryDenomsFromCreatorRequest)
  })
_sym_db.RegisterMessage(QueryDenomsFromCreatorRequest)

QueryDenomsFromCreatorResponse = _reflection.GeneratedProtocolMessageType('QueryDenomsFromCreatorResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMSFROMCREATORRESPONSE,
  '__module__' : 'injective.tokenfactory.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.QueryDenomsFromCreatorResponse)
  })
_sym_db.RegisterMessage(QueryDenomsFromCreatorResponse)

QueryModuleStateRequest = _reflection.GeneratedProtocolMessageType('QueryModuleStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATEREQUEST,
  '__module__' : 'injective.tokenfactory.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.QueryModuleStateRequest)
  })
_sym_db.RegisterMessage(QueryModuleStateRequest)

QueryModuleStateResponse = _reflection.GeneratedProtocolMessageType('QueryModuleStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATERESPONSE,
  '__module__' : 'injective.tokenfactory.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.QueryModuleStateResponse)
  })
_sym_db.RegisterMessage(QueryModuleStateResponse)


DESCRIPTOR._options = None
_QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
_QUERYDENOMAUTHORITYMETADATAREQUEST.fields_by_name['creator']._options = None
_QUERYDENOMAUTHORITYMETADATAREQUEST.fields_by_name['sub_denom']._options = None
_QUERYDENOMAUTHORITYMETADATARESPONSE.fields_by_name['authority_metadata']._options = None
_QUERYDENOMSFROMCREATORREQUEST.fields_by_name['creator']._options = None
_QUERYDENOMSFROMCREATORRESPONSE.fields_by_name['denoms']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='injective.tokenfactory.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=957,
  serialized_end=1798,
  methods=[
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='injective.tokenfactory.v1beta1.Query.Params',
    index=0,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002(\022&/injective/tokenfactory/v1beta1/params',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DenomAuthorityMetadata',
    full_name='injective.tokenfactory.v1beta1.Query.DenomAuthorityMetadata',
    index=1,
    containing_service=None,
    input_type=_QUERYDENOMAUTHORITYMETADATAREQUEST,
    output_type=_QUERYDENOMAUTHORITYMETADATARESPONSE,
    serialized_options=b'\202\323\344\223\002Q\022O/injective/tokenfactory/v1beta1/denoms/{creator}/{sub_denom}/authority_metadata',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DenomsFromCreator',
    full_name='injective.tokenfactory.v1beta1.Query.DenomsFromCreator',
    index=2,
    containing_service=None,
    input_type=_QUERYDENOMSFROMCREATORREQUEST,
    output_type=_QUERYDENOMSFROMCREATORRESPONSE,
    serialized_options=b'\202\323\344\223\002?\022=/injective/tokenfactory/v1beta1/denoms_from_creator/{creator}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TokenfactoryModuleState',
    full_name='injective.tokenfactory.v1beta1.Query.TokenfactoryModuleState',
    index=3,
    containing_service=None,
    input_type=_QUERYMODULESTATEREQUEST,
    output_type=_QUERYMODULESTATERESPONSE,
    serialized_options=b'\202\323\344\223\002.\022,/injective/tokenfactory/v1beta1/module_state',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
