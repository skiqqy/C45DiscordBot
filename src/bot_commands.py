import subprocess
import requests


def exec_command(command):
    if command.startswith("exec"):
        cmd = command[4:]
        print("Exec: " + str(cmd))
        return subprocess.getoutput(cmd)
    elif command.startswith("eval"):
        cmad = command[4:]
        return eval(cmad)
    elif command.lower() == "ip:route":
        return subprocess.getoutput("route")
    elif command.lower() == "ip:if":
        return subprocess.getoutput("ifconfig")
    elif command.lower() == "ip:arp":
        return subprocess.getoutput("arp")
    elif command.startswith("ls"):
        dirLS = command[2:]
        return subprocess.getoutput("ls " + dirLS)
    elif command.lower().startswith("ip:ping"):
        ip = command[7:]
        return subprocess.getoutput("ping " + ip + " -c 3")
    elif command.lower().startswith("ip:trace"):
        ip = command[8:]
        return subprocess.getoutput("traceroute " + ip)
    elif command.lower().startswith("fetch"):
        url = command[5:]
        body = requests.get(url).text
        return body
    elif command == "brink":
        return "EXACTLY - Old Khaki.com"
    elif command == "help":
        f = open("./resources/help.menu")
        strings = f.readlines()
        msg = ""
        for s in strings:
            msg += s
        return msg
