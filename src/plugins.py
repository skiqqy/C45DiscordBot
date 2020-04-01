# Plugin loader
#
# Modular plugin loader
import importlib

preloadedPlugins = []

def load(config):
    pluginsAvailable = config["plugins"]

    for plugin in pluginsAvailable:
        pluginKey = list(plugin.keys())[0]
        pluginData = plugin[pluginKey]
        print(pluginData)
        print("Preloading plugin: " + str(pluginKey))
        pluginModule = importlib.import_module("mods."+pluginData["file"])
        preloadedPlugins.append((pluginModule, plugin))

    print("Loaded plugins into memory: " + str(preloadedPlugins))
    
def find_plugin(commandString):
    for plugin in preloadedPlugins:
        pluginName = list(plugin[1].keys())[0]
        print(plugin[1][pluginName])
        if plugin[1][pluginName]["command"] == commandString:
            return plugin[0]
