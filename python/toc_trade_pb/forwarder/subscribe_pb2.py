# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: forwarder/subscribe.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'forwarder/subscribe.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from toc_trade_pb.forwarder import entity_pb2 as forwarder_dot_entity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x66orwarder/subscribe.proto\x12\tforwarder\x1a\x1bgoogle/protobuf/empty.proto\x1a\x16\x66orwarder/entity.proto\"%\n\x11SubscribeResponse\x12\x10\n\x08\x66\x61il_arr\x18\x01 \x03(\t2\xb8\x06\n\x16SubscribeDataInterface\x12L\n\x12SubscribeStockTick\x12\x16.forwarder.StockNumArr\x1a\x1c.forwarder.SubscribeResponse\"\x00\x12N\n\x14UnSubscribeStockTick\x12\x16.forwarder.StockNumArr\x1a\x1c.forwarder.SubscribeResponse\"\x00\x12N\n\x14SubscribeStockBidAsk\x12\x16.forwarder.StockNumArr\x1a\x1c.forwarder.SubscribeResponse\"\x00\x12P\n\x16UnSubscribeStockBidAsk\x12\x16.forwarder.StockNumArr\x1a\x1c.forwarder.SubscribeResponse\"\x00\x12O\n\x13SubscribeFutureTick\x12\x18.forwarder.FutureCodeArr\x1a\x1c.forwarder.SubscribeResponse\"\x00\x12Q\n\x15UnSubscribeFutureTick\x12\x18.forwarder.FutureCodeArr\x1a\x1c.forwarder.SubscribeResponse\"\x00\x12Q\n\x15SubscribeFutureBidAsk\x12\x18.forwarder.FutureCodeArr\x1a\x1c.forwarder.SubscribeResponse\"\x00\x12S\n\x17UnSubscribeFutureBidAsk\x12\x18.forwarder.FutureCodeArr\x1a\x1c.forwarder.SubscribeResponse\"\x00\x12G\n\x12UnSubscribeAllTick\x12\x16.google.protobuf.Empty\x1a\x17.forwarder.ErrorMessage\"\x00\x12I\n\x14UnSubscribeAllBidAsk\x12\x16.google.protobuf.Empty\x1a\x17.forwarder.ErrorMessage\"\x00\x42\x06Z\x04./pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'forwarder.subscribe_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\004./pb'
  _globals['_SUBSCRIBERESPONSE']._serialized_start=93
  _globals['_SUBSCRIBERESPONSE']._serialized_end=130
  _globals['_SUBSCRIBEDATAINTERFACE']._serialized_start=133
  _globals['_SUBSCRIBEDATAINTERFACE']._serialized_end=957
# @@protoc_insertion_point(module_scope)
