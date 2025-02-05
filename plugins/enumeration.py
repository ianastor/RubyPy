from core.plugin_base import PluginBase

class EnumerationPlugin(PluginBase):
    def run(self, **kwargs):
        print("[*] Running Enumeration Plugin...")
        # Insert enumeration logic here (e.g., list users, services, etc.)
        # Example: printing a dummy list of services
        services = ["HTTP", "SSH", "FTP"]
        print("Discovered services:", services)
    
    def stop(self):
        print("[*] Stopping Enumeration Plugin.")

# The plugin instance that the PluginManager will look for
PLUGIN = EnumerationPlugin()