#!/usr/bin/env python3

# Import the IrisInterface class
from iris_interface.IrisModuleInterface import IrisModuleInterface
import iris_dummy_module.IrisDummyConfig as interface_conf

# Create our module class
class IrisDummyModule(IrisModuleInterface):
    # Set the configuration
    _module_name = interface_conf.module_name
    _module_description = interface_conf.module_description
    _interface_version = interface_conf.interface_version
    _module_version = interface_conf.module_version
    _pipeline_support = interface_conf.pipeline_support
    _pipeline_info = interface_conf.pipeline_info
    _module_configuration = interface_conf.module_configuration
    _module_type = interface_conf.module_type

    def register_hooks(self, module_id: int):
        """
        Called by IRIS indicating it's time to register hooks.  

        :param module_id: Module ID provided by IRIS.
        """

        # Call the hook registration method. We need to pass the 
        # the module_id to this method, otherwise IRIS won't know 
        # to whom associate the hook. 
        # The hook name needs to be a well known hook name by IRIS. 
        status = self.register_to_hook(module_id, iris_hook_name='on_postload_ioc_create')

        if status.is_failure():
            # If we have a failure, log something out 
            self.log.error(status.get_message())

        else:
            # Log that we successfully registered to the hook 
            self.log.info(f"Successfully subscribed to on_postload_ioc_create hook")


def hooks_handler(self, hook_name: str, data):
    """
    Called by IRIS each time one of our hook is triggered. 
    """

    # read the current configuration and only log the call if 
    # our parameter is set to true 
    if self._dict_conf.get('log_received_hook') is True:
        self.log.info(f'Received {hook_name}')
        self.log.info(f'Received data of type {type(data)}')

    # Return a standardized message to IRIS saying that everything is ok. 
    # logs=list(self.message_queue) is needed, so the users can see the logs 
    # our module generated during its execution.  
    return InterfaceStatus.I2Success(data=data, logs=list(self.message_queue))