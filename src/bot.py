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

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        guilds = []
        async for guild in self.fetch_guilds():
            print(guild)
            guilds.append(guild)
        c45 = guilds[0]
        channels = await c45.fetch_channels()
        banter = None
        for channel in channels:
            if channel.id==615645678147862538:
                banter = channel
                self.banter = banter
                break
       

    async def on_message(self, message):
        # Ignore messages from the bot
        if message.author == self.user:
            return
        else:
            # Messages from everyone else
            if message.content.startswith(">"):
                # Remove the `>`
                command = message.content[1:].strip().lower()
                print("Got command: \"" + command + "\"")

                if command == "ip:route":
                    await self.banter.send(subprocess.getoutput("route"))
                elif command == "ip:if":
                    await self.banter.send(subprocess.getoutput("ifconfig"))
                elif command == "ip:arp":
                    await self.banter.send(subprocess.getoutput("arp"))
            else:
                print("Message dropped, not a command")
            

client = MyClient()
client.run(os.getenv("C45_Token"))