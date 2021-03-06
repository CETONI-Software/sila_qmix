#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: sila_cetoni

*neMESYS client*

:details: neMESYS:
    This is a sample service for controlling neMESYS syringe pumps via SiLA2

:file:    PumpUnitController_client.py
:authors: Florian Meinicke

:date: (creation)          2021-07-11T07:37:48.106113
:date: (last modification) 2021-07-11T07:37:48.106113

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
from .gRPC import PumpUnitController_pb2
from .gRPC import PumpUnitController_pb2_grpc
# import default arguments for this feature
from .PumpUnitController_default_arguments import default_dict as PumpUnitController_default_dict


# noinspection PyPep8Naming, PyUnusedLocal
class PumpUnitControllerClient:
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
        self.PumpUnitController_stub = \
            PumpUnitController_pb2_grpc.PumpUnitControllerStub(channel)


        # initialise class variables for server information storage
        self.server_version = ''
        self.server_display_name = ''
        self.server_description = ''

    def SetFlowUnit(self, VolumeUnit: str, TimeUnit: str): # -> (PumpUnitController):
        """
        Wrapper to call the unobservable command SetFlowUnit on the server.

        :param VolumeUnit: The volume unit of the flow rate (e.g. 'l' for 'litres')
        :param TimeUnit: The time unit of the flow rate (e.g. 'h' for 'hours' or 's' for 'seconds')

        :returns: A gRPC object with the response that has been defined for this command.
        """
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Calling SetFlowUnit:")
        try:
            parameter = PumpUnitController_pb2.SetFlowUnit_Parameters(
                FlowUnit=PumpUnitController_pb2.SetFlowUnit_Parameters.SetFlowUnit_Struct(
                    VolumeUnit=PumpUnitController_pb2.DataType_VolumeUnit(
                        VolumeUnit=silaFW_pb2.String(value=VolumeUnit)
                    ),
                    TimeUnit=PumpUnitController_pb2.DataType_TimeUnit(
                        TimeUnit=silaFW_pb2.String(value=TimeUnit)
                    )
                )
            )

            response = self.PumpUnitController_stub.SetFlowUnit(parameter)
            logging.debug(f"SetFlowUnit response: {response}")

        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return


    def SetVolumeUnit(self, VolumeUnit: str): # -> (PumpUnitController):
        """
        Wrapper to call the unobservable command SetVolumeUnit on the server.

        :param VolumeUnit: The volume unit to set (e.g. 'l' for 'litres')

        :returns: A gRPC object with the response that has been defined for this command.
        """
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Calling SetVolumeUnit:")
        try:
            parameter = PumpUnitController_pb2.SetVolumeUnit_Parameters(
                VolumeUnit=PumpUnitController_pb2.DataType_VolumeUnit(
                    VolumeUnit=silaFW_pb2.String(value=VolumeUnit)
                )
            )

            response = self.PumpUnitController_stub.SetVolumeUnit(parameter)
            logging.debug(f"SetVolumeUnit response: {response}")

        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return



    def Subscribe_FlowUnit(self) \
            -> PumpUnitController_pb2.Subscribe_FlowUnit_Responses:
        """Wrapper to get property FlowUnit from the server."""
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Reading observable property FlowUnit:")
        try:
            response = self.PumpUnitController_stub.Subscribe_FlowUnit(
                PumpUnitController_pb2.Subscribe_FlowUnit_Parameters()
            )
            logging.debug(
                'Subscribe_FlowUnit response: {response}'.format(
                    response=response
                )
            )
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response

    def Subscribe_VolumeUnit(self) \
            -> PumpUnitController_pb2.Subscribe_VolumeUnit_Responses:
        """Wrapper to get property VolumeUnit from the server."""
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Reading observable property VolumeUnit:")
        try:
            response = self.PumpUnitController_stub.Subscribe_VolumeUnit(
                PumpUnitController_pb2.Subscribe_VolumeUnit_Parameters()
            )
            logging.debug(
                'Subscribe_VolumeUnit response: {response}'.format(
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


