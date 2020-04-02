# Module loader
#
# Loads modules.

import os

def loadModules(typeOf):
	# Get a list of modules
	modules = os.listdir(typeOf)

	commands = {}
	
	for module in modules:
		print("Module: " + str(module))
		os.chdir(typeOf+"/")
		print(module.split(".")[0])
		import importlib
		print(eval("import pong"))
		moduleImported = importlib.import_module(module.split(".")[0])
		commands[moduleImported.command] = moduleImported
		os.chdir("../")

	# Now return a dictionary indexed by command word
	return commands