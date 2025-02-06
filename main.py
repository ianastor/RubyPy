#!/usr/bin/env python3
import sys
from core.plugin_manager import PluginManager
from ascii_art import display_ascii_art
from adapters.adapter_loader import load_adapters
from commands import dispatch_command

def main():
    command_history = []

    # Display ASCII art graphic on startup
    display_ascii_art()
    
    # Display welcome banner
    print("=============================================")
    print("           Welcome to RubyPy")
    print("  Rapid User Breach & Post-Exploitation Yield in Python")
    print("=============================================")
    print("Copyright (C) 2025 Blur3")
    
    # Load adapters at startup (stub)
    load_adapters()
    
    # Initialize and load plugins
    pm = PluginManager()
    pm.load_plugins()

    # Print the list of available commands on startup
    dispatch_command("help", pm, command_history)
    
    # Interactive command loop
    while True:
        input_command = input("RubyPy> ")
        if input_command.strip() == "":
            continue
        command_history.append(input_command)
        dispatch_command(input_command, pm, command_history)

if __name__ == "__main__":
    main()