from abc import ABC, abstractmethod

class PluginBase(ABC):
    @abstractmethod
    def run(self, **kwargs):
        """
        Execute the plugin's primary functionality.
        """
        pass

    def stop(self):
        """
        Optional: Clean up or stop the plugin if needed.
        """
        pass
