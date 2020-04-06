import re
import random


def _match_word(word_to_match, message_content):
    return re.search("^.*(\\w*[\b ]?{}([. !?@]+\\w*| +)?)$".format(word_to_match), message_content)


def regex_based_response(message_content):
    response = []

    if _match_word("test", message_content):
        print('[DEBUG] Test hit!')
        response.append("Marks out")
        response.append("?")
    elif _match_word("papi", message_content):
        response.append(random.choice([
            "UWU DID SOMEBODY SAY P A P I",
            "Yas daddi 🤪",
            "Big P A P I Dave 😍"
        ]))
    elif _match_word("triggered", message_content):
        fl = open("./resources/triggered.lol", "r")
        msg = fl.readlines()
        index = random.randint(0, len(msg) - 1)
        response.append(msg[index])
    elif _match_word("vim", message_content):
        f = open("./resources/vim.txt", "r")
        response.append(f.readline())
    elif _match_word("eclipse", message_content):
        response.append("eclipse kaka, IDE's kaka")

    return response
