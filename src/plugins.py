# Plugin loader
#
# Modular plugin loader
import importlib

def findPlugin(config, commandString):
	try:
		pluginsDirectory = config["plugins"]
		print("Found plugins")
		plugins = pluginsDirectory.keys()
		print("Plugins available are: " + str(plugins))

		for plugin in plugins:
			if pluginsDirectory[plugin]["command"] == commandString:
				return importlib.import_module("mods."+pluginsDirectory[plugin]["file"])
		else:
			print("Invalid plugin")
	except KeyError:
		print("Couldn't find plugins key")
