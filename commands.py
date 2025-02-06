# commands.py

import os
import subprocess

def help_command(args):
    """Display help information for all commands."""
    print("""
Available Commands:
  help                  - Show this help message.
  help <plugin>         - Show help for a specific plugin (stub).
  info <plugin>         - Show detailed info about a plugin (stub).
  reload <plugin>       - Force reload a plugin (stub).
  plugins               - List available and loaded plugins.
  config                - Display or modify configuration settings (stub).
  shell <command>       - Execute an OS command (stub).
  clear                 - Clear the terminal screen.
  history               - Show command history.
  about                 - Display information about RubyPy.
  exit                  - Exit the framework.
""")

def info_command(args, plugin_manager):
    if args:
        plugin_name = args[0]
        if plugin_name in plugin_manager.plugins:
            print(f"Information for plugin '{plugin_name}':")
            print("  Version: 1.0 (stub)")
            print("  Author: Unknown (stub)")
            print("  Description: This is a stub plugin.")
        else:
            print(f"No plugin named '{plugin_name}' is loaded.")
    else:
        print("Usage: info <plugin>")

def reload_command(args, plugin_manager):
    if args:
        plugin_name = args[0]
        print(f"Reloading plugin '{plugin_name}'... (stub)")
        # Add reload logic here
    else:
        print("Usage: reload <plugin>")

def plugins_command(plugin_manager):
    # List available plugins
    try:
        available_plugins = [
            f[:-3] for f in os.listdir("plugins")
            if f.endswith(".py") and f != "__init__.py"
        ]
    except Exception as e:
        print("Error scanning plugins directory:", e)
        available_plugins = []
    print("Available Plugins:", ", ".join(available_plugins))
    print("Loaded Plugins:", ", ".join(plugin_manager.plugins.keys()))

def config_command(args):
    print("Configuration settings (stub).")
    # Add configuration logic here

def shell_command(args):
    if args:
        command = " ".join(args)
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print("Error:", result.stderr)
        except Exception as e:
            print("Error executing shell command:", e)
    else:
        print("Usage: shell <command>")

def clear_command():
    os.system("cls" if os.name == "nt" else "clear")

def history_command(history):
    print("Command History:")
    for i, cmd in enumerate(history, 1):
        print(f"{i}: {cmd}")

def about_command():
    print("RubyPy - Rapid User Breach & Post-Exploitation Yield in Python")
    print("Developed by Blur3, 2025.")

def dispatch_command(input_command, plugin_manager, history):
    parts = input_command.strip().split()
    if not parts:
        return

    command = parts[0].lower()
    args = parts[1:]

    if command == "help":
        if args:
            print(f"Help for plugin '{args[0]}' (stub).")
        else:
            help_command(args)
    elif command == "info":
        info_command(args, plugin_manager)
    elif command == "reload":
        reload_command(args, plugin_manager)
    elif command == "plugins":
        plugins_command(plugin_manager)
    elif command == "config":
        config_command(args)
    elif command == "shell":
        shell_command(args)
    elif command == "clear":
        clear_command()
    elif command == "history":
        history_command(history)
    elif command == "about":
        about_command()
    elif command == "exit":
        print("Exiting RubyPy...")
        exit(0)
    else:
        print("Command not recognized. Type 'help' for available commands.")