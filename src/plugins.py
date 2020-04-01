# Plugin loader

import importlib

def findPlugin(config, commandString):
	try:
		pluginsDirectory = config["plugins"]
		print("Found plugins")
		plugins = pluginsDirectory.keys()
		print("Plugins available are: " + str(plugins))

		for plugin in plugins:
			print("What")
			if pluginsDirectory[plugin]["command"] == commandString:
				print("Valid plugin")
				return importlib.import_module("mods."+pluginsDirectory[plugin]["file"])
		else:
			print("Invalid plugin")
	except KeyError:
		print("Couldn't find plugins key")