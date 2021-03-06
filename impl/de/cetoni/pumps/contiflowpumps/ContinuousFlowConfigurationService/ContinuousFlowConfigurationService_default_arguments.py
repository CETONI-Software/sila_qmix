# This file contains default values that are used for the implementations to supply them with
#   working, albeit mostly useless arguments.
#   You can also use this file as an example to create your custom responses. Feel free to remove
#   Once you have replaced every occurrence of the defaults with more reasonable values.
#   Or you continue using this file, supplying good defaults..

# import the required packages
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2
import sila2lib.framework.SiLABinaryTransfer_pb2 as silaBinary_pb2
from .gRPC import ContinuousFlowConfigurationService_pb2 as pb2

# initialise the default dictionary so we can add keys.
#   We need to do this separately/add keys separately, so we can access keys already defined e.g.
#   for the use in data type identifiers
default_dict = dict()


default_dict['SetSwitchingMode_Parameters'] = {
    'SwitchingMode': silaFW_pb2.String(value='default string')
}

default_dict['SetSwitchingMode_Responses'] = {

}

default_dict['SetRefillFlowRate_Parameters'] = {
    'RefillFlowRate': silaFW_pb2.Real(value=1.0)
}

default_dict['SetRefillFlowRate_Responses'] = {

}

default_dict['SetCrossFlowDuration_Parameters'] = {
    'CrossFlowDuration': silaFW_pb2.Real(value=1.0)
}

default_dict['SetCrossFlowDuration_Responses'] = {

}

default_dict['SetOverlapDuration_Parameters'] = {
    'OverlapDuration': silaFW_pb2.Real(value=1.0)
}

default_dict['SetOverlapDuration_Responses'] = {

}

default_dict['Subscribe_SwitchingMode_Responses'] = {
    'SwitchingMode': silaFW_pb2.String(value='default string')
}

default_dict['Subscribe_MaxRefillFlowRate_Responses'] = {
    'MaxRefillFlowRate': silaFW_pb2.Real(value=1.0)
}

default_dict['Subscribe_RefillFlowRate_Responses'] = {
    'RefillFlowRate': silaFW_pb2.Real(value=1.0)
}

default_dict['Subscribe_MinFlowRate_Responses'] = {
    'MinFlowRate': silaFW_pb2.Real(value=1.0)
}

default_dict['Subscribe_CrossFlowDuration_Responses'] = {
    'CrossFlowDuration': silaFW_pb2.Real(value=1.0)
}

default_dict['Subscribe_OverlapDuration_Responses'] = {
    'OverlapDuration': silaFW_pb2.Real(value=1.0)
}
