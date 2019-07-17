#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: SiLA2_python

*neMESYS*

:details: neMESYS:
    This is a test service for neMESYS syringe pumps via SiLA2

:file:    neMESYS_server.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.321083
:date: (last modification) 2019-07-17T10:10:16.636752

.. note:: Code generated by SiLA2CodeGenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""
__version__ = "0.0.1"

import os
import logging
import coloredlogs
import argparse

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump

# Import the main SiLA library
from sila2lib.sila_server import SiLA2Server

# Import gRPC libraries of features
from PumpDriveControlService.gRPC import PumpDriveControlService_pb2
from PumpDriveControlService.gRPC import PumpDriveControlService_pb2_grpc
# import default arguments for this feature
from PumpDriveControlService.PumpDriveControlService_default_arguments import default_dict as PumpDriveControlService_default_dict
from PumpUnitController.gRPC import PumpUnitController_pb2
from PumpUnitController.gRPC import PumpUnitController_pb2_grpc
# import default arguments for this feature
from PumpUnitController.PumpUnitController_default_arguments import default_dict as PumpUnitController_default_dict
from PumpFluidDosingService.gRPC import PumpFluidDosingService_pb2
from PumpFluidDosingService.gRPC import PumpFluidDosingService_pb2_grpc
# import default arguments for this feature
from PumpFluidDosingService.PumpFluidDosingService_default_arguments import default_dict as PumpFluidDosingService_default_dict
from SyringeConfigurationController.gRPC import SyringeConfigurationController_pb2
from SyringeConfigurationController.gRPC import SyringeConfigurationController_pb2_grpc
# import default arguments for this feature
from SyringeConfigurationController.SyringeConfigurationController_default_arguments import default_dict as SyringeConfigurationController_default_dict
from ValvePositionController.gRPC import ValvePositionController_pb2
from ValvePositionController.gRPC import ValvePositionController_pb2_grpc
# import default arguments for this feature
from ValvePositionController.ValvePositionController_default_arguments import default_dict as ValvePositionController_default_dict
from ShutdownController.gRPC import ShutdownController_pb2
from ShutdownController.gRPC import ShutdownController_pb2_grpc
# import default arguments for this feature
from ShutdownController.ShutdownController_default_arguments import default_dict as ShutdownController_default_dict

# Import the servicer modules for each feature
from PumpDriveControlService.PumpDriveControlService_servicer import PumpDriveControlService
from PumpUnitController.PumpUnitController_servicer import PumpUnitController
from PumpFluidDosingService.PumpFluidDosingService_servicer import PumpFluidDosingService
from SyringeConfigurationController.SyringeConfigurationController_servicer import SyringeConfigurationController
from ValvePositionController.ValvePositionController_servicer import ValvePositionController
from ShutdownController.ShutdownController_servicer import ShutdownController


class neMESYSServer(SiLA2Server):
    """
        This is a test service for neMESYS syringe pumps via SiLA2
    """

    def __init__(self, args, simulation_mode: bool = True):
        """Class initialiser"""
        super().__init__(
            name=args.server_name,
            description=args.description,
            server_type=args.server_type,
            version=__version__,
            vendor_URL="cetoni.de",
            ip="127.0.0.1", port=50053,
            # UUID = None,
            # key = 'sila_server.key', cert = 'sila_server.crt'
        )

        logging.info(
            "Starting SiLA2 server with server name: {server_name}".format(
                server_name=args.server_name
            )
        )

        # connect to the QmixBUS and enable the pump drive
        self.connect_to_bus_and_enable_pump()

        # registering features
        #  Register PumpDriveControlService
        self.PumpDriveControlService_servicer = PumpDriveControlService(
            pump=self.pump,
            sila2_conf=self.sila2_config,
            simulation_mode=simulation_mode)
        PumpDriveControlService_pb2_grpc.add_PumpDriveControlServiceServicer_to_server(
            self.PumpDriveControlService_servicer,
            self.grpc_server
        )
        self.addFeature('PumpDriveControlService', 'meta')
        #  Register PumpUnitController
        self.PumpUnitController_servicer = PumpUnitController(
            pump=self.pump,
            simulation_mode=simulation_mode)
        PumpUnitController_pb2_grpc.add_PumpUnitControllerServicer_to_server(
            self.PumpUnitController_servicer,
            self.grpc_server
        )
        self.addFeature('PumpUnitController', 'meta')
        #  Register PumpFluidDosingService
        self.PumpFluidDosingService_servicer = PumpFluidDosingService(
            pump=self.pump,
            simulation_mode=simulation_mode)
        PumpFluidDosingService_pb2_grpc.add_PumpFluidDosingServiceServicer_to_server(
            self.PumpFluidDosingService_servicer,
            self.grpc_server
        )
        self.addFeature('PumpFluidDosingService', 'meta')
        #  Register SyringeConfigurationController
        self.SyringeConfigurationController_servicer = SyringeConfigurationController(
            pump=self.pump,
            simulation_mode=simulation_mode)
        SyringeConfigurationController_pb2_grpc.add_SyringeConfigurationControllerServicer_to_server(
            self.SyringeConfigurationController_servicer,
            self.grpc_server
        )
        self.addFeature('SyringeConfigurationController', 'meta')
        #  Register ValvePositionController
        self.ValvePositionController_servicer = ValvePositionController(
            pump=self.pump,
            simulation_mode=simulation_mode)
        ValvePositionController_pb2_grpc.add_ValvePositionControllerServicer_to_server(
            self.ValvePositionController_servicer,
            self.grpc_server
        )
        self.addFeature('ValvePositionController', 'meta')
        #  Register ShutdownController
        self.ShutdownController_servicer = ShutdownController(
            bus=self.bus,
            pump=self.pump,
            server_name=self.server_name,
            sila2_conf=self.sila2_config,
            simulation_mode=simulation_mode
        )
        ShutdownController_pb2_grpc.add_ShutdownControllerServicer_to_server(
            self.ShutdownController_servicer,
            self.grpc_server
        )
        self.addFeature('ShutdownController', 'meta')

        self.simulation_mode = simulation_mode

        # starting and running the gRPC/SiLA2 server
        self.run()

        print()


    def connect_to_bus_and_enable_pump(self):
        """
            Loads a valid Qmix configuration, connects to the bus,
            retrieves the pump and enables it.
        """
        logging.debug("Opening bus")

        self.bus = qmixbus.Bus()
        # let's see if that helps...
        # NOTE: probably caused by a pump in fault state.
        # TBD in the future with another Feature
        try:
            self.bus.open("/mnt/hgfs/Win_Data/SiLA/NDM-SiLA", 0)
        except qmixbus.DeviceError as err:
            logging.error("qmixbus.open(): %s", err)
            logging.info("trying again...")
            self.bus.open("/mnt/hgfs/Win_Data/SiLA/NDM-SiLA", 0)

        self.pump = qmixpump.Pump()
        self.pump.lookup_by_name("neMESYS_Low_Pressure_1_Pump")

        # let's see if that helps...
        # NOTE: probably caused by a pump in fault state.
        # TBD in the future with another Feature
        try:
            self.bus.start()
        except qmixbus.DeviceError as err:
            logging.error("qmixbus.start(): %s", err)
            logging.info("trying again...")
            self.bus.start()

        if self.pump.is_in_fault_state():
            self.pump.clear_fault()
            logging.debug("pump was in fault state")
        if not self.pump.is_enabled():
            self.pump.enable(True)
            logging.debug("pump was in disabled state")


    def switchToSimMode(self):
        """Switch to simulation mode of the server"""

        # perform implementation specific switch operations
        self.PumpDriveControlService_servicer.switch_to_simulation_mode()
        self.PumpUnitController_servicer.switch_to_simulation_mode()
        self.PumpFluidDosingService_servicer.switch_to_simulation_mode()
        self.SyringeConfigurationController_servicer.switch_to_simulation_mode()
        self.ValvePositionController_servicer.switch_to_simulation_mode()
        self.ShutdownController_servicer.switch_to_simulation_mode()

        self.simulation_mode = True

    def switchToRealMode(self):
        """Switch to real mode"""

        # perform implementation specific switch operations
        self.PumpDriveControlService_servicer.switch_to_real_mode()
        self.PumpUnitController_servicer.switch_to_real_mode()
        self.PumpFluidDosingService_servicer.switch_to_real_mode()
        self.SyringeConfigurationController_servicer.switch_to_real_mode()
        self.ValvePositionController_servicer.switch_to_real_mode()
        self.ShutdownController_servicer.switch_to_real_mode()

        self.simulation_mode = False


def parse_command_line():
    """
    Just looking for commandline arguments
    """
    parser = argparse.ArgumentParser(description="A SiLA2 service: neMESYS")
    parser.add_argument('-s', '--server-name', action='store',
                        default="neMESYS", help='start SiLA server with [server-name]')
    parser.add_argument('-t', '--server-type', action='store',
                        default="Unknown Type", help='start SiLA server with [server-type]')
    parser.add_argument('-d', '--description', action='store',
                        default="This is a test service for neMESYS syringe pumps via SiLA2", help='SiLA server description')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    return parser.parse_args()


if __name__ == '__main__':
    # or use logging.ERROR for less output
    coloredlogs.install(fmt='%(asctime)s %(levelname)s| %(module)s.%(funcName)s: %(message)s',
                        level=logging.DEBUG)
    # logging.basicConfig(format='%(levelname)s| %(module)s.%(funcName)s: %(message)s', level=logging.DEBUG)

    parsed_args = parse_command_line()

    # generate SiLA2Server
    sila_server = neMESYSServer(args=parsed_args, simulation_mode=False)