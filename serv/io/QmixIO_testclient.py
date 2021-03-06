#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: sila_cetoni

*QmixIO test client*

:details: QmixIO:
    The SiLA 2 driver for Qmix I/O Devices

:file:    QmixIO_testclient.py
:authors: Florian Meinicke

:date: (creation)          2021-07-08T12:20:27.648444
:date: (last modification) 2021-07-08T12:20:27.648444

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
import time
import datetime

# import meta packages
from typing import Union, Optional

# import SiLA client module
from .QmixIO_client import QmixIOClient


def parse_command_line():
    """
    Just looking for command line arguments
    """
    parser = argparse.ArgumentParser(
        description="A SiLA2 test client for: QmixIO")

    # connection parameters
    parser.add_argument('-i', '--server-ip-address', action='store', default='127.0.0.1',
                        help='SiLA server IP address')
    parser.add_argument('--server-hostname', action='store', default='localhost',
                        help='SiLA server hostname')
    parser.add_argument('-p', '--server-port', action='store', default=50052,
                        help='SiLA server port')

    # encryption
    parser.add_argument('-X', '--encryption', action='store', default='sila2_server',
                        help='The name of the private key and certificate file (without extension).')
    parser.add_argument('--encryption-key', action='store', default=None,
                        help='The name of the encryption key (*with* extension). Can be used if key and certificate '
                             'vary or non-standard file extensions are used.')
    parser.add_argument('--encryption-cert', action='store', default=None,
                        help='The name of the encryption certificate (*with* extension). Can be used if key and '
                             'certificate vary or non-standard file extensions are used.')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__)

    return parser.parse_args()


if __name__ == '__main__':
    # or use logging.INFO (=20) or logging.ERROR (=30) for less output
    logging.basicConfig(
        format='%(levelname)-8s| %(module)s.%(funcName)s: %(message)s', level=logging.DEBUG)

    parsed_args = parse_command_line()

    # start the client
    sila_client = QmixIOClient(server_ip=parsed_args.server_ip_address,
                                        server_port=int(parsed_args.server_port))
    sila_client.run()

    # Log connection info
    logging.info(
        (
            f'Connected to SiLA Server {sila_client.server_display_name} running in version {sila_client.server_version}.' '\n'
            f'Service description: {sila_client.server_description}'
        )
    )

    # TODO:
    #   Uncomment the calls you would like to test and remove type hints (given only for orientation) or
    #   write your further function calls here to run the client as a standalone application.

    # ------------- command calls -------------------

    # ----- de/cetoni/io/AnalogOutChannelController
    # results = sila_client.analogOutChannelController_client.SetOutputValue(Value: float = 1.0)
    # print("AnalogOutChannelController SetOutputValue res: ", results)

    # ----- de/cetoni/io/DigitalOutChannelController
    # results = sila_client.digitalOutChannelController_client.SetOutput(State: str = 'default string')
    # print("DigitalOutChannelController SetOutput res: ", results)


    # ------------- property calls -------------------

    # ----- de/cetoni/io/AnalogInChannelProvider
    # results = sila_client.analogInChannelProvider_client.Get_NumberOfChannels()
    # print("AnalogInChannelProvider NumberOfChannels res: ", results)

    # results = sila_client.analogInChannelProvider_client.Subscribe_Value()
    # print("Value res: ", results)

    # ----- de/cetoni/io/AnalogOutChannelController
    # results = sila_client.analogOutChannelController_client.Get_NumberOfChannels()
    # print("AnalogOutChannelController NumberOfChannels res: ", results)

    # results = sila_client.analogOutChannelController_client.Subscribe_Value()
    # print("AnalogOutChannelController Value res: ", results)

    # ----- de/cetoni/io/DigitalInChannelProvider
    # results = sila_client.digitalInChannelProvider_client.Get_NumberOfChannels()
    # print("DigitalInChannelProvider NumberOfChannels res: ", results)

    # results = sila_client.digitalInChannelProvider_client.Subscribe_State()
    # print("State res: ", results)

    # ----- de/cetoni/io/DigitalOutChannelController
    # results = sila_client.digitalOutChannelController_client.Get_NumberOfChannels()
    # print("DigitalOutChannelController NumberOfChannels res: ", results)

    # results = sila_client.digitalOutChannelController_client.Subscribe_State()
    # print("DigitalOutChannelController State res: ", results)



    # ------------- metadata calls -------------------

    # results = sila_client.AnalogInChannelProvider_client.Get_FCPAffectedByMetadata_ChannelIndex()
    # print("AnalogInChannelProvider FCPAffectedByMetadata_ChannelIndex res: ", results)

    # results = sila_client.AnalogOutChannelController_client.Get_FCPAffectedByMetadata_ChannelIndex()
    # print("AnalogOutChannelController FCPAffectedByMetadata_ChannelIndex res: ", results)

    # results = sila_client.DigitalInChannelProvider_client.Get_FCPAffectedByMetadata_ChannelIndex()
    # print("DigitalInChannelProvider FCPAffectedByMetadata_ChannelIndex res: ", results)

    # results = sila_client.DigitalOutChannelController_client.Get_FCPAffectedByMetadata_ChannelIndex()
    # print("DigitalOutChannelController FCPAffectedByMetadata_ChannelIndex res: ", results)


