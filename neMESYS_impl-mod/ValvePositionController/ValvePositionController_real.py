"""
________________________________________________________________________

:PROJECT: SiLA2_python

*Valve Position Controller*

:details: ValvePositionController:
    Allows to specify a certain logical position for a valve. The CurrentPosition property can be querried at any time
    to obtain the current valve position.

:file:    ValvePositionController_real.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.318610
:date: (last modification) 2019-07-16T11:11:31.318610

.. note:: Code generated by SiLA2CodeGenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""

__version__ = "0.0.1"

# import general packages
import logging
import uuid
import time

# import SiLA2 library
import sila2lib.SiLAFramework_pb2 as fwpb2
import sila2lib.sila_error_handling as sila_error

# import gRPC modules for this feature
from .gRPC import ValvePositionController_pb2 as pb2
from .gRPC import ValvePositionController_pb2_grpc as pb2_grpc

# import default arguments
from .ValvePositionController_default_arguments import default_dict

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump
from qmixsdk import qmixvalve


# noinspection PyPep8Naming
class ValvePositionControllerReal:
    """
    Implementation of the *Valve Position Controller* in *Real* mode
        This is a test service for neMESYS syringe pumps via SiLA2
    """

    def __init__(self, pump: qmixpump.Pump):
        """Class initialiser"""

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

        self.valve = pump.get_valve()
        self.num_of_valve_pos = self.valve.number_of_valve_positions()

    def SwitchToPosition(self, request, context) -> pb2.SwitchToPosition_Responses:
        """
        Executes the unobservable command Switch To Position
            Switches the valve to the specified position. The given position has to be less than the NumberOfPositions or else a ValidationError is thrown.

        :param request: gRPC request containing the parameters passed:
            request.Position (Position): The target position that the valve should be switched to.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.Success (Success): A boolean value where false represents a failed command execution and true represents a successful command execution.
        """

        requested_valve_pos = request.Position.value
        if requested_valve_pos < 0 or requested_valve_pos >= self.num_of_valve_pos:
            sila_error.raiseRPCError(context, sila_error.getValidationError(
                parameter="Position",
                cause="The given position is not in the range for this valve.",
                action=f"Adjust the valve position to fit in the range between 0 and {self.num_of_valve_pos}!"
            ))

        try:
            self.valve.switch_valve_to_position(requested_valve_pos)
        except qmixbus.DeviceError as err:
            logging.error("QmixSDK Error: %s", err)
            sila_error.raiseRPCError(context, sila_error.getStandardExecutionError(
                errorIdentifier="QmixSDKError", cause=str(err)
            ))

        return pb2.SwitchToPosition_Responses(Success=fwpb2.Boolean(value=True))

    def TogglePosition(self, request, context) -> pb2.TogglePosition_Responses:
        """
        Executes the unobservable command Toogle Position
            This command only applies for 2-way valves to toggle between its two different positions. If the command is called for any other valve type a ValveNotToggleable error is thrown.

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.Success (Success): A boolean value where false represents a failed command execution and true represents a successful command execution.
        """

        if self.valve.number_of_valve_positions() > 2:
            sila_error.raiseRPCError(context, sila_error.getStandardExecutionError(
                errorIdentifier="ValveNotToggleable",
                cause="The current vale does not suppprt toggling because it has more than only two possible positions."
            ))

        try:
            curr_pos = self.valve.actual_valve_position()
            self.valve.switch_valve_to_position((curr_pos + 1) % 2)
        except qmixbus.DeviceError as err:
            logging.error("QmixSDK Error: %s", err)
            sila_error.raiseRPCError(context, sila_error.getStandardExecutionError(
                errorIdentifier="QmixSDKError", cause=str(err)
            ))

        return pb2.TogglePosition_Responses(Success=fwpb2.Boolean(value=True))


    def Get_NumberOfPositions(self, request, context) -> pb2.Get_NumberOfPositions_Responses:
        """
        Requests the unobservable property Number Of Positions
            The number of the valve positions available.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.NumberOfPositions (Number Of Positions): The number of the valve positions available.
        """

        return pb2.Get_NumberOfPositions_Responses(
            NumberOfPositions=fwpb2.Integer(value=self.num_of_valve_pos)
        )

    def Subscribe_Position(self, request, context) -> pb2.Subscribe_Position_Responses:
        """
        Requests the observable property Position
            The current logic valve position. This is a value between 0 and NumberOfPositions - 1.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.Position (Position): The current logic valve position. This is a value between 0 and NumberOfPositions - 1.
        """

        while True:
            yield pb2.Subscribe_Position_Responses(
                Position=fwpb2.Integer(value=self.valve.actual_valve_position())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)

