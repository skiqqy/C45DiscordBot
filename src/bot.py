##C45 Bot for the c45 discord server
# TODO:
# * Add functionality to access bnet
# * Add functionality to host files
# * Add functionality to play songs
# * Add reminders (bot will message if something is due)
# * Welcome messgaes and role assignment
import discord
from discord.ext import commands
import os
import subprocess
import random
import emojis
import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def score_message_sentiment(sentence):
    score = int(analyser.polarity_scores(sentence)['compound'] * 10)
    return emojis.number_to_emoji(score)

async def add_emoji(message, emoji):
    try:
        await message.add_reaction(emoji)
    except Exception as e:
        print("Bruh:", str(e))

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
        await add_emoji(message, random.choice(emojis.troll_emojis))
        await add_emoji(message, score_message_sentiment(message))
        
        # Ignore messages from the bot
        if message.author == self.user:
            return
        else:
            # Messages from everyone else
            if "test" in message.content.lower():
                # get the id
                id = message.author.id
                print("ID is: " + str(id))
            
                await message.channel.send("Marks out")
                await message.channel.send("?")
            elif "papi" in message.content.lower():
                await message.channel.send("UWU DID SOMEBODY SAY P A P I")
                await message.pin()
            elif "triggered" in message.content.lower():
                fl = open("./resources/triggered.lol","r")
                msg = fl.readlines()
                index = random.randint(0,len(msg)-1)
                await message.channel.send(msg[index])
            elif message.content.startswith(">"):
                # Remove the `>`
                command = message.content[1:].strip()
                print("Got command: \"" + command + "\"")

                if command.startswith("exec"):
                    cmd = command[4:]
                    print("Exec: " + str(cmd))
                    await message.channel.send(subprocess.getoutput(cmd))
                elif command.lower() == "ip:route":
                    await message.channel.send(subprocess.getoutput("route"))
                elif command.lower() == "ip:if":
                    await message.channel.send(subprocess.getoutput("ifconfig"))
                elif command.lower() == "ip:arp":
                    await message.channel.send(subprocess.getoutput("arp"))
                elif command.startswith("ls"):
                    dirLS = command[2:]
                    await message.channel.send(subprocess.getoutput("ls " + dirLS))
                elif command.lower().startswith("ip:ping"):
                    ip = command[7:]
                    await message.channel.send(subprocess.getoutput("ping " + ip + " -c 3"))
                elif command.lower().startswith("ip:trace"):
                    ip = command[8:]
                    await message.channel.send(subprocess.getoutput("traceroute " + ip))        
                elif command.lower().startswith("fetch"):
                    import requests
                    url = command[5:]
                    body = requests.get(url).text
                    await message.channel.send(body)
                elif command == "brink":
                    await message.channel.send("EXACTLY - Old Khaki.com")
                elif command == "help":
                    f = open("./resources/help.menu");
                    strings = f.readlines()
                    msg = ""
                    for s in strings:
                        msg += s
                    await message.channel.send(msg)
            else:
                print("Message dropped, not a command")
            

client = MyClient()
client.run(os.getenv("C45_Token"))
