"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Control Loop Service*

:details: ControlLoopService:
    Allows to control a Qmix Device with a Control Loop

:file:    ControlLoopService_servicer.py
:authors: Florian Meinicke

:date: (creation)          2020-10-08T09:17:41.384349
:date: (last modification) 2020-10-08T09:17:41.384349

.. note:: Code generated by sila2codegenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""

__version__ = "0.1.0"

# import general packages
import logging
import grpc

# meta packages
from typing import Union

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2

# import SiLA errors
from impl.common.qmix_errors import QmixSDKSiLAError, DeviceError, SiLAFrameworkError, SiLAValidationError

# import gRPC modules for this feature
from .gRPC import ControlLoopService_pb2 as ControlLoopService_pb2
from .gRPC import ControlLoopService_pb2_grpc as ControlLoopService_pb2_grpc

# import simulation and real implementation
from .ControlLoopService_simulation import ControlLoopServiceSimulation
from .ControlLoopService_real import ControlLoopServiceReal


class ControlLoopService(ControlLoopService_pb2_grpc.ControlLoopServiceServicer):
    """
    The SiLA 2 driver for Qmix Control Devices
    """
    implementation: Union[ControlLoopServiceSimulation, ControlLoopServiceReal]
    simulation_mode: bool

    def __init__(self, channel_gateway, simulation_mode: bool = True):
        """
        Class initialiser.

        :param channel_gateway: The ChannelGatewayService feature that provides
                                the channels that this feature can operate on
        :param simulation_mode: Sets whether at initialisation the simulation mode is active or the real mode.
        """

        self.channel_gateway = channel_gateway
        self.simulation_mode = simulation_mode
        if simulation_mode:
            self.switch_to_simulation_mode()
        else:
            self.switch_to_real_mode()

    def _inject_implementation(self,
                               implementation: Union[ControlLoopServiceSimulation,
                                                     ControlLoopServiceReal]
                               ) -> bool:
        """
        Dependency injection of the implementation used.
            Allows to set the class used for simulation/real mode.

        :param implementation: A valid implementation of the Qmix ControlServicer.
        """

        self.implementation = implementation
        return True

    def switch_to_simulation_mode(self):
        """Method that will automatically be called by the server when the simulation mode is requested."""
        self.simulation_mode = True
        self._inject_implementation(ControlLoopServiceSimulation())

    def switch_to_real_mode(self):
        """Method that will automatically be called by the server when the real mode is requested."""
        self.simulation_mode = False
        self._inject_implementation(ControlLoopServiceReal(self.channel_gateway))

    def WriteSetPoint(self, request, context: grpc.ServicerContext) \
            -> ControlLoopService_pb2.WriteSetPoint_Responses:
        """
        Executes the unobservable command "Write Set Point"
            Write a Set Point value to the Controller Device

        :param request: gRPC request containing the parameters passed:
            request.SetPointValue (Set Point Value): The Set Point value to write
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "WriteSetPoint called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.WriteSetPoint(request, context)
        except (SiLAFrameworkError, SiLAValidationError, DeviceError) as err:
            if isinstance(err, QmixSDKSiLAError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context=context)

    def RunControlLoop(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Run Control Loop"
            Run the Control Loop

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        logging.debug(
            "RunControlLoop called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            return self.implementation.RunControlLoop(request, context)
        except (SiLAFrameworkError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context=context)

    def RunControlLoop_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.RunControlLoop`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """

        logging.debug(
            "RunControlLoop_Info called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            for value in self.implementation.RunControlLoop_Info(request, context):
                yield value
        except (SiLAFrameworkError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context=context)

    def RunControlLoop_Result(self, request, context: grpc.ServicerContext) \
            -> ControlLoopService_pb2.RunControlLoop_Responses:
        """
        Returns the final result of the command call :meth:`~.RunControlLoop`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "RunControlLoop_Result called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            return self.implementation.RunControlLoop_Result(request, context)
        except (SiLAFrameworkError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context=context)


    def StopControlLoop(self, request, context: grpc.ServicerContext) \
            -> ControlLoopService_pb2.StopControlLoop_Responses:
        """
        Executes the unobservable command "Stop Control Loop"
            Stops the Control Loop (has no effect, if no Loop is currently running)

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "StopControlLoop called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.StopControlLoop(request, context)
        except (SiLAFrameworkError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context=context)

    def Subscribe_ControllerValue(self, request, context: grpc.ServicerContext) \
            -> ControlLoopService_pb2.Subscribe_ControllerValue_Responses:
        """
        Requests the observable property Controller Value
            The actual value from the Device

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.ControllerValue (Controller Value): The actual value from the Device
        """

        logging.debug(
            "Property ControllerValue requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            for value in self.implementation.Subscribe_ControllerValue(request, context):
                yield value
        except (SiLAFrameworkError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context=context)


    def Subscribe_SetPointValue(self, request, context: grpc.ServicerContext) \
            -> ControlLoopService_pb2.Subscribe_SetPointValue_Responses:
        """
        Requests the observable property Set Point Value
            The current SetPoint value of the Device

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.SetPointValue (Set Point Value): The current SetPoint value of the Device
        """

        logging.debug(
            "Property SetPointValue requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            for value in self.implementation.Subscribe_SetPointValue(request, context):
                yield value
        except (SiLAFrameworkError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context=context)
