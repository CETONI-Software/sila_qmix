"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Continuous Flow Dosing Service*

:details: ContinuousFlowDosingService:
    Allows to continuously dose a specified fluid.
    The continuous flow mode is meant for dispensing volumes or generating flows and works only in one direction. That
    means using negative flow rates or negative volumes for aspiration is not possible.

:file:    ContinuousFlowDosingService_real.py
:authors: Florian Meinicke

:date: (creation)          2020-10-22T12:16:33.386427
:date: (last modification) 2021-07-10T10:33:25.058979

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

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2
# import SiLA errors
from impl.common.qmix_errors import SiLAFrameworkError, SiLAFrameworkErrorType, \
    QmixSDKSiLAError, SiLAValidationError

# import gRPC modules for this feature
from .gRPC import ContinuousFlowDosingService_pb2 as ContinuousFlowDosingService_pb2
# from .gRPC import ContinuousFlowDosingService_pb2_grpc as ContinuousFlowDosingService_pb2_grpc

# import default arguments
from .ContinuousFlowDosingService_default_arguments import default_dict

from impl.de.cetoni.pumps.syringepumps.PumpUnitController import unit_conversion as uc

# import qmixsdk
from qmixsdk import qmixbus, qmixpump

# noinspection PyPep8Naming,PyUnusedLocal
class ContinuousFlowDosingServiceReal:
    """
    Implementation of the *Continuous Flow Dosing Service* in *Real* mode
        Allows to control a continuous flow pump that is made up of two syringe pumps
    """

    def __init__(self, pump: qmixpump.Pump):
        """Class initialiser"""

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

        self.pump = pump

        self.dosage_uuid = ""

    def GenerateFlow(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Generate Flow"
            Generate a continuous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage.

        :param request: gRPC request containing the parameters passed:
            request.FlowRate (Flow Rate): The flow rate at which the pump should dose the fluid. This value cannot be negative since dosing is meant to only work in one direction.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        requested_flow_rate = request.FlowRate.value

        # We only allow one dosage at a time.
        # -> Stop the currently running dosage and after that start the new one.
        if self.dosage_uuid:
            self.StopDosage(0, 0)
            # wait for the currently running dosage to catch up
            time.sleep(0.25)

        msg = "The requested flow rate ({requested_val} {unit}) has to be in the range \
            between 0 {unit} and {max_val} {unit} for this pump."
        max_flow_rate = self.pump.get_flow_rate_max()
        if requested_flow_rate < 0 or requested_flow_rate > max_flow_rate:
            unit = uc.flow_unit_to_string(self.pump.get_flow_unit())
            raise SiLAValidationError(
                parameter=f"de.cetoni/pumps.contiflowpumps/ContinuousFlowDosingService/v1/Command/GenerateFlow/FlowRate",
                msg=msg.format(requested_val=requested_flow_rate, unit=unit, max_val=max_flow_rate)
            )

        self.dosage_uuid = str(uuid.uuid4())
        command_uuid = silaFW_pb2.CommandExecutionUUID(value=self.dosage_uuid)

        self.pump.generate_flow(requested_flow_rate)
        logging.info("Started dosing with a flow rate of %5.2f (UUID: %s)",
                     requested_flow_rate, self.dosage_uuid)
        return silaFW_pb2.CommandConfirmation(commandExecutionUUID=command_uuid)


    def GenerateFlow_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.GenerateFlow`.

        :param request: A request object with the following properties
            commandId: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """
        # Get the UUID of the command
        command_uuid = request.value

        # catch invalid CommandExecutionUUID:
        if not command_uuid or self.dosage_uuid != command_uuid:
            raise SiLAFrameworkError(
                SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        is_pumping = True
        while is_pumping:
            time.sleep(0.5)
            yield silaFW_pb2.ExecutionInfo(
                commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.running
            )
            is_pumping = self.pump.is_pumping()

        if not is_pumping and not self.pump.is_in_fault_state():
            yield silaFW_pb2.ExecutionInfo(
                commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.finishedSuccessfully
            )
        else:
            yield silaFW_pb2.ExecutionInfo(
                commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.finishedWithError
            )
            raise QmixSDKSiLAError(self.pump.read_last_error())


    def GenerateFlow_Result(self, request, context: grpc.ServicerContext) \
            -> ContinuousFlowDosingService_pb2.GenerateFlow_Responses:
        """
        Returns the final result of the command call :meth:`~.GenerateFlow`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        # Get the UUID of the command
        command_uuid = request.value

        # catch invalid CommandExecutionUUID:
        if not command_uuid and self.dosage_uuid != command_uuid:
            raise SiLAFrameworkError(
                SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        # catch premature command call
        if self.pump.is_pumping():
            raise SiLAFrameworkError(
                SiLAFrameworkErrorType.COMMAND_EXECUTION_NOT_FINISHED
            )

        logging.info("Finished dosing! (UUID: %s)", self.dosage_uuid)
        self.dosage_uuid = ""
        return ContinuousFlowDosingService_pb2.GenerateFlow_Responses()


    def StopDosage(self, request, context: grpc.ServicerContext) \
            -> ContinuousFlowDosingService_pb2.StopDosage_Responses:
        """
        Executes the unobservable command "Stop Dosage"
            Stops a currently running dosage immediately.

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        self.pump.stop_pumping()
        return ContinuousFlowDosingService_pb2.StopDosage_Responses()


    def Subscribe_MaxFlowRate(self, request, context: grpc.ServicerContext) \
            -> ContinuousFlowDosingService_pb2.Subscribe_MaxFlowRate_Responses:
        """
        Requests the observable property Maximum Flow Rate
            The maximum value of the flow rate at which this pump can dose a fluid.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            MaxFlowRate (Maximum Flow Rate): The maximum value of the flow rate at which this pump can dose a fluid.
        """

        while True:
            yield ContinuousFlowDosingService_pb2.Subscribe_MaxFlowRate_Responses(
                MaxFlowRate=silaFW_pb2.Real(value=self.pump.get_flow_rate_max())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)


    def Subscribe_FlowRate(self, request, context: grpc.ServicerContext) \
            -> ContinuousFlowDosingService_pb2.Subscribe_FlowRate_Responses:
        """
        Requests the observable property Flow Rate
            The current value of the flow rate. It is 0 if the pump does not dose any fluid.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            FlowRate (Flow Rate): The current value of the flow rate. It is 0 if the pump does not dose any fluid.
        """

        while True:
            yield ContinuousFlowDosingService_pb2.Subscribe_FlowRate_Responses(
                FlowRate=silaFW_pb2.Real(value=self.pump.get_flow_is())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)
