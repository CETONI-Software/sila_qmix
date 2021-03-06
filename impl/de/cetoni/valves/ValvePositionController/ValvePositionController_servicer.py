"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Valve Position Controller*

:details: ValvePositionController:
    Allows to specify a certain logical position for a valve. The Position property can be querried at any time to
    obtain the current valve position.

:file:    ValvePositionController_servicer.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.315160
:date: (last modification) 2021-07-10T09:27:04.748906

.. note:: Code generated by sila2codegenerator 0.3.6

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

# import gRPC modules for this feature
from .gRPC import ValvePositionController_pb2 as ValvePositionController_pb2
from .gRPC import ValvePositionController_pb2_grpc as ValvePositionController_pb2_grpc

# import SiLA errors
from impl.common.qmix_errors import SiLAFrameworkError, DeviceError, QmixSDKSiLAError, \
    ValvePositionOutOfRangeError

# import simulation and real implementation
from .ValvePositionController_simulation import ValvePositionControllerSimulation
from .ValvePositionController_real import ValvePositionControllerReal

# import SiLA Defined Error factories
from .ValvePositionController_defined_errors import ValveNotToggleableError, ValvePositionNotAvailableError

class ValvePositionController(ValvePositionController_pb2_grpc.ValvePositionControllerServicer):
    """
    Allows to control valve devices
    """
    implementation: Union[ValvePositionControllerSimulation, ValvePositionControllerReal]
    simulation_mode: bool

    def __init__(self, valve = None, valve_gateway = None, simulation_mode: bool = True):
        """
        Class initialiser.

        :param valve: A valid `qmixvalve.Valve` object for this service to use (if this is None
                      the ValveGatewayService Feature is expected to be implemented by the server
                      as otherwise there is no way for this Feature to know the)
        :param valve_gateway: The ValveGatewayService feature that provides the valves that
                              this feature can operate on (must be given in valve is None)
        :param simulation_mode: Sets whether at initialisation the simulation mode is active or the real mode
        """

        self.valve = valve
        self.valve_gateway = valve_gateway

        self.simulation_mode = simulation_mode
        if simulation_mode:
            self.switch_to_simulation_mode()
        else:
            self.switch_to_real_mode()

    def _inject_implementation(self,
                               implementation: Union[ValvePositionControllerSimulation,
                                                     ValvePositionControllerReal]
                               ) -> bool:
        """
        Dependency injection of the implementation used.
            Allows to set the class used for simulation/real mode.

        :param implementation: A valid implementation of the ValveServicer.
        """

        self.implementation = implementation
        return True

    def switch_to_simulation_mode(self):
        """Method that will automatically be called by the server when the simulation mode is requested."""
        self.simulation_mode = True
        self._inject_implementation(ValvePositionControllerSimulation())

    def switch_to_real_mode(self):
        """Method that will automatically be called by the server when the real mode is requested."""
        self.simulation_mode = False
        self._inject_implementation(ValvePositionControllerReal(self.valve, self.valve_gateway))

    def SwitchToPosition(self, request, context: grpc.ServicerContext) \
            -> ValvePositionController_pb2.SwitchToPosition_Responses:
        """
        Executes the unobservable command "Switch To Position"
            Switches the valve to the specified position. The given position has to be less than the NumberOfPositions or else a ValidationError is thrown.

        :param request: gRPC request containing the parameters passed:
            request.Position (Position): The target position that the valve should be switched to.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "SwitchToPosition called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        # parameter validation
        # if request.my_paramameter.value out of scope :
        #        sila_val_err = SiLAValidationError(parameter="myParameter",
        #                                           msg=f"Parameter {request.my_parameter.value} out of scope!")
        #        sila_val_err.raise_rpc_error(context)

        try:
            return self.implementation.SwitchToPosition(request, context)
        except (SiLAFrameworkError, ValvePositionOutOfRangeError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)


    def TogglePosition(self, request, context: grpc.ServicerContext) \
            -> ValvePositionController_pb2.TogglePosition_Responses:
        """
        Executes the unobservable command "Toggle Position"
            This command only applies for 2-way valves to toggle between its two different positions. If the command is called for any other valve type a ValveNotToggleable error is thrown.

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "TogglePosition called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        # parameter validation
        # if request.my_paramameter.value out of scope :
        #        sila_val_err = SiLAValidationError(parameter="myParameter",
        #                                           msg=f"Parameter {request.my_parameter.value} out of scope!")
        #        sila_val_err.raise_rpc_error(context)

        try:
            return self.implementation.TogglePosition(request, context)
        except (SiLAFrameworkError, ValvePositionNotAvailableError, ValveNotToggleableError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)

    def Get_NumberOfPositions(self, request, context: grpc.ServicerContext) \
            -> ValvePositionController_pb2.Get_NumberOfPositions_Responses:
        """
        Requests the unobservable property Number Of Positions
            The number of the valve positions available.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            NumberOfPositions (Number Of Positions): The number of the valve positions available.
        """

        logging.debug(
            "Property NumberOfPositions requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            return self.implementation.Get_NumberOfPositions(request, context)
        except SiLAFrameworkError as err:
            err.raise_rpc_error(context)

    def Subscribe_Position(self, request, context: grpc.ServicerContext) \
            -> ValvePositionController_pb2.Subscribe_Position_Responses:
        """
        Requests the observable property Position
            The current logical valve position. This is a value between 0 and NumberOfPositions - 1.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            Position (Position): The current logical valve position. This is a value between 0 and NumberOfPositions - 1.
        """

        logging.debug(
            "Property Position requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            for value in self.implementation.Subscribe_Position(request, context):
                yield value
        except (SiLAFrameworkError, ValvePositionNotAvailableError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)
