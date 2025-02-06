# core/plugin_manager.py
import importlib
import os
import sys

class PluginManager:
    def __init__(self, plugins_dir="plugins"):
        self.plugins_dir = plugins_dir
        self.plugins = {}  # Mapping: plugin_name -> plugin instance

    def load_plugins(self):
        """Scan the plugins directory and load each plugin that follows the interface.
        Instead of printing individual messages for each plugin, it prints a summary."""
        loaded_count = 0
        for filename in os.listdir(self.plugins_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                module_path = f"{self.plugins_dir}.{module_name}"
                try:
                    module = importlib.import_module(module_path)
                    if hasattr(module, "PLUGIN"):
                        self.plugins[module_name] = module.PLUGIN
                        loaded_count += 1
                    else:
                        print(f"[-] Module '{module_name}' does not define 'PLUGIN'.")
                except Exception as e:
                    print(f"[!] Error loading plugin '{module_name}': {e}")
        print(f"[+] {loaded_count} plugins loaded.")

    def unload_plugin(self, plugin_name):
        """Unload a plugin by name."""
        if plugin_name in self.plugins:
            plugin = self.plugins[plugin_name]
            if hasattr(plugin, "stop"):
                plugin.stop()
            del self.plugins[plugin_name]
            if plugin_name in sys.modules:
                del sys.modules[plugin_name]
            print(f"[+] Plugin '{plugin_name}' unloaded.")
        else:
            print(f"[-] Plugin '{plugin_name}' not found.")

    def list_plugins(self):
        """List all currently loaded plugins."""
        if self.plugins:
            print("Loaded Plugins:")
            for name in self.plugins:
                print(f" - {name}")
        else:
            print("No plugins loaded.")

    def run_plugin(self, plugin_name, **kwargs):
        """Execute the run() method of the specified plugin."""
        if plugin_name in self.plugins:
            plugin = self.plugins[plugin_name]
            plugin.run(**kwargs)
        else:
            print(f"[-] Plugin '{plugin_name}' not found.")