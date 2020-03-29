##C45 Bot for the c45 discord server
# TODO:
# * Add functionality to access bnet
# * Add functionality to host files
# * Add functionality to play songs
# * Add reminders (bot will message if something is due)
# * Welcome messgaes and role assignment
import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        guilds = []
        async for guild in self.fetch_guilds():
            print(guild)
            guilds.append(guild)
        c45 = guilds[0]
        channels = await c45.fetch_channels()
        print(channels)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == 'ping':
            await message.channel.send('pong')


token = os.getenv("C45_Token");
client = MyClient()
client.run(token)

