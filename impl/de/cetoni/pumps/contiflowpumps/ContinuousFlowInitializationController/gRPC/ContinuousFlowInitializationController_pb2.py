# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ContinuousFlowInitializationController.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sila2lib.framework.SiLAFramework_pb2 as SiLAFramework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ContinuousFlowInitializationController.proto',
  package='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,ContinuousFlowInitializationController.proto\x12Nsila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1\x1a\x13SiLAFramework.proto\" \n\x1eInitializeContiflow_Parameters\"\x1f\n\x1dInitializeContiflow_Responses\"$\n\"Subscribe_IsInitialized_Parameters\"[\n!Subscribe_IsInitialized_Responses\x12\x36\n\rIsInitialized\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Boolean2\x99\x06\n&ContinuousFlowInitializationController\x12\xb4\x01\n\x13InitializeContiflow\x12n.sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.InitializeContiflow_Parameters\x1a+.sila2.org.silastandard.CommandConfirmation\"\x00\x12s\n\x18InitializeContiflow_Info\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a%.sila2.org.silastandard.ExecutionInfo\"\x00\x30\x01\x12\xbb\x01\n\x1aInitializeContiflow_Result\x12,.sila2.org.silastandard.CommandExecutionUUID\x1am.sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.InitializeContiflow_Responses\"\x00\x12\x84\x02\n\x17Subscribe_IsInitialized\x12r.sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.Subscribe_IsInitialized_Parameters\x1aq.sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.Subscribe_IsInitialized_Responses\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_INITIALIZECONTIFLOW_PARAMETERS = _descriptor.Descriptor(
  name='InitializeContiflow_Parameters',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.InitializeContiflow_Parameters',
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
  serialized_start=149,
  serialized_end=181,
)


_INITIALIZECONTIFLOW_RESPONSES = _descriptor.Descriptor(
  name='InitializeContiflow_Responses',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.InitializeContiflow_Responses',
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
  serialized_start=183,
  serialized_end=214,
)


_SUBSCRIBE_ISINITIALIZED_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_IsInitialized_Parameters',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.Subscribe_IsInitialized_Parameters',
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
  serialized_start=216,
  serialized_end=252,
)


_SUBSCRIBE_ISINITIALIZED_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_IsInitialized_Responses',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.Subscribe_IsInitialized_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='IsInitialized', full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.Subscribe_IsInitialized_Responses.IsInitialized', index=0,
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
  serialized_start=254,
  serialized_end=345,
)

_SUBSCRIBE_ISINITIALIZED_RESPONSES.fields_by_name['IsInitialized'].message_type = SiLAFramework__pb2._BOOLEAN
DESCRIPTOR.message_types_by_name['InitializeContiflow_Parameters'] = _INITIALIZECONTIFLOW_PARAMETERS
DESCRIPTOR.message_types_by_name['InitializeContiflow_Responses'] = _INITIALIZECONTIFLOW_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_IsInitialized_Parameters'] = _SUBSCRIBE_ISINITIALIZED_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_IsInitialized_Responses'] = _SUBSCRIBE_ISINITIALIZED_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitializeContiflow_Parameters = _reflection.GeneratedProtocolMessageType('InitializeContiflow_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _INITIALIZECONTIFLOW_PARAMETERS,
  '__module__' : 'ContinuousFlowInitializationController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.InitializeContiflow_Parameters)
  })
_sym_db.RegisterMessage(InitializeContiflow_Parameters)

InitializeContiflow_Responses = _reflection.GeneratedProtocolMessageType('InitializeContiflow_Responses', (_message.Message,), {
  'DESCRIPTOR' : _INITIALIZECONTIFLOW_RESPONSES,
  '__module__' : 'ContinuousFlowInitializationController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.InitializeContiflow_Responses)
  })
_sym_db.RegisterMessage(InitializeContiflow_Responses)

Subscribe_IsInitialized_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_IsInitialized_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_ISINITIALIZED_PARAMETERS,
  '__module__' : 'ContinuousFlowInitializationController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.Subscribe_IsInitialized_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_IsInitialized_Parameters)

Subscribe_IsInitialized_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_IsInitialized_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_ISINITIALIZED_RESPONSES,
  '__module__' : 'ContinuousFlowInitializationController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.Subscribe_IsInitialized_Responses)
  })
_sym_db.RegisterMessage(Subscribe_IsInitialized_Responses)



_CONTINUOUSFLOWINITIALIZATIONCONTROLLER = _descriptor.ServiceDescriptor(
  name='ContinuousFlowInitializationController',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=348,
  serialized_end=1141,
  methods=[
  _descriptor.MethodDescriptor(
    name='InitializeContiflow',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController.InitializeContiflow',
    index=0,
    containing_service=None,
    input_type=_INITIALIZECONTIFLOW_PARAMETERS,
    output_type=SiLAFramework__pb2._COMMANDCONFIRMATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InitializeContiflow_Info',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController.InitializeContiflow_Info',
    index=1,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=SiLAFramework__pb2._EXECUTIONINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InitializeContiflow_Result',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController.InitializeContiflow_Result',
    index=2,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=_INITIALIZECONTIFLOW_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_IsInitialized',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController.Subscribe_IsInitialized',
    index=3,
    containing_service=None,
    input_type=_SUBSCRIBE_ISINITIALIZED_PARAMETERS,
    output_type=_SUBSCRIBE_ISINITIALIZED_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTINUOUSFLOWINITIALIZATIONCONTROLLER)

DESCRIPTOR.services_by_name['ContinuousFlowInitializationController'] = _CONTINUOUSFLOWINITIALIZATIONCONTROLLER

# @@protoc_insertion_point(module_scope)
