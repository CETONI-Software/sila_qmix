#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: sila_cetoni

*neMESYS client*

:details: neMESYS:
    This is a sample service for controlling neMESYS syringe pumps via SiLA2

:file:    PumpFluidDosingService_client.py
:authors: Florian Meinicke

:date: (creation)          2021-07-11T07:37:48.136114
:date: (last modification) 2021-07-11T07:37:48.136114

.. note:: Code generated by sila2codegenerator 0.3.6

_______________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""
__version__ = "0.1.0"

# import general packages
import logging
import argparse
import grpc
import time
import datetime

# import meta packages
from typing import Union, Optional

# import SiLA2 library modules
from sila2lib.framework import SiLAFramework_pb2 as silaFW_pb2
from sila2lib.sila_client import SiLA2Client
from sila2lib.framework.std_features import SiLAService_pb2 as SiLAService_feature_pb2
from sila2lib.error_handling import client_err
from sila2lib.error_handling.client_err import SiLAClientError
import sila2lib.utils.py2sila_types as p2s
#   Usually not needed, but - feel free to modify
# from sila2lib.framework.std_features import SimulationController_pb2 as SimController_feature_pb2

# import feature gRPC modules
# Import gRPC libraries of features
from .gRPC import PumpFluidDosingService_pb2
from .gRPC import PumpFluidDosingService_pb2_grpc
# import default arguments for this feature
from .PumpFluidDosingService_default_arguments import default_dict as PumpFluidDosingService_default_dict


# noinspection PyPep8Naming, PyUnusedLocal
class PumpFluidDosingServiceClient:
    """
        This is a sample service for controlling neMESYS syringe pumps via SiLA2

    .. note:: For an example on how to construct the parameter or read the response(s) for command calls and properties,
              compare the default dictionary that is stored in the directory of the corresponding feature.
    """
    # The following variables will be filled when run() is executed
    #: Storage for the connected servers version
    server_version: str = ''
    #: Storage for the display name of the connected server
    server_display_name: str = ''
    #: Storage for the description of the connected server
    server_description: str = ''

    def __init__(self,
                 channel = None):
        """Class initialiser"""

        # Create stub objects used to communicate with the server
        self.PumpFluidDosingService_stub = \
            PumpFluidDosingService_pb2_grpc.PumpFluidDosingServiceStub(channel)


        # initialise class variables for server information storage
        self.server_version = ''
        self.server_display_name = ''
        self.server_description = ''

    def SetFillLevel(self, FillLevel: float, FlowRate: float) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Wrapper to call the observable command SetFillLevel on the server.

        :param FillLevel: The requested fill level. A level of 0 indicates a completely
                          empty syringe. The value has to be between 0 and MaxSyringeFillLevel.
                          Depending on the requested fill level this may cause aspiration
                          or dispension of fluid.
        :param FlowRate: The flow rate at which the pump should dose the fluid.

        :returns: A command confirmation object with the following information:
            commandExecutionUUID: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution (optional): The (maximum) lifetime of this command call.
        """
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Calling SetFillLevel:")
        try:
            parameter = PumpFluidDosingService_pb2.SetFillLevel_Parameters(
                FillLevel=silaFW_pb2.Real(value=FillLevel),
                FlowRate=silaFW_pb2.Real(value=FlowRate)
            )

            response = self.PumpFluidDosingService_stub.SetFillLevel(parameter)

            logging.debug('SetFillLevel response: {response}'.format(response=response))
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def SetFillLevel_Info(self,
                          uuid: Union[str, silaFW_pb2.CommandExecutionUUID]) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Wrapper to get an intermediate response for the observable command SetFillLevel on the server.

        :param uuid: The UUID that has been returned with the first command call. Can be given as string or as the
                     corresponding SiLA2 gRPC object.

        :returns: A gRPC object with the status information that has been defined for this command. The following fields
                  are defined:
                    * *commandStatus*: Status of the command (enumeration)
                    * *progressInfo*: Information on the progress of the command (0 to 1)
                    * *estimatedRemainingTime*: Estimate of the remaining time required to run the command
                    * *updatedLifetimeOfExecution*: An update on the execution lifetime
        """
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        if type(uuid) is str:
            uuid = silaFW_pb2.CommandExecutionUUID(value=uuid)

        logging.debug(
            "Requesting status information for command SetFillLevel (UUID={uuid}):".format(
                uuid=uuid.value
            )
        )
        try:
            response = self.PumpFluidDosingService_stub.SetFillLevel_Info(uuid)
            logging.debug('SetFillLevel status information: {response}'.format(response=response))
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def SetFillLevel_Result(self,
                            uuid: Union[str, silaFW_pb2.CommandExecutionUUID]) \
            -> PumpFluidDosingService_pb2.SetFillLevel_Responses:
        """
        Wrapper to get an intermediate response for the observable command SetFillLevel on the server.

        :param uuid: The UUID that has been returned with the first command call. Can be given as string or as the
                     corresponding SiLA2 gRPC object.

        :returns: A gRPC object with the result response that has been defined for this command.

        .. note:: Whether the result is available or not can and should be evaluated by calling the
                  :meth:`SetFillLevel_Info` method of this call.
        """
        if type(uuid) is str:
            uuid = silaFW_pb2.CommandExecutionUUID(value=uuid)

        logging.debug(
            "Requesting status information for command SetFillLevel (UUID={uuid}):".format(
                uuid=uuid.value
            )
        )

        try:
            response = self.PumpFluidDosingService_stub.SetFillLevel_Result(uuid)
            logging.debug('SetFillLevel result response: {response}'.format(response=response))
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def DoseVolume(self, Volume: float, FlowRate: float) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Wrapper to call the observable command DoseVolume on the server.

        :param Volume: The amount of volume to dose. This value can be negative.
                       In that case the pump aspirates the fluid.
        :param FlowRate: The flow rate at which the pump should dose the fluid.

        :returns: A command confirmation object with the following information:
            commandExecutionUUID: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution (optional): The (maximum) lifetime of this command call.
        """
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Calling DoseVolume:")
        try:
            parameter = PumpFluidDosingService_pb2.DoseVolume_Parameters(
                Volume=silaFW_pb2.Real(value=Volume),
                FlowRate=silaFW_pb2.Real(value=FlowRate)
            )

            response = self.PumpFluidDosingService_stub.DoseVolume(parameter)

            logging.debug('DoseVolume response: {response}'.format(response=response))
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def DoseVolume_Info(self,
                        uuid: Union[str, silaFW_pb2.CommandExecutionUUID]) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Wrapper to get an intermediate response for the observable command DoseVolume on the server.

        :param uuid: The UUID that has been returned with the first command call. Can be given as string or as the
                     corresponding SiLA2 gRPC object.

        :returns: A gRPC object with the status information that has been defined for this command. The following fields
                  are defined:
                    * *commandStatus*: Status of the command (enumeration)
                    * *progressInfo*: Information on the progress of the command (0 to 1)
                    * *estimatedRemainingTime*: Estimate of the remaining time required to run the command
                    * *updatedLifetimeOfExecution*: An update on the execution lifetime
        """
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        if type(uuid) is str:
            uuid = silaFW_pb2.CommandExecutionUUID(value=uuid)

        logging.debug(
            "Requesting status information for command DoseVolume (UUID={uuid}):".format(
                uuid=uuid.value
            )
        )
        try:
            response = self.PumpFluidDosingService_stub.DoseVolume_Info(uuid)
            logging.debug('DoseVolume status information: {response}'.format(response=response))
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def DoseVolume_Result(self,
                          uuid: Union[str, silaFW_pb2.CommandExecutionUUID]) \
            -> PumpFluidDosingService_pb2.DoseVolume_Responses:
        """
        Wrapper to get an intermediate response for the observable command DoseVolume on the server.

        :param uuid: The UUID that has been returned with the first command call. Can be given as string or as the
                     corresponding SiLA2 gRPC object.

        :returns: A gRPC object with the result response that has been defined for this command.

        .. note:: Whether the result is available or not can and should be evaluated by calling the
                  :meth:`DoseVolume_Info` method of this call.
        """
        if type(uuid) is str:
            uuid = silaFW_pb2.CommandExecutionUUID(value=uuid)

        logging.debug(
            "Requesting status information for command DoseVolume (UUID={uuid}):".format(
                uuid=uuid.value
            )
        )

        try:
            response = self.PumpFluidDosingService_stub.DoseVolume_Result(uuid)
            logging.debug('DoseVolume result response: {response}'.format(response=response))
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def GenerateFlow(self, FlowRate: float) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Wrapper to call the observable command GenerateFlow on the server.

        :param FlowRate: The flow rate at which the pump should dose the fluid.
                         This value can be negative. In that case the pump
                         aspirates the fluid.

        :returns: A command confirmation object with the following information:
            commandExecutionUUID: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution (optional): The (maximum) lifetime of this command call.
        """
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Calling GenerateFlow:")
        try:
            parameter = PumpFluidDosingService_pb2.GenerateFlow_Parameters(
                FlowRate=silaFW_pb2.Real(value=FlowRate)
            )

            response = self.PumpFluidDosingService_stub.GenerateFlow(parameter)

            logging.debug('GenerateFlow response: {response}'.format(response=response))
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def GenerateFlow_Info(self,
                          uuid: Union[str, silaFW_pb2.CommandExecutionUUID]) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Wrapper to get an intermediate response for the observable command GenerateFlow on the server.

        :param uuid: The UUID that has been returned with the first command call. Can be given as string or as the
                     corresponding SiLA2 gRPC object.

        :returns: A gRPC object with the status information that has been defined for this command. The following fields
                  are defined:
                    * *commandStatus*: Status of the command (enumeration)
                    * *progressInfo*: Information on the progress of the command (0 to 1)
                    * *estimatedRemainingTime*: Estimate of the remaining time required to run the command
                    * *updatedLifetimeOfExecution*: An update on the execution lifetime
        """
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        if type(uuid) is str:
            uuid = silaFW_pb2.CommandExecutionUUID(value=uuid)

        logging.debug(
            "Requesting status information for command GenerateFlow (UUID={uuid}):".format(
                uuid=uuid.value
            )
        )
        try:
            response = self.PumpFluidDosingService_stub.GenerateFlow_Info(uuid)
            logging.debug('GenerateFlow status information: {response}'.format(response=response))
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def GenerateFlow_Result(self,
                            uuid: Union[str, silaFW_pb2.CommandExecutionUUID]) \
            -> PumpFluidDosingService_pb2.GenerateFlow_Responses:
        """
        Wrapper to get an intermediate response for the observable command GenerateFlow on the server.

        :param uuid: The UUID that has been returned with the first command call. Can be given as string or as the
                     corresponding SiLA2 gRPC object.

        :returns: A gRPC object with the result response that has been defined for this command.

        .. note:: Whether the result is available or not can and should be evaluated by calling the
                  :meth:`GenerateFlow_Info` method of this call.
        """
        if type(uuid) is str:
            uuid = silaFW_pb2.CommandExecutionUUID(value=uuid)

        logging.debug(
            "Requesting status information for command GenerateFlow (UUID={uuid}):".format(
                uuid=uuid.value
            )
        )

        try:
            response = self.PumpFluidDosingService_stub.GenerateFlow_Result(uuid)
            logging.debug('GenerateFlow result response: {response}'.format(response=response))
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def StopDosage(self): # -> (PumpFluidDosingService):
        """
        Wrapper to call the unobservable command StopDosage on the server.

        :returns: A gRPC object with the response that has been defined for this command.
        """
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        parameter = None
        metadata = None  # add metadata generator here

        logging.debug("Calling StopDosage:")
        try:
            # resolve to default if no value given
            #   TODO: Implement a more reasonable default value
            if parameter is None:
                parameter = PumpFluidDosingService_pb2.StopDosage_Parameters(

                )

            response = self.PumpFluidDosingService_stub.StopDosage(parameter, metadata)
            logging.debug(f"StopDosage response: {response}")

        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return



    def Subscribe_MaxSyringeFillLevel(self) \
            -> PumpFluidDosingService_pb2.Subscribe_MaxSyringeFillLevel_Responses:
        """Wrapper to get property MaxSyringeFillLevel from the server."""
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Reading observable property MaxSyringeFillLevel:")
        try:
            response = self.PumpFluidDosingService_stub.Subscribe_MaxSyringeFillLevel(
                PumpFluidDosingService_pb2.Subscribe_MaxSyringeFillLevel_Parameters()
            )
            logging.debug(
                'Subscribe_MaxSyringeFillLevel response: {response}'.format(
                    response=response
                )
            )
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def Subscribe_SyringeFillLevel(self) \
            -> PumpFluidDosingService_pb2.Subscribe_SyringeFillLevel_Responses:
        """Wrapper to get property SyringeFillLevel from the server."""
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Reading observable property SyringeFillLevel:")
        try:
            response = self.PumpFluidDosingService_stub.Subscribe_SyringeFillLevel(
                PumpFluidDosingService_pb2.Subscribe_SyringeFillLevel_Parameters()
            )
            logging.debug(
                'Subscribe_SyringeFillLevel response: {response}'.format(
                    response=response
                )
            )
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def Subscribe_MaxFlowRate(self) \
            -> PumpFluidDosingService_pb2.Subscribe_MaxFlowRate_Responses:
        """Wrapper to get property MaxFlowRate from the server."""
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Reading observable property MaxFlowRate:")
        try:
            response = self.PumpFluidDosingService_stub.Subscribe_MaxFlowRate(
                PumpFluidDosingService_pb2.Subscribe_MaxFlowRate_Parameters()
            )
            logging.debug(
                'Subscribe_MaxFlowRate response: {response}'.format(
                    response=response
                )
            )
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def Subscribe_FlowRate(self) \
            -> PumpFluidDosingService_pb2.Subscribe_FlowRate_Responses:
        """Wrapper to get property FlowRate from the server."""
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Reading observable property FlowRate:")
        try:
            response = self.PumpFluidDosingService_stub.Subscribe_FlowRate(
                PumpFluidDosingService_pb2.Subscribe_FlowRate_Parameters()
            )
            logging.debug(
                'Subscribe_FlowRate response: {response}'.format(
                    response=response
                )
            )
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response


    #   No metadata defined

    @staticmethod
    def grpc_error_handling(error_object: grpc.Call) -> None:
        """Handles exceptions of type grpc.RpcError"""
        # pass to the default error handling
        grpc_error =  client_err.grpc_error_handling(error_object=error_object)

        logging.error(grpc_error.error_type)
        if hasattr(grpc_error.message, "parameter"):
            logging.error(grpc_error.message.parameter)
        logging.error(grpc_error.message.message)


