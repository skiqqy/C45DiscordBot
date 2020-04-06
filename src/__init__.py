import yaml
import os

if not os.path.isfile("./resources/config.yml"):
    print("No configuration file found! Using default settings.")
    with open("../resources/config.default.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
else:
    with open("./resources/config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
