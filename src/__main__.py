import os
import random
import subprocess
import discord
import irc.client
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plugins
import emojis
import bot_commands
from message_based_responses import regex_based_response
from __init__ import cfg

analyser = SentimentIntensityAnalyzer()


def score_message_sentiment(sentence):
    score = int(((analyser.polarity_scores(sentence)['compound'] + 1) / 2) * 10)
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
            except Exception as irc_e:
                print("[ERR] Failed to send IRC.", irc_e)
                try:
                    server.connect("192.168.1.121", 6667, "c45_bot")
                except Exception as recon_e:
                    print("[ERR] Reconnect failed", recon_e)

        message_content = message.content.lower()
        await add_emoji(message, score_message_sentiment(message_content))

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
            for m in regex_based_response(message_content):
                await message.channel.send(m)

            if message_content[:3] == "how":
                message_wiggle = ""
                i = True
                p = 0
                for ch in message.content:
                    if i:
                        message_wiggle += ch.upper()
                        i = False
                    else:
                        message_wiggle += ch.lower()
                        i = True
                    print(message_wiggle)
                    p += 1
                await message.channel.send(message_wiggle)
            elif message_content.startswith("/"):
                command = message_content[1:].strip()
                print("[DEBUG] Got command: \"" + command + "\"")
                command_output = bot_commands.exec_command(command)
                await message.channel.send("[Host Machine: " +
                                           subprocess.getoutput("hostname") + "]\n" +
                                           str(command_output))

                # if message.content.startswith('del'):
                if command.startswith('del'):

                    if message.content.split()[2:]:
                        text_match = ' '.join(message.content.split()[1:])
                    else:
                        text_match = None
                    
                    def check(msg):
                        return msg.author.id == client.user.id and (text_match.lower() in message.content.lower() if text_match is not None else True)

                    deleted = await message.channel.purge(limit=int(message.content.split()[1]), check=check)
                    await message.channel.send(message.author.mention, embed=discord.Embed(title=f"Deleted `{len(deleted)}` messages", colour=discord.Colour.green()), delete_after=3)
            else:
                print("[WARN] Message dropped, not a command")


if __name__ == "__main__":
    if not os.path.isfile("resources/config.yml"):
        print("No configuration file found! See README.md.")

    # Preload plugins
    plugins.load(cfg)

    try:
        if cfg["irc"]["enabled"]:
            print("[INFO] Connecting to IRC server...")
            # Create a client
            client = irc.client.Reactor()
            server = client.server()
            server.connect(cfg["irc"]["hostname"], int(cfg["irc"]["port"]), cfg["irc"]["nickname"])
            server.join("#club45")
            print("[INFO] Successful connection to IRC server!")
    except KeyError as e:
        print("[ERR] Configuration error: " + str(e))
    except irc.client.ServerConnectionError as e:
        print("[ERR] Error connecting IRC. ", str(e))

    print("[INFO] Starting client...")
    client = MyClient()
    client.run(cfg["token"]["secret"])
    print("[INFO] Client successfully started!")
