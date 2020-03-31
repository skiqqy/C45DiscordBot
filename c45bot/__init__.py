##C45 Bot for the c45 discord server
# TODO:
# * Add functionality to access bnet
# * Add functionality to host files
# * Add functionality to play songs
# * Add reminders (bot will message if something is due)
# * Welcome messgaes and role assignment
import os
import random

import discord
import irc.client
from discord.ext import commands
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import c45bot.bot_commands
import c45bot.emojis

analyser = SentimentIntensityAnalyzer()


def score_message_sentiment(sentence):
    score = int(analyser.polarity_scores(sentence)['compound'] * 10)
    return emojis.number_emojis[score]


async def add_emoji(message, emoji):
    try:
        await message.add_reaction(emoji)
    except Exception as e:
        print("Bruh:", str(e))


def sendIRC(channel, message):
    chan = "#" + str(channel)
    server.privmsg("#club45", "[" + str(message.author) + "]: " + message.content)


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

        sendIRC(message.channel, message)

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
                command_output = commands.exec_command(command)
                await message.channel.send(command_output)
            else:
                print("Message dropped, not a command")


if __name__ == "__main__":
    # Create a client
    client = irc.client.Reactor()
    server = client.server()
    server.connect("192.168.1.121", 6667, "c45_bot")
    server.join("#club45")

    client = MyClient()
    client.run(os.getenv("C45_Token"))
