#!/usr/bin/env python3
import sys
from core.plugin_manager import PluginManager
from ascii_art import display_ascii_art

def main():
    # Display welcome banner
    print("=============================================")
    print("           Welcome to RubyPy")
    print("  Rapid User Breach & Post-Exploitation Yield in Python")
    print("=============================================")
    
    # Display an ASCII art graphic on startup
    display_ascii_art()

    # Initialize and load plugins
    pm = PluginManager()
    pm.load_plugins()

    # Interactive command loop
    while True:
        print("\nOptions: list | run [plugin] | unload [plugin] | exit")
        command = input("Command> ").strip().split()

        if not command:
            continue

        action = command[0].lower()
        if action == "list":
            pm.list_plugins()
        elif action == "run" and len(command) > 1:
            plugin_name = command[1]
            pm.run_plugin(plugin_name)
        elif action == "unload" and len(command) > 1:
            plugin_name = command[1]
            pm.unload_plugin(plugin_name)
        elif action == "exit":
            print("Exiting RubyPy...")
            sys.exit(0)
        else:
            print("Command not recognized.")

if __name__ == "__main__":
    main()