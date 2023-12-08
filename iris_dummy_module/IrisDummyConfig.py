# Import the module types list,  so we can indicate the type of our module 
from iris_interface.IrisModuleInterface import IrisModuleTypes 

# Human name displayed in the GUI Manage > Modules. This can be anything, 
# but try to put something meaningful, so users recognize your module. 
module_name = "IrisDummy"

# Description displayed when editing the module configuration in the UI. 
# This can be anything, 
module_description = "Provides a dummy module that replies to one hook"

# Set the interface version used. This needs to be the version of 
# the IrisModuleInterface package. This version is check by the server to
# to ensure our module can run on this specific server 
interface_version = 1.1

# The version of the module itself, it can be anything 
module_version = 1.0

# The type of the module, here processor 
module_type = IrisModuleTypes.module_processor

# Our module is a processor type, so it doesn't offer any pipeline 
pipeline_support = False

# Provide no pipeline information as our module don't implement any 
pipeline_info = {}

# The configuration of the module that will be displayed and configurable 
# by administrators on the UI. This describes every parameter that can 
# be set. 
module_configuration = [
    {
        "param_name": "log_received_hook",

        "param_human_name": "Log received hook",

        "param_description": "Logs a message upon hook receiving if set to true. Otherwise do nothing.",

        "default": True,

        "mandatory": True,

        "type": "bool"
    }
]
