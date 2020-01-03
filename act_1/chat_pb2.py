# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='chat',
  syntax='proto3',
  serialized_options=_b('\n\033io.grpc.examples.routeguideB\017RouteGuideProtoP\001\242\002\003RTG'),
  serialized_pb=_b('\n\nchat.proto\x12\x04\x63hat\"\x07\n\x05Vacio\"\x1d\n\x0bNotaInicial\x12\x0e\n\x06nombre\x18\x01 \x01(\t\"Y\n\x04Nota\x12\n\n\x02ID\x18\x01 \x01(\x05\x12\x0e\n\x06log_ID\x18\x04 \x01(\x05\x12\x11\n\temisor_ID\x18\x05 \x01(\x05\x12\x0f\n\x07mensaje\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"&\n\tListaNota\x12\x19\n\x05lista\x18\x01 \x03(\x0b\x32\n.chat.Nota2\xc4\x01\n\nChatServer\x12\'\n\nChatStream\x12\x0b.chat.Vacio\x1a\n.chat.Nota0\x01\x12%\n\nEnviarNota\x12\n.chat.Nota\x1a\x0b.chat.Vacio\x12\x32\n\x11\x45nviarNotaInicial\x12\x11.chat.NotaInicial\x1a\n.chat.Nota\x12\x32\n\x13\x45nviarListaMensajes\x12\n.chat.Nota\x1a\x0f.chat.ListaNotaB6\n\x1bio.grpc.examples.routeguideB\x0fRouteGuideProtoP\x01\xa2\x02\x03RTGb\x06proto3')
)




_VACIO = _descriptor.Descriptor(
  name='Vacio',
  full_name='chat.Vacio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=20,
  serialized_end=27,
)


_NOTAINICIAL = _descriptor.Descriptor(
  name='NotaInicial',
  full_name='chat.NotaInicial',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nombre', full_name='chat.NotaInicial.nombre', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=58,
)


_NOTA = _descriptor.Descriptor(
  name='Nota',
  full_name='chat.Nota',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='chat.Nota.ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_ID', full_name='chat.Nota.log_ID', index=1,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emisor_ID', full_name='chat.Nota.emisor_ID', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mensaje', full_name='chat.Nota.mensaje', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='chat.Nota.timestamp', index=4,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=149,
)


_LISTANOTA = _descriptor.Descriptor(
  name='ListaNota',
  full_name='chat.ListaNota',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lista', full_name='chat.ListaNota.lista', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=189,
)

_LISTANOTA.fields_by_name['lista'].message_type = _NOTA
DESCRIPTOR.message_types_by_name['Vacio'] = _VACIO
DESCRIPTOR.message_types_by_name['NotaInicial'] = _NOTAINICIAL
DESCRIPTOR.message_types_by_name['Nota'] = _NOTA
DESCRIPTOR.message_types_by_name['ListaNota'] = _LISTANOTA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vacio = _reflection.GeneratedProtocolMessageType('Vacio', (_message.Message,), {
  'DESCRIPTOR' : _VACIO,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Vacio)
  })
_sym_db.RegisterMessage(Vacio)

NotaInicial = _reflection.GeneratedProtocolMessageType('NotaInicial', (_message.Message,), {
  'DESCRIPTOR' : _NOTAINICIAL,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.NotaInicial)
  })
_sym_db.RegisterMessage(NotaInicial)

Nota = _reflection.GeneratedProtocolMessageType('Nota', (_message.Message,), {
  'DESCRIPTOR' : _NOTA,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Nota)
  })
_sym_db.RegisterMessage(Nota)

ListaNota = _reflection.GeneratedProtocolMessageType('ListaNota', (_message.Message,), {
  'DESCRIPTOR' : _LISTANOTA,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ListaNota)
  })
_sym_db.RegisterMessage(ListaNota)


DESCRIPTOR._options = None

_CHATSERVER = _descriptor.ServiceDescriptor(
  name='ChatServer',
  full_name='chat.ChatServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=192,
  serialized_end=388,
  methods=[
  _descriptor.MethodDescriptor(
    name='ChatStream',
    full_name='chat.ChatServer.ChatStream',
    index=0,
    containing_service=None,
    input_type=_VACIO,
    output_type=_NOTA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EnviarNota',
    full_name='chat.ChatServer.EnviarNota',
    index=1,
    containing_service=None,
    input_type=_NOTA,
    output_type=_VACIO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EnviarNotaInicial',
    full_name='chat.ChatServer.EnviarNotaInicial',
    index=2,
    containing_service=None,
    input_type=_NOTAINICIAL,
    output_type=_NOTA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EnviarListaMensajes',
    full_name='chat.ChatServer.EnviarListaMensajes',
    index=3,
    containing_service=None,
    input_type=_NOTA,
    output_type=_LISTANOTA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHATSERVER)

DESCRIPTOR.services_by_name['ChatServer'] = _CHATSERVER

# @@protoc_insertion_point(module_scope)
