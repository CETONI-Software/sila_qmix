"""
________________________________________________________________________

:PROJECT: SiLA2_python

*valvepositioncontroller_server_simulation *

:details: valvepositioncontroller_server_simulation: Allows to specify a certain logical position for a valve. The CurrentPosition property can be querried at any time to obtain the current valve position.. 
           
:file:    valvepositioncontroller_server_simulation.py
:authors: Florian Meinicke

:date: (creation)          20190627
:date: (last modification) 20190627

.. note:: Code generated automatically by SiLA2codegenerator v0.1.9!


           - 0.1.6
.. todo:: - 
________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""
__version__ = "0.0.1"


import logging
import uuid
# importing protobuf and gRPC handler/stubs
import sila2lib.SiLAFramework_pb2 as fwpb2
import ValvePositionController_pb2 as pb2
import ValvePositionController_pb2_grpc as pb2_grpc


class ValvePositionController(pb2_grpc.ValvePositionControllerServicer):
    """ ValvePositionController - Allows to specify a certain logical position for a valve. The CurrentPosition property can be querried at any time to obtain the current valve position. """
    def __init__ (self):
        """ ValvePositionController class initialiser """
        logging.debug("init class: ValvePositionController ")

        # if self.implementation is set to None, it will use
        # the fallback simulation mode as default
        # if required, one could also create a simulation module and set this to the default implementation, like:
        #~ self.injectImplementation(GreetingProviderSimulation())

        self.implementation = None # this corresponds to the simple, fallback simulation mode

    # dependency injection - setter injection s. https://en.wikipedia.org/wiki/Dependency_injection
    def injectImplementation(self, implementation):
        self.implementation = implementation

    def SwitchToPosition(self, request, context):
        """Switches the valve to the specified position. The given position has to be less than the NumberOfPositions or else a PositionOutOfRange error is thrown.
            :param request: gRPC request
            :param context: gRPC context
            :param request.Position: The target position that the valve should be switched to.

        """
        logging.debug("SwitchToPosition - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.SwitchToPosition(request, context)
        else:
            pass #~ return_val = request.Position.value
            #~ return pb2.SwitchToPosition_Responses( Success=fwpb2.Boolean(value=False) )

    def TogglePosition(self, request, context):
        """A boolean value where false represents a failed command execution and true represents a successful command execution.
        empty parameter
        """
        logging.debug("TogglePosition - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.TogglePosition(request, context)
        else:
            pass #~ return_val = request.Void.value
            #~ return pb2.TogglePosition_Responses( Success=fwpb2.Boolean(value=False) )

    def Get_NumberOfPositions(self, request, context):
        """The number of the valve positions available.
            :param request: gRPC request
            :param context: gRPC context
            :param response.NumberOfPositions: The number of the valve positions available.

        """
        logging.debug("Get_NumberOfPositions - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.Get_NumberOfPositions(request, context)
        else:
            #~ return_val = request.NumberOfPositions.value
            pass #~ return pb2.Get_NumberOfPositions_Responses( NumberOfPositions=fwpb2.Integer(value=0) )

    def Subscribe_Position(self, request, context):
        """The current logic valve position. This is a value between 0 and NumberOfPositions - 1.
            :param request: gRPC request
            :param context: gRPC context
            :param response.Position: The current logic valve position. This is a value between 0 and NumberOfPositions - 1.

        """
        logging.debug("Subscribe_Position - Mode: simulation ")

        if self.implementation is not None:
            self.implementation.Subscribe_Position(request, context)
        else:
            #~ yield_val = request.Position.value
            pass #~ yield pb2.Subscribe_Position_Responses( Position=fwpb2.Integer(value=0) )



