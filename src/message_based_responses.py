import re
import random


def regex_based_response(message):
    message_content = message.content.lower()

    if re.search("^.*(\\w*[\b ]?test([. ]+\\w*| +)?)$", message_content):
        print('[DEBUG] Test hit!')
        # get the id
        author_id = message.author.id
        print("[DEBUG] ID is: ", author_id)
        await message.channel.send("Marks out")
        await message.channel.send("?")
    elif re.search("^.*(\\w*[\b ]?papi([. ]+\\w*| +)?)$", message_content):
        await message.channel.send(random.choice([
            "UWU DID SOMEBODY SAY P A P I",
            "Yas daddi 🤪",
            "Big P A P I Dave 😍"
        ]))
        await message.pin()
    elif re.search("^.*(\\w*[\b ]?triggered([. ]+\\w*| +)?)$", message_content):
        fl = open("./resources/triggered.lol", "r")
        msg = fl.readlines()
        index = random.randint(0, len(msg) - 1)
        await message.channel.send(msg[index])
    elif re.search("^.*(\\w*[\b ]?vim([. ]+\\w*| +)?)$", message_content):
        f = open("./resources/vim.txt", "r")
        await message.channel.send(f.readline())
    elif re.search("^.*(\\w*[\b ]?eclipse([. ]+\\w*| +)?)$", message_content):
        await message.channel.send("eclipse kaka, IDE's kaka")
