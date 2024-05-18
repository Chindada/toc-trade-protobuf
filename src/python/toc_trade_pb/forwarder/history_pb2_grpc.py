# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from toc_trade_pb.forwarder import history_pb2 as forwarder_dot_history__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in forwarder/history_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class HistoryDataInterfaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStockHistoryTick = channel.unary_unary(
                '/forwarder.HistoryDataInterface/GetStockHistoryTick',
                request_serializer=forwarder_dot_history__pb2.StockNumArrWithDate.SerializeToString,
                response_deserializer=forwarder_dot_history__pb2.HistoryTickResponse.FromString,
                _registered_method=True)
        self.GetStockHistoryKbar = channel.unary_unary(
                '/forwarder.HistoryDataInterface/GetStockHistoryKbar',
                request_serializer=forwarder_dot_history__pb2.StockNumArrWithDate.SerializeToString,
                response_deserializer=forwarder_dot_history__pb2.HistoryKbarResponse.FromString,
                _registered_method=True)
        self.GetStockHistoryClose = channel.unary_unary(
                '/forwarder.HistoryDataInterface/GetStockHistoryClose',
                request_serializer=forwarder_dot_history__pb2.StockNumArrWithDate.SerializeToString,
                response_deserializer=forwarder_dot_history__pb2.HistoryCloseResponse.FromString,
                _registered_method=True)
        self.GetFutureHistoryKbar = channel.unary_unary(
                '/forwarder.HistoryDataInterface/GetFutureHistoryKbar',
                request_serializer=forwarder_dot_history__pb2.FutureCodeArrWithDate.SerializeToString,
                response_deserializer=forwarder_dot_history__pb2.HistoryKbarResponse.FromString,
                _registered_method=True)


class HistoryDataInterfaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStockHistoryTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockHistoryKbar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockHistoryClose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFutureHistoryKbar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HistoryDataInterfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStockHistoryTick': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryTick,
                    request_deserializer=forwarder_dot_history__pb2.StockNumArrWithDate.FromString,
                    response_serializer=forwarder_dot_history__pb2.HistoryTickResponse.SerializeToString,
            ),
            'GetStockHistoryKbar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryKbar,
                    request_deserializer=forwarder_dot_history__pb2.StockNumArrWithDate.FromString,
                    response_serializer=forwarder_dot_history__pb2.HistoryKbarResponse.SerializeToString,
            ),
            'GetStockHistoryClose': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryClose,
                    request_deserializer=forwarder_dot_history__pb2.StockNumArrWithDate.FromString,
                    response_serializer=forwarder_dot_history__pb2.HistoryCloseResponse.SerializeToString,
            ),
            'GetFutureHistoryKbar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFutureHistoryKbar,
                    request_deserializer=forwarder_dot_history__pb2.FutureCodeArrWithDate.FromString,
                    response_serializer=forwarder_dot_history__pb2.HistoryKbarResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'forwarder.HistoryDataInterface', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HistoryDataInterface(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStockHistoryTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/forwarder.HistoryDataInterface/GetStockHistoryTick',
            forwarder_dot_history__pb2.StockNumArrWithDate.SerializeToString,
            forwarder_dot_history__pb2.HistoryTickResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetStockHistoryKbar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/forwarder.HistoryDataInterface/GetStockHistoryKbar',
            forwarder_dot_history__pb2.StockNumArrWithDate.SerializeToString,
            forwarder_dot_history__pb2.HistoryKbarResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetStockHistoryClose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/forwarder.HistoryDataInterface/GetStockHistoryClose',
            forwarder_dot_history__pb2.StockNumArrWithDate.SerializeToString,
            forwarder_dot_history__pb2.HistoryCloseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFutureHistoryKbar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/forwarder.HistoryDataInterface/GetFutureHistoryKbar',
            forwarder_dot_history__pb2.FutureCodeArrWithDate.SerializeToString,
            forwarder_dot_history__pb2.HistoryKbarResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
