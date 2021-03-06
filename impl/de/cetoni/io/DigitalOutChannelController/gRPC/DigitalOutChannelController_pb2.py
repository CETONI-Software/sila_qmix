# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DigitalOutChannelController.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sila2lib.framework.SiLAFramework_pb2 as SiLAFramework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DigitalOutChannelController.proto',
  package='sila2.de.cetoni.io.digitaloutchannelcontroller.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!DigitalOutChannelController.proto\x12\x31sila2.de.cetoni.io.digitaloutchannelcontroller.v1\x1a\x13SiLAFramework.proto\"?\n\x0e\x44\x61taType_State\x12-\n\x05State\x18\x01 \x01(\x0b\x32\x1e.sila2.org.silastandard.String\"h\n\x14SetOutput_Parameters\x12P\n\x05State\x18\x01 \x01(\x0b\x32\x41.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DataType_State\"\x15\n\x13SetOutput_Responses\"!\n\x1fGet_NumberOfChannels_Parameters\"[\n\x1eGet_NumberOfChannels_Responses\x12\x39\n\x10NumberOfChannels\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Integer\"\x1c\n\x1aSubscribe_State_Parameters\"m\n\x19Subscribe_State_Responses\x12P\n\x05State\x18\x01 \x01(\x0b\x32\x41.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DataType_State\"3\n1Get_FCPAffectedByMetadata_ChannelIndex_Parameters\"i\n0Get_FCPAffectedByMetadata_ChannelIndex_Responses\x12\x35\n\rAffectedCalls\x18\x01 \x03(\x0b\x32\x1e.sila2.org.silastandard.String\"N\n\x15Metadata_ChannelIndex\x12\x35\n\x0c\x43hannelIndex\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Integer2\xad\x06\n\x1b\x44igitalOutChannelController\x12\x9e\x01\n\tSetOutput\x12G.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.SetOutput_Parameters\x1a\x46.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.SetOutput_Responses\"\x00\x12\xbf\x01\n\x14Get_NumberOfChannels\x12R.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_NumberOfChannels_Parameters\x1aQ.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_NumberOfChannels_Responses\"\x00\x12\xb2\x01\n\x0fSubscribe_State\x12M.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Subscribe_State_Parameters\x1aL.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Subscribe_State_Responses\"\x00\x30\x01\x12\xf5\x01\n&Get_FCPAffectedByMetadata_ChannelIndex\x12\x64.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_FCPAffectedByMetadata_ChannelIndex_Parameters\x1a\x63.sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_FCPAffectedByMetadata_ChannelIndex_Responses\"\x00\x62\x06proto3'
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_DATATYPE_STATE = _descriptor.Descriptor(
  name='DataType_State',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DataType_State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='State', full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DataType_State.State', index=0,
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
  serialized_start=109,
  serialized_end=172,
)


_SETOUTPUT_PARAMETERS = _descriptor.Descriptor(
  name='SetOutput_Parameters',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.SetOutput_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='State', full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.SetOutput_Parameters.State', index=0,
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
  serialized_start=174,
  serialized_end=278,
)


_SETOUTPUT_RESPONSES = _descriptor.Descriptor(
  name='SetOutput_Responses',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.SetOutput_Responses',
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
  serialized_start=280,
  serialized_end=301,
)


_GET_NUMBEROFCHANNELS_PARAMETERS = _descriptor.Descriptor(
  name='Get_NumberOfChannels_Parameters',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_NumberOfChannels_Parameters',
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
  serialized_start=303,
  serialized_end=336,
)


_GET_NUMBEROFCHANNELS_RESPONSES = _descriptor.Descriptor(
  name='Get_NumberOfChannels_Responses',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_NumberOfChannels_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='NumberOfChannels', full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_NumberOfChannels_Responses.NumberOfChannels', index=0,
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
  serialized_start=338,
  serialized_end=429,
)


_SUBSCRIBE_STATE_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_State_Parameters',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Subscribe_State_Parameters',
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
  serialized_start=431,
  serialized_end=459,
)


_SUBSCRIBE_STATE_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_State_Responses',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Subscribe_State_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='State', full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Subscribe_State_Responses.State', index=0,
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
  serialized_start=461,
  serialized_end=570,
)


_GET_FCPAFFECTEDBYMETADATA_CHANNELINDEX_PARAMETERS = _descriptor.Descriptor(
  name='Get_FCPAffectedByMetadata_ChannelIndex_Parameters',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_FCPAffectedByMetadata_ChannelIndex_Parameters',
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
  serialized_start=572,
  serialized_end=623,
)


_GET_FCPAFFECTEDBYMETADATA_CHANNELINDEX_RESPONSES = _descriptor.Descriptor(
  name='Get_FCPAffectedByMetadata_ChannelIndex_Responses',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_FCPAffectedByMetadata_ChannelIndex_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='AffectedCalls', full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_FCPAffectedByMetadata_ChannelIndex_Responses.AffectedCalls', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=625,
  serialized_end=730,
)


_METADATA_CHANNELINDEX = _descriptor.Descriptor(
  name='Metadata_ChannelIndex',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Metadata_ChannelIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ChannelIndex', full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Metadata_ChannelIndex.ChannelIndex', index=0,
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
  serialized_start=732,
  serialized_end=810,
)

_DATATYPE_STATE.fields_by_name['State'].message_type = SiLAFramework__pb2._STRING
_SETOUTPUT_PARAMETERS.fields_by_name['State'].message_type = _DATATYPE_STATE
_GET_NUMBEROFCHANNELS_RESPONSES.fields_by_name['NumberOfChannels'].message_type = SiLAFramework__pb2._INTEGER
_SUBSCRIBE_STATE_RESPONSES.fields_by_name['State'].message_type = _DATATYPE_STATE
_GET_FCPAFFECTEDBYMETADATA_CHANNELINDEX_RESPONSES.fields_by_name['AffectedCalls'].message_type = SiLAFramework__pb2._STRING
_METADATA_CHANNELINDEX.fields_by_name['ChannelIndex'].message_type = SiLAFramework__pb2._INTEGER
DESCRIPTOR.message_types_by_name['DataType_State'] = _DATATYPE_STATE
DESCRIPTOR.message_types_by_name['SetOutput_Parameters'] = _SETOUTPUT_PARAMETERS
DESCRIPTOR.message_types_by_name['SetOutput_Responses'] = _SETOUTPUT_RESPONSES
DESCRIPTOR.message_types_by_name['Get_NumberOfChannels_Parameters'] = _GET_NUMBEROFCHANNELS_PARAMETERS
DESCRIPTOR.message_types_by_name['Get_NumberOfChannels_Responses'] = _GET_NUMBEROFCHANNELS_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_State_Parameters'] = _SUBSCRIBE_STATE_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_State_Responses'] = _SUBSCRIBE_STATE_RESPONSES
DESCRIPTOR.message_types_by_name['Get_FCPAffectedByMetadata_ChannelIndex_Parameters'] = _GET_FCPAFFECTEDBYMETADATA_CHANNELINDEX_PARAMETERS
DESCRIPTOR.message_types_by_name['Get_FCPAffectedByMetadata_ChannelIndex_Responses'] = _GET_FCPAFFECTEDBYMETADATA_CHANNELINDEX_RESPONSES
DESCRIPTOR.message_types_by_name['Metadata_ChannelIndex'] = _METADATA_CHANNELINDEX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataType_State = _reflection.GeneratedProtocolMessageType('DataType_State', (_message.Message,), {
  'DESCRIPTOR' : _DATATYPE_STATE,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DataType_State)
  })
_sym_db.RegisterMessage(DataType_State)

SetOutput_Parameters = _reflection.GeneratedProtocolMessageType('SetOutput_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SETOUTPUT_PARAMETERS,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.SetOutput_Parameters)
  })
_sym_db.RegisterMessage(SetOutput_Parameters)

SetOutput_Responses = _reflection.GeneratedProtocolMessageType('SetOutput_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SETOUTPUT_RESPONSES,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.SetOutput_Responses)
  })
_sym_db.RegisterMessage(SetOutput_Responses)

Get_NumberOfChannels_Parameters = _reflection.GeneratedProtocolMessageType('Get_NumberOfChannels_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _GET_NUMBEROFCHANNELS_PARAMETERS,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_NumberOfChannels_Parameters)
  })
_sym_db.RegisterMessage(Get_NumberOfChannels_Parameters)

Get_NumberOfChannels_Responses = _reflection.GeneratedProtocolMessageType('Get_NumberOfChannels_Responses', (_message.Message,), {
  'DESCRIPTOR' : _GET_NUMBEROFCHANNELS_RESPONSES,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_NumberOfChannels_Responses)
  })
_sym_db.RegisterMessage(Get_NumberOfChannels_Responses)

Subscribe_State_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_State_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_STATE_PARAMETERS,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Subscribe_State_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_State_Parameters)

Subscribe_State_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_State_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_STATE_RESPONSES,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Subscribe_State_Responses)
  })
_sym_db.RegisterMessage(Subscribe_State_Responses)

Get_FCPAffectedByMetadata_ChannelIndex_Parameters = _reflection.GeneratedProtocolMessageType('Get_FCPAffectedByMetadata_ChannelIndex_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _GET_FCPAFFECTEDBYMETADATA_CHANNELINDEX_PARAMETERS,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_FCPAffectedByMetadata_ChannelIndex_Parameters)
  })
_sym_db.RegisterMessage(Get_FCPAffectedByMetadata_ChannelIndex_Parameters)

Get_FCPAffectedByMetadata_ChannelIndex_Responses = _reflection.GeneratedProtocolMessageType('Get_FCPAffectedByMetadata_ChannelIndex_Responses', (_message.Message,), {
  'DESCRIPTOR' : _GET_FCPAFFECTEDBYMETADATA_CHANNELINDEX_RESPONSES,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Get_FCPAffectedByMetadata_ChannelIndex_Responses)
  })
_sym_db.RegisterMessage(Get_FCPAffectedByMetadata_ChannelIndex_Responses)

Metadata_ChannelIndex = _reflection.GeneratedProtocolMessageType('Metadata_ChannelIndex', (_message.Message,), {
  'DESCRIPTOR' : _METADATA_CHANNELINDEX,
  '__module__' : 'DigitalOutChannelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitaloutchannelcontroller.v1.Metadata_ChannelIndex)
  })
_sym_db.RegisterMessage(Metadata_ChannelIndex)



_DIGITALOUTCHANNELCONTROLLER = _descriptor.ServiceDescriptor(
  name='DigitalOutChannelController',
  full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DigitalOutChannelController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=813,
  serialized_end=1626,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetOutput',
    full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DigitalOutChannelController.SetOutput',
    index=0,
    containing_service=None,
    input_type=_SETOUTPUT_PARAMETERS,
    output_type=_SETOUTPUT_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get_NumberOfChannels',
    full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DigitalOutChannelController.Get_NumberOfChannels',
    index=1,
    containing_service=None,
    input_type=_GET_NUMBEROFCHANNELS_PARAMETERS,
    output_type=_GET_NUMBEROFCHANNELS_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_State',
    full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DigitalOutChannelController.Subscribe_State',
    index=2,
    containing_service=None,
    input_type=_SUBSCRIBE_STATE_PARAMETERS,
    output_type=_SUBSCRIBE_STATE_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get_FCPAffectedByMetadata_ChannelIndex',
    full_name='sila2.de.cetoni.io.digitaloutchannelcontroller.v1.DigitalOutChannelController.Get_FCPAffectedByMetadata_ChannelIndex',
    index=3,
    containing_service=None,
    input_type=_GET_FCPAFFECTEDBYMETADATA_CHANNELINDEX_PARAMETERS,
    output_type=_GET_FCPAFFECTEDBYMETADATA_CHANNELINDEX_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIGITALOUTCHANNELCONTROLLER)

DESCRIPTOR.services_by_name['DigitalOutChannelController'] = _DIGITALOUTCHANNELCONTROLLER

# @@protoc_insertion_point(module_scope)
