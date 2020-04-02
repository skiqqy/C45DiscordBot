# Plugin loader
#
# Modular plugin loader
import importlib


def find_plugin(config, commandString):
	try:
		plugins_directory = config["plugins"]
		print("Found plugins")
		plugins = plugins_directory.keys()
		print("Plugins available are: " + str(plugins))

		for plugin in plugins:
			if plugins_directory[plugin]["command"] == commandString:
				return importlib.import_module("mods." + plugins_directory[plugin]["file"])
		else:
			print("Invalid plugin")
	except KeyError:
		print("Couldn't find plugins key")
