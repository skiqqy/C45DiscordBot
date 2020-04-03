# Module loader
#
# Loads modules.

import os


def load_modules(type_of):
    # Get a list of modules
    modules = os.listdir(type_of)

    commands = {}

    for module in modules:
        print("Module: " + str(module))
        os.chdir(type_of + "/")
        print(module.split(".")[0])
        import importlib
        print(eval("import pong"))
        module_imported = importlib.import_module(module.split(".")[0])
        commands[module_imported.command] = module_imported
        os.chdir("../")

    # Now return a dictionary indexed by command word
    return commands
