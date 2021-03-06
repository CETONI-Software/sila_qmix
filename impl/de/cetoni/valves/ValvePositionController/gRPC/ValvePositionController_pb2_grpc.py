# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import ValvePositionController_pb2 as ValvePositionController__pb2


class ValvePositionControllerStub(object):
    """Feature: Valve Position Controller
    Allows to specify a certain logical position for a valve. The Position property can be querried at any time to obtain
    the current valve position.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SwitchToPosition = channel.unary_unary(
                '/sila2.de.cetoni.valves.valvepositioncontroller.v1.ValvePositionController/SwitchToPosition',
                request_serializer=ValvePositionController__pb2.SwitchToPosition_Parameters.SerializeToString,
                response_deserializer=ValvePositionController__pb2.SwitchToPosition_Responses.FromString,
                )
        self.TogglePosition = channel.unary_unary(
                '/sila2.de.cetoni.valves.valvepositioncontroller.v1.ValvePositionController/TogglePosition',
                request_serializer=ValvePositionController__pb2.TogglePosition_Parameters.SerializeToString,
                response_deserializer=ValvePositionController__pb2.TogglePosition_Responses.FromString,
                )
        self.Get_NumberOfPositions = channel.unary_unary(
                '/sila2.de.cetoni.valves.valvepositioncontroller.v1.ValvePositionController/Get_NumberOfPositions',
                request_serializer=ValvePositionController__pb2.Get_NumberOfPositions_Parameters.SerializeToString,
                response_deserializer=ValvePositionController__pb2.Get_NumberOfPositions_Responses.FromString,
                )
        self.Subscribe_Position = channel.unary_stream(
                '/sila2.de.cetoni.valves.valvepositioncontroller.v1.ValvePositionController/Subscribe_Position',
                request_serializer=ValvePositionController__pb2.Subscribe_Position_Parameters.SerializeToString,
                response_deserializer=ValvePositionController__pb2.Subscribe_Position_Responses.FromString,
                )


class ValvePositionControllerServicer(object):
    """Feature: Valve Position Controller
    Allows to specify a certain logical position for a valve. The Position property can be querried at any time to obtain
    the current valve position.
    """

    def SwitchToPosition(self, request, context):
        """Switch To Position
        Switches the valve to the specified position. The given position has to be less than the NumberOfPositions or else a
        ValidationError is thrown.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TogglePosition(self, request, context):
        """Toggle Position
        This command only applies for 2-way valves to toggle between its two different positions. If the command is called for
        any other valve type a ValveNotToggleable error is thrown.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get_NumberOfPositions(self, request, context):
        """Number Of Positions
        The number of the valve positions available.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe_Position(self, request, context):
        """Position
        The current logical valve position. This is a value between 0 and NumberOfPositions - 1.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ValvePositionControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SwitchToPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.SwitchToPosition,
                    request_deserializer=ValvePositionController__pb2.SwitchToPosition_Parameters.FromString,
                    response_serializer=ValvePositionController__pb2.SwitchToPosition_Responses.SerializeToString,
            ),
            'TogglePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.TogglePosition,
                    request_deserializer=ValvePositionController__pb2.TogglePosition_Parameters.FromString,
                    response_serializer=ValvePositionController__pb2.TogglePosition_Responses.SerializeToString,
            ),
            'Get_NumberOfPositions': grpc.unary_unary_rpc_method_handler(
                    servicer.Get_NumberOfPositions,
                    request_deserializer=ValvePositionController__pb2.Get_NumberOfPositions_Parameters.FromString,
                    response_serializer=ValvePositionController__pb2.Get_NumberOfPositions_Responses.SerializeToString,
            ),
            'Subscribe_Position': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe_Position,
                    request_deserializer=ValvePositionController__pb2.Subscribe_Position_Parameters.FromString,
                    response_serializer=ValvePositionController__pb2.Subscribe_Position_Responses.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sila2.de.cetoni.valves.valvepositioncontroller.v1.ValvePositionController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ValvePositionController(object):
    """Feature: Valve Position Controller
    Allows to specify a certain logical position for a valve. The Position property can be querried at any time to obtain
    the current valve position.
    """

    @staticmethod
    def SwitchToPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.valves.valvepositioncontroller.v1.ValvePositionController/SwitchToPosition',
            ValvePositionController__pb2.SwitchToPosition_Parameters.SerializeToString,
            ValvePositionController__pb2.SwitchToPosition_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TogglePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.valves.valvepositioncontroller.v1.ValvePositionController/TogglePosition',
            ValvePositionController__pb2.TogglePosition_Parameters.SerializeToString,
            ValvePositionController__pb2.TogglePosition_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get_NumberOfPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.valves.valvepositioncontroller.v1.ValvePositionController/Get_NumberOfPositions',
            ValvePositionController__pb2.Get_NumberOfPositions_Parameters.SerializeToString,
            ValvePositionController__pb2.Get_NumberOfPositions_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe_Position(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sila2.de.cetoni.valves.valvepositioncontroller.v1.ValvePositionController/Subscribe_Position',
            ValvePositionController__pb2.Subscribe_Position_Parameters.SerializeToString,
            ValvePositionController__pb2.Subscribe_Position_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
