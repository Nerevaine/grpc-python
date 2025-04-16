"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import geyser_pb2 as geyser__pb2


class GeyserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.stream_stream(
                '/geyser.Geyser/Subscribe',
                request_serializer=geyser__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=geyser__pb2.SubscribeUpdate.FromString,
                )
        self.Ping = channel.unary_unary(
                '/geyser.Geyser/Ping',
                request_serializer=geyser__pb2.PingRequest.SerializeToString,
                response_deserializer=geyser__pb2.PongResponse.FromString,
                )
        self.GetLatestBlockhash = channel.unary_unary(
                '/geyser.Geyser/GetLatestBlockhash',
                request_serializer=geyser__pb2.GetLatestBlockhashRequest.SerializeToString,
                response_deserializer=geyser__pb2.GetLatestBlockhashResponse.FromString,
                )
        self.GetBlockHeight = channel.unary_unary(
                '/geyser.Geyser/GetBlockHeight',
                request_serializer=geyser__pb2.GetBlockHeightRequest.SerializeToString,
                response_deserializer=geyser__pb2.GetBlockHeightResponse.FromString,
                )
        self.GetSlot = channel.unary_unary(
                '/geyser.Geyser/GetSlot',
                request_serializer=geyser__pb2.GetSlotRequest.SerializeToString,
                response_deserializer=geyser__pb2.GetSlotResponse.FromString,
                )
        self.IsBlockhashValid = channel.unary_unary(
                '/geyser.Geyser/IsBlockhashValid',
                request_serializer=geyser__pb2.IsBlockhashValidRequest.SerializeToString,
                response_deserializer=geyser__pb2.IsBlockhashValidResponse.FromString,
                )
        self.GetVersion = channel.unary_unary(
                '/geyser.Geyser/GetVersion',
                request_serializer=geyser__pb2.GetVersionRequest.SerializeToString,
                response_deserializer=geyser__pb2.GetVersionResponse.FromString,
                )


class GeyserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Subscribe(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLatestBlockhash(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockHeight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSlot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsBlockhashValid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GeyserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.stream_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=geyser__pb2.SubscribeRequest.FromString,
                    response_serializer=geyser__pb2.SubscribeUpdate.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=geyser__pb2.PingRequest.FromString,
                    response_serializer=geyser__pb2.PongResponse.SerializeToString,
            ),
            'GetLatestBlockhash': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLatestBlockhash,
                    request_deserializer=geyser__pb2.GetLatestBlockhashRequest.FromString,
                    response_serializer=geyser__pb2.GetLatestBlockhashResponse.SerializeToString,
            ),
            'GetBlockHeight': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockHeight,
                    request_deserializer=geyser__pb2.GetBlockHeightRequest.FromString,
                    response_serializer=geyser__pb2.GetBlockHeightResponse.SerializeToString,
            ),
            'GetSlot': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSlot,
                    request_deserializer=geyser__pb2.GetSlotRequest.FromString,
                    response_serializer=geyser__pb2.GetSlotResponse.SerializeToString,
            ),
            'IsBlockhashValid': grpc.unary_unary_rpc_method_handler(
                    servicer.IsBlockhashValid,
                    request_deserializer=geyser__pb2.IsBlockhashValidRequest.FromString,
                    response_serializer=geyser__pb2.IsBlockhashValidResponse.SerializeToString,
            ),
            'GetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVersion,
                    request_deserializer=geyser__pb2.GetVersionRequest.FromString,
                    response_serializer=geyser__pb2.GetVersionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'geyser.Geyser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


class Geyser(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Subscribe(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/geyser.Geyser/Subscribe',
            geyser__pb2.SubscribeRequest.SerializeToString,
            geyser__pb2.SubscribeUpdate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/geyser.Geyser/Ping',
            geyser__pb2.PingRequest.SerializeToString,
            geyser__pb2.PongResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLatestBlockhash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/geyser.Geyser/GetLatestBlockhash',
            geyser__pb2.GetLatestBlockhashRequest.SerializeToString,
            geyser__pb2.GetLatestBlockhashResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockHeight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/geyser.Geyser/GetBlockHeight',
            geyser__pb2.GetBlockHeightRequest.SerializeToString,
            geyser__pb2.GetBlockHeightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSlot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/geyser.Geyser/GetSlot',
            geyser__pb2.GetSlotRequest.SerializeToString,
            geyser__pb2.GetSlotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsBlockhashValid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/geyser.Geyser/IsBlockhashValid',
            geyser__pb2.IsBlockhashValidRequest.SerializeToString,
            geyser__pb2.IsBlockhashValidResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/geyser.Geyser/GetVersion',
            geyser__pb2.GetVersionRequest.SerializeToString,
            geyser__pb2.GetVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
