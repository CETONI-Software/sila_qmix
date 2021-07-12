"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Axis Position Controller*

:details: AxisPositionController:
    Allows to control the position of one axis of an axis system

:file:    AxisPositionController_real.py
:authors: Florian Meinicke

:date: (creation)          2020-12-17T10:31:32.047799
:date: (last modification) 2021-07-09T10:33:25.248903

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
import time         # used for observables
import uuid         # used for observables
import grpc         # used for type hinting only

from typing import Dict, Union

from collections import namedtuple

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2

# import SiLA errors
from impl.common.qmix_errors import SiLAFrameworkError, SiLAFrameworkErrorType, SiLAValidationError

# import gRPC modules for this feature
from .gRPC import AxisPositionController_pb2 as AxisPositionController_pb2
# from .gRPC import AxisPositionController_pb2_grpc as AxisPositionController_pb2_grpc

# import default arguments
from .AxisPositionController_default_arguments import default_dict

from qmixsdk.qmixmotion import Axis, AxisSystem, PositionUnit

from . import METADATA_AXIS_IDENTIFIER

class MovableAxis:
    """
    A small wrapper around qmixmotion.Axis that adds a member for the current UUID
    of the axis' movement
    """

    device: Axis
    uuid: silaFW_pb2.CommandExecutionUUID

    def __init__(self, device: Axis, uuid: silaFW_pb2.CommandExecutionUUID = None):
        self.device = device
        self.uuid = uuid


# noinspection PyPep8Naming,PyUnusedLocal
class AxisPositionControllerReal:
    """
    Implementation of the *Axis Position Controller* in *Real* mode
        Allows to control motion systems like axis systems
    """

    def __init__(self, axis_system: AxisSystem):
        """
        Class initialiser.

        :param axis_system: The axis system that this feature shall operate on
        """

        self.axis_system = axis_system

        self.axes: Dict[str, MovableAxis] = {
            self.axis_system.get_axis_device(i).get_device_name():
                MovableAxis(self.axis_system.get_axis_device(i))
            for i in range(self.axis_system.get_axes_count())
        }

        for name, axis in self.axes.items():
            unit = axis.device.get_position_unit()
            unit_string = (unit.prefix.name if unit.prefix.name != 'unit' else '') + unit.unitid.name
            logging.debug(f"{name}, {unit_string}")

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

    def _get_axis_name(self, invocation_metadata: Dict) -> str:
        """
        Retrieves the axis name that is given in the `invocation_metadata` of a RPC.
        If the metadatum is not present an appropriate error is raised.
        """
        invocation_metadata = {key: value for key, value in invocation_metadata}
        logging.debug(f"Received invocation metadata: {invocation_metadata}")
        try:
            message = AxisPositionController_pb2.Metadata_AxisIdentifier()
            message.ParseFromString(invocation_metadata[METADATA_AXIS_IDENTIFIER])
            return message.AxisIdentifier.value
        except KeyError:
            raise SiLAFrameworkError(SiLAFrameworkErrorType.INVALID_METADATA,
                                     'This Command requires the AxisIdentifier metadata!')

    def _get_axis(self, invocation_metadata: Dict) -> MovableAxis:
        """
        Retrieves the axis that is requested by the `invocation_metadata` of a RPC.
        If the axis cannot be found an appropriate error is raised.
        """

        axis_name = self._get_axis_name(invocation_metadata)
        try:
            return self.axes[axis_name]
        except KeyError:
            raise SiLAFrameworkError(SiLAFrameworkErrorType.INVALID_METADATA,
                                     f'Axis {axis_name} is invalid.')

    def _validate_position(self, axis: MovableAxis, position):
        """
        Validates that the given position lies within the allowed range
        for the given axis
        """
        min_position = axis.device.get_position_min()
        max_position = axis.device.get_position_max()

        if position < min_position or \
            position > max_position:
            raise SiLAValidationError(
                'de.cetoni/motioncontrol.axis/AxisPositionController/v1/Command/MoveToPosition/Parameter/Position',
                f'The given position {position} is not in the valid range '\
                f'{min_position, max_position} for this axis.'
            )

    def _validate_velocity(self, axis: MovableAxis, velocity):
        """
        Validates that the given velocity lies within the allowed range
        for the given axis
        """
        min_velocity = 0
        max_velocity = axis.device.get_velocity_max()

        if velocity < min_velocity or \
            velocity > max_velocity:
            raise SiLAValidationError(
                'de.cetoni/motioncontrol.axis/AxisPositionController/v1/Command/MoveToPosition/Parameter/Velocity',
                f'The given velocity {velocity} is not in the valid range '\
                f'{min_velocity, max_velocity} for this axis.'
            )

    def _validate_uuid(
        self,
        axis: MovableAxis,
        uuid: silaFW_pb2.CommandExecutionUUID, check_premature_call = False):
        """
        Checks the given UUID for validity (i.e. if this is the UUID of the current
        movement command) and raises a SiLAFrameworkError if the UUID is not valid.
        Additionally, if `check_premature_call` is set to `True` then it is also
        checked that the axis system is not moving (this is only useful for
        `..._Result` functions). If this check fails, the corresponding FrameworkError
        will be raised, as well.

        :param uuid: The UUID to check
        :param check_premature_call: Whether to check if the axis system is still
                                     moving and raise an error if it is.
        """
        # catch invalid CommandExecutionUUID:
        if not uuid and axis.uuid != uuid:
            raise SiLAFrameworkError(
                SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        # catch premature command call
        if check_premature_call and not axis.device.is_target_position_reached():
            raise SiLAFrameworkError(
                SiLAFrameworkErrorType.COMMAND_EXECUTION_NOT_FINISHED
            )

    def _wait_movement_finished(self, axis: Axis):
        """
        The function waits until the last movement command for the given axis has finished
        """

        is_moving = True
        while is_moving:
            time.sleep(0.5)
            logging.info("Position: %s", axis.get_actual_position())
            yield silaFW_pb2.ExecutionInfo(
                commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.running
            )
            is_moving = not axis.is_target_position_reached()

        if not is_moving:
            yield silaFW_pb2.ExecutionInfo(
                commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.finishedSuccessfully
            )
        else:
            yield silaFW_pb2.ExecutionInfo(
                commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.finishedWithError
            )
            logging.error("An unexpected error occurred: %s", axis.read_last_error())

    def MoveToPosition(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Move To Position"
            Move the axis to the given position with a certain velocity

        :param request: gRPC request containing the parameters passed:
            request.Position (Position): The position to move to. Has to be in the range between MinimumPosition and MaximumPosition. See PositionUnit for the unit that is used for a specific axis. E.g. for rotational axis systems one of the axes needs a position specified in radians.
            request.Velocity (Velocity): The velocity value for the movement. Has to be in the range between MinimumVelocity and MaximumVelocity.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        requested_position = request.Position.value
        requested_velocity = request.Velocity.Velocity.value

        axis = self._get_axis(context.invocation_metadata())
        self._validate_position(axis, requested_position)
        self._validate_velocity(axis, requested_velocity)

        axis.uuid = silaFW_pb2.CommandExecutionUUID(value=str(uuid.uuid4()))

        axis.device.move_to_position(requested_position, requested_velocity)
        logging.info(f"Started moving to {requested_position} with velocity of {requested_velocity}")

        return silaFW_pb2.CommandConfirmation(commandExecutionUUID=axis.uuid)

    def MoveToPosition_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.MoveToPosition`.

        :param request: A request object with the following properties
            commandId: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """
        axis = self._get_axis(context.invocation_metadata())

        # Get the UUID of the command
        self._validate_uuid(axis, request.value)

        logging.info("Requested MoveToPosition_Info for movement (UUID: %s)", request.value)
        logging.info("Current movement is UUID: %s", axis.uuid)

        return self._wait_movement_finished(axis.device)

    def MoveToPosition_Result(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.MoveToPosition_Responses:
        """
        Returns the final result of the command call :meth:`~.MoveToPosition`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        axis = self._get_axis(context.invocation_metadata())

        # Get the UUID of the command
        self._validate_uuid(axis, request.value, check_premature_call=True)

        logging.info("Finished moving! (UUID: %s)", axis.uuid)
        axis.uuid = ''
        time.sleep(0.6)

        return AxisPositionController_pb2.MoveToPosition_Responses()


    def MoveToHomePosition(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.MoveToHomePosition_Responses:
        """
        Executes the unobservable command "Move To Home Position"
            Move the axis to its home position

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        axis = self._get_axis(context.invocation_metadata())
        axis_name = axis.device.get_device_name()
        axis.device.find_home()

        is_moving = True
        while is_moving:
            time.sleep(0.5)
            logging.info("Position: %s (axis: %s)", axis.device.get_actual_position(), axis_name)
            is_moving = not axis.device.is_homing_position_attained()
        logging.info(f"MoveToHomePosition for {axis_name} done")

        return AxisPositionController_pb2.MoveToHomePosition_Responses()


    def StopMoving(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.StopMoving_Responses:
        """
        Executes the unobservable command "Stop Moving"
            Immediately stops axis movement of a single axis

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        axis = self._get_axis(context.invocation_metadata())
        axis.device.stop_move()

        return AxisPositionController_pb2.StopMoving_Responses()


    def Subscribe_Position(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.Subscribe_Position_Responses:
        """
        Requests the observable property Position
            The current position of an axis

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            Position (Position): The current position of an axis
        """

        axis = self._get_axis(context.invocation_metadata())

        while True:
            position = axis.device.get_actual_position()

            yield AxisPositionController_pb2.Subscribe_Position_Responses(
                Position=silaFW_pb2.Real(value=position)
            )
            time.sleep(0.5) # give client some time to catch up


    def Get_PositionUnit(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.Get_PositionUnit_Responses:
        """
        Requests the unobservable property PositionUnit
            The position unit used for specifying the position of an axis

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            PositionUnit (PositionUnit): The position unit used for specifying the position of an axis
        """

        axis = self._get_axis(context.invocation_metadata())
        unit = axis.device.get_position_unit()
        unit_str = (unit.prefix.name if unit.prefix.name != 'unit' else '') + unit.unitid.name

        return AxisPositionController_pb2.Get_PositionUnit_Responses(
            PositionUnit=silaFW_pb2.String(value=unit_str)
        )

    def Get_MinimumPosition(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.Get_MinimumPosition_Responses:
        """
        Requests the unobservable property Minimum Position
            The minimum position limit of an axis

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            MinimumPosition (Minimum Position): The minimum position limit of an axis
        """

        axis = self._get_axis(context.invocation_metadata())

        return AxisPositionController_pb2.Get_MinimumPosition_Responses(
            MinimumPosition=silaFW_pb2.Real(value=axis.device.get_position_min())
        )

    def Get_MaximumPosition(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.Get_MaximumPosition_Responses:
        """
        Requests the unobservable property Maximum Position
            The maximum position limit of an axis

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            MaximumPosition (Maximum Position): The maximum position limit of an axis
        """

        axis = self._get_axis(context.invocation_metadata())

        return AxisPositionController_pb2.Get_MaximumPosition_Responses(
            MaximumPosition=silaFW_pb2.Real(value=axis.device.get_position_max())
        )


    def Get_MinimumVelocity(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.Get_MinimumVelocity_Responses:
        """
        Requests the unobservable property Minimum Velocity
            The minimum velocity limit of an axis

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            MinimumVelocity (Minimum Velocity): The minimum velocity limit of an axis
        """

        return AxisPositionController_pb2.Get_MinimumVelocity_Responses(
            MinimumVelocity=AxisPositionController_pb2.DataType_Velocity(
                Velocity=silaFW_pb2.Real(value=0)
            )
        )


    def Get_MaximumVelocity(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.Get_MaximumVelocity_Responses:
        """
        Requests the unobservable property Maximum Velocity
            The maximum velocity limit of an axis

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            MaximumVelocity (Maximum Velocity): The maximum velocity limit of an axis
        """

        axis = self._get_axis(context.invocation_metadata())

        return AxisPositionController_pb2.Get_MaximumVelocity_Responses(
            MaximumVelocity=AxisPositionController_pb2.DataType_Velocity(
                Velocity=silaFW_pb2.Real(value=axis.device.get_velocity_max())
            )
        )


    def Get_FCPAffectedByMetadata_AxisIdentifier(self, request, context: grpc.ServicerContext) \
            -> AxisPositionController_pb2.Get_FCPAffectedByMetadata_AxisIdentifier_Responses:
        """
        Requests the unobservable property FCPAffectedByMetadata Axis Identifier
            Specifies which Features/Commands/Properties of the SiLA server are affected by the Axis Identifier Metadata.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            AffectedCalls (AffectedCalls): A string containing a list of Fully Qualified Identifiers of Features, Commands and Properties for which the SiLA Client Metadata is expected as part of the respective RPCs.
        """

        return AxisPositionController_pb2.Get_FCPAffectedByMetadata_AxisIdentifier_Responses(
            AffectedCalls=[
                silaFW_pb2.String(value="de.cetoni/motioncontrol.axis/AxisPositionController/v1"),
            ]
        )
