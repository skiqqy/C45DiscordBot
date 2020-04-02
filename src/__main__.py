import os
import random
import subprocess
import discord
import irc.client
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from src import emojis, bot_commands

analyser = SentimentIntensityAnalyzer()


def score_message_sentiment(sentence):
    score = int(analyser.polarity_scores(sentence)['compound'] * 10)
    return emojis.number_emojis[score]


async def add_emoji(message, emoji):
    try:
        await message.add_reaction(emoji)
    except Exception as e:
        print("Bruh:", str(e))


def send_irc(channel, message):
    chan = "#" + str(channel)
    server.join(chan)
    server.topic(chan, "CLUB45 bot is ?LOST?")

    # Send message(s)
    if message.content != "":
        for send in message.content.split("."):
            server.privmsg(chan, "[" + str(message.author) + "]: " + send)

    # Send attachment URLs if there are some
    if len(message.attachments) > 0:
        i = 0
        for attach in message.attachments:
            print(attach)
            server.privmsg(chan, "[" + str(message.author) + "]: Attachment " + str(i) + ":" + str(attach.url))
            i += 1


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        guilds = []
        async for guild in self.fetch_guilds():
            print(guild)
            guilds.append(guild)
        c45 = guilds[0]
        webdev = guilds[1]
        channels = await webdev.fetch_channels()
        print(channels)

    async def on_message(self, message):
        if message.channel.id == 679599402935123968:
            return
        print(message.reactions)

        import discord
        if message.type == discord.MessageType.new_member:
            await message.channel.send(
                "https://toot.aquilenet.fr/system/accounts/avatars/000/027/478/original/92ec832ba0fbfd74.png?1578998921")
            await message.channel.send("welcome to da house, my bro.")
            return

        if os.getenv("bot_irc") == "1":
            try:
                send_irc(message.channel, message)
            except Exception as e:
                try:
                    server.connect("192.168.1.121", 6667, "c45_bot")
                except:
                    print("Reconnect failed")
                print("Failed to send IRC")
                print(e)

        # moduleLoader.loadModules("on_message")

        await add_emoji(message, score_message_sentiment(message.content))

        # Ignore messages from the bot
        if message.author == self.user:
            return
        else:
            await add_emoji(message, random.choice(emojis.troll_emojis))
            # Other user-specific messages
            if "bigdatadave" in str(message.author).lower():
                await add_emoji(message, "🅱️")
                await add_emoji(message, "ℹ️")
                await add_emoji(message, "🇬")
                await add_emoji(message, "📊")
            elif "brink" in str(message.author).lower():
                await add_emoji(message, "🅱️")
                await add_emoji(message, "🇷")
                await add_emoji(message, "ℹ️")
                await add_emoji(message, "🇳")
                await add_emoji(message, "🇰")
                await message.channel.send("Thank you Brink, very cool!")
            # Messages from everyone else
            if "test" in message.content.lower():
                # get the id
                id = message.author.id
                print("ID is: " + str(id))

                await message.channel.send("Marks out")
                await message.channel.send("?")
            elif message.content.lower()[:3] == "how":
                messageWiggle = ""
                i = True
                p = 0
                for ch in message.content:
                    if i:
                        messageWiggle += ch.upper()
                        i = False
                    else:
                        messageWiggle += ch.lower()
                        i = True
                    print(messageWiggle)
                    p += 1
                await message.channel.send(messageWiggle)
            elif "papi" in message.content.lower():
                await message.channel.send(random.choice([
                    "UWU DID SOMEBODY SAY P A P I",
                    "Yas daddi 🤪",
                    "Big P A P I Dave 😍"
                ]))
                await message.pin()
            elif "triggered" in message.content.lower():
                fl = open("./resources/triggered.lol", "r")
                msg = fl.readlines()
                index = random.randint(0, len(msg) - 1)
                await message.channel.send(msg[index])
            elif message.content.startswith(">"):
                # Remove the `>`
                command = message.content[1:].strip()
                print("Got command: \"" + command + "\"")
                command_output = bot_commands.exec_command(command)
                await message.channel.send("[Host Machine: " + \
                                           subprocess.getoutput("hostname") + "]\n" + \
                                           str(command_output))
            elif "vim" in message.content.lower():
                response = "vim is where its at chief\nif you have no idea how to use it or configure it, then look " \
                           "no further than the __epic gamer__:tm: config " \
                           "https://github.com/skippy404/.dotfilesMinimal for litty configs for vim and other " \
                           "stuff.\nThis message is endorsed by: Skippy \"vim or gtfo\" Cochrane. "
                await message.channel.send(response)
            elif "eclipse" in message.content.lower():
                await message.channel.send("eclipse kaka, IDE's kaka")
            else:
                print("Message dropped, not a command")


if __name__ == "__main__":
    if os.getenv("bot_irc") == "1":
        try:
            # Create a client
            client = irc.client.Reactor()
            server = client.server()
            server.connect("192.168.1.121", 6667, "c45_bot")
            server.join("#club45")
        except Exception:
            print("Error connecting IRC")

    client = MyClient()
    client.run(os.getenv("C45_Token"))
